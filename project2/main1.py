# 2024.7.19
# Q1:曝光时间上限为99.99；
# Q2：曝光时间设置缺少确认按钮，实时获取输入数据，可能会导致程序崩溃
# Q3：UI界面中的保存图像功能尚未开发

import sys
 
from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from multispectral.project2.UI.MainWindow1 import Ui_MainWindow
import cv2
import DahengCamera
from PyQt5 import QtCore


# 启用高 DPI 支持
QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)

class MainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
 
        self.Camera = DahengCamera.DahengCamera()
        self.TimerForShowImageInGraphicsView = QTimer()
        self.ImageWidthInGraphicsView = 600
        self.scene = QGraphicsScene()
 
        self.SlotInit()
        self.UpdateUI()
 
    """ 初始化槽信号函数"""
    def SlotInit(self):
        self.ui.pushButton_UpdateCameraList.clicked.connect(self.PB_UpdateCameraList_clicked)
        self.ui.pushButton_OpenCamera.clicked.connect(self.PB_OpenCamera_clicked)
        self.ui.pushButton_CloseCamera.clicked.connect(self.PB_CloseCamera_clicked)
        self.ui.pushButton_StartAcq.clicked.connect(self.PB_StartAcq_clicked)
        self.ui.pushButton_StopAcq.clicked.connect(self.PB_StopAcq_clicked)
        # self.ui.pushButton_ZoomIn.clicked.connect(self.PB_ZoomIn_clicked)
        # self.ui.pushButton_ZoomOut.clicked.connect(self.PB_ZoomOut_clicked)
        self.TimerForShowImageInGraphicsView.timeout.connect(self.SlotForShowImageInGraphicsView)
        # self.ui.pushButton_SendSoftwareCommand.clicked.connect(self.SendSoftwareCommand)
        self.SlotConnect()
 
    def SlotConnect(self):
        self.ui.comboBox_ExposureAuto.currentIndexChanged.connect(self.SetExposureAuto)
        self.ui.doubleSpinBox_ExposureTime.valueChanged.connect(self.SetExposureTime)
        # self.ui.comboBox_TriggerMode.currentIndexChanged.connect(self.SetTriggerAuto)
        # self.ui.comboBox_TriggerSource.currentIndexChanged.connect(self.SetTriggerSource)
        self.ui.comboBox_GainAuto.currentIndexChanged.connect(self.SetGainAuto)
        self.ui.doubleSpinBox_GainValue.valueChanged.connect(self.SetGainValue)
 
    def SlotDisConnect(self):
        self.ui.comboBox_ExposureAuto.currentIndexChanged.disconnect(self.SetExposureAuto)
        self.ui.doubleSpinBox_ExposureTime.valueChanged.disconnect(self.SetExposureTime)
        # self.ui.comboBox_TriggerMode.currentIndexChanged.disconnect(self.SetTriggerAuto)
        # self.ui.comboBox_TriggerSource.currentIndexChanged.disconnect(self.SetTriggerSource)
        self.ui.comboBox_GainAuto.currentIndexChanged.disconnect(self.SetGainAuto)
        self.ui.doubleSpinBox_GainValue.valueChanged.disconnect(self.SetGainValue)
 
    """ 更新UI界面"""
    def UpdateUI(self):
        self.ui.pushButton_OpenCamera.setDisabled(self.Camera.IsCameraOpened)
        self.ui.pushButton_CloseCamera.setDisabled(not self.Camera.IsCameraOpened)
        self.ui.pushButton_StartAcq.setDisabled(not self.Camera.IsCameraOpened or self.Camera.IsCameraStartAcq)
        self.ui.pushButton_StopAcq.setDisabled(not self.Camera.IsCameraStartAcq)
        self.ui.comboBox_ExposureMode.setDisabled(not self.Camera.IsCameraOpened)
        self.ui.comboBox_ExposureAuto.setDisabled(not self.Camera.IsCameraOpened)
        self.ui.doubleSpinBox_ExposureTime.setDisabled(not self.Camera.IsCameraOpened or
                                                       not self.ui.comboBox_ExposureAuto.currentIndex() == 0)
        # self.ui.pushButton_ZoomIn.setDisabled(not self.Camera.IsCameraStartAcq)
        # self.ui.pushButton_ZoomOut.setDisabled(not self.Camera.IsCameraStartAcq)
        # self.ui.comboBox_TriggerMode.setDisabled(not self.Camera.IsCameraOpened)
        # self.ui.comboBox_TriggerSource.setDisabled(not self.Camera.IsCameraOpened or
        #                                            self.ui.comboBox_TriggerMode.currentIndex() == 0)
        # self.ui.pushButton_SendSoftwareCommand.setDisabled(not self.Camera.IsCameraOpened or
        #                                                    self.ui.comboBox_TriggerMode.currentIndex() == 0 or
        #                                                    not self.ui.comboBox_TriggerSource.currentIndex() == 0)
        self.ui.comboBox_GainAuto.setDisabled(not self.Camera.IsCameraOpened)
        self.ui.doubleSpinBox_GainValue.setDisabled(not self.Camera.IsCameraOpened or
                                                    not self.ui.comboBox_GainAuto.currentIndex() == 0)
 
    """ 更新相机参数的可选项目"""
    def UpdateCameraPara_Range(self):
        self.SlotDisConnect()
 
        self.ui.comboBox_ExposureMode.clear()
        for Range in self.Camera.GetExposureModeRange():
            self.ui.comboBox_ExposureMode.addItem(Range)
 
        self.ui.comboBox_ExposureAuto.clear()
        for Range in self.Camera.GetExposureAutoRange():
            self.ui.comboBox_ExposureAuto.addItem(Range)
 
        # self.ui.comboBox_TriggerMode.clear()
        # for Range in self.Camera.GetTriggerAutoRange():
        #     self.ui.comboBox_TriggerMode.addItem(Range)
 
        # self.ui.comboBox_TriggerSource.clear()
        # for Range in self.Camera.GetTriggerSourceRange():
        #     self.ui.comboBox_TriggerSource.addItem(Range)
 
        self.ui.comboBox_GainAuto.clear()
        for Range in self.Camera.GetGainAutoRange():
            self.ui.comboBox_GainAuto.addItem(Range)
 
        self.SlotConnect()
 
    """ 读取相机当前参数值"""
    def GetCameraPara(self):
        self.SlotDisConnect()
 
        ExposureAuto = self.Camera.GetExposureAuto()
        self.ui.comboBox_ExposureAuto.setCurrentText(ExposureAuto[1])
 
        ExposureTime = self.Camera.GetExposureTime()
        self.ui.doubleSpinBox_ExposureTime.setValue(ExposureTime)
 
        # TriggerMode = self.Camera.GetTriggerAuto()
        # self.ui.comboBox_TriggerMode.setCurrentText(TriggerMode[1])
 
        # TriggerSource = self.Camera.GetTriggerSource()
        # self.ui.comboBox_TriggerSource.setCurrentText(TriggerSource[1])
 
        GainAuto = self.Camera.GetGainAuto()
        self.ui.comboBox_GainAuto.setCurrentText(GainAuto[1])
 
        GainValue = self.Camera.GetGainValue()
        self.ui.doubleSpinBox_GainValue.setValue(GainValue)
 
        self.SlotConnect()
 
    """ 点击UpdateCameraList"""
    def PB_UpdateCameraList_clicked(self):
        status, CameraNameList = self.Camera.UpdateCameraList()
        if status:
            for CameraName in CameraNameList:
                self.ui.comboBox_CameraList.addItem(CameraName)
 
    """ 点击OpenCamera"""
    def PB_OpenCamera_clicked(self):
        if self.ui.comboBox_CameraList.count() == 0:
            return
        self.Camera.OpenCamera(int(self.ui.comboBox_CameraList.currentIndex()) + 1)
        self.UpdateCameraPara_Range()
        self.GetCameraPara()
 
        self.UpdateUI()
 
    """ 点击CloseCamera"""
    def PB_CloseCamera_clicked(self):
        self.Camera.CloseCamera(int(self.ui.comboBox_CameraList.currentIndex()) + 1)
        if self.TimerForShowImageInGraphicsView.isActive():
            self.TimerForShowImageInGraphicsView.stop()
        DahengCamera.num = 0
 
        self.UpdateUI()
 
    """ 点击StartAcq"""
    def PB_StartAcq_clicked(self):
        self.Camera.StartAcquisition()
        self.TimerForShowImageInGraphicsView.start(33)
 
        self.UpdateUI()
 
    """ 点击StopAcq"""
    def PB_StopAcq_clicked(self):
        self.Camera.StopAcquisition()
        self.TimerForShowImageInGraphicsView.stop()
        self.UpdateUI()
 
        DahengCamera.num = 0
 
    """ 点击ZoomIn"""
    def PB_ZoomIn_clicked(self):
        self.ImageWidthInGraphicsView += 100
 
    """ 点击ZoomOut"""
    def PB_ZoomOut_clicked(self):
        if self.ImageWidthInGraphicsView >= 200:
            self.ImageWidthInGraphicsView -= 100
 
    """ 图像显示回调函数"""
    def SlotForShowImageInGraphicsView(self):
        if DahengCamera.rawImageUpdate is None:
            return
        else:
            ImageShow = DahengCamera.rawImageUpdateList[0]
            ImageRatio = float(ImageShow.shape[0] / ImageShow.shape[1])
            image_width = self.ImageWidthInGraphicsView
            show = cv2.resize(ImageShow, (image_width, int(image_width * ImageRatio)))
            show = cv2.cvtColor(show, cv2.COLOR_BGR2RGB)  # 视频色彩转换回RGB，这样才是现实的颜色
            showImage = QImage(show.data, show.shape[1], show.shape[0],
                               QImage.Format_RGB888)  # 把读取到的视频数据变成QImage形式
            item = QGraphicsPixmapItem(QPixmap.fromImage(showImage))
            self.scene.clear()
            self.scene.addItem(item)
            self.scene.setSceneRect(0, 0, image_width + 1, image_width * ImageRatio + 1)
            self.ui.graphicsView.setScene(self.scene)
            self.ui.graphicsView.show()
 
            # self.ui.label_AcqNum.setText(str(DahengCamera.num))
            # self.ui.label_FPS.setText(str(self.Camera.GetFPS()))
 
    """ ExposureAuto值改变"""
    def SetExposureAuto(self):
        self.Camera.SetExposureAuto(self.ui.comboBox_ExposureAuto.currentText())
        self.UpdateCameraPara_Range()
        self.GetCameraPara()
        self.UpdateUI()
 
    """ ExposureTime改变"""
    def SetExposureTime(self):
        self.Camera.SetExposureTime(self.ui.doubleSpinBox_ExposureTime.value())
        self.UpdateCameraPara_Range()
        self.GetCameraPara()
 
    # """ TriggerMode改变"""
    # def SetTriggerAuto(self):
    #     self.Camera.SetTriggerAuto(self.ui.comboBox_TriggerMode.currentText())
    #     self.UpdateCameraPara_Range()
    #     self.GetCameraPara()
    #     self.UpdateUI()
 
    # """ TriggerSource改变"""
    # def SetTriggerSource(self):
    #     self.Camera.SetTriggerSource(self.ui.comboBox_TriggerSource.currentText())
    #     self.UpdateCameraPara_Range()
    #     self.GetCameraPara()
    #     self.UpdateUI()
 
    # """ 发送软触发"""
    # def SendSoftwareCommand(self):
    #     self.Camera.SendSoftWareCommand()
 
    """ GainAuto改变"""
    def SetGainAuto(self):
        self.Camera.SetGainAuto(self.ui.comboBox_GainAuto.currentText())
        self.UpdateCameraPara_Range()
        self.GetCameraPara()
        self.UpdateUI()
 
    """ GainValue值改变"""
    def SetGainValue(self):
        self.Camera.SetGainValue(self.ui.doubleSpinBox_GainValue.value())
        self.UpdateCameraPara_Range()
        self.GetCameraPara()
 
 
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
 
    sys.exit(app.exec_())