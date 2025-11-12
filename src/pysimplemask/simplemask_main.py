import json
import logging
import os
import sys
import traceback
from pathlib import Path

import numpy as np
import pyqtgraph as pg
from pyqtgraph.parametertree import Parameter
from PySide6.QtCore import QByteArray
from PySide6.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QDoubleSpinBox,
    QFileDialog,
    QHeaderView,
    QLineEdit,
    QMainWindow,
    QMessageBox,
    QRadioButton,
    QSpinBox,
    QTabWidget,
)

from . import __version__
from .simplemask_kernel import SimpleMask
from .simplemask_ui import Ui_SimpleMask as Ui
from .table_model import XmapConstraintsTableModel

HOME_DIR = Path.home()
CONFIG_FILE = HOME_DIR / ".pysimplemask" / "config.json"
CONFIG_FILE.parent.mkdir(parents=True, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(name)-24s: %(message)s",
    handlers=[logging.StreamHandler()],
)

logger = logging.getLogger(__name__)


def exception_hook(exc_type, exc_value, exc_traceback):
    logger.error("Uncaught exception", exc_info=(exc_type, exc_value, exc_traceback))


sys.excepthook = exception_hook


def text_to_array(pts, dtype=np.int64):
    for symbol in "[](),":
        pts = pts.replace(symbol, " ")
    pts = pts.split(" ")

    if dtype == np.int64:
        pts = [int(x) for x in pts if x != ""]
    elif dtype == np.float64:
        pts = [float(x) for x in pts if x != ""]

    pts = np.array(pts).astype(dtype)

    return pts


PVMAP = {
    "bcx": "db_cenx",
    "bcy": "db_ceny",
    "energy": "db_energy",
    "pix_dim": "db_pix_dim",
    "det_dist": "db_det_dist",
}


class SimpleMaskGUI(QMainWindow, Ui):
    def __init__(self, path=None):

        super(SimpleMaskGUI, self).__init__()

        self.setupUi(self)
        self.setWindowTitle(f"pySimpleMask {__version__}")
        self.btn_load.clicked.connect(self.load)
        self.btn_plot.clicked.connect(self.plot)
        self.btn_compute_qpartition.clicked.connect(self.compute_partition)
        self.btn_compute_qpartition2.clicked.connect(self.compute_partition)
        self.btn_compute_qpartition3.clicked.connect(self.compute_partition)

        self.btn_select_raw.clicked.connect(self.select_raw)
        # self.btn_select_txt.clicked.connect(self.select_txt)
        self.btn_update_parameters.clicked.connect(self.update_parameters)
        self.btn_swapxy.clicked.connect(lambda: self.update_parameters(swapxy=True))

        self.btn_find_center.clicked.connect(self.find_center)

        # need a function for save button -- simple_mask_ui
        self.pushButton.clicked.connect(self.save_mask)

        self.plot_index.currentIndexChanged.connect(self.mp1.setCurrentIndex)

        # reset, redo, undo botton for mask
        self.btn_mask_reset.clicked.connect(lambda: self.mask_action("reset"))
        self.btn_mask_redo.clicked.connect(lambda: self.mask_action("redo"))
        self.btn_mask_undo.clicked.connect(lambda: self.mask_action("undo"))

        # simple mask kernep
        self.sm = SimpleMask(self.mp1, self.infobar)
        self.metadata_parameter = None
        self.mp1.sigTimeChanged.connect(self.update_index)
        self.state = "lock"

        # mask_list
        self.btn_mask_list_load.clicked.connect(self.mask_list_load)
        self.btn_mask_list_clear.clicked.connect(self.mask_list_clear)
        self.btn_mask_list_add.clicked.connect(self.mask_list_add)

        self.btn_mask_list_evaluate.clicked.connect(
            lambda: self.mask_evaluate("mask_list")
        )
        self.btn_mask_list_apply.clicked.connect(lambda: self.mask_apply("mask_list"))

        # blemish
        self.btn_select_blemish.clicked.connect(self.select_blemish)
        self.btn_apply_blemish.clicked.connect(
            lambda: self.mask_evaluate("mask_blemish")
        )
        self.btn_mask_blemish_apply.clicked.connect(
            lambda: self.mask_apply("mask_blemish")
        )

        # mask_file
        self.btn_select_maskfile.clicked.connect(self.select_maskfile)
        self.btn_apply_maskfile.clicked.connect(lambda: self.mask_evaluate("mask_file"))
        self.btn_mask_file_apply.clicked.connect(lambda: self.mask_apply("mask_file"))

        # draw method / array
        self.btn_mask_draw_add.clicked.connect(self.add_drawing)
        self.btn_mask_draw_evaluate.clicked.connect(
            lambda: self.mask_evaluate("mask_draw")
        )
        self.btn_mask_draw_apply.clicked.connect(lambda: self.mask_apply("mask_draw"))

        # binary threshold
        self.btn_mask_threshold_evaluate.clicked.connect(
            lambda: self.mask_evaluate("mask_threshold")
        )
        self.btn_mask_threshold_apply.clicked.connect(
            lambda: self.mask_apply("mask_threshold")
        )
        self.checkBox_threshold_low_preset.currentIndexChanged.connect(
            lambda: self.update_threshold_preset("low")
        )
        self.checkBox_threshold_high_preset.currentIndexChanged.connect(
            lambda: self.update_threshold_preset("high")
        )

        # btn_mask_outlier_evaluate
        self.btn_mask_outlier_evaluate.clicked.connect(
            lambda: self.mask_evaluate("mask_outlier")
        )
        self.btn_mask_outlier_apply.clicked.connect(
            lambda: self.mask_apply("mask_outlier")
        )

        self.mask_outlier_hdl.setBackground((255, 255, 255))
        self.mp1.scene.sigMouseClicked.connect(self.mouse_clicked)

        # xmap constraint
        self.model = XmapConstraintsTableModel()
        self.tableView.setModel(self.model)
        self.btn_mask_param_add.clicked.connect(self.add_param_constraint)
        self.btn_mask_param_delete.clicked.connect(self.delete_param_constraint)

        self.btn_mask_param_evaluate.clicked.connect(
            lambda: self.mask_evaluate("mask_parameter")
        )
        self.btn_mask_param_apply.clicked.connect(
            lambda: self.mask_apply("mask_parameter")
        )

        self.work_dir = None
        if path is not None:
            path = os.path.abspath(path)
            if os.path.isfile(path):
                self.fname.setText(str(path))
                self.work_dir = os.path.dirname(path)
            elif os.path.isdir(path):
                self.work_dir = path
        else:
            self.work_dir = os.path.expanduser("~")

        self.MaskWidget.setCurrentIndex(0)
        header = self.tableView.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)
        self.tabWidget.setCurrentIndex(0)

        self.comboBox_partition_mapname0.currentIndexChanged.connect(
            self.update_partition_mapname
        )
        self.comboBox_partition_mapname1.currentIndexChanged.connect(
            self.update_partition_mapname
        )
        self.save_load_settings(mode="load")
        self.show()

    def update_partition_mapname(self):
        idx0 = self.comboBox_partition_mapname0.currentIndex()
        idx1 = self.comboBox_partition_mapname1.currentIndex()
        if idx0 == idx1:
            total_size = self.comboBox_partition_mapname1.count()
            new_idx = (idx0 + 1) % total_size
            self.comboBox_partition_mapname1.setCurrentIndex(new_idx)

    def mouse_clicked(self, event):
        if not event.double():
            return
        current_idx = self.MaskWidget.currentIndex()
        if current_idx not in [3, 5]:
            return

        if not self.mp1.scene.itemsBoundingRect().contains(event.pos()):
            return

        mouse_point = self.mp1.getView().mapSceneToView(event.pos())
        col = int(mouse_point.x())
        row = int(mouse_point.y())
        if current_idx == 3:
            # manual mode; select the dead pixel with mouse click
            if not self.mask_list_include.isChecked():
                self.mask_list_add_pts([np.array([col, row])])
            else:
                kwargs = {
                    "radius": self.mask_list_radius.value(),
                    "variation": self.mask_list_variation.value(),
                    "cen": (row, col),
                }
                pos = self.sm.get_pts_with_similar_intensity(**kwargs)
                self.mask_list_add_pts(pos)

    def mask_action(self, action):
        if not self.is_ready():
            return
        self.sm.mask_action(action)
        self.plot_index.setCurrentIndex(0)
        self.plot_index.setCurrentIndex(1)

    def find_center(self):
        if not self.is_ready():
            return
        try:
            self.btn_find_center.setText("Finding Center ...")
            self.btn_find_center.setDisabled(True)
            self.centralwidget.repaint()
            center_vh = self.sm.find_center()
        except Exception:
            traceback.print_exc()
            self.statusbar.showMessage("Failed to find center. Abort", 2000)
        else:
            cen_old = self.sm.get_center()
            self.update_parameters(new_center=center_vh)
            cen_new = self.sm.get_center()
            logger.info(f"found center: {cen_old} --> {cen_new}")
        finally:
            self.btn_find_center.setText("Find Center")
            self.btn_find_center.setEnabled(True)

    def mask_evaluate(self, target=None):
        if target is None or not self.is_ready():
            return

        if target == "mask_blemish":
            kwargs = {
                "fname": self.blemish_fname.text(),
                "key": self.blemish_path.text(),
            }
        elif target == "mask_file":
            kwargs = {
                "fname": self.maskfile_fname.text(),
                "key": self.maskfile_path.text(),
            }
        elif target == "mask_list":
            num_row = self.mask_list_xylist.count()
            val = [str(self.mask_list_xylist.item(i).text()) for i in range(num_row)]
            val = " ".join(val)
            xy = text_to_array(val)
            xy = xy[0 : xy.size // 2 * 2].reshape(-1, 2).T
            xy = np.roll(xy, shift=1, axis=0)
            kwargs = {"zero_loc": xy}
        elif target == "mask_draw":
            kwargs = {"arr": np.logical_not(self.sm.apply_drawing())}
        elif target == "mask_threshold":
            kwargs = {
                "low": self.binary_threshold_low.value(),
                "high": self.binary_threshold_high.value(),
                "low_enable": self.checkBox_threshold_low_enable.isChecked(),
                "high_enable": self.checkBox_threshold_high_enable.isChecked(),
            }

        elif target == "mask_outlier":
            num = self.outlier_num_roi.value()
            cutoff = self.outlier_cutoff.value()
            method = self.comboBox_outlier_method.currentText()
            method = {"percentile": "percentile", "median_absolute_deviation": "mad"}[
                method
            ]
            saxs1d, zero_loc = self.sm.compute_saxs1d(
                num=num, cutoff=cutoff, method=method
            )
            self.mask_outlier_hdl.clear()
            p = self.mask_outlier_hdl
            p.addLegend()
            p.plot(
                saxs1d[0],
                saxs1d[1],
                name="average_ref",
                pen=pg.mkPen(color="g", width=2),
            )
            # p.plot(saxs1d[0], saxs1d[4], name='average_raw',
            #        pen=pg.mkPen(color='m', width=2))
            p.plot(
                saxs1d[0], saxs1d[2], name="cutoff", pen=pg.mkPen(color="b", width=2)
            )
            p.plot(
                saxs1d[0],
                saxs1d[3],
                name="maximum value",
                pen=pg.mkPen(color="r", width=2),
            )
            p.setLabel("bottom", "q (Å⁻¹)")
            p.setLabel("left", "Intensity (a.u.)")
            p.setLogMode(y=True)
            kwargs = {"zero_loc": zero_loc}

        elif target == "mask_parameter":
            kwargs = {"constraints": self.model._data}

        msg = self.sm.mask_evaluate(target, **kwargs)
        self.statusbar.showMessage(msg, 10000)
        self.plot_index.setCurrentIndex(0)
        self.plot_index.setCurrentIndex(5)
        return

    def update_threshold_preset(self, target="low"):
        preset_value_mapping = {
            "None": None,
            "0": 0,
            "1": 1,
            "-1": -1,
            "uint8": 255,
            "int8": 127,
            "uint16": 65535,
            "int16": 32767,
            "uint32": 4294967295,
            "int32": 2147483647,
            "uint24": 16777215,
            "int24": 8388607,
        }
        if target == "low":
            key = self.checkBox_threshold_low_preset.currentText()
            if key != "None":
                self.binary_threshold_low.setValue(preset_value_mapping[key])
        elif target == "high":
            key = self.checkBox_threshold_high_preset.currentText()
            if key != "None":
                self.binary_threshold_high.setValue(preset_value_mapping[key])

    def mask_apply(self, target):
        if not self.is_ready():
            return

        self.sm.mask_apply(target)
        # perform evaluate again so the saxs1d shows the new results;
        if target == "mask_outlier":
            self.mask_evaluate(target=target)
        elif target == "mask_list":
            self.mask_list_clear()
        elif target == "mask_parameter":
            self.model.clear()

        self.plot_index.setCurrentIndex(0)
        self.plot_index.setCurrentIndex(1)

    def update_index(self):
        idx = self.mp1.currentIndex
        self.plot_index.setCurrentIndex(idx)
        # make the mask and preview binary
        if idx in [2, 5]:
            self.mp1.setLevels(0, 1)

    def is_ready(self):
        if not self.sm.is_ready():
            self.statusbar.showMessage("No scattering image is loaded.", 500)
            return False
        return True

    def update_parameters(self, swapxy=False, new_center=None):
        if not self.is_ready():
            return

        new_metadata = {}
        for name, widget_name in PVMAP.items():
            scale = 1e-6 if name == "pix_dim" else 1
            widget = getattr(self, widget_name)
            new_metadata[name] = widget.value() * scale

        if new_center:
            new_metadata["bcy"], new_metadata["bcx"] = new_center

        if swapxy:
            y, x = new_metadata["bcx"], new_metadata["bcy"]
            new_metadata["bcx"], new_metadata["bcy"] = x, y
            self.db_cenx.setValue(x)
            self.db_ceny.setValue(y)

        self.sm.update_parameters(new_metadata)
        self.display_metadata()
        self.groupBox.repaint()
        self.plot()

    def select_raw(self):
        default_dir = self.work_dir if self.work_dir else os.getcwd()

        fname = QFileDialog.getOpenFileName(
            self,
            caption="Select raw file hdf",
            dir=default_dir,  # <-- Fixed!
            filter="Supported Formats(*.hdf *.h5 *.hdf5 *.imm *.bin *.tif *.tiff *.fits *.raw, *.bin.*)",
        )[0]
        if fname:
            self.fname.setText(fname)
            self.work_dir = os.path.dirname(fname)
        return

    def select_blemish(self):
        fname = QFileDialog.getOpenFileName(
            self,
            "Select blemish file",
            filter="Supported Formats(*.tiff *.tif *.h5 *.hdf *.hdf5)",
        )[0]
        if fname not in [None, ""]:
            self.blemish_fname.setText(fname)

        if fname.endswith(".tif") or fname.endswith(".tiff"):
            self.blemish_path.setDisabled(True)
        else:
            self.blemish_path.setEnabled(True)

        return

    def select_maskfile(self):
        fname = QFileDialog.getOpenFileName(
            self,
            "Select mask file",
            filter="Supported Formats(*.tiff *.tif *.h5 *.hdf *.hdf5)",
        )[0]
        # fname = "../tests/data/triangle_mask/mask_lambda_test.h5"
        if fname not in [None, ""]:
            self.maskfile_fname.setText(fname)
        if fname.endswith(".tif") or fname.endswith(".tiff"):
            self.maskfile_path.setDisabled(True)
        else:
            self.maskfile_path.setEnabled(True)
        return

    def load(self):
        # self.fname.setText('/mnt/c/Users/mqichu/Documents/local_dev/pysimplemask/tests/data/E0135_La0p65_L2_013C_att04_Rq0_00001/E0135_La0p65_L2_013C_att04_Rq0_00001_0001-100000.hdf')
        if not os.path.isfile(self.fname.text()):
            self.select_raw()
        if not os.path.isfile(self.fname.text()):
            self.statusbar.showMessage("select a valid file")
            return

        self.btn_load.setText("loading...")
        self.statusbar.showMessage("loading data...", 120000)
        self.centralwidget.repaint()

        fname = self.fname.text()
        kwargs = {
            "begin_idx": self.spinBox_3.value(),
            "num_frames": self.spinBox_4.value(),
            "beamline": self.comboBox_beamline.currentText(),
        }
        if not self.sm.read_data(fname, **kwargs):
            return
        else:
            stype = self.sm.dset.stype
            if stype == "Transmission":
                self.tabWidget_2.setCurrentIndex(0)
            elif stype == "Reflection":
                self.tabWidget_2.setCurrentIndex(1)

        for key in (
            "comboBox_param_xmap_name",
            "comboBox_partition_mapname0",
            "comboBox_partition_mapname1",
        ):
            widget = getattr(self, key)
            widget.clear()
            widget.addItems(list(self.sm.qmap.keys()))

        self.comboBox_param_xmap_name.currentIndexChanged.connect(
            self.update_xmap_limits
        )
        self.update_xmap_limits()

        while self.plot_index.count() > 6:
            self.plot_index.removeItem(6)
        for key in self.sm.qmap.keys():
            self.plot_index.addItem(key)

        self.display_metadata()
        self.plot()
        self.statusbar.showMessage("data is loaded", 500)
        self.btn_load.setText("load data")
        self.btn_load.repaint()

    def display_metadata(self):
        for label, widget_name in PVMAP.items():
            widget = getattr(self, widget_name)
            scale = 1e6 if label == "pix_dim" else 1
            widget.setValue(self.sm.dset.metadata[label] * scale)

        self.le_shape.setText(str(self.sm.shape))
        self.groupBox.repaint()

        param_struct = self.sm.dset.get_parametertree_structure()
        self.metadata_parameter = Parameter.create(**param_struct)
        self.metadata_parameter.sigTreeStateChanged.connect(
            self.update_parameter_to_dset
        )
        self.metadata_tree.setParameters(self.metadata_parameter, showTop=False)

    def update_parameter_to_dset(self, param, changes):
        self.sm.dset.update_metadata_from_changes(changes)

    def plot(self):
        kwargs = {
            "cmap": self.plot_cmap.currentText(),
            "log": self.plot_log.isChecked(),
            "plot_center": self.plot_center.isChecked(),
        }
        self.sm.show_saxs(**kwargs)
        self.plot_index.setCurrentIndex(1)

    def add_drawing(self):
        if not self.is_ready():
            return
        if self.MaskWidget.currentIndex() == 1:
            color = ("r", "g", "y", "b", "c", "m", "k", "w")[
                self.cb_selector_color.currentIndex()
            ]
            kwargs = {
                "color": color,
                "sl_type": self.cb_selector_type.currentText(),
                "sl_mode": self.cb_selector_mode.currentText(),
                "width": self.plot_width.value(),
                "num_edges": self.spinBox_num_edges.value(),
            }
        self.sm.add_drawing(**kwargs)
        return

    def update_xmap_limits(self):
        xmap_name = self.comboBox_param_xmap_name.currentText()
        if not xmap_name:
            return
        vmin, vmax = self.sm.qmap[xmap_name].min(), self.sm.qmap[xmap_name].max()
        unit = self.sm.qmap_unit[xmap_name]
        self.label_param_minval.setText(f"Min: {vmin:.4f} {unit}")
        self.label_param_maxval.setText(f"Max: {vmax:.4f} {unit}")
        self.doubleSpinBox_param_vbeg.setValue(vmin)
        self.doubleSpinBox_param_vend.setValue(vmax)

    def add_param_constraint(self):
        xmap_name = self.comboBox_param_xmap_name.currentText()
        if not xmap_name:
            return
        vbeg = self.doubleSpinBox_param_vbeg.value()
        vend = self.doubleSpinBox_param_vend.value()
        if vbeg > vend:
            vbeg, vend = vend, vbeg
            self.doubleSpinBox_param_vbeg.setValue(vbeg)
            self.doubleSpinBox_param_vend.setValue(vend)
        logic = self.comboBox_param_logic.currentText()
        unit = self.sm.qmap_unit[xmap_name]
        self.model.addRow([xmap_name, logic, unit, vbeg, vend])

    def delete_param_constraint(self):
        idx = self.tableView.currentIndex().row()
        self.model.removeRow(idx)

    # self.btn_mask_draw_apply_corr.clicked.connect(self.corr_add_roi)
    def corr_add_roi(self):
        roi = self.sm.apply_drawing()
        self.sm.set_corr_roi(roi)
        return

    def update_corr_angle(self):
        angle_deg = 360.0 / self.angle_n_corr.value()
        self.angle_corr_text.setText(f"{angle_deg:.2f} (deg)")

    def perform_correlation(self):
        angle = 2 * np.pi / self.angle_n_corr.value()
        self.sm.perform_correlation(angle)

    def compute_partition(self):
        if not self.is_ready():
            return

        def least_multiple(a: int, b: int) -> int:
            return ((b + a - 1) // a) * a

        if self.tabWidget.currentIndex() == 0:
            kwargs = {
                "mode": "q-phi",
                "sq_num": self.sb_sqnum.value(),
                "dq_num": self.sb_dqnum.value(),
                "sp_num": self.sb_spnum.value(),
                "dp_num": self.sb_dpnum.value(),
                "phi_offset": self.doubleSpinBox_phi_offset.value(),
                "style": self.partition_style.currentText(),
                "symmetry_fold": self.spinBox_symmetry_fold.value(),
            }
        elif self.tabWidget.currentIndex() == 1:
            kwargs = {
                "mode": "x-y",
                "sq_num": self.sb_sxnum.value(),
                "sp_num": self.sb_synum.value(),
                "dq_num": self.sb_dxnum.value(),
                "dp_num": self.sb_dynum.value(),
            }
        elif self.tabWidget.currentIndex() == 2:
            map0 = self.comboBox_partition_mapname0.currentText()
            map1 = self.comboBox_partition_mapname1.currentText()
            kwargs = {
                "mode": f"{map0}-{map1}",
                "sq_num": self.sb_partition_sn0.value(),
                "sp_num": self.sb_partition_sn1.value(),
                "dq_num": self.sb_partition_dn0.value(),
                "dp_num": self.sb_partition_dn1.value(),
            }

        sq_num = least_multiple(kwargs["dq_num"], kwargs["sq_num"])
        sp_num = least_multiple(kwargs["dp_num"], kwargs["sp_num"])
        if sq_num != kwargs["sq_num"]:
            if self.tabWidget.currentIndex() == 0:
                self.sb_sqnum.setValue(sq_num)
            else:
                self.sb_sxnum.setValue(sq_num)
            kwargs["sq_num"] = sq_num
        if sp_num != kwargs["sp_num"]:
            if self.tabWidget.currentIndex() == 0:
                self.sb_spnum.setValue(sp_num)
            else:
                self.sb_synum.setValue(sp_num)
            kwargs["sp_num"] = sp_num

        self.btn_compute_qpartition.setDisabled(True)
        self.statusbar.showMessage("Computing partition ... ", 10000)
        self.centralwidget.repaint()

        try:
            self.sm.compute_partition(**kwargs)
            self.statusbar.showMessage("New partition is generated.", 1000)
            self.plot_index.setCurrentIndex(0)
            self.plot_index.setCurrentIndex(3)
        except Exception:
            traceback.print_exc()
        finally:
            self.btn_compute_qpartition.setEnabled(True)
            # self.btn_compute_qpartition.setStyleSheet("background-color: green")

    def save_mask(self):
        if not self.is_ready():
            return
        save_type = self.comboBox_output_type.currentText()
        if save_type == "Nexus-XPCS":
            save_fname = QFileDialog.getSaveFileName(
                self, caption="Save mask/qmap as", filter="HDF (*.hdf)"
            )[0]
            if not save_fname.endswith(".hdf"):
                save_fname += ".hdf"
            if self.sm.new_partition is None:
                self.compute_partition()
            target_function = self.sm.save_partition
        elif save_type == "Mask-Only":
            save_fname = QFileDialog.getSaveFileName(
                self, caption="Save mask as tif", filter="TIF (*.tif)"
            )[0]
            if not save_fname.endswith(".tif") and not save_fname.endswith(".tiff"):
                save_fname += ".tif"
            target_function = self.sm.save_mask
        elif save_type == "P10 FPGA":
            save_fname = QFileDialog.getSaveFileName(
                self, caption="Save mask as tif", filter="TIF (*.tif)"
            )[0]
            if not save_fname.endswith(".tif") and not save_fname.endswith(".tiff"):
                save_fname += ".tif"
            target_function = self.sm.save_fpga_partition

        try:
            target_function(save_fname)
            success_dialog = QMessageBox(self)
            success_dialog.setIcon(QMessageBox.Information)
            if save_type == "Nexus-XPCS":
                success_dialog.setText(
                    f"Successfully saved mask/qmap to file: {save_fname}"
                )
            else:
                success_dialog.setText(f"Successfully saved mask to file: {save_fname}")
            success_dialog.setDetailedText(save_fname)
            success_dialog.setWindowTitle("Success")
            success_dialog.exec()
        except Exception:
            error_message = traceback.format_exc()
            traceback.print_exc()
            error_dialog = QMessageBox(self)
            error_dialog.setIcon(QMessageBox.Critical)
            error_dialog.setText("Failed to save mask/qmap to file")
            error_dialog.setDetailedText(error_message)
            error_dialog.setWindowTitle("Error")
            error_dialog.exec()

    def mask_list_load(self):
        if not self.is_ready():
            return

        fname = QFileDialog.getOpenFileName(
            self,
            "Select mask file",
            filter="Text/Json (*.txt *.csv *.json);;All files(*.*)",
        )[0]
        if fname in ["", None]:
            return

        if fname.endswith(".json"):
            with open(fname, "r") as f:
                x = json.load(f)["Bad pixels"]
            xy = []
            for t in x:
                xy.append(t["Pixel"])
            xy = np.array(xy)
        elif fname.endswith(".txt") or fname.endswith(".csv"):
            try:
                xy = np.loadtxt(fname, delimiter=",")
            except ValueError:
                xy = np.loadtxt(fname)
            except Exception:
                self.statusbar.showMessage(
                    "only support csv and space separated file", 500
                )
                return

        if self.mask_list_rowcol.isChecked():
            xy = np.roll(xy, shift=1, axis=1)
        if self.mask_list_1based.isChecked():
            xy = xy - 1

        xy = xy.astype(np.int64)
        self.mask_list_add_pts(xy)

    def mask_list_add(self):
        pts = self.mask_list_input.text()
        self.mask_list_input.clear()
        if len(pts) < 1:
            self.statusbar.showMessage("Input list is almost empty.", 500)
            return

        xy = text_to_array(pts)
        xy = xy[0 : xy.size // 2 * 2].reshape(-1, 2)
        self.mask_list_add_pts(xy)

    def mask_list_add_pts(self, pts):
        for xy in pts:
            xy_str = str(xy)
            if xy_str not in self.sm.bad_pixel_set:
                self.mask_list_xylist.addItem(xy_str)
                self.sm.bad_pixel_set.add(xy_str)
        self.groupBox_11.setTitle("xy list: %d" % len(self.sm.bad_pixel_set))

    def mask_list_clear(self):
        self.sm.bad_pixel_set.clear()
        self.mask_list_xylist.clear()
        self.groupBox_11.setTitle("xy list")

    def save_load_settings(self, mode="save"):
        keys = [
            "comboBox_beamline",
        ]

        if mode == "save":
            config = {}
            # Save widget states
            for key in keys:
                widget = getattr(self, key, None)
                if isinstance(widget, QLineEdit):
                    config[key] = widget.text()
                elif isinstance(widget, QRadioButton):
                    config[key] = widget.isChecked()
                elif isinstance(widget, (QDoubleSpinBox, QSpinBox)):
                    config[key] = widget.value()
                elif isinstance(widget, QComboBox):
                    config[key] = widget.currentIndex()
                elif isinstance(widget, QCheckBox):
                    config[key] = widget.isChecked()
                elif isinstance(widget, QTabWidget):
                    config[key] = widget.currentIndex()

            with open(CONFIG_FILE, "w") as f:
                json.dump(config, f, indent=4)
            logger.info(f"Saved configuration to [{CONFIG_FILE}]")

        elif mode == "load":
            if CONFIG_FILE.is_file():
                logger.info(f"Loading configuration from [{CONFIG_FILE}]")
                with open(CONFIG_FILE, "r") as f:
                    config = json.load(f)

                for key, value in config.items():
                    widget = getattr(self, key, None)
                    if key == "main_geometry":
                        self.restoreGeometry(QByteArray.fromBase64(value.encode()))
                    elif key == "splitter_state" and hasattr(self, "splitter"):
                        self.splitter.restoreState(
                            QByteArray.fromBase64(value.encode())
                        )
                    elif key == "splitter_2_state" and hasattr(self, "splitter_2"):
                        self.splitter_2.restoreState(
                            QByteArray.fromBase64(value.encode())
                        )
                    elif isinstance(widget, QLineEdit):
                        widget.setText(value)
                    elif isinstance(widget, QRadioButton):
                        widget.setChecked(value)
                    elif isinstance(widget, (QDoubleSpinBox, QSpinBox)):
                        widget.setValue(value)
                    elif isinstance(widget, QComboBox):
                        widget.setCurrentIndex(value)
                    elif isinstance(widget, QCheckBox):
                        widget.setChecked(value)
                    elif isinstance(widget, QTabWidget):
                        widget.setCurrentIndex(value)
            else:
                logger.error(f"Configuration file [{CONFIG_FILE}] not found.")

    def closeEvent(self, event):
        self.save_load_settings(mode="save")
        event.accept()


def main_gui(path=None):
    # if os.name == 'nt':
    #     setup_windows_icon()
    # QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
    app = QApplication(sys.argv)
    window = SimpleMaskGUI(path)
    app.exec_()


if __name__ == "__main__":
    main_gui()
