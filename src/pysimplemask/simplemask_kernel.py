import logging
import os
import time

import h5py
import numpy as np
import pyqtgraph as pg
import tifffile
from pyqtgraph.Qt import QtCore

from pysimplemask import __version__

from .area_mask import MaskAssemble
from .file_handler import get_handler
from .find_center import find_center
from .outlier_removal import outlier_removal_with_saxs
from .pyqtgraph_mod import LineROI
from .utils import (check_consistency, combine_partitions, generate_partition,
                    hash_numpy_dict, optimize_integer_array)

pg.setConfigOptions(imageAxisOrder="row-major")


logger = logging.getLogger(__name__)


class SimpleMask(object):
    def __init__(self, pg_hdl, infobar):
        self.dset = None
        self.shape = None
        self.qmap = None
        self.mask = None
        self.mask_kernel = None
        self.new_partition = None

        self.hdl = pg_hdl
        self.infobar = infobar
        self.hdl.scene.sigMouseMoved.connect(self.show_location)
        self.bad_pixel_set = set()

    def is_ready(self):
        return self.dset is not None

    def find_center(self):
        if self.dset is None:
            return

        center_guess = self.get_center(mode="vh")
        center = find_center(
            self.dset.scat,
            mask=self.mask,
            center_guess=center_guess,
            scale="log",
        )
        return center

    def mask_evaluate(self, target, **kwargs):
        msg = self.mask_kernel.evaluate(target, **kwargs)
        # preview the mask
        mask = self.mask_kernel.get_one_mask(target)
        self.dset.set_preview(mask)
        return msg

    def mask_action(self, action="undo"):
        self.mask_kernel.redo_undo(action=action)
        self.mask_apply()

    def mask_apply(self, target=None):
        if target == "default_mask":
            self.mask = self.mask_kernel.apply_default_mask()
        else:
            # if target is None, apply will return the current mask
            self.mask = self.mask_kernel.apply(target)
        self.dset.update_mask(self.mask)

    def get_pts_with_similar_intensity(self, cen=None, radius=50, variation=50):
        return self.dset.get_pts_with_similar_intensity(cen, radius, variation)

    def save_mask(self, save_name):
        mask = self.mask.astype(np.uint8)
        tifffile.imwrite(save_name, mask, compression="LZW")

    def save_fpga_partition(self, save_name):
        # if no partition is computed yet
        if self.new_partition is None:
            return

        for key, val in self.new_partition.items():
            self.new_partition[key] = optimize_integer_array(val)

        def optimize_save(key, val):
            if isinstance(val, np.ndarray) and val.size > 1024:
                compression = "lzf"
            else:
                compression = None
            dset = group_handle.create_dataset(key, data=val, compression=compression)
            return dset

        for key, val in self.new_partition.items():
            print(f"key: {key}, val: {val}")
            # dset = optimize_save(key, val)

    def save_partition(self, save_fname, root="/qmap"):
        # if no partition is computed yet
        if self.new_partition is None:
            return

        for key, val in self.new_partition.items():
            self.new_partition[key] = optimize_integer_array(val)

        hash_val = hash_numpy_dict(self.new_partition)
        logger.info("Hash value of the partition: {}".format(hash_val))

        def optimize_save(group_handle, key, val):
            if isinstance(val, np.ndarray) and val.size > 1024:
                compression = "lzf"
            else:
                compression = None
            dset = group_handle.create_dataset(key, data=val, compression=compression)
            return dset

        with h5py.File(save_fname, "w") as hf:
            if root in hf:
                del hf[root]
            group_handle = hf.create_group(root)
            for key, val in self.new_partition.items():
                dset = optimize_save(group_handle, key, val)
                if "_v_list_dim" in key:
                    dim = int(key[-1])
                    dset.attrs["unit"] = self.new_partition["map_units"][dim]
                    dset.attrs["name"] = self.new_partition["map_names"][dim]
                    dset.attrs["size"] = val.size

            group_handle.attrs["hash"] = hash_val
            group_handle.attrs["version"] = __version__

    # generate 2d saxs
    def read_data(self, fname=None, beamline="APS_8IDI", **kwargs):
        self.dset = get_handler(beamline, fname)
        if self.dset is None:
            logger.error(f"failed to create a dataset handler for {fname}")
            return False

        t0 = time.perf_counter()
        self.dset.prepare_data(**kwargs)
        t1 = time.perf_counter()
        logger.info(f"data loaded in {t1 - t0: .1f} seconds")

        self.shape = self.dset.shape
        self.mask = np.ones(self.shape, dtype=bool)

        self.qmap, self.qmap_unit, _ = self.compute_qmap()
        self.mask_kernel = MaskAssemble(self.shape, self.dset.scat)
        self.mask_apply(target="default_mask")
        self.mask_kernel.update_qmap(self.qmap)
        return True

    def compute_qmap(self):
        return self.dset.get_qmap()

    def show_location(self, pos):
        if not self.hdl.scene.itemsBoundingRect().contains(pos) or self.shape is None:
            return
        mouse_point = self.hdl.getView().mapSceneToView(pos)
        idx = self.hdl.currentIndex
        col = int(mouse_point.x())
        row = int(mouse_point.y())
        msg = self.dset.get_coordinates(col, row, idx)
        if msg:
            self.infobar.clear()
            self.infobar.setText(msg)
        return None

    def show_saxs(
        self,
        cmap="jet",
        log=True,
        plot_center=True,
        plot_index=0,
        **kwargs,
    ):
        if self.dset is None:
            return
        self.hdl.clear()
        center = self.get_center()
        self.hdl.setImage(self.dset.data_display)
        self.hdl.adjust_viewbox()
        self.hdl.set_colormap(cmap)

        # plot center
        if plot_center:
            t = pg.ScatterPlotItem()
            t.addPoints(x=[center[0]], y=[center[1]], symbol="+", size=15)
            self.hdl.add_item(t, label="center")

        self.hdl.setCurrentIndex(plot_index)

        return

    def apply_drawing(self):
        if self.dset is None:
            return
        shape = self.dset.shape
        ones = np.ones((shape[0] + 1, shape[1] + 1), dtype=bool)
        mask_n = np.zeros_like(ones, dtype=bool)
        mask_e = np.zeros_like(mask_n)
        mask_i = np.zeros_like(mask_n)

        for k, x in self.hdl.roi.items():
            if not k.startswith("roi_"):
                continue

            mask_temp = np.zeros_like(ones, dtype=bool)
            # return slice and transfrom
            sl, _ = x.getArraySlice(self.dset.data_display[1], self.hdl.imageItem)
            y = x.getArrayRegion(ones, self.hdl.imageItem)

            # sometimes the roi size returned from getArraySlice and
            # getArrayRegion are different;
            nz_idx = np.nonzero(y)

            h_beg = np.min(nz_idx[1])
            h_end = np.max(nz_idx[1]) + 1

            v_beg = np.min(nz_idx[0])
            v_end = np.max(nz_idx[0]) + 1

            sl_v = slice(sl[0].start, sl[0].start + v_end - v_beg)
            sl_h = slice(sl[1].start, sl[1].start + h_end - h_beg)
            mask_temp[sl_v, sl_h] = y[v_beg:v_end, h_beg:h_end]

            if x.sl_mode == "exclusive":
                mask_e[mask_temp] = 1
            elif x.sl_mode == "inclusive":
                mask_i[mask_temp] = 1

        self.hdl.remove_rois(filter_str="roi_")

        if np.sum(mask_i) == 0:
            mask_i = 1

        mask_p = np.logical_not(mask_e) * mask_i
        mask_p = mask_p[:-1, :-1]

        return mask_p

    def add_drawing(
        self,
        num_edges=None,
        radius=60,
        color="r",
        sl_type="Polygon",
        width=3,
        sl_mode="exclusive",
        second_point=None,
        label=None,
        movable=True,
    ):
        # label: label of roi; default is None, which is for roi-draw
        if label is not None and label in self.hdl.roi:
            self.hdl.remove_item(label)

        cen = self.get_center()
        if cen[0] < 0 or cen[1] < 0 or cen[0] > self.shape[1] or cen[1] > self.shape[0]:
            logger.warning("beam center is out of range, use image center instead")
            cen = (self.shape[1] // 2, self.shape[0] // 2)

        if sl_mode == "inclusive":
            pen = pg.mkPen(color=color, width=width, style=QtCore.Qt.DotLine)
        else:
            pen = pg.mkPen(color=color, width=width)

        handle_pen = pg.mkPen(color=color, width=width)

        kwargs = {
            "pen": pen,
            "removable": True,
            "hoverPen": pen,
            "handlePen": handle_pen,
            "movable": movable,
        }
        if sl_type == "Ellipse":
            new_roi = pg.EllipseROI(cen, [60, 80], **kwargs)
            # add scale handle
            new_roi.addScaleHandle(
                [0.5, 0],
                [0.5, 1],
            )
            new_roi.addScaleHandle([0.5, 1], [0.5, 0])
            new_roi.addScaleHandle([0, 0.5], [1, 0.5])
            new_roi.addScaleHandle([1, 0.5], [0, 0.5])

        elif sl_type == "Circle":
            if second_point is not None:
                radius = np.sqrt(
                    (second_point[1] - cen[1]) ** 2 + (second_point[0] - cen[0]) ** 2
                )
            new_roi = pg.CircleROI(
                pos=[cen[0] - radius, cen[1] - radius], radius=radius, **kwargs
            )

        elif sl_type == "Polygon":
            if num_edges is None:
                num_edges = np.random.random_integers(6, 10)

            # add angle offset so that the new rois don't overlap with each
            # other
            offset = np.random.random_integers(0, 359)
            theta = np.linspace(0, np.pi * 2, num_edges + 1) + offset
            x = radius * np.cos(theta) + cen[0]
            y = radius * np.sin(theta) + cen[1]
            pts = np.vstack([x, y]).T
            new_roi = pg.PolyLineROI(pts, closed=True, **kwargs)

        elif sl_type == "Rectangle":
            new_roi = pg.RectROI(cen, [30, 150], **kwargs)
            new_roi.addScaleHandle([0, 0], [1, 1])
            # new_roi.addRotateHandle([0, 1], [0.5, 0.5])

        elif sl_type == "Line":
            if second_point is None:
                return
            width = kwargs.pop("width", 1)
            new_roi = LineROI(cen, second_point, width, **kwargs)
        else:
            raise TypeError("type not implemented. %s" % sl_type)

        new_roi.sl_mode = sl_mode
        roi_key = self.hdl.add_item(new_roi, label)
        new_roi.sigRemoveRequested.connect(lambda: self.remove_roi(roi_key))
        return new_roi

    def remove_roi(self, roi_key):
        self.hdl.remove_item(roi_key)

    def compute_saxs1d(self, method="percentile", cutoff=3.0, num=180):
        t0 = time.perf_counter()
        saxs_pack = generate_partition(
            "q", self.mask, self.qmap["q"], num, style="linear"
        )
        qlist, partition = saxs_pack["v_list"], saxs_pack["partition"]
        saxs1d, zero_loc = outlier_removal_with_saxs(
            qlist, partition, self.dset.scat, method=method, cutoff=cutoff
        )
        t1 = time.perf_counter()
        logger.info(
            "outlier removal with azimuthal average finished in %f seconds" % (t1 - t0)
        )
        return saxs1d, zero_loc

    def compute_partition(self, mode="q-phi", **kwargs):
        map_names = mode.split("-")
        logger.info(f"compute partition with mode {mode}: map_names {map_names}")
        t0 = time.perf_counter()
        flag = self.compute_partition_general(map_names=map_names, **kwargs)
        t1 = time.perf_counter()
        logger.info("compute partition finished in %f seconds" % (t1 - t0))
        return flag

    def compute_partition_general(
        self,
        map_names=("q", "phi"),
        dq_num=10,
        sq_num=100,
        style="linear",
        dp_num=36,
        sp_num=360,
        phi_offset=0.0,
        symmetry_fold=1,
    ):
        if self.dset is None:
            return

        # assert map_names in (("q", "phi"), ("x", "y"))
        name0, name1 = map_names
        #  generate dynamic partition
        pack_dq = generate_partition(
            name0, self.mask, self.qmap[name0], dq_num, style=style, phi_offset=None
        )
        pack_dp = generate_partition(
            name1,
            self.mask,
            self.qmap[name1],
            dp_num,
            style=style,
            phi_offset=phi_offset,
            symmetry_fold=symmetry_fold,
        )
        dynamic_map = combine_partitions(pack_dq, pack_dp, prefix="dynamic")

        # generate static partition
        pack_sq = generate_partition(
            name0, self.mask, self.qmap[name0], sq_num, style=style, phi_offset=None
        )
        pack_sp = generate_partition(
            name1,
            self.mask,
            self.qmap[name1],
            sp_num,
            style=style,
            phi_offset=phi_offset,
            symmetry_fold=symmetry_fold,
        )
        static_map = combine_partitions(pack_sq, pack_sp, prefix="static")

        # dump result to file;
        self.dset.update_partitions(
            dynamic_map["dynamic_roi_map"], static_map["static_roi_map"]
        )
        self.hdl.setCurrentIndex(3)

        flag_consistency = check_consistency(
            dynamic_map["dynamic_roi_map"], static_map["static_roi_map"], self.mask
        )
        logger.info("dqmap/sqmap consistency check: {}".format(flag_consistency))

        center = self.get_center()
        partition = {
            "beam_center_x": center[0],
            "beam_center_y": center[1],
            "pixel_size": self.dset.metadata["pix_dim"],
            "mask": self.mask,
            "energy": self.dset.metadata["energy"],
            "detector_distance": self.dset.metadata["det_dist"],
            "map_names": list(map_names),
            "map_units": [self.qmap_unit[name0], self.qmap_unit[name1]],
            "source_file": os.path.realpath(self.dset.fname),
        }
        partition.update(dynamic_map)
        partition.update(static_map)

        self.new_partition = partition
        return partition

    def update_parameters(self, new_metadata):
        self.dset.update_metadata(new_metadata)
        self.qmap, self.qmap_unit, _labels = self.compute_qmap()
        self.mask_kernel.update_qmap(self.qmap)

    def get_center(self, mode="xy"):
        if self.dset is None:
            return (None, None)
        else:
            assert mode in ("xy", "vh"), "mode must be either 'xy' or 'vh'"
            if mode == "xy":
                center = (self.dset.metadata["bcx"], self.dset.metadata["bcy"])
            elif mode == "vh":
                center = (self.dset.metadata["bcy"], self.dset.metadata["bcx"])
            return center


def test01():
    fname = "../data/H187_D100_att0_Rq0_00001_0001-100000.hdf"
    sm = SimpleMask()
    sm.read_data(fname)


if __name__ == "__main__":
    test01()
