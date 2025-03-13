import LibLoader
import ctypes
import numpy as np

bufferSize = ctypes.c_size_t(1000)
charBuffer = ctypes.create_string_buffer(bufferSize.value)

class FliCblueSfnc:
	#------------------------------------------------------------
	LibLoader.lib.FliCblueSfnc_getDeviceScanType_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_int)]
	LibLoader.lib.FliCblueSfnc_getDeviceScanType_V2.restype = ctypes.c_bool
	def GetDeviceScanType(self, context):
		val = ctypes.c_int(0)
		res = LibLoader.lib.FliCblueSfnc_getDeviceScanType_V2(context, ctypes.byref(val))
		return res, val.value

	#------------------------------------------------------------
	LibLoader.lib.FliCblueSfnc_getDeviceIndicatorMode_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_int)]
	LibLoader.lib.FliCblueSfnc_getDeviceIndicatorMode_V2.restype = ctypes.c_bool
	def GetDeviceIndicatorMode(self, context):
		val = ctypes.c_int(0)
		res = LibLoader.lib.FliCblueSfnc_getDeviceIndicatorMode_V2(context, ctypes.byref(val))
		return res, val.value

	#------------------------------------------------------------
	LibLoader.lib.FliCblueSfnc_setDeviceIndicatorMode_V2.argtypes = [ctypes.c_void_p, ctypes.c_int]
	LibLoader.lib.FliCblueSfnc_setDeviceIndicatorMode_V2.restype = ctypes.c_bool
	def SetDeviceIndicatorMode(self, context, val):
		return LibLoader.lib.FliCblueSfnc_setDeviceIndicatorMode_V2(context, val)

	#------------------------------------------------------------
	LibLoader.lib.FliCblueSfnc_getSensorShutterMode_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_int)]
	LibLoader.lib.FliCblueSfnc_getSensorShutterMode_V2.restype = ctypes.c_bool
	def GetSensorShutterMode(self, context):
		val = ctypes.c_int(0)
		res = LibLoader.lib.FliCblueSfnc_getSensorShutterMode_V2(context, ctypes.byref(val))
		return res, val.value

	#------------------------------------------------------------
	LibLoader.lib.FliCblueSfnc_getRegionSelector_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_int)]
	LibLoader.lib.FliCblueSfnc_getRegionSelector_V2.restype = ctypes.c_bool
	def GetRegionSelector(self, context):
		val = ctypes.c_int(0)
		res = LibLoader.lib.FliCblueSfnc_getRegionSelector_V2(context, ctypes.byref(val))
		return res, val.value

	#------------------------------------------------------------
	LibLoader.lib.FliCblueSfnc_setRegionSelector_V2.argtypes = [ctypes.c_void_p, ctypes.c_int]
	LibLoader.lib.FliCblueSfnc_setRegionSelector_V2.restype = ctypes.c_bool
	def SetRegionSelector(self, context, val):
		return LibLoader.lib.FliCblueSfnc_setRegionSelector_V2(context, val)

	#------------------------------------------------------------
	LibLoader.lib.FliCblueSfnc_getRegionMode_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_int)]
	LibLoader.lib.FliCblueSfnc_getRegionMode_V2.restype = ctypes.c_bool
	def GetRegionMode(self, context):
		val = ctypes.c_int(0)
		res = LibLoader.lib.FliCblueSfnc_getRegionMode_V2(context, ctypes.byref(val))
		return res, val.value

	#------------------------------------------------------------
	LibLoader.lib.FliCblueSfnc_getRegionDestination_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_int)]
	LibLoader.lib.FliCblueSfnc_getRegionDestination_V2.restype = ctypes.c_bool
	def GetRegionDestination(self, context):
		val = ctypes.c_int(0)
		res = LibLoader.lib.FliCblueSfnc_getRegionDestination_V2(context, ctypes.byref(val))
		return res, val.value

	#------------------------------------------------------------
	LibLoader.lib.FliCblueSfnc_setRegionDestination_V2.argtypes = [ctypes.c_void_p, ctypes.c_int]
	LibLoader.lib.FliCblueSfnc_setRegionDestination_V2.restype = ctypes.c_bool
	def SetRegionDestination(self, context, val):
		return LibLoader.lib.FliCblueSfnc_setRegionDestination_V2(context, val)

	#------------------------------------------------------------
	LibLoader.lib.FliCblueSfnc_getPixelFormat_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_int)]
	LibLoader.lib.FliCblueSfnc_getPixelFormat_V2.restype = ctypes.c_bool
	def GetPixelFormat(self, context):
		val = ctypes.c_int(0)
		res = LibLoader.lib.FliCblueSfnc_getPixelFormat_V2(context, ctypes.byref(val))
		return res, val.value

	#------------------------------------------------------------
	LibLoader.lib.FliCblueSfnc_setPixelFormat_V2.argtypes = [ctypes.c_void_p, ctypes.c_int]
	LibLoader.lib.FliCblueSfnc_setPixelFormat_V2.restype = ctypes.c_bool
	def SetPixelFormat(self, context, val):
		return LibLoader.lib.FliCblueSfnc_setPixelFormat_V2(context, val)

	#------------------------------------------------------------
	LibLoader.lib.FliCblueSfnc_getAcquisitionMode_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_int)]
	LibLoader.lib.FliCblueSfnc_getAcquisitionMode_V2.restype = ctypes.c_bool
	def GetAcquisitionMode(self, context):
		val = ctypes.c_int(0)
		res = LibLoader.lib.FliCblueSfnc_getAcquisitionMode_V2(context, ctypes.byref(val))
		return res, val.value

	#------------------------------------------------------------
	LibLoader.lib.FliCblueSfnc_setAcquisitionMode_V2.argtypes = [ctypes.c_void_p, ctypes.c_int]
	LibLoader.lib.FliCblueSfnc_setAcquisitionMode_V2.restype = ctypes.c_bool
	def SetAcquisitionMode(self, context, val):
		return LibLoader.lib.FliCblueSfnc_setAcquisitionMode_V2(context, val)

	#------------------------------------------------------------
	LibLoader.lib.FliCblueSfnc_getExposureMode_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_int)]
	LibLoader.lib.FliCblueSfnc_getExposureMode_V2.restype = ctypes.c_bool
	def GetExposureMode(self, context):
		val = ctypes.c_int(0)
		res = LibLoader.lib.FliCblueSfnc_getExposureMode_V2(context, ctypes.byref(val))
		return res, val.value

	#------------------------------------------------------------
	LibLoader.lib.FliCblueSfnc_setExposureMode_V2.argtypes = [ctypes.c_void_p, ctypes.c_int]
	LibLoader.lib.FliCblueSfnc_setExposureMode_V2.restype = ctypes.c_bool
	def SetExposureMode(self, context, val):
		return LibLoader.lib.FliCblueSfnc_setExposureMode_V2(context, val)

	#------------------------------------------------------------
	LibLoader.lib.FliCblueSfnc_getGainSelector_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_int)]
	LibLoader.lib.FliCblueSfnc_getGainSelector_V2.restype = ctypes.c_bool
	def GetGainSelector(self, context):
		val = ctypes.c_int(0)
		res = LibLoader.lib.FliCblueSfnc_getGainSelector_V2(context, ctypes.byref(val))
		return res, val.value

	#------------------------------------------------------------
	LibLoader.lib.FliCblueSfnc_setGainSelector_V2.argtypes = [ctypes.c_void_p, ctypes.c_int]
	LibLoader.lib.FliCblueSfnc_setGainSelector_V2.restype = ctypes.c_bool
	def SetGainSelector(self, context, val):
		return LibLoader.lib.FliCblueSfnc_setGainSelector_V2(context, val)

	#------------------------------------------------------------
	LibLoader.lib.FliCblueSfnc_getBlackLevelSelector_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_int)]
	LibLoader.lib.FliCblueSfnc_getBlackLevelSelector_V2.restype = ctypes.c_bool
	def GetBlackLevelSelector(self, context):
		val = ctypes.c_int(0)
		res = LibLoader.lib.FliCblueSfnc_getBlackLevelSelector_V2(context, ctypes.byref(val))
		return res, val.value

	#------------------------------------------------------------
	LibLoader.lib.FliCblueSfnc_setBlackLevelSelector_V2.argtypes = [ctypes.c_void_p, ctypes.c_int]
	LibLoader.lib.FliCblueSfnc_setBlackLevelSelector_V2.restype = ctypes.c_bool
	def SetBlackLevelSelector(self, context, val):
		return LibLoader.lib.FliCblueSfnc_setBlackLevelSelector_V2(context, val)

	#------------------------------------------------------------
	LibLoader.lib.FliCblueSfnc_getBlackLevelAuto_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_int)]
	LibLoader.lib.FliCblueSfnc_getBlackLevelAuto_V2.restype = ctypes.c_bool
	def GetBlackLevelAuto(self, context):
		val = ctypes.c_int(0)
		res = LibLoader.lib.FliCblueSfnc_getBlackLevelAuto_V2(context, ctypes.byref(val))
		return res, val.value

	#------------------------------------------------------------
	LibLoader.lib.FliCblueSfnc_setBlackLevelAuto_V2.argtypes = [ctypes.c_void_p, ctypes.c_int]
	LibLoader.lib.FliCblueSfnc_setBlackLevelAuto_V2.restype = ctypes.c_bool
	def SetBlackLevelAuto(self, context, val):
		return LibLoader.lib.FliCblueSfnc_setBlackLevelAuto_V2(context, val)

	#------------------------------------------------------------
	LibLoader.lib.FliCblueSfnc_getCxpLinkConfigurationStatus_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_int)]
	LibLoader.lib.FliCblueSfnc_getCxpLinkConfigurationStatus_V2.restype = ctypes.c_bool
	def GetCxpLinkConfigurationStatus(self, context):
		val = ctypes.c_int(0)
		res = LibLoader.lib.FliCblueSfnc_getCxpLinkConfigurationStatus_V2(context, ctypes.byref(val))
		return res, val.value

	#------------------------------------------------------------
	LibLoader.lib.FliCblueSfnc_getCxpLinkConfigurationPreferred_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_int)]
	LibLoader.lib.FliCblueSfnc_getCxpLinkConfigurationPreferred_V2.restype = ctypes.c_bool
	def GetCxpLinkConfigurationPreferred(self, context):
		val = ctypes.c_int(0)
		res = LibLoader.lib.FliCblueSfnc_getCxpLinkConfigurationPreferred_V2(context, ctypes.byref(val))
		return res, val.value

	#------------------------------------------------------------
	LibLoader.lib.FliCblueSfnc_getCxpLinkConfiguration_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_int)]
	LibLoader.lib.FliCblueSfnc_getCxpLinkConfiguration_V2.restype = ctypes.c_bool
	def GetCxpLinkConfiguration(self, context):
		val = ctypes.c_int(0)
		res = LibLoader.lib.FliCblueSfnc_getCxpLinkConfiguration_V2(context, ctypes.byref(val))
		return res, val.value

	#------------------------------------------------------------
	LibLoader.lib.FliCblueSfnc_getCxpConnectionTestMode_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_int)]
	LibLoader.lib.FliCblueSfnc_getCxpConnectionTestMode_V2.restype = ctypes.c_bool
	def GetCxpConnectionTestMode(self, context):
		val = ctypes.c_int(0)
		res = LibLoader.lib.FliCblueSfnc_getCxpConnectionTestMode_V2(context, ctypes.byref(val))
		return res, val.value

	#------------------------------------------------------------
	LibLoader.lib.FliCblueSfnc_setCxpConnectionTestMode_V2.argtypes = [ctypes.c_void_p, ctypes.c_int]
	LibLoader.lib.FliCblueSfnc_setCxpConnectionTestMode_V2.restype = ctypes.c_bool
	def SetCxpConnectionTestMode(self, context, val):
		return LibLoader.lib.FliCblueSfnc_setCxpConnectionTestMode_V2(context, val)

	#------------------------------------------------------------
	LibLoader.lib.FliCblueSfnc_getCxpSendReceiveSelector_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_int)]
	LibLoader.lib.FliCblueSfnc_getCxpSendReceiveSelector_V2.restype = ctypes.c_bool
	def GetCxpSendReceiveSelector(self, context):
		val = ctypes.c_int(0)
		res = LibLoader.lib.FliCblueSfnc_getCxpSendReceiveSelector_V2(context, ctypes.byref(val))
		return res, val.value

	#------------------------------------------------------------
	LibLoader.lib.FliCblueSfnc_setCxpSendReceiveSelector_V2.argtypes = [ctypes.c_void_p, ctypes.c_int]
	LibLoader.lib.FliCblueSfnc_setCxpSendReceiveSelector_V2.restype = ctypes.c_bool
	def SetCxpSendReceiveSelector(self, context, val):
		return LibLoader.lib.FliCblueSfnc_setCxpSendReceiveSelector_V2(context, val)

	#------------------------------------------------------------
	LibLoader.lib.FliCblueSfnc_getCxpErrorCounterSelector_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_int)]
	LibLoader.lib.FliCblueSfnc_getCxpErrorCounterSelector_V2.restype = ctypes.c_bool
	def GetCxpErrorCounterSelector(self, context):
		val = ctypes.c_int(0)
		res = LibLoader.lib.FliCblueSfnc_getCxpErrorCounterSelector_V2(context, ctypes.byref(val))
		return res, val.value

	#------------------------------------------------------------
	LibLoader.lib.FliCblueSfnc_setCxpErrorCounterSelector_V2.argtypes = [ctypes.c_void_p, ctypes.c_int]
	LibLoader.lib.FliCblueSfnc_setCxpErrorCounterSelector_V2.restype = ctypes.c_bool
	def SetCxpErrorCounterSelector(self, context, val):
		return LibLoader.lib.FliCblueSfnc_setCxpErrorCounterSelector_V2(context, val)

	#------------------------------------------------------------
	LibLoader.lib.FliCblueSfnc_getCxpErrorCounterStatus_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_int)]
	LibLoader.lib.FliCblueSfnc_getCxpErrorCounterStatus_V2.restype = ctypes.c_bool
	def GetCxpErrorCounterStatus(self, context):
		val = ctypes.c_int(0)
		res = LibLoader.lib.FliCblueSfnc_getCxpErrorCounterStatus_V2(context, ctypes.byref(val))
		return res, val.value

	#------------------------------------------------------------
	LibLoader.lib.FliCblueSfnc_getSensorWidth_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_int)]
	LibLoader.lib.FliCblueSfnc_getSensorWidth_V2.restype = ctypes.c_bool
	def GetSensorWidth(self, context):
		val = ctypes.c_int(0)
		res = LibLoader.lib.FliCblueSfnc_getSensorWidth_V2(context, ctypes.byref(val))
		return res, val.value

	#------------------------------------------------------------
	LibLoader.lib.FliCblueSfnc_getSensorHeight_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_int)]
	LibLoader.lib.FliCblueSfnc_getSensorHeight_V2.restype = ctypes.c_bool
	def GetSensorHeight(self, context):
		val = ctypes.c_int(0)
		res = LibLoader.lib.FliCblueSfnc_getSensorHeight_V2(context, ctypes.byref(val))
		return res, val.value

	#------------------------------------------------------------
	LibLoader.lib.FliCblueSfnc_getWidthMax_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_int)]
	LibLoader.lib.FliCblueSfnc_getWidthMax_V2.restype = ctypes.c_bool
	def GetWidthMax(self, context):
		val = ctypes.c_int(0)
		res = LibLoader.lib.FliCblueSfnc_getWidthMax_V2(context, ctypes.byref(val))
		return res, val.value

	#------------------------------------------------------------
	LibLoader.lib.FliCblueSfnc_getHeightMax_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_int)]
	LibLoader.lib.FliCblueSfnc_getHeightMax_V2.restype = ctypes.c_bool
	def GetHeightMax(self, context):
		val = ctypes.c_int(0)
		res = LibLoader.lib.FliCblueSfnc_getHeightMax_V2(context, ctypes.byref(val))
		return res, val.value

	#------------------------------------------------------------
	LibLoader.lib.FliCblueSfnc_getWidth_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_int)]
	LibLoader.lib.FliCblueSfnc_getWidth_V2.restype = ctypes.c_bool
	def GetWidth(self, context):
		val = ctypes.c_int(0)
		res = LibLoader.lib.FliCblueSfnc_getWidth_V2(context, ctypes.byref(val))
		return res, val.value

	#------------------------------------------------------------
	LibLoader.lib.FliCblueSfnc_setWidth_V2.argtypes = [ctypes.c_void_p, ctypes.c_int]
	LibLoader.lib.FliCblueSfnc_setWidth_V2.restype = ctypes.c_bool
	def SetWidth(self, context, val):
		return LibLoader.lib.FliCblueSfnc_setWidth_V2(context, val)

	#------------------------------------------------------------
	LibLoader.lib.FliCblueSfnc_getHeight_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_int)]
	LibLoader.lib.FliCblueSfnc_getHeight_V2.restype = ctypes.c_bool
	def GetHeight(self, context):
		val = ctypes.c_int(0)
		res = LibLoader.lib.FliCblueSfnc_getHeight_V2(context, ctypes.byref(val))
		return res, val.value

	#------------------------------------------------------------
	LibLoader.lib.FliCblueSfnc_setHeight_V2.argtypes = [ctypes.c_void_p, ctypes.c_int]
	LibLoader.lib.FliCblueSfnc_setHeight_V2.restype = ctypes.c_bool
	def SetHeight(self, context, val):
		return LibLoader.lib.FliCblueSfnc_setHeight_V2(context, val)

	#------------------------------------------------------------
	LibLoader.lib.FliCblueSfnc_getOffsetX_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_int)]
	LibLoader.lib.FliCblueSfnc_getOffsetX_V2.restype = ctypes.c_bool
	def GetOffsetX(self, context):
		val = ctypes.c_int(0)
		res = LibLoader.lib.FliCblueSfnc_getOffsetX_V2(context, ctypes.byref(val))
		return res, val.value

	#------------------------------------------------------------
	LibLoader.lib.FliCblueSfnc_setOffsetX_V2.argtypes = [ctypes.c_void_p, ctypes.c_int]
	LibLoader.lib.FliCblueSfnc_setOffsetX_V2.restype = ctypes.c_bool
	def SetOffsetX(self, context, val):
		return LibLoader.lib.FliCblueSfnc_setOffsetX_V2(context, val)

	#------------------------------------------------------------
	LibLoader.lib.FliCblueSfnc_getOffsetY_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_int)]
	LibLoader.lib.FliCblueSfnc_getOffsetY_V2.restype = ctypes.c_bool
	def GetOffsetY(self, context):
		val = ctypes.c_int(0)
		res = LibLoader.lib.FliCblueSfnc_getOffsetY_V2(context, ctypes.byref(val))
		return res, val.value

	#------------------------------------------------------------
	LibLoader.lib.FliCblueSfnc_setOffsetY_V2.argtypes = [ctypes.c_void_p, ctypes.c_int]
	LibLoader.lib.FliCblueSfnc_setOffsetY_V2.restype = ctypes.c_bool
	def SetOffsetY(self, context, val):
		return LibLoader.lib.FliCblueSfnc_setOffsetY_V2(context, val)

	#------------------------------------------------------------
	LibLoader.lib.FliCblueSfnc_getAcquisitionFrameCount_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_int)]
	LibLoader.lib.FliCblueSfnc_getAcquisitionFrameCount_V2.restype = ctypes.c_bool
	def GetAcquisitionFrameCount(self, context):
		val = ctypes.c_int(0)
		res = LibLoader.lib.FliCblueSfnc_getAcquisitionFrameCount_V2(context, ctypes.byref(val))
		return res, val.value

	#------------------------------------------------------------
	LibLoader.lib.FliCblueSfnc_setAcquisitionFrameCount_V2.argtypes = [ctypes.c_void_p, ctypes.c_int]
	LibLoader.lib.FliCblueSfnc_setAcquisitionFrameCount_V2.restype = ctypes.c_bool
	def SetAcquisitionFrameCount(self, context, val):
		return LibLoader.lib.FliCblueSfnc_setAcquisitionFrameCount_V2(context, val)

	#------------------------------------------------------------
	LibLoader.lib.FliCblueSfnc_getCxpConnectionSelector_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_int)]
	LibLoader.lib.FliCblueSfnc_getCxpConnectionSelector_V2.restype = ctypes.c_bool
	def GetCxpConnectionSelector(self, context):
		val = ctypes.c_int(0)
		res = LibLoader.lib.FliCblueSfnc_getCxpConnectionSelector_V2(context, ctypes.byref(val))
		return res, val.value

	#------------------------------------------------------------
	LibLoader.lib.FliCblueSfnc_setCxpConnectionSelector_V2.argtypes = [ctypes.c_void_p, ctypes.c_int]
	LibLoader.lib.FliCblueSfnc_setCxpConnectionSelector_V2.restype = ctypes.c_bool
	def SetCxpConnectionSelector(self, context, val):
		return LibLoader.lib.FliCblueSfnc_setCxpConnectionSelector_V2(context, val)

	#------------------------------------------------------------
	LibLoader.lib.FliCblueSfnc_getCxpConnectionTestErrorCount_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_int)]
	LibLoader.lib.FliCblueSfnc_getCxpConnectionTestErrorCount_V2.restype = ctypes.c_bool
	def GetCxpConnectionTestErrorCount(self, context):
		val = ctypes.c_int(0)
		res = LibLoader.lib.FliCblueSfnc_getCxpConnectionTestErrorCount_V2(context, ctypes.byref(val))
		return res, val.value

	#------------------------------------------------------------
	LibLoader.lib.FliCblueSfnc_setCxpConnectionTestErrorCount_V2.argtypes = [ctypes.c_void_p, ctypes.c_int]
	LibLoader.lib.FliCblueSfnc_setCxpConnectionTestErrorCount_V2.restype = ctypes.c_bool
	def SetCxpConnectionTestErrorCount(self, context, val):
		return LibLoader.lib.FliCblueSfnc_setCxpConnectionTestErrorCount_V2(context, val)

	#------------------------------------------------------------
	LibLoader.lib.FliCblueSfnc_getCxpConnectionTestPacketCount_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_int)]
	LibLoader.lib.FliCblueSfnc_getCxpConnectionTestPacketCount_V2.restype = ctypes.c_bool
	def GetCxpConnectionTestPacketCount(self, context):
		val = ctypes.c_int(0)
		res = LibLoader.lib.FliCblueSfnc_getCxpConnectionTestPacketCount_V2(context, ctypes.byref(val))
		return res, val.value

	#------------------------------------------------------------
	LibLoader.lib.FliCblueSfnc_setCxpConnectionTestPacketCount_V2.argtypes = [ctypes.c_void_p, ctypes.c_int]
	LibLoader.lib.FliCblueSfnc_setCxpConnectionTestPacketCount_V2.restype = ctypes.c_bool
	def SetCxpConnectionTestPacketCount(self, context, val):
		return LibLoader.lib.FliCblueSfnc_setCxpConnectionTestPacketCount_V2(context, val)

	#------------------------------------------------------------
	LibLoader.lib.FliCblueSfnc_getCxpErrorCounterValue_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_int)]
	LibLoader.lib.FliCblueSfnc_getCxpErrorCounterValue_V2.restype = ctypes.c_bool
	def GetCxpErrorCounterValue(self, context):
		val = ctypes.c_int(0)
		res = LibLoader.lib.FliCblueSfnc_getCxpErrorCounterValue_V2(context, ctypes.byref(val))
		return res, val.value

	#------------------------------------------------------------
	LibLoader.lib.FliCblueSfnc_setCxpErrorCounterValue_V2.argtypes = [ctypes.c_void_p, ctypes.c_int]
	LibLoader.lib.FliCblueSfnc_setCxpErrorCounterValue_V2.restype = ctypes.c_bool
	def SetCxpErrorCounterValue(self, context, val):
		return LibLoader.lib.FliCblueSfnc_setCxpErrorCounterValue_V2(context, val)

	#------------------------------------------------------------
	LibLoader.lib.FliCblueSfnc_getTLParamsLocked_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_int)]
	LibLoader.lib.FliCblueSfnc_getTLParamsLocked_V2.restype = ctypes.c_bool
	def GetTLParamsLocked(self, context):
		val = ctypes.c_int(0)
		res = LibLoader.lib.FliCblueSfnc_getTLParamsLocked_V2(context, ctypes.byref(val))
		return res, val.value

	#------------------------------------------------------------
	LibLoader.lib.FliCblueSfnc_setTLParamsLocked_V2.argtypes = [ctypes.c_void_p, ctypes.c_int]
	LibLoader.lib.FliCblueSfnc_setTLParamsLocked_V2.restype = ctypes.c_bool
	def SetTLParamsLocked(self, context, val):
		return LibLoader.lib.FliCblueSfnc_setTLParamsLocked_V2(context, val)

	#------------------------------------------------------------
	LibLoader.lib.FliCblueSfnc_getDeviceVendorName_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_size_t]
	LibLoader.lib.FliCblueSfnc_getDeviceVendorName_V2.restype = ctypes.c_bool
	def GetDeviceVendorName(self, context):
		res = LibLoader.lib.FliCblueSfnc_getDeviceVendorName_V2(context, charBuffer, bufferSize)
		return res, charBuffer.value.decode('utf-8', 'ignore')

	#------------------------------------------------------------
	LibLoader.lib.FliCblueSfnc_getDeviceModelName_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_size_t]
	LibLoader.lib.FliCblueSfnc_getDeviceModelName_V2.restype = ctypes.c_bool
	def GetDeviceModelName(self, context):
		res = LibLoader.lib.FliCblueSfnc_getDeviceModelName_V2(context, charBuffer, bufferSize)
		return res, charBuffer.value.decode('utf-8', 'ignore')

	#------------------------------------------------------------
	LibLoader.lib.FliCblueSfnc_getDeviceManufacturerInfo_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_size_t]
	LibLoader.lib.FliCblueSfnc_getDeviceManufacturerInfo_V2.restype = ctypes.c_bool
	def GetDeviceManufacturerInfo(self, context):
		res = LibLoader.lib.FliCblueSfnc_getDeviceManufacturerInfo_V2(context, charBuffer, bufferSize)
		return res, charBuffer.value.decode('utf-8', 'ignore')

	#------------------------------------------------------------
	LibLoader.lib.FliCblueSfnc_getDeviceVersion_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_size_t]
	LibLoader.lib.FliCblueSfnc_getDeviceVersion_V2.restype = ctypes.c_bool
	def GetDeviceVersion(self, context):
		res = LibLoader.lib.FliCblueSfnc_getDeviceVersion_V2(context, charBuffer, bufferSize)
		return res, charBuffer.value.decode('utf-8', 'ignore')

	#------------------------------------------------------------
	LibLoader.lib.FliCblueSfnc_getDeviceFirmwareVersion_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_size_t]
	LibLoader.lib.FliCblueSfnc_getDeviceFirmwareVersion_V2.restype = ctypes.c_bool
	def GetDeviceFirmwareVersion(self, context):
		res = LibLoader.lib.FliCblueSfnc_getDeviceFirmwareVersion_V2(context, charBuffer, bufferSize)
		return res, charBuffer.value.decode('utf-8', 'ignore')

	#------------------------------------------------------------
	LibLoader.lib.FliCblueSfnc_getDeviceSerialNumber_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_size_t]
	LibLoader.lib.FliCblueSfnc_getDeviceSerialNumber_V2.restype = ctypes.c_bool
	def GetDeviceSerialNumber(self, context):
		res = LibLoader.lib.FliCblueSfnc_getDeviceSerialNumber_V2(context, charBuffer, bufferSize)
		return res, charBuffer.value.decode('utf-8', 'ignore')

	#------------------------------------------------------------
	LibLoader.lib.FliCblueSfnc_getDeviceUserID_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_size_t]
	LibLoader.lib.FliCblueSfnc_getDeviceUserID_V2.restype = ctypes.c_bool
	def GetDeviceUserID(self, context):
		res = LibLoader.lib.FliCblueSfnc_getDeviceUserID_V2(context, charBuffer, bufferSize)
		return res, charBuffer.value.decode('utf-8', 'ignore')

	#------------------------------------------------------------
	LibLoader.lib.FliCblueSfnc_setDeviceUserID_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
	LibLoader.lib.FliCblueSfnc_setDeviceUserID_V2.restype = ctypes.c_bool
	def SetDeviceUserID(self, context, val):
		return LibLoader.lib.FliCblueSfnc_setDeviceUserID_V2(context, val.encode())

	#------------------------------------------------------------
	LibLoader.lib.FliCblueSfnc_getDeviceTemperature_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_double)]
	LibLoader.lib.FliCblueSfnc_getDeviceTemperature_V2.restype = ctypes.c_bool
	def GetDeviceTemperature(self, context):
		val = ctypes.c_double(0)
		res = LibLoader.lib.FliCblueSfnc_getDeviceTemperature_V2(context, ctypes.byref(val))
		return res, val.value

	#------------------------------------------------------------
	LibLoader.lib.FliCblueSfnc_getSensorPixelWidth_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_double)]
	LibLoader.lib.FliCblueSfnc_getSensorPixelWidth_V2.restype = ctypes.c_bool
	def GetSensorPixelWidth(self, context):
		val = ctypes.c_double(0)
		res = LibLoader.lib.FliCblueSfnc_getSensorPixelWidth_V2(context, ctypes.byref(val))
		return res, val.value

	#------------------------------------------------------------
	LibLoader.lib.FliCblueSfnc_getSensorPixelHeight_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_double)]
	LibLoader.lib.FliCblueSfnc_getSensorPixelHeight_V2.restype = ctypes.c_bool
	def GetSensorPixelHeight(self, context):
		val = ctypes.c_double(0)
		res = LibLoader.lib.FliCblueSfnc_getSensorPixelHeight_V2(context, ctypes.byref(val))
		return res, val.value

	#------------------------------------------------------------
	LibLoader.lib.FliCblueSfnc_getAcquisitionFrameRate_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_double)]
	LibLoader.lib.FliCblueSfnc_getAcquisitionFrameRate_V2.restype = ctypes.c_bool
	def GetAcquisitionFrameRate(self, context):
		val = ctypes.c_double(0)
		res = LibLoader.lib.FliCblueSfnc_getAcquisitionFrameRate_V2(context, ctypes.byref(val))
		return res, val.value

	#------------------------------------------------------------
	LibLoader.lib.FliCblueSfnc_setAcquisitionFrameRate_V2.argtypes = [ctypes.c_void_p, ctypes.c_double]
	LibLoader.lib.FliCblueSfnc_setAcquisitionFrameRate_V2.restype = ctypes.c_bool
	def SetAcquisitionFrameRate(self, context, val):
		return LibLoader.lib.FliCblueSfnc_setAcquisitionFrameRate_V2(context, val)

	#------------------------------------------------------------
	LibLoader.lib.FliCblueSfnc_getAcquisitionFrameRateMin_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_double)]
	LibLoader.lib.FliCblueSfnc_getAcquisitionFrameRateMin_V2.restype = ctypes.c_bool
	def GetAcquisitionFrameRateMin(self, context):
		val = ctypes.c_double(0)
		res = LibLoader.lib.FliCblueSfnc_getAcquisitionFrameRateMin_V2(context, ctypes.byref(val))
		return res, val.value

	#------------------------------------------------------------
	LibLoader.lib.FliCblueSfnc_getAcquisitionFrameRateMax_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_double)]
	LibLoader.lib.FliCblueSfnc_getAcquisitionFrameRateMax_V2.restype = ctypes.c_bool
	def GetAcquisitionFrameRateMax(self, context):
		val = ctypes.c_double(0)
		res = LibLoader.lib.FliCblueSfnc_getAcquisitionFrameRateMax_V2(context, ctypes.byref(val))
		return res, val.value

	#------------------------------------------------------------
	LibLoader.lib.FliCblueSfnc_getExposureTime_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_double)]
	LibLoader.lib.FliCblueSfnc_getExposureTime_V2.restype = ctypes.c_bool
	def GetExposureTime(self, context):
		val = ctypes.c_double(0)
		res = LibLoader.lib.FliCblueSfnc_getExposureTime_V2(context, ctypes.byref(val))
		return res, val.value

	#------------------------------------------------------------
	LibLoader.lib.FliCblueSfnc_setExposureTime_V2.argtypes = [ctypes.c_void_p, ctypes.c_double]
	LibLoader.lib.FliCblueSfnc_setExposureTime_V2.restype = ctypes.c_bool
	def SetExposureTime(self, context, val):
		return LibLoader.lib.FliCblueSfnc_setExposureTime_V2(context, val)

	#------------------------------------------------------------
	LibLoader.lib.FliCblueSfnc_getExposureTimeMin_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_double)]
	LibLoader.lib.FliCblueSfnc_getExposureTimeMin_V2.restype = ctypes.c_bool
	def GetExposureTimeMin(self, context):
		val = ctypes.c_double(0)
		res = LibLoader.lib.FliCblueSfnc_getExposureTimeMin_V2(context, ctypes.byref(val))
		return res, val.value

	#------------------------------------------------------------
	LibLoader.lib.FliCblueSfnc_getExposureTimeMax_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_double)]
	LibLoader.lib.FliCblueSfnc_getExposureTimeMax_V2.restype = ctypes.c_bool
	def GetExposureTimeMax(self, context):
		val = ctypes.c_double(0)
		res = LibLoader.lib.FliCblueSfnc_getExposureTimeMax_V2(context, ctypes.byref(val))
		return res, val.value

	#------------------------------------------------------------
	LibLoader.lib.FliCblueSfnc_getGain_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_double)]
	LibLoader.lib.FliCblueSfnc_getGain_V2.restype = ctypes.c_bool
	def GetGain(self, context):
		val = ctypes.c_double(0)
		res = LibLoader.lib.FliCblueSfnc_getGain_V2(context, ctypes.byref(val))
		return res, val.value

	#------------------------------------------------------------
	LibLoader.lib.FliCblueSfnc_setGain_V2.argtypes = [ctypes.c_void_p, ctypes.c_double]
	LibLoader.lib.FliCblueSfnc_setGain_V2.restype = ctypes.c_bool
	def SetGain(self, context, val):
		return LibLoader.lib.FliCblueSfnc_setGain_V2(context, val)

	#------------------------------------------------------------
	LibLoader.lib.FliCblueSfnc_getGainMin_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_double)]
	LibLoader.lib.FliCblueSfnc_getGainMin_V2.restype = ctypes.c_bool
	def GetGainMin(self, context):
		val = ctypes.c_double(0)
		res = LibLoader.lib.FliCblueSfnc_getGainMin_V2(context, ctypes.byref(val))
		return res, val.value

	#------------------------------------------------------------
	LibLoader.lib.FliCblueSfnc_getGainMax_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_double)]
	LibLoader.lib.FliCblueSfnc_getGainMax_V2.restype = ctypes.c_bool
	def GetGainMax(self, context):
		val = ctypes.c_double(0)
		res = LibLoader.lib.FliCblueSfnc_getGainMax_V2(context, ctypes.byref(val))
		return res, val.value

	#------------------------------------------------------------
	LibLoader.lib.FliCblueSfnc_getBlackLevel_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_double)]
	LibLoader.lib.FliCblueSfnc_getBlackLevel_V2.restype = ctypes.c_bool
	def GetBlackLevel(self, context):
		val = ctypes.c_double(0)
		res = LibLoader.lib.FliCblueSfnc_getBlackLevel_V2(context, ctypes.byref(val))
		return res, val.value

	#------------------------------------------------------------
	LibLoader.lib.FliCblueSfnc_setBlackLevel_V2.argtypes = [ctypes.c_void_p, ctypes.c_double]
	LibLoader.lib.FliCblueSfnc_setBlackLevel_V2.restype = ctypes.c_bool
	def SetBlackLevel(self, context, val):
		return LibLoader.lib.FliCblueSfnc_setBlackLevel_V2(context, val)

	#------------------------------------------------------------
	LibLoader.lib.FliCblueSfnc_getReverseX_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_bool)]
	LibLoader.lib.FliCblueSfnc_getReverseX_V2.restype = ctypes.c_bool
	def GetReverseX(self, context):
		val = ctypes.c_bool(0)
		res = LibLoader.lib.FliCblueSfnc_getReverseX_V2(context, ctypes.byref(val))
		return res, val.value

	#------------------------------------------------------------
	LibLoader.lib.FliCblueSfnc_setReverseX_V2.argtypes = [ctypes.c_void_p, ctypes.c_bool]
	LibLoader.lib.FliCblueSfnc_setReverseX_V2.restype = ctypes.c_bool
	def SetReverseX(self, context, val):
		return LibLoader.lib.FliCblueSfnc_setReverseX_V2(context, val)

	#------------------------------------------------------------
	LibLoader.lib.FliCblueSfnc_getReverseY_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_bool)]
	LibLoader.lib.FliCblueSfnc_getReverseY_V2.restype = ctypes.c_bool
	def GetReverseY(self, context):
		val = ctypes.c_bool(0)
		res = LibLoader.lib.FliCblueSfnc_getReverseY_V2(context, ctypes.byref(val))
		return res, val.value

	#------------------------------------------------------------
	LibLoader.lib.FliCblueSfnc_setReverseY_V2.argtypes = [ctypes.c_void_p, ctypes.c_bool]
	LibLoader.lib.FliCblueSfnc_setReverseY_V2.restype = ctypes.c_bool
	def SetReverseY(self, context, val):
		return LibLoader.lib.FliCblueSfnc_setReverseY_V2(context, val)

	#------------------------------------------------------------
	LibLoader.lib.FliCblueSfnc_executeDeviceReset_V2.restype = ctypes.c_bool
	def ExecuteDeviceReset(self, context):
		return LibLoader.lib.FliCblueSfnc_executeDeviceReset_V2(ctypes.c_void_p(context))

	#------------------------------------------------------------
	LibLoader.lib.FliCblueSfnc_executeAcquisitionStart_V2.restype = ctypes.c_bool
	def ExecuteAcquisitionStart(self, context):
		return LibLoader.lib.FliCblueSfnc_executeAcquisitionStart_V2(ctypes.c_void_p(context))

	#------------------------------------------------------------
	LibLoader.lib.FliCblueSfnc_executeAcquisitionStop_V2.restype = ctypes.c_bool
	def ExecuteAcquisitionStop(self, context):
		return LibLoader.lib.FliCblueSfnc_executeAcquisitionStop_V2(ctypes.c_void_p(context))

	#------------------------------------------------------------
	LibLoader.lib.FliCblueSfnc_executeAcquisitionAbort_V2.restype = ctypes.c_bool
	def ExecuteAcquisitionAbort(self, context):
		return LibLoader.lib.FliCblueSfnc_executeAcquisitionAbort_V2(ctypes.c_void_p(context))

	#------------------------------------------------------------
	LibLoader.lib.FliCblueSfnc_executeUserSetLoad_V2.restype = ctypes.c_bool
	def ExecuteUserSetLoad(self, context):
		return LibLoader.lib.FliCblueSfnc_executeUserSetLoad_V2(ctypes.c_void_p(context))

	#------------------------------------------------------------
	LibLoader.lib.FliCblueSfnc_executeUserSetSave_V2.restype = ctypes.c_bool
	def ExecuteUserSetSave(self, context):
		return LibLoader.lib.FliCblueSfnc_executeUserSetSave_V2(ctypes.c_void_p(context))

	#------------------------------------------------------------
	LibLoader.lib.FliCblueSfnc_executeCxpErrorCounterReset_V2.restype = ctypes.c_bool
	def ExecuteCxpErrorCounterReset(self, context):
		return LibLoader.lib.FliCblueSfnc_executeCxpErrorCounterReset_V2(ctypes.c_void_p(context))

