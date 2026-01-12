# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mask.ui'
##
## Created by: Qt User Interface Compiler version 6.8.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDoubleSpinBox,
    QGridLayout, QGroupBox, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QListWidget, QListWidgetItem,
    QMainWindow, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QSpinBox, QSplitter, QStatusBar,
    QTabWidget, QTableView, QToolButton, QVBoxLayout,
    QWidget)

from .pyqtgraph_mod import ImageViewROI
from pyqtgraph import PlotWidget
from pyqtgraph.parametertree import ParameterTree

class Ui_SimpleMask(object):
    def setupUi(self, SimpleMask):
        if not SimpleMask.objectName():
            SimpleMask.setObjectName(u"SimpleMask")
        SimpleMask.resize(1687, 902)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SimpleMask.sizePolicy().hasHeightForWidth())
        SimpleMask.setSizePolicy(sizePolicy)
        SimpleMask.setMinimumSize(QSize(800, 600))
        SimpleMask.setMaximumSize(QSize(16777215, 16777215))
        self.centralwidget = QWidget(SimpleMask)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_16 = QGridLayout(self.centralwidget)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Orientation.Vertical)
        self.groupBox = QGroupBox(self.splitter)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(1)
        sizePolicy1.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy1)
        self.groupBox.setMaximumSize(QSize(600, 16777215))
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(1, 1, 1, 1)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.comboBox_beamline = QComboBox(self.groupBox)
        self.comboBox_beamline.addItem("")
        self.comboBox_beamline.addItem("")
        self.comboBox_beamline.addItem("")
        self.comboBox_beamline.addItem("")
        self.comboBox_beamline.setObjectName(u"comboBox_beamline")

        self.horizontalLayout.addWidget(self.comboBox_beamline)

        self.label_9 = QLabel(self.groupBox)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout.addWidget(self.label_9)

        self.spinBox_3 = QSpinBox(self.groupBox)
        self.spinBox_3.setObjectName(u"spinBox_3")
        self.spinBox_3.setMaximum(99999)

        self.horizontalLayout.addWidget(self.spinBox_3)

        self.label_28 = QLabel(self.groupBox)
        self.label_28.setObjectName(u"label_28")

        self.horizontalLayout.addWidget(self.label_28)

        self.spinBox_4 = QSpinBox(self.groupBox)
        self.spinBox_4.setObjectName(u"spinBox_4")
        self.spinBox_4.setMinimum(-1)
        self.spinBox_4.setMaximum(1000000)
        self.spinBox_4.setSingleStep(100)
        self.spinBox_4.setValue(-1)

        self.horizontalLayout.addWidget(self.spinBox_4)

        self.btn_load = QPushButton(self.groupBox)
        self.btn_load.setObjectName(u"btn_load")

        self.horizontalLayout.addWidget(self.btn_load)


        self.gridLayout_2.addLayout(self.horizontalLayout, 1, 0, 1, 1)

        self.tabWidget_2 = QTabWidget(self.groupBox)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tabWidget_2.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(1)
        sizePolicy2.setHeightForWidth(self.tabWidget_2.sizePolicy().hasHeightForWidth())
        self.tabWidget_2.setSizePolicy(sizePolicy2)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_10 = QGridLayout(self.tab)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.label_2 = QLabel(self.tab)
        self.label_2.setObjectName(u"label_2")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy3)

        self.gridLayout_10.addWidget(self.label_2, 0, 0, 1, 1)

        self.db_cenx = QDoubleSpinBox(self.tab)
        self.db_cenx.setObjectName(u"db_cenx")
        self.db_cenx.setEnabled(True)
        self.db_cenx.setDecimals(4)
        self.db_cenx.setMinimum(-9999.000000000000000)
        self.db_cenx.setMaximum(9999.000000000000000)

        self.gridLayout_10.addWidget(self.db_cenx, 0, 1, 1, 1)

        self.label_3 = QLabel(self.tab)
        self.label_3.setObjectName(u"label_3")
        sizePolicy3.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy3)

        self.gridLayout_10.addWidget(self.label_3, 0, 2, 1, 1)

        self.db_ceny = QDoubleSpinBox(self.tab)
        self.db_ceny.setObjectName(u"db_ceny")
        self.db_ceny.setEnabled(True)
        self.db_ceny.setDecimals(4)
        self.db_ceny.setMinimum(-9999.000000000000000)
        self.db_ceny.setMaximum(9999.000000000000000)

        self.gridLayout_10.addWidget(self.db_ceny, 0, 3, 1, 1)

        self.label_4 = QLabel(self.tab)
        self.label_4.setObjectName(u"label_4")
        sizePolicy3.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy3)

        self.gridLayout_10.addWidget(self.label_4, 1, 0, 1, 1)

        self.db_energy = QDoubleSpinBox(self.tab)
        self.db_energy.setObjectName(u"db_energy")
        self.db_energy.setEnabled(True)
        self.db_energy.setDecimals(4)

        self.gridLayout_10.addWidget(self.db_energy, 1, 1, 1, 1)

        self.label_5 = QLabel(self.tab)
        self.label_5.setObjectName(u"label_5")
        sizePolicy3.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy3)

        self.gridLayout_10.addWidget(self.label_5, 1, 2, 1, 1)

        self.db_det_dist = QDoubleSpinBox(self.tab)
        self.db_det_dist.setObjectName(u"db_det_dist")
        self.db_det_dist.setEnabled(True)
        self.db_det_dist.setDecimals(4)
        self.db_det_dist.setMaximum(99999.000000000000000)

        self.gridLayout_10.addWidget(self.db_det_dist, 1, 3, 1, 1)

        self.label_21 = QLabel(self.tab)
        self.label_21.setObjectName(u"label_21")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_21.sizePolicy().hasHeightForWidth())
        self.label_21.setSizePolicy(sizePolicy4)

        self.gridLayout_10.addWidget(self.label_21, 2, 0, 1, 1)

        self.det_rx = QDoubleSpinBox(self.tab)
        self.det_rx.setObjectName(u"det_rx")
        self.det_rx.setEnabled(True)
        self.det_rx.setDecimals(4)
        self.det_rx.setMinimum(-99.000000000000000)

        self.gridLayout_10.addWidget(self.det_rx, 2, 1, 1, 1)

        self.label_6 = QLabel(self.tab)
        self.label_6.setObjectName(u"label_6")
        sizePolicy3.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy3)

        self.gridLayout_10.addWidget(self.label_6, 2, 2, 1, 1)

        self.db_pix_dim = QDoubleSpinBox(self.tab)
        self.db_pix_dim.setObjectName(u"db_pix_dim")
        self.db_pix_dim.setEnabled(True)
        self.db_pix_dim.setDecimals(4)

        self.gridLayout_10.addWidget(self.db_pix_dim, 2, 3, 1, 1)

        self.label_35 = QLabel(self.tab)
        self.label_35.setObjectName(u"label_35")

        self.gridLayout_10.addWidget(self.label_35, 3, 0, 1, 1)

        self.det_ry = QDoubleSpinBox(self.tab)
        self.det_ry.setObjectName(u"det_ry")
        self.det_ry.setDecimals(4)
        self.det_ry.setMinimum(-99.000000000000000)

        self.gridLayout_10.addWidget(self.det_ry, 3, 1, 1, 1)

        self.label_7 = QLabel(self.tab)
        self.label_7.setObjectName(u"label_7")
        sizePolicy3.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy3)

        self.gridLayout_10.addWidget(self.label_7, 3, 2, 1, 1)

        self.le_shape = QLineEdit(self.tab)
        self.le_shape.setObjectName(u"le_shape")
        self.le_shape.setEnabled(True)
        sizePolicy3.setHeightForWidth(self.le_shape.sizePolicy().hasHeightForWidth())
        self.le_shape.setSizePolicy(sizePolicy3)

        self.gridLayout_10.addWidget(self.le_shape, 3, 3, 1, 1)

        self.label_40 = QLabel(self.tab)
        self.label_40.setObjectName(u"label_40")

        self.gridLayout_10.addWidget(self.label_40, 4, 0, 1, 1)

        self.det_rz = QDoubleSpinBox(self.tab)
        self.det_rz.setObjectName(u"det_rz")
        self.det_rz.setDecimals(4)
        self.det_rz.setMinimum(-99.000000000000000)

        self.gridLayout_10.addWidget(self.det_rz, 4, 1, 1, 1)

        self.tabWidget_2.addTab(self.tab, "")
        self.tab_7 = QWidget()
        self.tab_7.setObjectName(u"tab_7")
        self.gridLayout_26 = QGridLayout(self.tab_7)
        self.gridLayout_26.setObjectName(u"gridLayout_26")
        self.scrollArea = QScrollArea(self.tab_7)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 559, 145))
        self.gridLayout_29 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_29.setObjectName(u"gridLayout_29")
        self.gridLayout_29.setContentsMargins(0, 0, 0, 0)
        self.metadata_tree = ParameterTree(self.scrollAreaWidgetContents)
        self.metadata_tree.setObjectName(u"metadata_tree")

        self.gridLayout_29.addWidget(self.metadata_tree, 0, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_26.addWidget(self.scrollArea, 0, 0, 1, 1)

        self.tabWidget_2.addTab(self.tab_7, "")

        self.gridLayout_2.addWidget(self.tabWidget_2, 2, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_17 = QLabel(self.groupBox)
        self.label_17.setObjectName(u"label_17")

        self.horizontalLayout_2.addWidget(self.label_17)

        self.fname = QLineEdit(self.groupBox)
        self.fname.setObjectName(u"fname")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.fname.sizePolicy().hasHeightForWidth())
        self.fname.setSizePolicy(sizePolicy5)
        self.fname.setReadOnly(True)

        self.horizontalLayout_2.addWidget(self.fname)

        self.btn_select_raw = QToolButton(self.groupBox)
        self.btn_select_raw.setObjectName(u"btn_select_raw")

        self.horizontalLayout_2.addWidget(self.btn_select_raw)


        self.gridLayout_2.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.btn_swapxy = QPushButton(self.groupBox)
        self.btn_swapxy.setObjectName(u"btn_swapxy")

        self.horizontalLayout_3.addWidget(self.btn_swapxy)

        self.btn_find_center = QPushButton(self.groupBox)
        self.btn_find_center.setObjectName(u"btn_find_center")

        self.horizontalLayout_3.addWidget(self.btn_find_center)

        self.btn_update_parameters = QPushButton(self.groupBox)
        self.btn_update_parameters.setObjectName(u"btn_update_parameters")
        sizePolicy3.setHeightForWidth(self.btn_update_parameters.sizePolicy().hasHeightForWidth())
        self.btn_update_parameters.setSizePolicy(sizePolicy3)

        self.horizontalLayout_3.addWidget(self.btn_update_parameters)


        self.gridLayout_2.addLayout(self.horizontalLayout_3, 3, 0, 1, 1)

        self.splitter.addWidget(self.groupBox)
        self.groupBox_2 = QGroupBox(self.splitter)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(2)
        sizePolicy6.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy6)
        self.groupBox_2.setMaximumSize(QSize(600, 16777215))
        self.gridLayout_4 = QGridLayout(self.groupBox_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(1, 1, 1, 1)
        self.MaskWidget = QTabWidget(self.groupBox_2)
        self.MaskWidget.setObjectName(u"MaskWidget")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.MaskWidget.sizePolicy().hasHeightForWidth())
        self.MaskWidget.setSizePolicy(sizePolicy7)
        self.MaskWidget.setMaximumSize(QSize(16777215, 16777215))
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.gridLayout_25 = QGridLayout(self.tab_6)
        self.gridLayout_25.setObjectName(u"gridLayout_25")
        self.groupBox_7 = QGroupBox(self.tab_6)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.gridLayout_24 = QGridLayout(self.groupBox_7)
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.gridLayout_24.setContentsMargins(2, 2, 2, 2)
        self.gridLayout_9 = QGridLayout()
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.label_30 = QLabel(self.groupBox_7)
        self.label_30.setObjectName(u"label_30")
        sizePolicy8 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.label_30.sizePolicy().hasHeightForWidth())
        self.label_30.setSizePolicy(sizePolicy8)

        self.gridLayout_9.addWidget(self.label_30, 0, 0, 1, 1)

        self.blemish_fname = QLineEdit(self.groupBox_7)
        self.blemish_fname.setObjectName(u"blemish_fname")
        sizePolicy4.setHeightForWidth(self.blemish_fname.sizePolicy().hasHeightForWidth())
        self.blemish_fname.setSizePolicy(sizePolicy4)
        self.blemish_fname.setMinimumSize(QSize(300, 0))

        self.gridLayout_9.addWidget(self.blemish_fname, 0, 1, 1, 1)

        self.btn_select_blemish = QPushButton(self.groupBox_7)
        self.btn_select_blemish.setObjectName(u"btn_select_blemish")
        sizePolicy3.setHeightForWidth(self.btn_select_blemish.sizePolicy().hasHeightForWidth())
        self.btn_select_blemish.setSizePolicy(sizePolicy3)

        self.gridLayout_9.addWidget(self.btn_select_blemish, 0, 2, 1, 1)

        self.label_31 = QLabel(self.groupBox_7)
        self.label_31.setObjectName(u"label_31")
        sizePolicy8.setHeightForWidth(self.label_31.sizePolicy().hasHeightForWidth())
        self.label_31.setSizePolicy(sizePolicy8)

        self.gridLayout_9.addWidget(self.label_31, 1, 0, 1, 1)

        self.blemish_path = QLineEdit(self.groupBox_7)
        self.blemish_path.setObjectName(u"blemish_path")
        sizePolicy4.setHeightForWidth(self.blemish_path.sizePolicy().hasHeightForWidth())
        self.blemish_path.setSizePolicy(sizePolicy4)
        self.blemish_path.setMinimumSize(QSize(300, 0))

        self.gridLayout_9.addWidget(self.blemish_path, 1, 1, 1, 1)

        self.btn_apply_blemish = QPushButton(self.groupBox_7)
        self.btn_apply_blemish.setObjectName(u"btn_apply_blemish")
        sizePolicy9 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.btn_apply_blemish.sizePolicy().hasHeightForWidth())
        self.btn_apply_blemish.setSizePolicy(sizePolicy9)
        self.btn_apply_blemish.setMinimumSize(QSize(60, 0))

        self.gridLayout_9.addWidget(self.btn_apply_blemish, 1, 2, 1, 1)


        self.gridLayout_24.addLayout(self.gridLayout_9, 0, 0, 1, 1)

        self.btn_mask_blemish_apply = QPushButton(self.groupBox_7)
        self.btn_mask_blemish_apply.setObjectName(u"btn_mask_blemish_apply")
        sizePolicy9.setHeightForWidth(self.btn_mask_blemish_apply.sizePolicy().hasHeightForWidth())
        self.btn_mask_blemish_apply.setSizePolicy(sizePolicy9)
        self.btn_mask_blemish_apply.setMaximumSize(QSize(80, 16777215))

        self.gridLayout_24.addWidget(self.btn_mask_blemish_apply, 0, 1, 1, 1)


        self.gridLayout_25.addWidget(self.groupBox_7, 0, 0, 1, 1)

        self.groupBox_8 = QGroupBox(self.tab_6)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.gridLayout_17 = QGridLayout(self.groupBox_8)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.gridLayout_17.setContentsMargins(2, 2, 2, 2)
        self.gridLayout_12 = QGridLayout()
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.label_18 = QLabel(self.groupBox_8)
        self.label_18.setObjectName(u"label_18")
        sizePolicy8.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy8)

        self.gridLayout_12.addWidget(self.label_18, 0, 0, 1, 1)

        self.maskfile_fname = QLineEdit(self.groupBox_8)
        self.maskfile_fname.setObjectName(u"maskfile_fname")
        sizePolicy4.setHeightForWidth(self.maskfile_fname.sizePolicy().hasHeightForWidth())
        self.maskfile_fname.setSizePolicy(sizePolicy4)
        self.maskfile_fname.setMinimumSize(QSize(300, 0))

        self.gridLayout_12.addWidget(self.maskfile_fname, 0, 1, 1, 1)

        self.btn_select_maskfile = QPushButton(self.groupBox_8)
        self.btn_select_maskfile.setObjectName(u"btn_select_maskfile")
        sizePolicy3.setHeightForWidth(self.btn_select_maskfile.sizePolicy().hasHeightForWidth())
        self.btn_select_maskfile.setSizePolicy(sizePolicy3)

        self.gridLayout_12.addWidget(self.btn_select_maskfile, 0, 2, 1, 1)

        self.label_32 = QLabel(self.groupBox_8)
        self.label_32.setObjectName(u"label_32")
        sizePolicy7.setHeightForWidth(self.label_32.sizePolicy().hasHeightForWidth())
        self.label_32.setSizePolicy(sizePolicy7)

        self.gridLayout_12.addWidget(self.label_32, 1, 0, 1, 1)

        self.maskfile_path = QLineEdit(self.groupBox_8)
        self.maskfile_path.setObjectName(u"maskfile_path")
        sizePolicy4.setHeightForWidth(self.maskfile_path.sizePolicy().hasHeightForWidth())
        self.maskfile_path.setSizePolicy(sizePolicy4)
        self.maskfile_path.setMinimumSize(QSize(300, 0))

        self.gridLayout_12.addWidget(self.maskfile_path, 1, 1, 1, 1)

        self.btn_apply_maskfile = QPushButton(self.groupBox_8)
        self.btn_apply_maskfile.setObjectName(u"btn_apply_maskfile")
        sizePolicy9.setHeightForWidth(self.btn_apply_maskfile.sizePolicy().hasHeightForWidth())
        self.btn_apply_maskfile.setSizePolicy(sizePolicy9)
        self.btn_apply_maskfile.setMinimumSize(QSize(60, 0))

        self.gridLayout_12.addWidget(self.btn_apply_maskfile, 1, 2, 1, 1)


        self.gridLayout_17.addLayout(self.gridLayout_12, 1, 0, 1, 1)

        self.btn_mask_file_apply = QPushButton(self.groupBox_8)
        self.btn_mask_file_apply.setObjectName(u"btn_mask_file_apply")
        sizePolicy9.setHeightForWidth(self.btn_mask_file_apply.sizePolicy().hasHeightForWidth())
        self.btn_mask_file_apply.setSizePolicy(sizePolicy9)
        self.btn_mask_file_apply.setMaximumSize(QSize(80, 16777215))

        self.gridLayout_17.addWidget(self.btn_mask_file_apply, 1, 1, 1, 1)


        self.gridLayout_25.addWidget(self.groupBox_8, 1, 0, 1, 1)

        self.MaskWidget.addTab(self.tab_6, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_23 = QGridLayout(self.tab_2)
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.verticalSpacer = QSpacerItem(20, 120, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_23.addItem(self.verticalSpacer, 1, 0, 1, 1)

        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.label_14 = QLabel(self.tab_2)
        self.label_14.setObjectName(u"label_14")
        sizePolicy7.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy7)

        self.gridLayout_8.addWidget(self.label_14, 1, 0, 1, 1)

        self.label_8 = QLabel(self.tab_2)
        self.label_8.setObjectName(u"label_8")
        sizePolicy7.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy7)

        self.gridLayout_8.addWidget(self.label_8, 1, 2, 1, 1)

        self.btn_mask_draw_evaluate = QPushButton(self.tab_2)
        self.btn_mask_draw_evaluate.setObjectName(u"btn_mask_draw_evaluate")

        self.gridLayout_8.addWidget(self.btn_mask_draw_evaluate, 3, 2, 1, 1)

        self.plot_width = QSpinBox(self.tab_2)
        self.plot_width.setObjectName(u"plot_width")
        self.plot_width.setMinimum(1)
        self.plot_width.setValue(3)

        self.gridLayout_8.addWidget(self.plot_width, 1, 3, 1, 1)

        self.label_22 = QLabel(self.tab_2)
        self.label_22.setObjectName(u"label_22")

        self.gridLayout_8.addWidget(self.label_22, 0, 2, 1, 1)

        self.cb_selector_type = QComboBox(self.tab_2)
        self.cb_selector_type.addItem("")
        self.cb_selector_type.addItem("")
        self.cb_selector_type.addItem("")
        self.cb_selector_type.addItem("")
        self.cb_selector_type.setObjectName(u"cb_selector_type")

        self.gridLayout_8.addWidget(self.cb_selector_type, 0, 1, 1, 1)

        self.cb_selector_mode = QComboBox(self.tab_2)
        self.cb_selector_mode.addItem("")
        self.cb_selector_mode.addItem("")
        self.cb_selector_mode.setObjectName(u"cb_selector_mode")

        self.gridLayout_8.addWidget(self.cb_selector_mode, 0, 3, 1, 1)

        self.btn_mask_draw_apply = QPushButton(self.tab_2)
        self.btn_mask_draw_apply.setObjectName(u"btn_mask_draw_apply")

        self.gridLayout_8.addWidget(self.btn_mask_draw_apply, 3, 3, 1, 1)

        self.label_23 = QLabel(self.tab_2)
        self.label_23.setObjectName(u"label_23")

        self.gridLayout_8.addWidget(self.label_23, 0, 0, 1, 1)

        self.cb_selector_color = QComboBox(self.tab_2)
        self.cb_selector_color.addItem("")
        self.cb_selector_color.addItem("")
        self.cb_selector_color.addItem("")
        self.cb_selector_color.addItem("")
        self.cb_selector_color.addItem("")
        self.cb_selector_color.addItem("")
        self.cb_selector_color.addItem("")
        self.cb_selector_color.addItem("")
        self.cb_selector_color.setObjectName(u"cb_selector_color")

        self.gridLayout_8.addWidget(self.cb_selector_color, 1, 1, 1, 1)

        self.label_39 = QLabel(self.tab_2)
        self.label_39.setObjectName(u"label_39")

        self.gridLayout_8.addWidget(self.label_39, 2, 2, 1, 1)

        self.spinBox_num_edges = QSpinBox(self.tab_2)
        self.spinBox_num_edges.setObjectName(u"spinBox_num_edges")
        self.spinBox_num_edges.setMinimum(3)
        self.spinBox_num_edges.setMaximum(12)
        self.spinBox_num_edges.setValue(6)

        self.gridLayout_8.addWidget(self.spinBox_num_edges, 2, 3, 1, 1)

        self.btn_mask_draw_add = QPushButton(self.tab_2)
        self.btn_mask_draw_add.setObjectName(u"btn_mask_draw_add")

        self.gridLayout_8.addWidget(self.btn_mask_draw_add, 3, 0, 1, 2)


        self.gridLayout_23.addLayout(self.gridLayout_8, 0, 0, 1, 1)

        self.MaskWidget.addTab(self.tab_2, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.gridLayout_21 = QGridLayout(self.tab_4)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.btn_mask_threshold_apply = QPushButton(self.tab_4)
        self.btn_mask_threshold_apply.setObjectName(u"btn_mask_threshold_apply")

        self.gridLayout_21.addWidget(self.btn_mask_threshold_apply, 4, 1, 1, 1)

        self.groupBox_10 = QGroupBox(self.tab_4)
        self.groupBox_10.setObjectName(u"groupBox_10")
        self.groupBox_10.setEnabled(False)
        self.gridLayout_20 = QGridLayout(self.groupBox_10)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.gridLayout_20.setContentsMargins(2, 2, 2, 2)
        self.pushButton_9 = QPushButton(self.groupBox_10)
        self.pushButton_9.setObjectName(u"pushButton_9")

        self.gridLayout_20.addWidget(self.pushButton_9, 0, 1, 1, 1)

        self.pushButton_5 = QPushButton(self.groupBox_10)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.gridLayout_20.addWidget(self.pushButton_5, 0, 0, 1, 1)

        self.pushButton_15 = QPushButton(self.groupBox_10)
        self.pushButton_15.setObjectName(u"pushButton_15")

        self.gridLayout_20.addWidget(self.pushButton_15, 0, 3, 1, 1)

        self.pushButton_16 = QPushButton(self.groupBox_10)
        self.pushButton_16.setObjectName(u"pushButton_16")

        self.gridLayout_20.addWidget(self.pushButton_16, 0, 2, 1, 1)


        self.gridLayout_21.addWidget(self.groupBox_10, 3, 0, 1, 2)

        self.btn_mask_threshold_evaluate = QPushButton(self.tab_4)
        self.btn_mask_threshold_evaluate.setObjectName(u"btn_mask_threshold_evaluate")

        self.gridLayout_21.addWidget(self.btn_mask_threshold_evaluate, 4, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_21.addItem(self.verticalSpacer_3, 5, 1, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_21.addItem(self.verticalSpacer_4, 5, 0, 1, 1)

        self.groupBox_9 = QGroupBox(self.tab_4)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.gridLayout_15 = QGridLayout(self.groupBox_9)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.gridLayout_15.setContentsMargins(2, 2, 2, 2)
        self.label_26 = QLabel(self.groupBox_9)
        self.label_26.setObjectName(u"label_26")

        self.gridLayout_15.addWidget(self.label_26, 0, 2, 1, 1)

        self.checkBox_threshold_low_enable = QCheckBox(self.groupBox_9)
        self.checkBox_threshold_low_enable.setObjectName(u"checkBox_threshold_low_enable")
        self.checkBox_threshold_low_enable.setChecked(True)

        self.gridLayout_15.addWidget(self.checkBox_threshold_low_enable, 0, 3, 1, 1)

        self.binary_threshold_high = QDoubleSpinBox(self.groupBox_9)
        self.binary_threshold_high.setObjectName(u"binary_threshold_high")
        self.binary_threshold_high.setDecimals(2)
        self.binary_threshold_high.setMaximum(4294967296.000000000000000)
        self.binary_threshold_high.setValue(1024.000000000000000)

        self.gridLayout_15.addWidget(self.binary_threshold_high, 1, 6, 1, 1)

        self.checkBox_threshold_high_preset = QComboBox(self.groupBox_9)
        self.checkBox_threshold_high_preset.addItem("")
        self.checkBox_threshold_high_preset.addItem("")
        self.checkBox_threshold_high_preset.addItem("")
        self.checkBox_threshold_high_preset.addItem("")
        self.checkBox_threshold_high_preset.addItem("")
        self.checkBox_threshold_high_preset.addItem("")
        self.checkBox_threshold_high_preset.addItem("")
        self.checkBox_threshold_high_preset.addItem("")
        self.checkBox_threshold_high_preset.addItem("")
        self.checkBox_threshold_high_preset.setObjectName(u"checkBox_threshold_high_preset")

        self.gridLayout_15.addWidget(self.checkBox_threshold_high_preset, 1, 4, 1, 1)

        self.binary_threshold_low = QDoubleSpinBox(self.groupBox_9)
        self.binary_threshold_low.setObjectName(u"binary_threshold_low")
        self.binary_threshold_low.setMinimum(-9999.000000000000000)
        self.binary_threshold_low.setMaximum(10000.000000000000000)

        self.gridLayout_15.addWidget(self.binary_threshold_low, 0, 6, 1, 1)

        self.label_27 = QLabel(self.groupBox_9)
        self.label_27.setObjectName(u"label_27")
        sizePolicy3.setHeightForWidth(self.label_27.sizePolicy().hasHeightForWidth())
        self.label_27.setSizePolicy(sizePolicy3)

        self.gridLayout_15.addWidget(self.label_27, 1, 2, 1, 1)

        self.checkBox_threshold_high_enable = QCheckBox(self.groupBox_9)
        self.checkBox_threshold_high_enable.setObjectName(u"checkBox_threshold_high_enable")
        self.checkBox_threshold_high_enable.setChecked(True)

        self.gridLayout_15.addWidget(self.checkBox_threshold_high_enable, 1, 3, 1, 1)

        self.checkBox_threshold_low_preset = QComboBox(self.groupBox_9)
        self.checkBox_threshold_low_preset.addItem("")
        self.checkBox_threshold_low_preset.addItem("")
        self.checkBox_threshold_low_preset.addItem("")
        self.checkBox_threshold_low_preset.addItem("")
        self.checkBox_threshold_low_preset.setObjectName(u"checkBox_threshold_low_preset")

        self.gridLayout_15.addWidget(self.checkBox_threshold_low_preset, 0, 4, 1, 1)

        self.label_25 = QLabel(self.groupBox_9)
        self.label_25.setObjectName(u"label_25")
        sizePolicy8.setHeightForWidth(self.label_25.sizePolicy().hasHeightForWidth())
        self.label_25.setSizePolicy(sizePolicy8)

        self.gridLayout_15.addWidget(self.label_25, 0, 5, 1, 1)

        self.label_33 = QLabel(self.groupBox_9)
        self.label_33.setObjectName(u"label_33")
        sizePolicy8.setHeightForWidth(self.label_33.sizePolicy().hasHeightForWidth())
        self.label_33.setSizePolicy(sizePolicy8)

        self.gridLayout_15.addWidget(self.label_33, 1, 5, 1, 1)


        self.gridLayout_21.addWidget(self.groupBox_9, 0, 0, 1, 2)

        self.MaskWidget.addTab(self.tab_4, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout_5 = QGridLayout(self.tab_3)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.groupBox_12 = QGroupBox(self.tab_3)
        self.groupBox_12.setObjectName(u"groupBox_12")
        sizePolicy4.setHeightForWidth(self.groupBox_12.sizePolicy().hasHeightForWidth())
        self.groupBox_12.setSizePolicy(sizePolicy4)
        self.gridLayout_18 = QGridLayout(self.groupBox_12)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.gridLayout_18.setContentsMargins(2, 2, 2, 2)
        self.mask_list_1based = QCheckBox(self.groupBox_12)
        self.mask_list_1based.setObjectName(u"mask_list_1based")

        self.gridLayout_18.addWidget(self.mask_list_1based, 0, 0, 1, 1)

        self.mask_list_rowcol = QCheckBox(self.groupBox_12)
        self.mask_list_rowcol.setObjectName(u"mask_list_rowcol")

        self.gridLayout_18.addWidget(self.mask_list_rowcol, 0, 1, 1, 1)

        self.btn_mask_list_load = QPushButton(self.groupBox_12)
        self.btn_mask_list_load.setObjectName(u"btn_mask_list_load")

        self.gridLayout_18.addWidget(self.btn_mask_list_load, 0, 2, 1, 1)


        self.gridLayout_5.addWidget(self.groupBox_12, 0, 0, 1, 1)

        self.groupBox_13 = QGroupBox(self.tab_3)
        self.groupBox_13.setObjectName(u"groupBox_13")
        sizePolicy4.setHeightForWidth(self.groupBox_13.sizePolicy().hasHeightForWidth())
        self.groupBox_13.setSizePolicy(sizePolicy4)
        self.gridLayout_19 = QGridLayout(self.groupBox_13)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.gridLayout_19.setContentsMargins(2, 2, 2, 2)
        self.btn_mask_list_add = QPushButton(self.groupBox_13)
        self.btn_mask_list_add.setObjectName(u"btn_mask_list_add")
        sizePolicy9.setHeightForWidth(self.btn_mask_list_add.sizePolicy().hasHeightForWidth())
        self.btn_mask_list_add.setSizePolicy(sizePolicy9)

        self.gridLayout_19.addWidget(self.btn_mask_list_add, 0, 1, 1, 1)

        self.mask_list_input = QLineEdit(self.groupBox_13)
        self.mask_list_input.setObjectName(u"mask_list_input")
        sizePolicy4.setHeightForWidth(self.mask_list_input.sizePolicy().hasHeightForWidth())
        self.mask_list_input.setSizePolicy(sizePolicy4)
        self.mask_list_input.setMinimumSize(QSize(120, 0))

        self.gridLayout_19.addWidget(self.mask_list_input, 0, 0, 1, 1)


        self.gridLayout_5.addWidget(self.groupBox_13, 0, 1, 1, 1)

        self.groupBox_14 = QGroupBox(self.tab_3)
        self.groupBox_14.setObjectName(u"groupBox_14")
        sizePolicy10 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.groupBox_14.sizePolicy().hasHeightForWidth())
        self.groupBox_14.setSizePolicy(sizePolicy10)
        self.gridLayout_27 = QGridLayout(self.groupBox_14)
        self.gridLayout_27.setObjectName(u"gridLayout_27")
        self.gridLayout_27.setContentsMargins(2, 2, 2, 2)
        self.mask_list_include = QCheckBox(self.groupBox_14)
        self.mask_list_include.setObjectName(u"mask_list_include")
        self.mask_list_include.setChecked(True)

        self.gridLayout_27.addWidget(self.mask_list_include, 0, 1, 1, 2)

        self.label_24 = QLabel(self.groupBox_14)
        self.label_24.setObjectName(u"label_24")

        self.gridLayout_27.addWidget(self.label_24, 2, 1, 1, 1)

        self.mask_list_variation = QDoubleSpinBox(self.groupBox_14)
        self.mask_list_variation.setObjectName(u"mask_list_variation")
        self.mask_list_variation.setMinimum(1.000000000000000)
        self.mask_list_variation.setValue(80.000000000000000)

        self.gridLayout_27.addWidget(self.mask_list_variation, 2, 2, 1, 1)

        self.mask_list_radius = QDoubleSpinBox(self.groupBox_14)
        self.mask_list_radius.setObjectName(u"mask_list_radius")
        self.mask_list_radius.setMinimum(10.000000000000000)
        self.mask_list_radius.setMaximum(1000.000000000000000)
        self.mask_list_radius.setValue(50.000000000000000)

        self.gridLayout_27.addWidget(self.mask_list_radius, 1, 2, 1, 1)

        self.label_19 = QLabel(self.groupBox_14)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout_27.addWidget(self.label_19, 1, 1, 1, 1)


        self.gridLayout_5.addWidget(self.groupBox_14, 2, 0, 1, 2)

        self.groupBox_11 = QGroupBox(self.tab_3)
        self.groupBox_11.setObjectName(u"groupBox_11")
        sizePolicy.setHeightForWidth(self.groupBox_11.sizePolicy().hasHeightForWidth())
        self.groupBox_11.setSizePolicy(sizePolicy)
        self.gridLayout_22 = QGridLayout(self.groupBox_11)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.gridLayout_22.setContentsMargins(2, 2, 2, 2)
        self.mask_list_xylist = QListWidget(self.groupBox_11)
        self.mask_list_xylist.setObjectName(u"mask_list_xylist")
        sizePolicy11 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy11.setHorizontalStretch(0)
        sizePolicy11.setVerticalStretch(0)
        sizePolicy11.setHeightForWidth(self.mask_list_xylist.sizePolicy().hasHeightForWidth())
        self.mask_list_xylist.setSizePolicy(sizePolicy11)
        self.mask_list_xylist.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_22.addWidget(self.mask_list_xylist, 0, 0, 3, 6)

        self.btn_mask_list_apply = QPushButton(self.groupBox_11)
        self.btn_mask_list_apply.setObjectName(u"btn_mask_list_apply")
        sizePolicy9.setHeightForWidth(self.btn_mask_list_apply.sizePolicy().hasHeightForWidth())
        self.btn_mask_list_apply.setSizePolicy(sizePolicy9)

        self.gridLayout_22.addWidget(self.btn_mask_list_apply, 3, 5, 1, 1)

        self.btn_mask_list_evaluate = QPushButton(self.groupBox_11)
        self.btn_mask_list_evaluate.setObjectName(u"btn_mask_list_evaluate")
        sizePolicy9.setHeightForWidth(self.btn_mask_list_evaluate.sizePolicy().hasHeightForWidth())
        self.btn_mask_list_evaluate.setSizePolicy(sizePolicy9)

        self.gridLayout_22.addWidget(self.btn_mask_list_evaluate, 3, 0, 1, 1)

        self.btn_mask_list_clear = QPushButton(self.groupBox_11)
        self.btn_mask_list_clear.setObjectName(u"btn_mask_list_clear")
        sizePolicy9.setHeightForWidth(self.btn_mask_list_clear.sizePolicy().hasHeightForWidth())
        self.btn_mask_list_clear.setSizePolicy(sizePolicy9)

        self.gridLayout_22.addWidget(self.btn_mask_list_clear, 3, 1, 1, 1)


        self.gridLayout_5.addWidget(self.groupBox_11, 3, 0, 1, 2)

        self.MaskWidget.addTab(self.tab_3, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.gridLayout_14 = QGridLayout(self.tab_5)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.mask_outlier_hdl = PlotWidget(self.tab_5)
        self.mask_outlier_hdl.setObjectName(u"mask_outlier_hdl")
        sizePolicy12 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy12.setHorizontalStretch(0)
        sizePolicy12.setVerticalStretch(0)
        sizePolicy12.setHeightForWidth(self.mask_outlier_hdl.sizePolicy().hasHeightForWidth())
        self.mask_outlier_hdl.setSizePolicy(sizePolicy12)
        self.mask_outlier_hdl.setMinimumSize(QSize(0, 0))

        self.gridLayout_14.addWidget(self.mask_outlier_hdl, 1, 0, 1, 1)

        self.gridLayout_13 = QGridLayout()
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.label_16 = QLabel(self.tab_5)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout_13.addWidget(self.label_16, 0, 0, 1, 1)

        self.outlier_num_roi = QSpinBox(self.tab_5)
        self.outlier_num_roi.setObjectName(u"outlier_num_roi")
        self.outlier_num_roi.setMaximum(2000)
        self.outlier_num_roi.setValue(400)

        self.gridLayout_13.addWidget(self.outlier_num_roi, 0, 1, 1, 1)

        self.label_15 = QLabel(self.tab_5)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_13.addWidget(self.label_15, 0, 2, 1, 2)

        self.outlier_cutoff = QDoubleSpinBox(self.tab_5)
        self.outlier_cutoff.setObjectName(u"outlier_cutoff")
        self.outlier_cutoff.setMaximum(999.000000000000000)
        self.outlier_cutoff.setSingleStep(0.100000000000000)
        self.outlier_cutoff.setValue(10.000000000000000)

        self.gridLayout_13.addWidget(self.outlier_cutoff, 0, 4, 1, 2)

        self.label_44 = QLabel(self.tab_5)
        self.label_44.setObjectName(u"label_44")

        self.gridLayout_13.addWidget(self.label_44, 1, 0, 1, 1)

        self.btn_mask_outlier_apply = QPushButton(self.tab_5)
        self.btn_mask_outlier_apply.setObjectName(u"btn_mask_outlier_apply")

        self.gridLayout_13.addWidget(self.btn_mask_outlier_apply, 1, 5, 1, 1)

        self.btn_mask_outlier_evaluate = QPushButton(self.tab_5)
        self.btn_mask_outlier_evaluate.setObjectName(u"btn_mask_outlier_evaluate")

        self.gridLayout_13.addWidget(self.btn_mask_outlier_evaluate, 1, 4, 1, 1)

        self.comboBox_outlier_method = QComboBox(self.tab_5)
        self.comboBox_outlier_method.addItem("")
        self.comboBox_outlier_method.addItem("")
        self.comboBox_outlier_method.setObjectName(u"comboBox_outlier_method")

        self.gridLayout_13.addWidget(self.comboBox_outlier_method, 1, 1, 1, 3)


        self.gridLayout_14.addLayout(self.gridLayout_13, 0, 0, 1, 1)

        self.MaskWidget.addTab(self.tab_5, "")
        self.tab6 = QWidget()
        self.tab6.setObjectName(u"tab6")
        self.gridLayout_28 = QGridLayout(self.tab6)
        self.gridLayout_28.setObjectName(u"gridLayout_28")
        self.tableView = QTableView(self.tab6)
        self.tableView.setObjectName(u"tableView")
        sizePolicy2.setHeightForWidth(self.tableView.sizePolicy().hasHeightForWidth())
        self.tableView.setSizePolicy(sizePolicy2)

        self.gridLayout_28.addWidget(self.tableView, 2, 0, 1, 5)

        self.comboBox_param_logic = QComboBox(self.tab6)
        self.comboBox_param_logic.addItem("")
        self.comboBox_param_logic.addItem("")
        self.comboBox_param_logic.addItem("")
        self.comboBox_param_logic.setObjectName(u"comboBox_param_logic")

        self.gridLayout_28.addWidget(self.comboBox_param_logic, 3, 0, 1, 1)

        self.btn_mask_param_evaluate = QPushButton(self.tab6)
        self.btn_mask_param_evaluate.setObjectName(u"btn_mask_param_evaluate")
        sizePolicy4.setHeightForWidth(self.btn_mask_param_evaluate.sizePolicy().hasHeightForWidth())
        self.btn_mask_param_evaluate.setSizePolicy(sizePolicy4)

        self.gridLayout_28.addWidget(self.btn_mask_param_evaluate, 3, 3, 1, 1)

        self.btn_mask_param_apply = QPushButton(self.tab6)
        self.btn_mask_param_apply.setObjectName(u"btn_mask_param_apply")
        sizePolicy4.setHeightForWidth(self.btn_mask_param_apply.sizePolicy().hasHeightForWidth())
        self.btn_mask_param_apply.setSizePolicy(sizePolicy4)

        self.gridLayout_28.addWidget(self.btn_mask_param_apply, 3, 4, 1, 1)

        self.btn_mask_param_delete = QPushButton(self.tab6)
        self.btn_mask_param_delete.setObjectName(u"btn_mask_param_delete")
        sizePolicy4.setHeightForWidth(self.btn_mask_param_delete.sizePolicy().hasHeightForWidth())
        self.btn_mask_param_delete.setSizePolicy(sizePolicy4)

        self.gridLayout_28.addWidget(self.btn_mask_param_delete, 3, 2, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_29 = QLabel(self.tab6)
        self.label_29.setObjectName(u"label_29")
        sizePolicy13 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy13.setHorizontalStretch(0)
        sizePolicy13.setVerticalStretch(0)
        sizePolicy13.setHeightForWidth(self.label_29.sizePolicy().hasHeightForWidth())
        self.label_29.setSizePolicy(sizePolicy13)

        self.horizontalLayout_4.addWidget(self.label_29)

        self.comboBox_param_xmap_name = QComboBox(self.tab6)
        self.comboBox_param_xmap_name.setObjectName(u"comboBox_param_xmap_name")

        self.horizontalLayout_4.addWidget(self.comboBox_param_xmap_name)

        self.label_param_minval = QLabel(self.tab6)
        self.label_param_minval.setObjectName(u"label_param_minval")
        sizePolicy11.setHeightForWidth(self.label_param_minval.sizePolicy().hasHeightForWidth())
        self.label_param_minval.setSizePolicy(sizePolicy11)

        self.horizontalLayout_4.addWidget(self.label_param_minval)

        self.doubleSpinBox_param_vbeg = QDoubleSpinBox(self.tab6)
        self.doubleSpinBox_param_vbeg.setObjectName(u"doubleSpinBox_param_vbeg")
        self.doubleSpinBox_param_vbeg.setDecimals(5)
        self.doubleSpinBox_param_vbeg.setMinimum(-99999.000000000000000)
        self.doubleSpinBox_param_vbeg.setMaximum(99999.000000000000000)
        self.doubleSpinBox_param_vbeg.setValue(0.000000000000000)

        self.horizontalLayout_4.addWidget(self.doubleSpinBox_param_vbeg)

        self.label_param_maxval = QLabel(self.tab6)
        self.label_param_maxval.setObjectName(u"label_param_maxval")
        sizePolicy11.setHeightForWidth(self.label_param_maxval.sizePolicy().hasHeightForWidth())
        self.label_param_maxval.setSizePolicy(sizePolicy11)

        self.horizontalLayout_4.addWidget(self.label_param_maxval)

        self.doubleSpinBox_param_vend = QDoubleSpinBox(self.tab6)
        self.doubleSpinBox_param_vend.setObjectName(u"doubleSpinBox_param_vend")
        self.doubleSpinBox_param_vend.setDecimals(5)
        self.doubleSpinBox_param_vend.setMinimum(-9999.000000000000000)
        self.doubleSpinBox_param_vend.setMaximum(9999.000000000000000)
        self.doubleSpinBox_param_vend.setValue(0.004200000000000)

        self.horizontalLayout_4.addWidget(self.doubleSpinBox_param_vend)


        self.gridLayout_28.addLayout(self.horizontalLayout_4, 0, 0, 1, 5)

        self.btn_mask_param_add = QPushButton(self.tab6)
        self.btn_mask_param_add.setObjectName(u"btn_mask_param_add")
        sizePolicy4.setHeightForWidth(self.btn_mask_param_add.sizePolicy().hasHeightForWidth())
        self.btn_mask_param_add.setSizePolicy(sizePolicy4)

        self.gridLayout_28.addWidget(self.btn_mask_param_add, 3, 1, 1, 1)

        self.label_42 = QLabel(self.tab6)
        self.label_42.setObjectName(u"label_42")

        self.gridLayout_28.addWidget(self.label_42, 1, 0, 1, 5)

        self.MaskWidget.addTab(self.tab6, "")

        self.gridLayout_4.addWidget(self.MaskWidget, 1, 0, 1, 3)

        self.btn_mask_reset = QPushButton(self.groupBox_2)
        self.btn_mask_reset.setObjectName(u"btn_mask_reset")

        self.gridLayout_4.addWidget(self.btn_mask_reset, 2, 0, 1, 1)

        self.btn_mask_undo = QPushButton(self.groupBox_2)
        self.btn_mask_undo.setObjectName(u"btn_mask_undo")

        self.gridLayout_4.addWidget(self.btn_mask_undo, 2, 1, 1, 1)

        self.btn_mask_redo = QPushButton(self.groupBox_2)
        self.btn_mask_redo.setObjectName(u"btn_mask_redo")

        self.gridLayout_4.addWidget(self.btn_mask_redo, 2, 2, 1, 1)

        self.splitter.addWidget(self.groupBox_2)

        self.gridLayout_16.addWidget(self.splitter, 0, 0, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBox_5 = QGroupBox(self.centralwidget)
        self.groupBox_5.setObjectName(u"groupBox_5")
        sizePolicy14 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        sizePolicy14.setHorizontalStretch(1)
        sizePolicy14.setVerticalStretch(1)
        sizePolicy14.setHeightForWidth(self.groupBox_5.sizePolicy().hasHeightForWidth())
        self.groupBox_5.setSizePolicy(sizePolicy14)
        self.groupBox_5.setMinimumSize(QSize(800, 0))
        self.gridLayout = QGridLayout(self.groupBox_5)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(1, 1, 1, 1)
        self.plot_index = QComboBox(self.groupBox_5)
        self.plot_index.addItem("")
        self.plot_index.addItem("")
        self.plot_index.addItem("")
        self.plot_index.addItem("")
        self.plot_index.addItem("")
        self.plot_index.addItem("")
        self.plot_index.setObjectName(u"plot_index")
        sizePolicy9.setHeightForWidth(self.plot_index.sizePolicy().hasHeightForWidth())
        self.plot_index.setSizePolicy(sizePolicy9)

        self.gridLayout.addWidget(self.plot_index, 0, 0, 1, 1)

        self.label_11 = QLabel(self.groupBox_5)
        self.label_11.setObjectName(u"label_11")
        sizePolicy8.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy8)

        self.gridLayout.addWidget(self.label_11, 0, 1, 1, 1)

        self.infobar = QLineEdit(self.groupBox_5)
        self.infobar.setObjectName(u"infobar")

        self.gridLayout.addWidget(self.infobar, 0, 2, 1, 1)

        self.mp1 = ImageViewROI(self.groupBox_5)
        self.mp1.setObjectName(u"mp1")
        sizePolicy15 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy15.setHorizontalStretch(4)
        sizePolicy15.setVerticalStretch(0)
        sizePolicy15.setHeightForWidth(self.mp1.sizePolicy().hasHeightForWidth())
        self.mp1.setSizePolicy(sizePolicy15)
        self.mp1.setMinimumSize(QSize(400, 0))

        self.gridLayout.addWidget(self.mp1, 1, 0, 1, 3)

        self.groupBox_4 = QGroupBox(self.groupBox_5)
        self.groupBox_4.setObjectName(u"groupBox_4")
        sizePolicy3.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy3)
        self.gridLayout_3 = QGridLayout(self.groupBox_4)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(1, 1, 1, 1)
        self.plot_center = QCheckBox(self.groupBox_4)
        self.plot_center.setObjectName(u"plot_center")
        self.plot_center.setChecked(True)

        self.gridLayout_3.addWidget(self.plot_center, 0, 0, 1, 1)

        self.plot_log = QCheckBox(self.groupBox_4)
        self.plot_log.setObjectName(u"plot_log")
        self.plot_log.setChecked(True)

        self.gridLayout_3.addWidget(self.plot_log, 0, 1, 1, 1)

        self.plot_cmap = QComboBox(self.groupBox_4)
        self.plot_cmap.addItem("")
        self.plot_cmap.addItem("")
        self.plot_cmap.addItem("")
        self.plot_cmap.addItem("")
        self.plot_cmap.addItem("")
        self.plot_cmap.addItem("")
        self.plot_cmap.addItem("")
        self.plot_cmap.addItem("")
        self.plot_cmap.addItem("")
        self.plot_cmap.addItem("")
        self.plot_cmap.addItem("")
        self.plot_cmap.setObjectName(u"plot_cmap")
        sizePolicy3.setHeightForWidth(self.plot_cmap.sizePolicy().hasHeightForWidth())
        self.plot_cmap.setSizePolicy(sizePolicy3)

        self.gridLayout_3.addWidget(self.plot_cmap, 0, 3, 1, 1)

        self.btn_plot = QPushButton(self.groupBox_4)
        self.btn_plot.setObjectName(u"btn_plot")

        self.gridLayout_3.addWidget(self.btn_plot, 0, 4, 1, 1)

        self.label_45 = QLabel(self.groupBox_4)
        self.label_45.setObjectName(u"label_45")

        self.gridLayout_3.addWidget(self.label_45, 0, 2, 1, 1)


        self.gridLayout.addWidget(self.groupBox_4, 2, 0, 1, 3)


        self.verticalLayout_2.addWidget(self.groupBox_5)

        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        sizePolicy16 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy16.setHorizontalStretch(1)
        sizePolicy16.setVerticalStretch(0)
        sizePolicy16.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy16)
        self.gridLayout_11 = QGridLayout(self.groupBox_3)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.tabWidget = QTabWidget(self.groupBox_3)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab_9 = QWidget()
        self.tab_9.setObjectName(u"tab_9")
        self.gridLayout_32 = QGridLayout(self.tab_9)
        self.gridLayout_32.setObjectName(u"gridLayout_32")
        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.doubleSpinBox_phi_offset = QDoubleSpinBox(self.tab_9)
        self.doubleSpinBox_phi_offset.setObjectName(u"doubleSpinBox_phi_offset")
        self.doubleSpinBox_phi_offset.setMinimum(-180.000000000000000)
        self.doubleSpinBox_phi_offset.setMaximum(180.000000000000000)

        self.gridLayout_6.addWidget(self.doubleSpinBox_phi_offset, 1, 6, 2, 1)

        self.label_43 = QLabel(self.tab_9)
        self.label_43.setObjectName(u"label_43")

        self.gridLayout_6.addWidget(self.label_43, 1, 5, 2, 1)

        self.label_13 = QLabel(self.tab_9)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_6.addWidget(self.label_13, 1, 3, 2, 1)

        self.sb_spnum = QSpinBox(self.tab_9)
        self.sb_spnum.setObjectName(u"sb_spnum")
        self.sb_spnum.setMinimum(1)
        self.sb_spnum.setMaximum(9999)
        self.sb_spnum.setValue(1)

        self.gridLayout_6.addWidget(self.sb_spnum, 1, 2, 2, 1)

        self.sb_sqnum = QSpinBox(self.tab_9)
        self.sb_sqnum.setObjectName(u"sb_sqnum")
        self.sb_sqnum.setMinimum(2)
        self.sb_sqnum.setMaximum(9999)
        self.sb_sqnum.setValue(360)

        self.gridLayout_6.addWidget(self.sb_sqnum, 0, 2, 1, 1)

        self.label = QLabel(self.tab_9)
        self.label.setObjectName(u"label")

        self.gridLayout_6.addWidget(self.label, 0, 1, 1, 1)

        self.partition_style = QComboBox(self.tab_9)
        self.partition_style.addItem("")
        self.partition_style.addItem("")
        self.partition_style.setObjectName(u"partition_style")

        self.gridLayout_6.addWidget(self.partition_style, 0, 6, 1, 1)

        self.label_12 = QLabel(self.tab_9)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_6.addWidget(self.label_12, 1, 1, 2, 1)

        self.sb_dqnum = QSpinBox(self.tab_9)
        self.sb_dqnum.setObjectName(u"sb_dqnum")
        self.sb_dqnum.setMinimum(1)
        self.sb_dqnum.setMaximum(999)
        self.sb_dqnum.setValue(36)

        self.gridLayout_6.addWidget(self.sb_dqnum, 0, 4, 1, 1)

        self.label_10 = QLabel(self.tab_9)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_6.addWidget(self.label_10, 0, 3, 1, 1)

        self.label_20 = QLabel(self.tab_9)
        self.label_20.setObjectName(u"label_20")

        self.gridLayout_6.addWidget(self.label_20, 0, 5, 1, 1)

        self.sb_dpnum = QSpinBox(self.tab_9)
        self.sb_dpnum.setObjectName(u"sb_dpnum")
        self.sb_dpnum.setMinimum(1)
        self.sb_dpnum.setMaximum(999)
        self.sb_dpnum.setValue(1)

        self.gridLayout_6.addWidget(self.sb_dpnum, 1, 4, 2, 1)

        self.label_41 = QLabel(self.tab_9)
        self.label_41.setObjectName(u"label_41")

        self.gridLayout_6.addWidget(self.label_41, 1, 7, 2, 1)

        self.spinBox_symmetry_fold = QSpinBox(self.tab_9)
        self.spinBox_symmetry_fold.setObjectName(u"spinBox_symmetry_fold")
        self.spinBox_symmetry_fold.setMinimum(1)
        self.spinBox_symmetry_fold.setMaximum(12)

        self.gridLayout_6.addWidget(self.spinBox_symmetry_fold, 1, 8, 2, 1)

        self.btn_compute_qpartition = QPushButton(self.tab_9)
        self.btn_compute_qpartition.setObjectName(u"btn_compute_qpartition")

        self.gridLayout_6.addWidget(self.btn_compute_qpartition, 0, 7, 1, 2)


        self.gridLayout_32.addLayout(self.gridLayout_6, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_9, "")
        self.tab_10 = QWidget()
        self.tab_10.setObjectName(u"tab_10")
        self.gridLayout_34 = QGridLayout(self.tab_10)
        self.gridLayout_34.setObjectName(u"gridLayout_34")
        self.gridLayout_33 = QGridLayout()
        self.gridLayout_33.setObjectName(u"gridLayout_33")
        self.sb_dynum = QSpinBox(self.tab_10)
        self.sb_dynum.setObjectName(u"sb_dynum")
        self.sb_dynum.setMinimum(1)
        self.sb_dynum.setMaximum(999)
        self.sb_dynum.setValue(1)

        self.gridLayout_33.addWidget(self.sb_dynum, 1, 4, 1, 1)

        self.sb_synum = QSpinBox(self.tab_10)
        self.sb_synum.setObjectName(u"sb_synum")
        self.sb_synum.setMinimum(1)
        self.sb_synum.setMaximum(9999)
        self.sb_synum.setValue(8)

        self.gridLayout_33.addWidget(self.sb_synum, 1, 2, 1, 1)

        self.label_34 = QLabel(self.tab_10)
        self.label_34.setObjectName(u"label_34")

        self.gridLayout_33.addWidget(self.label_34, 0, 1, 1, 1)

        self.sb_dxnum = QSpinBox(self.tab_10)
        self.sb_dxnum.setObjectName(u"sb_dxnum")
        self.sb_dxnum.setMinimum(1)
        self.sb_dxnum.setMaximum(999)
        self.sb_dxnum.setValue(1)

        self.gridLayout_33.addWidget(self.sb_dxnum, 0, 4, 1, 1)

        self.sb_sxnum = QSpinBox(self.tab_10)
        self.sb_sxnum.setObjectName(u"sb_sxnum")
        self.sb_sxnum.setMinimum(1)
        self.sb_sxnum.setMaximum(9999)
        self.sb_sxnum.setValue(6)

        self.gridLayout_33.addWidget(self.sb_sxnum, 0, 2, 1, 1)

        self.label_38 = QLabel(self.tab_10)
        self.label_38.setObjectName(u"label_38")

        self.gridLayout_33.addWidget(self.label_38, 1, 1, 1, 1)

        self.label_37 = QLabel(self.tab_10)
        self.label_37.setObjectName(u"label_37")

        self.gridLayout_33.addWidget(self.label_37, 0, 3, 1, 1)

        self.label_36 = QLabel(self.tab_10)
        self.label_36.setObjectName(u"label_36")

        self.gridLayout_33.addWidget(self.label_36, 1, 3, 1, 1)

        self.btn_compute_qpartition2 = QPushButton(self.tab_10)
        self.btn_compute_qpartition2.setObjectName(u"btn_compute_qpartition2")

        self.gridLayout_33.addWidget(self.btn_compute_qpartition2, 1, 5, 1, 1)


        self.gridLayout_34.addLayout(self.gridLayout_33, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_10, "")
        self.tab_8 = QWidget()
        self.tab_8.setObjectName(u"tab_8")
        self.gridLayout_31 = QGridLayout(self.tab_8)
        self.gridLayout_31.setObjectName(u"gridLayout_31")
        self.gridLayout_30 = QGridLayout()
        self.gridLayout_30.setObjectName(u"gridLayout_30")
        self.comboBox_partition_mapname1 = QComboBox(self.tab_8)
        self.comboBox_partition_mapname1.setObjectName(u"comboBox_partition_mapname1")

        self.gridLayout_30.addWidget(self.comboBox_partition_mapname1, 2, 0, 2, 1)

        self.label_46 = QLabel(self.tab_8)
        self.label_46.setObjectName(u"label_46")

        self.gridLayout_30.addWidget(self.label_46, 0, 3, 1, 1)

        self.sb_partition_dn0 = QSpinBox(self.tab_8)
        self.sb_partition_dn0.setObjectName(u"sb_partition_dn0")
        self.sb_partition_dn0.setMinimum(1)
        self.sb_partition_dn0.setMaximum(999)
        self.sb_partition_dn0.setValue(36)

        self.gridLayout_30.addWidget(self.sb_partition_dn0, 1, 2, 1, 1)

        self.label_48 = QLabel(self.tab_8)
        self.label_48.setObjectName(u"label_48")

        self.gridLayout_30.addWidget(self.label_48, 0, 1, 1, 1)

        self.label_50 = QLabel(self.tab_8)
        self.label_50.setObjectName(u"label_50")

        self.gridLayout_30.addWidget(self.label_50, 0, 2, 1, 1)

        self.comboBox_partition_style1 = QComboBox(self.tab_8)
        self.comboBox_partition_style1.addItem("")
        self.comboBox_partition_style1.addItem("")
        self.comboBox_partition_style1.setObjectName(u"comboBox_partition_style1")

        self.gridLayout_30.addWidget(self.comboBox_partition_style1, 2, 3, 2, 1)

        self.sb_partition_sn0 = QSpinBox(self.tab_8)
        self.sb_partition_sn0.setObjectName(u"sb_partition_sn0")
        self.sb_partition_sn0.setMinimum(2)
        self.sb_partition_sn0.setMaximum(9999)
        self.sb_partition_sn0.setValue(360)

        self.gridLayout_30.addWidget(self.sb_partition_sn0, 1, 1, 1, 1)

        self.label_53 = QLabel(self.tab_8)
        self.label_53.setObjectName(u"label_53")

        self.gridLayout_30.addWidget(self.label_53, 0, 0, 1, 1)

        self.comboBox_partition_mapname0 = QComboBox(self.tab_8)
        self.comboBox_partition_mapname0.setObjectName(u"comboBox_partition_mapname0")

        self.gridLayout_30.addWidget(self.comboBox_partition_mapname0, 1, 0, 1, 1)

        self.sb_partition_dn1 = QSpinBox(self.tab_8)
        self.sb_partition_dn1.setObjectName(u"sb_partition_dn1")
        self.sb_partition_dn1.setMinimum(1)
        self.sb_partition_dn1.setMaximum(999)
        self.sb_partition_dn1.setValue(1)

        self.gridLayout_30.addWidget(self.sb_partition_dn1, 2, 2, 2, 1)

        self.sb_partition_sn1 = QSpinBox(self.tab_8)
        self.sb_partition_sn1.setObjectName(u"sb_partition_sn1")
        self.sb_partition_sn1.setMinimum(1)
        self.sb_partition_sn1.setMaximum(9999)
        self.sb_partition_sn1.setValue(1)

        self.gridLayout_30.addWidget(self.sb_partition_sn1, 2, 1, 2, 1)

        self.comboBox_partition_style0 = QComboBox(self.tab_8)
        self.comboBox_partition_style0.addItem("")
        self.comboBox_partition_style0.addItem("")
        self.comboBox_partition_style0.setObjectName(u"comboBox_partition_style0")

        self.gridLayout_30.addWidget(self.comboBox_partition_style0, 1, 3, 1, 1)

        self.btn_compute_qpartition3 = QPushButton(self.tab_8)
        self.btn_compute_qpartition3.setObjectName(u"btn_compute_qpartition3")

        self.gridLayout_30.addWidget(self.btn_compute_qpartition3, 0, 6, 4, 1)


        self.gridLayout_31.addLayout(self.gridLayout_30, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_8, "")

        self.gridLayout_11.addWidget(self.tabWidget, 1, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.groupBox_3)

        self.groupBox_6 = QGroupBox(self.centralwidget)
        self.groupBox_6.setObjectName(u"groupBox_6")
        sizePolicy17 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy17.setHorizontalStretch(1)
        sizePolicy17.setVerticalStretch(0)
        sizePolicy17.setHeightForWidth(self.groupBox_6.sizePolicy().hasHeightForWidth())
        self.groupBox_6.setSizePolicy(sizePolicy17)
        self.gridLayout_7 = QGridLayout(self.groupBox_6)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.label_47 = QLabel(self.groupBox_6)
        self.label_47.setObjectName(u"label_47")
        sizePolicy8.setHeightForWidth(self.label_47.sizePolicy().hasHeightForWidth())
        self.label_47.setSizePolicy(sizePolicy8)

        self.gridLayout_7.addWidget(self.label_47, 0, 0, 1, 1)

        self.comboBox_output_type = QComboBox(self.groupBox_6)
        self.comboBox_output_type.addItem("")
        self.comboBox_output_type.addItem("")
        self.comboBox_output_type.addItem("")
        self.comboBox_output_type.setObjectName(u"comboBox_output_type")
        sizePolicy4.setHeightForWidth(self.comboBox_output_type.sizePolicy().hasHeightForWidth())
        self.comboBox_output_type.setSizePolicy(sizePolicy4)

        self.gridLayout_7.addWidget(self.comboBox_output_type, 0, 1, 1, 1)

        self.pushButton = QPushButton(self.groupBox_6)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout_7.addWidget(self.pushButton, 0, 2, 1, 1)


        self.verticalLayout_2.addWidget(self.groupBox_6)


        self.gridLayout_16.addLayout(self.verticalLayout_2, 0, 1, 1, 1)

        SimpleMask.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(SimpleMask)
        self.statusbar.setObjectName(u"statusbar")
        SimpleMask.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.plot_log, self.plot_index)
        QWidget.setTabOrder(self.plot_index, self.infobar)

        self.retranslateUi(SimpleMask)
        self.mask_list_include.toggled.connect(self.mask_list_radius.setEnabled)
        self.mask_list_include.toggled.connect(self.mask_list_variation.setEnabled)

        self.tabWidget_2.setCurrentIndex(1)
        self.MaskWidget.setCurrentIndex(5)
        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(SimpleMask)
    # setupUi

    def retranslateUi(self, SimpleMask):
        SimpleMask.setWindowTitle(QCoreApplication.translate("SimpleMask", u"SimpleMask(beta)", None))
        self.groupBox.setTitle(QCoreApplication.translate("SimpleMask", u"Input", None))
        self.comboBox_beamline.setItemText(0, QCoreApplication.translate("SimpleMask", u"APS_8IDI", None))
        self.comboBox_beamline.setItemText(1, QCoreApplication.translate("SimpleMask", u"APS_9IDD", None))
        self.comboBox_beamline.setItemText(2, QCoreApplication.translate("SimpleMask", u"NativeFiles", None))
        self.comboBox_beamline.setItemText(3, QCoreApplication.translate("SimpleMask", u"DESY_P10", None))

        self.label_9.setText(QCoreApplication.translate("SimpleMask", u"begin index:", None))
        self.label_28.setText(QCoreApplication.translate("SimpleMask", u"num_frames", None))
        self.btn_load.setText(QCoreApplication.translate("SimpleMask", u"Load", None))
        self.label_2.setText(QCoreApplication.translate("SimpleMask", u"center x:", None))
        self.label_3.setText(QCoreApplication.translate("SimpleMask", u"center y:", None))
        self.label_4.setText(QCoreApplication.translate("SimpleMask", u"energy (keV):", None))
        self.label_5.setText(QCoreApplication.translate("SimpleMask", u"detector distance (m):", None))
        self.label_21.setText(QCoreApplication.translate("SimpleMask", u"detector Rx (deg):", None))
        self.label_6.setText(QCoreApplication.translate("SimpleMask", u"pixel size (\u00b5m):", None))
        self.label_35.setText(QCoreApplication.translate("SimpleMask", u"detector Ry (deg):", None))
        self.label_7.setText(QCoreApplication.translate("SimpleMask", u"detector shape:", None))
        self.label_40.setText(QCoreApplication.translate("SimpleMask", u"detector Rz (deg):", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab), QCoreApplication.translate("SimpleMask", u"Small Angle", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_7), QCoreApplication.translate("SimpleMask", u"Grazing Incidence", None))
        self.label_17.setText(QCoreApplication.translate("SimpleMask", u"Scattering File:", None))
        self.fname.setPlaceholderText(QCoreApplication.translate("SimpleMask", u"filename", None))
        self.btn_select_raw.setText(QCoreApplication.translate("SimpleMask", u"...", None))
        self.btn_swapxy.setText(QCoreApplication.translate("SimpleMask", u"Swap X-Y", None))
        self.btn_find_center.setText(QCoreApplication.translate("SimpleMask", u"Find Center", None))
        self.btn_update_parameters.setText(QCoreApplication.translate("SimpleMask", u"Update Metadata", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("SimpleMask", u"Mask", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("SimpleMask", u"Blemish File:", None))
        self.label_30.setText(QCoreApplication.translate("SimpleMask", u"Blemish file:", None))
        self.btn_select_blemish.setText(QCoreApplication.translate("SimpleMask", u"Select", None))
        self.label_31.setText(QCoreApplication.translate("SimpleMask", u"HDF path:", None))
        self.blemish_path.setText(QCoreApplication.translate("SimpleMask", u"/qmap/mask", None))
        self.btn_apply_blemish.setText(QCoreApplication.translate("SimpleMask", u"Evaluate", None))
        self.btn_mask_blemish_apply.setText(QCoreApplication.translate("SimpleMask", u"Apply", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("SimpleMask", u"Additional File (hdf/tiff/mat):", None))
        self.label_18.setText(QCoreApplication.translate("SimpleMask", u"File name:", None))
        self.maskfile_fname.setText("")
        self.btn_select_maskfile.setText(QCoreApplication.translate("SimpleMask", u"Select", None))
        self.label_32.setText(QCoreApplication.translate("SimpleMask", u"HDF path:", None))
        self.maskfile_path.setText(QCoreApplication.translate("SimpleMask", u"/xpcs/mask", None))
        self.btn_apply_maskfile.setText(QCoreApplication.translate("SimpleMask", u"Evaluate", None))
        self.btn_mask_file_apply.setText(QCoreApplication.translate("SimpleMask", u"Apply", None))
        self.MaskWidget.setTabText(self.MaskWidget.indexOf(self.tab_6), QCoreApplication.translate("SimpleMask", u"Blemish/Files", None))
        self.label_14.setText(QCoreApplication.translate("SimpleMask", u"color:", None))
        self.label_8.setText(QCoreApplication.translate("SimpleMask", u"linewidth:", None))
        self.btn_mask_draw_evaluate.setText(QCoreApplication.translate("SimpleMask", u"Evaluate", None))
        self.plot_width.setSpecialValueText("")
        self.label_22.setText(QCoreApplication.translate("SimpleMask", u"type:", None))
        self.cb_selector_type.setItemText(0, QCoreApplication.translate("SimpleMask", u"Circle", None))
        self.cb_selector_type.setItemText(1, QCoreApplication.translate("SimpleMask", u"Polygon", None))
        self.cb_selector_type.setItemText(2, QCoreApplication.translate("SimpleMask", u"Ellipse", None))
        self.cb_selector_type.setItemText(3, QCoreApplication.translate("SimpleMask", u"Rectangle", None))

        self.cb_selector_mode.setItemText(0, QCoreApplication.translate("SimpleMask", u"exclusive", None))
        self.cb_selector_mode.setItemText(1, QCoreApplication.translate("SimpleMask", u"inclusive", None))

        self.btn_mask_draw_apply.setText(QCoreApplication.translate("SimpleMask", u"Apply", None))
        self.label_23.setText(QCoreApplication.translate("SimpleMask", u"shape:", None))
        self.cb_selector_color.setItemText(0, QCoreApplication.translate("SimpleMask", u"red", None))
        self.cb_selector_color.setItemText(1, QCoreApplication.translate("SimpleMask", u"green", None))
        self.cb_selector_color.setItemText(2, QCoreApplication.translate("SimpleMask", u"yellow", None))
        self.cb_selector_color.setItemText(3, QCoreApplication.translate("SimpleMask", u"blue", None))
        self.cb_selector_color.setItemText(4, QCoreApplication.translate("SimpleMask", u"cyan", None))
        self.cb_selector_color.setItemText(5, QCoreApplication.translate("SimpleMask", u"magenta", None))
        self.cb_selector_color.setItemText(6, QCoreApplication.translate("SimpleMask", u"black", None))
        self.cb_selector_color.setItemText(7, QCoreApplication.translate("SimpleMask", u"white", None))

        self.label_39.setText(QCoreApplication.translate("SimpleMask", u"num_edges:", None))
        self.btn_mask_draw_add.setText(QCoreApplication.translate("SimpleMask", u"Add", None))
        self.MaskWidget.setTabText(self.MaskWidget.indexOf(self.tab_2), QCoreApplication.translate("SimpleMask", u"Draw", None))
        self.btn_mask_threshold_apply.setText(QCoreApplication.translate("SimpleMask", u"Apply", None))
        self.groupBox_10.setTitle(QCoreApplication.translate("SimpleMask", u"Binary operation: (acts on the mask)", None))
        self.pushButton_9.setText(QCoreApplication.translate("SimpleMask", u"dilate", None))
        self.pushButton_5.setText(QCoreApplication.translate("SimpleMask", u"erode", None))
        self.pushButton_15.setText(QCoreApplication.translate("SimpleMask", u"close", None))
        self.pushButton_16.setText(QCoreApplication.translate("SimpleMask", u"open", None))
        self.btn_mask_threshold_evaluate.setText(QCoreApplication.translate("SimpleMask", u"Evaluate", None))
        self.groupBox_9.setTitle(QCoreApplication.translate("SimpleMask", u"Threshold: (acts on the scattering image)", None))
        self.label_26.setText(QCoreApplication.translate("SimpleMask", u"low:", None))
        self.checkBox_threshold_low_enable.setText(QCoreApplication.translate("SimpleMask", u"Enable", None))
        self.checkBox_threshold_high_preset.setItemText(0, QCoreApplication.translate("SimpleMask", u"None", None))
        self.checkBox_threshold_high_preset.setItemText(1, QCoreApplication.translate("SimpleMask", u"uint8", None))
        self.checkBox_threshold_high_preset.setItemText(2, QCoreApplication.translate("SimpleMask", u"int8", None))
        self.checkBox_threshold_high_preset.setItemText(3, QCoreApplication.translate("SimpleMask", u"uint16", None))
        self.checkBox_threshold_high_preset.setItemText(4, QCoreApplication.translate("SimpleMask", u"int16", None))
        self.checkBox_threshold_high_preset.setItemText(5, QCoreApplication.translate("SimpleMask", u"uint24", None))
        self.checkBox_threshold_high_preset.setItemText(6, QCoreApplication.translate("SimpleMask", u"int24", None))
        self.checkBox_threshold_high_preset.setItemText(7, QCoreApplication.translate("SimpleMask", u"uint32", None))
        self.checkBox_threshold_high_preset.setItemText(8, QCoreApplication.translate("SimpleMask", u"int32", None))

        self.label_27.setText(QCoreApplication.translate("SimpleMask", u"high:", None))
        self.checkBox_threshold_high_enable.setText(QCoreApplication.translate("SimpleMask", u"Enable", None))
        self.checkBox_threshold_low_preset.setItemText(0, QCoreApplication.translate("SimpleMask", u"None", None))
        self.checkBox_threshold_low_preset.setItemText(1, QCoreApplication.translate("SimpleMask", u"-1", None))
        self.checkBox_threshold_low_preset.setItemText(2, QCoreApplication.translate("SimpleMask", u"0", None))
        self.checkBox_threshold_low_preset.setItemText(3, QCoreApplication.translate("SimpleMask", u"1", None))

        self.label_25.setText(QCoreApplication.translate("SimpleMask", u">=", None))
        self.label_33.setText(QCoreApplication.translate("SimpleMask", u"<", None))
        self.MaskWidget.setTabText(self.MaskWidget.indexOf(self.tab_4), QCoreApplication.translate("SimpleMask", u"Binary", None))
        self.groupBox_12.setTitle(QCoreApplication.translate("SimpleMask", u"Import from a file", None))
        self.mask_list_1based.setText(QCoreApplication.translate("SimpleMask", u"1-based", None))
        self.mask_list_rowcol.setText(QCoreApplication.translate("SimpleMask", u"row-col", None))
        self.btn_mask_list_load.setText(QCoreApplication.translate("SimpleMask", u"Load File", None))
        self.groupBox_13.setTitle(QCoreApplication.translate("SimpleMask", u"Input coordinates", None))
        self.btn_mask_list_add.setText(QCoreApplication.translate("SimpleMask", u"Add ", None))
        self.mask_list_input.setText("")
        self.mask_list_input.setPlaceholderText(QCoreApplication.translate("SimpleMask", u"(x1, y1), (x2, y2), ...", None))
        self.groupBox_14.setTitle(QCoreApplication.translate("SimpleMask", u"Select with double-click", None))
        self.mask_list_include.setText(QCoreApplication.translate("SimpleMask", u"Include points with simiar intensity", None))
        self.label_24.setText(QCoreApplication.translate("SimpleMask", u"Intensity Variation (%):", None))
        self.label_19.setText(QCoreApplication.translate("SimpleMask", u"Radius:", None))
        self.groupBox_11.setTitle(QCoreApplication.translate("SimpleMask", u"xy list", None))
        self.btn_mask_list_apply.setText(QCoreApplication.translate("SimpleMask", u"Apply", None))
        self.btn_mask_list_evaluate.setText(QCoreApplication.translate("SimpleMask", u"Evaluate", None))
        self.btn_mask_list_clear.setText(QCoreApplication.translate("SimpleMask", u"Clear List", None))
        self.MaskWidget.setTabText(self.MaskWidget.indexOf(self.tab_3), QCoreApplication.translate("SimpleMask", u"Manual", None))
        self.label_16.setText(QCoreApplication.translate("SimpleMask", u"num. circular ROI:", None))
        self.label_15.setText(QCoreApplication.translate("SimpleMask", u"cutoff (\u00b1std):", None))
        self.label_44.setText(QCoreApplication.translate("SimpleMask", u"method", None))
        self.btn_mask_outlier_apply.setText(QCoreApplication.translate("SimpleMask", u"Apply", None))
        self.btn_mask_outlier_evaluate.setText(QCoreApplication.translate("SimpleMask", u"Evaluate", None))
        self.comboBox_outlier_method.setItemText(0, QCoreApplication.translate("SimpleMask", u"median_absolute_deviation", None))
        self.comboBox_outlier_method.setItemText(1, QCoreApplication.translate("SimpleMask", u"percentile", None))

        self.MaskWidget.setTabText(self.MaskWidget.indexOf(self.tab_5), QCoreApplication.translate("SimpleMask", u"Outlier", None))
        self.comboBox_param_logic.setItemText(0, QCoreApplication.translate("SimpleMask", u"AND", None))
        self.comboBox_param_logic.setItemText(1, QCoreApplication.translate("SimpleMask", u"OR", None))
        self.comboBox_param_logic.setItemText(2, QCoreApplication.translate("SimpleMask", u"NOT", None))

        self.btn_mask_param_evaluate.setText(QCoreApplication.translate("SimpleMask", u"Evaluate", None))
        self.btn_mask_param_apply.setText(QCoreApplication.translate("SimpleMask", u"Apply", None))
        self.btn_mask_param_delete.setText(QCoreApplication.translate("SimpleMask", u"Delete", None))
        self.label_29.setText(QCoreApplication.translate("SimpleMask", u"map_name", None))
        self.label_param_minval.setText(QCoreApplication.translate("SimpleMask", u"Min:", None))
        self.label_param_maxval.setText(QCoreApplication.translate("SimpleMask", u"Max:", None))
        self.btn_mask_param_add.setText(QCoreApplication.translate("SimpleMask", u"Add", None))
        self.label_42.setText(QCoreApplication.translate("SimpleMask", u"Mask_parametrization = [Mask_all_True] [logic_1] [mask_1] ... [logic_n] [mask_n]", None))
        self.MaskWidget.setTabText(self.MaskWidget.indexOf(self.tab6), QCoreApplication.translate("SimpleMask", u"Parametrization", None))
        self.btn_mask_reset.setText(QCoreApplication.translate("SimpleMask", u"Reset", None))
        self.btn_mask_undo.setText(QCoreApplication.translate("SimpleMask", u"Undo", None))
        self.btn_mask_redo.setText(QCoreApplication.translate("SimpleMask", u"Redo", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("SimpleMask", u"Scattering, Mask and Partitions", None))
        self.plot_index.setItemText(0, QCoreApplication.translate("SimpleMask", u"scattering", None))
        self.plot_index.setItemText(1, QCoreApplication.translate("SimpleMask", u"scattering * mask", None))
        self.plot_index.setItemText(2, QCoreApplication.translate("SimpleMask", u"mask", None))
        self.plot_index.setItemText(3, QCoreApplication.translate("SimpleMask", u"dynamic_q_partition", None))
        self.plot_index.setItemText(4, QCoreApplication.translate("SimpleMask", u"static_q_partition", None))
        self.plot_index.setItemText(5, QCoreApplication.translate("SimpleMask", u"preview", None))

        self.label_11.setText(QCoreApplication.translate("SimpleMask", u"coordinates:", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("SimpleMask", u"Plot Settings", None))
        self.plot_center.setText(QCoreApplication.translate("SimpleMask", u"show center", None))
        self.plot_log.setText(QCoreApplication.translate("SimpleMask", u"log scale", None))
        self.plot_cmap.setItemText(0, QCoreApplication.translate("SimpleMask", u"jet", None))
        self.plot_cmap.setItemText(1, QCoreApplication.translate("SimpleMask", u"cool", None))
        self.plot_cmap.setItemText(2, QCoreApplication.translate("SimpleMask", u"ocean", None))
        self.plot_cmap.setItemText(3, QCoreApplication.translate("SimpleMask", u"prism", None))
        self.plot_cmap.setItemText(4, QCoreApplication.translate("SimpleMask", u"coolwarm", None))
        self.plot_cmap.setItemText(5, QCoreApplication.translate("SimpleMask", u"seismic", None))
        self.plot_cmap.setItemText(6, QCoreApplication.translate("SimpleMask", u"gray", None))
        self.plot_cmap.setItemText(7, QCoreApplication.translate("SimpleMask", u"viridis", None))
        self.plot_cmap.setItemText(8, QCoreApplication.translate("SimpleMask", u"inferno", None))
        self.plot_cmap.setItemText(9, QCoreApplication.translate("SimpleMask", u"plasma", None))
        self.plot_cmap.setItemText(10, QCoreApplication.translate("SimpleMask", u"magma", None))

        self.btn_plot.setText(QCoreApplication.translate("SimpleMask", u"Plot", None))
        self.label_45.setText(QCoreApplication.translate("SimpleMask", u"colormap", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("SimpleMask", u"Partition", None))
        self.label_43.setText(QCoreApplication.translate("SimpleMask", u"offset (deg):", None))
        self.label_13.setText(QCoreApplication.translate("SimpleMask", u"dynamic phi partition:", None))
        self.label.setText(QCoreApplication.translate("SimpleMask", u"static q partition:", None))
        self.partition_style.setItemText(0, QCoreApplication.translate("SimpleMask", u"linear", None))
        self.partition_style.setItemText(1, QCoreApplication.translate("SimpleMask", u"logarithmic", None))

        self.label_12.setText(QCoreApplication.translate("SimpleMask", u"static phi partition:", None))
        self.label_10.setText(QCoreApplication.translate("SimpleMask", u"dynamic q partition:", None))
        self.label_20.setText(QCoreApplication.translate("SimpleMask", u"q-style:", None))
        self.label_41.setText(QCoreApplication.translate("SimpleMask", u"symmetry", None))
        self.btn_compute_qpartition.setText(QCoreApplication.translate("SimpleMask", u"compute", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_9), QCoreApplication.translate("SimpleMask", u"q-phi", None))
        self.label_34.setText(QCoreApplication.translate("SimpleMask", u"static x:", None))
        self.label_38.setText(QCoreApplication.translate("SimpleMask", u"static y:", None))
        self.label_37.setText(QCoreApplication.translate("SimpleMask", u"dynamic x:", None))
        self.label_36.setText(QCoreApplication.translate("SimpleMask", u"dynamic y:", None))
        self.btn_compute_qpartition2.setText(QCoreApplication.translate("SimpleMask", u"compute", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_10), QCoreApplication.translate("SimpleMask", u"xy-mesh", None))
        self.label_46.setText(QCoreApplication.translate("SimpleMask", u"Style", None))
        self.label_48.setText(QCoreApplication.translate("SimpleMask", u"Static partition:", None))
        self.label_50.setText(QCoreApplication.translate("SimpleMask", u"Dynamic partition", None))
        self.comboBox_partition_style1.setItemText(0, QCoreApplication.translate("SimpleMask", u"Linear", None))
        self.comboBox_partition_style1.setItemText(1, QCoreApplication.translate("SimpleMask", u"Logarithmic", None))

        self.label_53.setText(QCoreApplication.translate("SimpleMask", u"MapName", None))
        self.comboBox_partition_style0.setItemText(0, QCoreApplication.translate("SimpleMask", u"Linear", None))
        self.comboBox_partition_style0.setItemText(1, QCoreApplication.translate("SimpleMask", u"Logarithmic", None))

        self.btn_compute_qpartition3.setText(QCoreApplication.translate("SimpleMask", u"compute", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_8), QCoreApplication.translate("SimpleMask", u"General", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("SimpleMask", u"Output", None))
        self.label_47.setText(QCoreApplication.translate("SimpleMask", u"Format", None))
        self.comboBox_output_type.setItemText(0, QCoreApplication.translate("SimpleMask", u"Nexus-XPCS", None))
        self.comboBox_output_type.setItemText(1, QCoreApplication.translate("SimpleMask", u"Mask-Only", None))
        self.comboBox_output_type.setItemText(2, QCoreApplication.translate("SimpleMask", u"P10 FPGA", None))

        self.pushButton.setText(QCoreApplication.translate("SimpleMask", u"save", None))
    # retranslateUi

