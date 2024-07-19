import gxipy as gx
import time
import threading
 
rawImageUpdateList = []
rawImageUpdate = None
num = 0
 
 
def capture_callback(raw_image):
    if raw_image.get_status() == gx.GxFrameStatusList.INCOMPLETE:
        print("incomplete frame")
    else:
        global rawImageUpdateList, num, rawImageUpdate
        rawImageUpdate = raw_image.get_numpy_array()
        if len(rawImageUpdateList) == 0:
            rawImageUpdateList.append(rawImageUpdate)
        else:
            rawImageUpdateList.pop()
            rawImageUpdateList.append(rawImageUpdate)
        num += 1
 
 
class DahengCamera:
    def __init__(self):
        self.cam = None             #   相机对象
        self.dev_num = None
        self.dev_info_list = None
        self.device_manager = gx.DeviceManager()
        self.AcquisitionThread = None
        self.AcquisitionThreadNeedBeStop = False
        self.IsCameraOpened = False
        self.IsCameraStartAcq = False
 
    def UpdateCameraList(self):
        self.dev_num, self.dev_info_list = self.device_manager.update_device_list()
        if self.dev_num == 0:
            return False, '0'
        else:
            CameraNameList = []
            for info in self.dev_info_list:
                name = info['model_name']
                CameraNameList.append(name)
            return True, CameraNameList
 
    def OpenCamera(self, Index):
        if self.dev_num == 0:
            return False
        elif self.IsCameraOpened:
            return True
        else:
            # self.cam = self.device_manager.open_device_by_index(Index)
            self.cam = self.device_manager.open_device_by_sn(self.dev_info_list[0].get("sn"))
 
        self.AcquisitionThread = threading.Thread(target=self.AcquisitionThreadFunc_CallBack, args=(), daemon=True)
        self.AcquisitionThread.start()
        self.IsCameraOpened = True
        self.AcquisitionThreadNeedBeStop = False
 
        return True
 
    def AcquisitionThreadFunc_CallBack(self):
        self.cam.data_stream[0].register_capture_callback(capture_callback)
 
        while not self.AcquisitionThreadNeedBeStop:
            time.sleep(1)
 
    def CloseCamera(self, Index):
        if not self.IsCameraOpened:
            return
 
        self.AcquisitionThreadNeedBeStop = True
        self.StopAcquisition()
        time.sleep(1)
        self.cam.data_stream[0].unregister_capture_callback()
        self.cam.close_device()
 
        self.IsCameraOpened = False
 
    def StartAcquisition(self):
        if self.IsCameraOpened and not self.IsCameraStartAcq:
            self.cam.stream_on()
            self.IsCameraStartAcq = True
        else:
            return
 
    def StopAcquisition(self):
        if self.IsCameraOpened and self.IsCameraStartAcq:
            self.cam.stream_off()
            self.IsCameraStartAcq = False
        else:
            return
 
    def GetFPS(self):
        return self.cam.CurrentAcquisitionFrameRate.get()
 
    def GetExposureModeRange(self):
        return self.cam.ExposureMode.get_range()
 
    def GetExposureMode(self):
        return self.cam.ExposureMode.get()
 
    def GetExposureAutoRange(self):
        return self.cam.ExposureAuto.get_range()
 
    def GetExposureAuto(self):
        return self.cam.ExposureAuto.get()
 
    def SetExposureAuto(self, ExposureAuto):
        self.cam.ExposureAuto.set(eval('gx.GxAutoEntry.' + ExposureAuto.upper()))
        # self.cam.ExposureAuto.set(Index)
 
    def GetExposureTime(self):
        return self.cam.ExposureTime.get()
 
    def SetExposureTime(self, ExposureTime):
        self.cam.ExposureTime.set(ExposureTime)
 
    def GetTriggerAutoRange(self):
        return self.cam.TriggerMode.get_range()
 
    def SetTriggerAuto(self, TriggerAuto):
        self.cam.TriggerMode.set(eval('gx.GxSwitchEntry.' + TriggerAuto.upper()))
 
    def GetTriggerAuto(self):
        return self.cam.TriggerMode.get()
 
    def GetTriggerSourceRange(self):
        return self.cam.TriggerSource.get_range()
 
    def SetTriggerSource(self, TriggerSource):
        self.cam.TriggerSource.set(eval('gx.GxTriggerSourceEntry.' + TriggerSource.upper()))
 
    def GetTriggerSource(self):
        return self.cam.TriggerSource.get()
 
    def SendSoftWareCommand(self):
        self.cam.TriggerSoftware.send_command()
 
    def GetGainAutoRange(self):
        return self.cam.GainAuto.get_range()
 
    def GetGainAuto(self):
        return self.cam.GainAuto.get()
 
    def GetGainValue(self):
        return self.cam.Gain.get()
 
    def SetGainAuto(self, GainAuto):
        self.cam.GainAuto.set(eval('gx.GxAutoEntry.' + GainAuto.upper()))
 
    def SetGainValue(self, GainValue):
        self.cam.Gain.set(GainValue)