# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MultiCamDlg.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
# version:1.0.2312.9221

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MultiCamDlg(object):
    def setupUi(self, MultiCamDlg):
        MultiCamDlg.setObjectName("MultiCamDlg")
        MultiCamDlg.resize(821, 802)
        self.groupBox = QtWidgets.QGroupBox(MultiCamDlg)
        self.groupBox.setGeometry(QtCore.QRect(20, 20, 291, 51))
        self.groupBox.setObjectName("groupBox")
        self.device_list_box = QtWidgets.QComboBox(self.groupBox)
        self.device_list_box.setGeometry(QtCore.QRect(10, 20, 271, 22))
        self.device_list_box.setObjectName("device_list_box")
        self.groupBox_3 = QtWidgets.QGroupBox(MultiCamDlg)
        self.groupBox_3.setGeometry(QtCore.QRect(20, 210, 291, 81))
        self.groupBox_3.setObjectName("groupBox_3")
        self.exposure_range = QtWidgets.QLabel(self.groupBox_3)
        self.exposure_range.setGeometry(QtCore.QRect(50, 20, 91, 21))
        self.exposure_range.setText("")
        self.exposure_range.setObjectName("exposure_range")
        self.gain_range = QtWidgets.QLabel(self.groupBox_3)
        self.gain_range.setGeometry(QtCore.QRect(50, 50, 91, 16))
        self.gain_range.setText("")
        self.gain_range.setObjectName("gain_range")
        self.label_4 = QtWidgets.QLabel(self.groupBox_3)
        self.label_4.setGeometry(QtCore.QRect(11, 50, 24, 16))
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(self.groupBox_3)
        self.label_3.setGeometry(QtCore.QRect(11, 20, 24, 21))
        self.label_3.setObjectName("label_3")
        self.layoutWidget = QtWidgets.QWidget(self.groupBox_3)
        self.layoutWidget.setGeometry(QtCore.QRect(150, 20, 135, 57))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.exposure_time_edit = QtWidgets.QLineEdit(self.layoutWidget)
        self.exposure_time_edit.setObjectName("exposure_time_edit")
        self.verticalLayout_2.addWidget(self.exposure_time_edit)
        self.gain_edit = QtWidgets.QLineEdit(self.layoutWidget)
        self.gain_edit.setObjectName("gain_edit")
        self.verticalLayout_2.addWidget(self.gain_edit)
        self.groupBox_2 = QtWidgets.QGroupBox(MultiCamDlg)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 80, 291, 121))
        self.groupBox_2.setObjectName("groupBox_2")
        self.layoutWidget_2 = QtWidgets.QWidget(self.groupBox_2)
        self.layoutWidget_2.setGeometry(QtCore.QRect(10, 10, 271, 101))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget_2)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.open_device_btn = QtWidgets.QPushButton(self.layoutWidget_2)
        self.open_device_btn.setObjectName("open_device_btn")
        self.gridLayout.addWidget(self.open_device_btn, 0, 0, 1, 1)
        self.close_device_btn = QtWidgets.QPushButton(self.layoutWidget_2)
        self.close_device_btn.setObjectName("close_device_btn")
        self.gridLayout.addWidget(self.close_device_btn, 0, 1, 1, 1)
        self.acquisition_start_btn = QtWidgets.QPushButton(self.layoutWidget_2)
        self.acquisition_start_btn.setObjectName("acquisition_start_btn")
        self.gridLayout.addWidget(self.acquisition_start_btn, 1, 0, 1, 1)
        self.acquisition_stop_btn = QtWidgets.QPushButton(self.layoutWidget_2)
        self.acquisition_stop_btn.setObjectName("acquisition_stop_btn")
        self.gridLayout.addWidget(self.acquisition_stop_btn, 1, 1, 1, 1)
        self.show_image_up = QtWidgets.QLabel(MultiCamDlg)
        self.show_image_up.setGeometry(QtCore.QRect(322, 12, 491, 381))
        self.show_image_up.setStyleSheet("")
        self.show_image_up.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.show_image_up.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.show_image_up.setText("")
        self.show_image_up.setObjectName("show_image_up")
        self.show_image_down = QtWidgets.QLabel(MultiCamDlg)
        self.show_image_down.setGeometry(QtCore.QRect(322, 400, 491, 401))
        self.show_image_down.setStyleSheet("")
        self.show_image_down.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.show_image_down.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.show_image_down.setText("")
        self.show_image_down.setObjectName("show_image_down")

        self.retranslateUi(MultiCamDlg)
        QtCore.QMetaObject.connectSlotsByName(MultiCamDlg)

    def retranslateUi(self, MultiCamDlg):
        _translate = QtCore.QCoreApplication.translate
        MultiCamDlg.setWindowTitle(_translate("MultiCamDlg", "MultiCam"))
        self.groupBox.setTitle(_translate("MultiCamDlg", "设备列表"))
        self.groupBox_3.setTitle(_translate("MultiCamDlg", "参数基本设置"))
        self.label_4.setText(_translate("MultiCamDlg", "增益"))
        self.label_3.setText(_translate("MultiCamDlg", "曝光"))
        self.groupBox_2.setTitle(_translate("MultiCamDlg", "设备控制"))
        self.open_device_btn.setText(_translate("MultiCamDlg", "打开相机"))
        self.close_device_btn.setText(_translate("MultiCamDlg", "关闭相机"))
        self.acquisition_start_btn.setText(_translate("MultiCamDlg", "开始采集"))
        self.acquisition_stop_btn.setText(_translate("MultiCamDlg", "停止采集"))
