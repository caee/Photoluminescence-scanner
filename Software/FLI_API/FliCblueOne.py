import LibLoader
import ctypes
import numpy as np

bufferSize = ctypes.c_size_t(1000)
charBuffer = ctypes.create_string_buffer(bufferSize.value)

class FliCblueOne:
	#------------------------------------------------------------
	LibLoader.lib.FliCblueOne_getDeviceTemperatureSelector_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_int)]
	LibLoader.lib.FliCblueOne_getDeviceTemperatureSelector_V2.restype = ctypes.c_bool
	def GetDeviceTemperatureSelector(self, context):
		val = ctypes.c_int(0)
		res = LibLoader.lib.FliCblueOne_getDeviceTemperatureSelector_V2(context, ctypes.byref(val))
		return res, val.value

	#------------------------------------------------------------
	LibLoader.lib.FliCblueOne_setDeviceTemperatureSelector_V2.argtypes = [ctypes.c_void_p, ctypes.c_int]
	LibLoader.lib.FliCblueOne_setDeviceTemperatureSelector_V2.restype = ctypes.c_bool
	def SetDeviceTemperatureSelector(self, context, val):
		return LibLoader.lib.FliCblueOne_setDeviceTemperatureSelector_V2(context, val)

	#------------------------------------------------------------
	LibLoader.lib.FliCblueOne_getDeviceTecSelector_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_int)]
	LibLoader.lib.FliCblueOne_getDeviceTecSelector_V2.restype = ctypes.c_bool
	def GetDeviceTecSelector(self, context):
		val = ctypes.c_int(0)
		res = LibLoader.lib.FliCblueOne_getDeviceTecSelector_V2(context, ctypes.byref(val))
		return res, val.value

	#------------------------------------------------------------
	LibLoader.lib.FliCblueOne_setDeviceTecSelector_V2.argtypes = [ctypes.c_void_p, ctypes.c_int]
	LibLoader.lib.FliCblueOne_setDeviceTecSelector_V2.restype = ctypes.c_bool
	def SetDeviceTecSelector(self, context, val):
		return LibLoader.lib.FliCblueOne_setDeviceTecSelector_V2(context, val)

	#------------------------------------------------------------
	LibLoader.lib.FliCblueOne_getDeviceFanMode_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_int)]
	LibLoader.lib.FliCblueOne_getDeviceFanMode_V2.restype = ctypes.c_bool
	def GetDeviceFanMode(self, context):
		val = ctypes.c_int(0)
		res = LibLoader.lib.FliCblueOne_getDeviceFanMode_V2(context, ctypes.byref(val))
		return res, val.value

	#------------------------------------------------------------
	LibLoader.lib.FliCblueOne_setDeviceFanMode_V2.argtypes = [ctypes.c_void_p, ctypes.c_int]
	LibLoader.lib.FliCblueOne_setDeviceFanMode_V2.restype = ctypes.c_bool
	def SetDeviceFanMode(self, context, val):
		return LibLoader.lib.FliCblueOne_setDeviceFanMode_V2(context, val)

	#------------------------------------------------------------
	LibLoader.lib.FliCblueOne_getFirmwareUpdateStatus_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_int)]
	LibLoader.lib.FliCblueOne_getFirmwareUpdateStatus_V2.restype = ctypes.c_bool
	def GetFirmwareUpdateStatus(self, context):
		val = ctypes.c_int(0)
		res = LibLoader.lib.FliCblueOne_getFirmwareUpdateStatus_V2(context, ctypes.byref(val))
		return res, val.value

	#------------------------------------------------------------
	LibLoader.lib.FliCblueOne_getLogCollectStatus_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_int)]
	LibLoader.lib.FliCblueOne_getLogCollectStatus_V2.restype = ctypes.c_bool
	def GetLogCollectStatus(self, context):
		val = ctypes.c_int(0)
		res = LibLoader.lib.FliCblueOne_getLogCollectStatus_V2(context, ctypes.byref(val))
		return res, val.value

	#------------------------------------------------------------
	LibLoader.lib.FliCblueOne_getIPMode_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_int)]
	LibLoader.lib.FliCblueOne_getIPMode_V2.restype = ctypes.c_bool
	def GetIPMode(self, context):
		val = ctypes.c_int(0)
		res = LibLoader.lib.FliCblueOne_getIPMode_V2(context, ctypes.byref(val))
		return res, val.value

	#------------------------------------------------------------
	LibLoader.lib.FliCblueOne_setIPMode_V2.argtypes = [ctypes.c_void_p, ctypes.c_int]
	LibLoader.lib.FliCblueOne_setIPMode_V2.restype = ctypes.c_bool
	def SetIPMode(self, context, val):
		return LibLoader.lib.FliCblueOne_setIPMode_V2(context, val)

	#------------------------------------------------------------
	LibLoader.lib.FliCblueOne_getSparseSelector_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_int)]
	LibLoader.lib.FliCblueOne_getSparseSelector_V2.restype = ctypes.c_bool
	def GetSparseSelector(self, context):
		val = ctypes.c_int(0)
		res = LibLoader.lib.FliCblueOne_getSparseSelector_V2(context, ctypes.byref(val))
		return res, val.value

	#------------------------------------------------------------
	LibLoader.lib.FliCblueOne_setSparseSelector_V2.argtypes = [ctypes.c_void_p, ctypes.c_int]
	LibLoader.lib.FliCblueOne_setSparseSelector_V2.restype = ctypes.c_bool
	def SetSparseSelector(self, context, val):
		return LibLoader.lib.FliCblueOne_setSparseSelector_V2(context, val)

	#------------------------------------------------------------
	LibLoader.lib.FliCblueOne_getSparseMode_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_int)]
	LibLoader.lib.FliCblueOne_getSparseMode_V2.restype = ctypes.c_bool
	def GetSparseMode(self, context):
		val = ctypes.c_int(0)
		res = LibLoader.lib.FliCblueOne_getSparseMode_V2(context, ctypes.byref(val))
		return res, val.value

	#------------------------------------------------------------
	LibLoader.lib.FliCblueOne_setSparseMode_V2.argtypes = [ctypes.c_void_p, ctypes.c_int]
	LibLoader.lib.FliCblueOne_setSparseMode_V2.restype = ctypes.c_bool
	def SetSparseMode(self, context, val):
		return LibLoader.lib.FliCblueOne_setSparseMode_V2(context, val)

	#------------------------------------------------------------
	LibLoader.lib.FliCblueOne_getTestPatternGeneratorSelector_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_int)]
	LibLoader.lib.FliCblueOne_getTestPatternGeneratorSelector_V2.restype = ctypes.c_bool
	def GetTestPatternGeneratorSelector(self, context):
		val = ctypes.c_int(0)
		res = LibLoader.lib.FliCblueOne_getTestPatternGeneratorSelector_V2(context, ctypes.byref(val))
		return res, val.value

	#------------------------------------------------------------
	LibLoader.lib.FliCblueOne_setTestPatternGeneratorSelector_V2.argtypes = [ctypes.c_void_p, ctypes.c_int]
	LibLoader.lib.FliCblueOne_setTestPatternGeneratorSelector_V2.restype = ctypes.c_bool
	def SetTestPatternGeneratorSelector(self, context, val):
		return LibLoader.lib.FliCblueOne_setTestPatternGeneratorSelector_V2(context, val)

	#------------------------------------------------------------
	LibLoader.lib.FliCblueOne_getTestPattern_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_int)]
	LibLoader.lib.FliCblueOne_getTestPattern_V2.restype = ctypes.c_bool
	def GetTestPattern(self, context):
		val = ctypes.c_int(0)
		res = LibLoader.lib.FliCblueOne_getTestPattern_V2(context, ctypes.byref(val))
		return res, val.value

	#------------------------------------------------------------
	LibLoader.lib.FliCblueOne_setTestPattern_V2.argtypes = [ctypes.c_void_p, ctypes.c_int]
	LibLoader.lib.FliCblueOne_setTestPattern_V2.restype = ctypes.c_bool
	def SetTestPattern(self, context, val):
		return LibLoader.lib.FliCblueOne_setTestPattern_V2(context, val)

	#------------------------------------------------------------
	LibLoader.lib.FliCblueOne_getGlowReduction_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_int)]
	LibLoader.lib.FliCblueOne_getGlowReduction_V2.restype = ctypes.c_bool
	def GetGlowReduction(self, context):
		val = ctypes.c_int(0)
		res = LibLoader.lib.FliCblueOne_getGlowReduction_V2(context, ctypes.byref(val))
		return res, val.value

	#------------------------------------------------------------
	LibLoader.lib.FliCblueOne_setGlowReduction_V2.argtypes = [ctypes.c_void_p, ctypes.c_int]
	LibLoader.lib.FliCblueOne_setGlowReduction_V2.restype = ctypes.c_bool
	def SetGlowReduction(self, context, val):
		return LibLoader.lib.FliCblueOne_setGlowReduction_V2(context, val)

	#------------------------------------------------------------
	LibLoader.lib.FliCblueOne_getConversionEfficiency_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_int)]
	LibLoader.lib.FliCblueOne_getConversionEfficiency_V2.restype = ctypes.c_bool
	def GetConversionEfficiency(self, context):
		val = ctypes.c_int(0)
		res = LibLoader.lib.FliCblueOne_getConversionEfficiency_V2(context, ctypes.byref(val))
		return res, val.value

	#------------------------------------------------------------
	LibLoader.lib.FliCblueOne_setConversionEfficiency_V2.argtypes = [ctypes.c_void_p, ctypes.c_int]
	LibLoader.lib.FliCblueOne_setConversionEfficiency_V2.restype = ctypes.c_bool
	def SetConversionEfficiency(self, context, val):
		return LibLoader.lib.FliCblueOne_setConversionEfficiency_V2(context, val)

	#------------------------------------------------------------
	LibLoader.lib.FliCblueOne_getUserSetSelector_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_int)]
	LibLoader.lib.FliCblueOne_getUserSetSelector_V2.restype = ctypes.c_bool
	def GetUserSetSelector(self, context):
		val = ctypes.c_int(0)
		res = LibLoader.lib.FliCblueOne_getUserSetSelector_V2(context, ctypes.byref(val))
		return res, val.value

	#------------------------------------------------------------
	LibLoader.lib.FliCblueOne_setUserSetSelector_V2.argtypes = [ctypes.c_void_p, ctypes.c_int]
	LibLoader.lib.FliCblueOne_setUserSetSelector_V2.restype = ctypes.c_bool
	def SetUserSetSelector(self, context, val):
		return LibLoader.lib.FliCblueOne_setUserSetSelector_V2(context, val)

	#------------------------------------------------------------
	LibLoader.lib.FliCblueOne_getUserSetDefault_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_int)]
	LibLoader.lib.FliCblueOne_getUserSetDefault_V2.restype = ctypes.c_bool
	def GetUserSetDefault(self, context):
		val = ctypes.c_int(0)
		res = LibLoader.lib.FliCblueOne_getUserSetDefault_V2(context, ctypes.byref(val))
		return res, val.value

	#------------------------------------------------------------
	LibLoader.lib.FliCblueOne_setUserSetDefault_V2.argtypes = [ctypes.c_void_p, ctypes.c_int]
	LibLoader.lib.FliCblueOne_setUserSetDefault_V2.restype = ctypes.c_bool
	def SetUserSetDefault(self, context, val):
		return LibLoader.lib.FliCblueOne_setUserSetDefault_V2(context, val)

	#------------------------------------------------------------
	LibLoader.lib.FliCblueOne_getSparseWidth_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_int)]
	LibLoader.lib.FliCblueOne_getSparseWidth_V2.restype = ctypes.c_bool
	def GetSparseWidth(self, context):
		val = ctypes.c_int(0)
		res = LibLoader.lib.FliCblueOne_getSparseWidth_V2(context, ctypes.byref(val))
		return res, val.value

	#------------------------------------------------------------
	LibLoader.lib.FliCblueOne_setSparseWidth_V2.argtypes = [ctypes.c_void_p, ctypes.c_int]
	LibLoader.lib.FliCblueOne_setSparseWidth_V2.restype = ctypes.c_bool
	def SetSparseWidth(self, context, val):
		return LibLoader.lib.FliCblueOne_setSparseWidth_V2(context, val)

	#------------------------------------------------------------
	LibLoader.lib.FliCblueOne_getSparseHeight_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_int)]
	LibLoader.lib.FliCblueOne_getSparseHeight_V2.restype = ctypes.c_bool
	def GetSparseHeight(self, context):
		val = ctypes.c_int(0)
		res = LibLoader.lib.FliCblueOne_getSparseHeight_V2(context, ctypes.byref(val))
		return res, val.value

	#------------------------------------------------------------
	LibLoader.lib.FliCblueOne_setSparseHeight_V2.argtypes = [ctypes.c_void_p, ctypes.c_int]
	LibLoader.lib.FliCblueOne_setSparseHeight_V2.restype = ctypes.c_bool
	def SetSparseHeight(self, context, val):
		return LibLoader.lib.FliCblueOne_setSparseHeight_V2(context, val)

	#------------------------------------------------------------
	LibLoader.lib.FliCblueOne_getSparseOffsetX_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_int)]
	LibLoader.lib.FliCblueOne_getSparseOffsetX_V2.restype = ctypes.c_bool
	def GetSparseOffsetX(self, context):
		val = ctypes.c_int(0)
		res = LibLoader.lib.FliCblueOne_getSparseOffsetX_V2(context, ctypes.byref(val))
		return res, val.value

	#------------------------------------------------------------
	LibLoader.lib.FliCblueOne_setSparseOffsetX_V2.argtypes = [ctypes.c_void_p, ctypes.c_int]
	LibLoader.lib.FliCblueOne_setSparseOffsetX_V2.restype = ctypes.c_bool
	def SetSparseOffsetX(self, context, val):
		return LibLoader.lib.FliCblueOne_setSparseOffsetX_V2(context, val)

	#------------------------------------------------------------
	LibLoader.lib.FliCblueOne_getSparseOffsetY_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_int)]
	LibLoader.lib.FliCblueOne_getSparseOffsetY_V2.restype = ctypes.c_bool
	def GetSparseOffsetY(self, context):
		val = ctypes.c_int(0)
		res = LibLoader.lib.FliCblueOne_getSparseOffsetY_V2(context, ctypes.byref(val))
		return res, val.value

	#------------------------------------------------------------
	LibLoader.lib.FliCblueOne_setSparseOffsetY_V2.argtypes = [ctypes.c_void_p, ctypes.c_int]
	LibLoader.lib.FliCblueOne_setSparseOffsetY_V2.restype = ctypes.c_bool
	def SetSparseOffsetY(self, context, val):
		return LibLoader.lib.FliCblueOne_setSparseOffsetY_V2(context, val)

	#------------------------------------------------------------
	LibLoader.lib.FliCblueOne_getDeviceFanSpeed_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_int)]
	LibLoader.lib.FliCblueOne_getDeviceFanSpeed_V2.restype = ctypes.c_bool
	def GetDeviceFanSpeed(self, context):
		val = ctypes.c_int(0)
		res = LibLoader.lib.FliCblueOne_getDeviceFanSpeed_V2(context, ctypes.byref(val))
		return res, val.value

	#------------------------------------------------------------
	LibLoader.lib.FliCblueOne_setDeviceFanSpeed_V2.argtypes = [ctypes.c_void_p, ctypes.c_int]
	LibLoader.lib.FliCblueOne_setDeviceFanSpeed_V2.restype = ctypes.c_bool
	def SetDeviceFanSpeed(self, context, val):
		return LibLoader.lib.FliCblueOne_setDeviceFanSpeed_V2(context, val)

	#------------------------------------------------------------
	LibLoader.lib.FliCblueOne_getLogHistoryDepth_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_int)]
	LibLoader.lib.FliCblueOne_getLogHistoryDepth_V2.restype = ctypes.c_bool
	def GetLogHistoryDepth(self, context):
		val = ctypes.c_int(0)
		res = LibLoader.lib.FliCblueOne_getLogHistoryDepth_V2(context, ctypes.byref(val))
		return res, val.value

	#------------------------------------------------------------
	LibLoader.lib.FliCblueOne_setLogHistoryDepth_V2.argtypes = [ctypes.c_void_p, ctypes.c_int]
	LibLoader.lib.FliCblueOne_setLogHistoryDepth_V2.restype = ctypes.c_bool
	def SetLogHistoryDepth(self, context, val):
		return LibLoader.lib.FliCblueOne_setLogHistoryDepth_V2(context, val)

	#------------------------------------------------------------
	LibLoader.lib.FliCblueOne_getDeviceStatus_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_size_t]
	LibLoader.lib.FliCblueOne_getDeviceStatus_V2.restype = ctypes.c_bool
	def GetDeviceStatus(self, context):
		res = LibLoader.lib.FliCblueOne_getDeviceStatus_V2(context, charBuffer, bufferSize)
		return res, charBuffer.value.decode('utf-8', 'ignore')

	#------------------------------------------------------------
	LibLoader.lib.FliCblueOne_getDeviceStatusDetailed_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_size_t]
	LibLoader.lib.FliCblueOne_getDeviceStatusDetailed_V2.restype = ctypes.c_bool
	def GetDeviceStatusDetailed(self, context):
		res = LibLoader.lib.FliCblueOne_getDeviceStatusDetailed_V2(context, charBuffer, bufferSize)
		return res, charBuffer.value.decode('utf-8', 'ignore')

	#------------------------------------------------------------
	LibLoader.lib.FliCblueOne_getFirmwareUpdateUri_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_size_t]
	LibLoader.lib.FliCblueOne_getFirmwareUpdateUri_V2.restype = ctypes.c_bool
	def GetFirmwareUpdateUri(self, context):
		res = LibLoader.lib.FliCblueOne_getFirmwareUpdateUri_V2(context, charBuffer, bufferSize)
		return res, charBuffer.value.decode('utf-8', 'ignore')

	#------------------------------------------------------------
	LibLoader.lib.FliCblueOne_setFirmwareUpdateUri_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
	LibLoader.lib.FliCblueOne_setFirmwareUpdateUri_V2.restype = ctypes.c_bool
	def SetFirmwareUpdateUri(self, context, val):
		return LibLoader.lib.FliCblueOne_setFirmwareUpdateUri_V2(context, val.encode())

	#------------------------------------------------------------
	LibLoader.lib.FliCblueOne_getLogServeUri_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_size_t]
	LibLoader.lib.FliCblueOne_getLogServeUri_V2.restype = ctypes.c_bool
	def GetLogServeUri(self, context):
		res = LibLoader.lib.FliCblueOne_getLogServeUri_V2(context, charBuffer, bufferSize)
		return res, charBuffer.value.decode('utf-8', 'ignore')

	#------------------------------------------------------------
	LibLoader.lib.FliCblueOne_getCurrentIPAddress_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_size_t]
	LibLoader.lib.FliCblueOne_getCurrentIPAddress_V2.restype = ctypes.c_bool
	def GetCurrentIPAddress(self, context):
		res = LibLoader.lib.FliCblueOne_getCurrentIPAddress_V2(context, charBuffer, bufferSize)
		return res, charBuffer.value.decode('utf-8', 'ignore')

	#------------------------------------------------------------
	LibLoader.lib.FliCblueOne_getCurrentSubnetMask_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_size_t]
	LibLoader.lib.FliCblueOne_getCurrentSubnetMask_V2.restype = ctypes.c_bool
	def GetCurrentSubnetMask(self, context):
		res = LibLoader.lib.FliCblueOne_getCurrentSubnetMask_V2(context, charBuffer, bufferSize)
		return res, charBuffer.value.decode('utf-8', 'ignore')

	#------------------------------------------------------------
	LibLoader.lib.FliCblueOne_getStaticIPAddress_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_size_t]
	LibLoader.lib.FliCblueOne_getStaticIPAddress_V2.restype = ctypes.c_bool
	def GetStaticIPAddress(self, context):
		res = LibLoader.lib.FliCblueOne_getStaticIPAddress_V2(context, charBuffer, bufferSize)
		return res, charBuffer.value.decode('utf-8', 'ignore')

	#------------------------------------------------------------
	LibLoader.lib.FliCblueOne_setStaticIPAddress_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
	LibLoader.lib.FliCblueOne_setStaticIPAddress_V2.restype = ctypes.c_bool
	def SetStaticIPAddress(self, context, val):
		return LibLoader.lib.FliCblueOne_setStaticIPAddress_V2(context, val.encode())

	#------------------------------------------------------------
	LibLoader.lib.FliCblueOne_getStaticSubnetMask_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_size_t]
	LibLoader.lib.FliCblueOne_getStaticSubnetMask_V2.restype = ctypes.c_bool
	def GetStaticSubnetMask(self, context):
		res = LibLoader.lib.FliCblueOne_getStaticSubnetMask_V2(context, charBuffer, bufferSize)
		return res, charBuffer.value.decode('utf-8', 'ignore')

	#------------------------------------------------------------
	LibLoader.lib.FliCblueOne_setStaticSubnetMask_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
	LibLoader.lib.FliCblueOne_setStaticSubnetMask_V2.restype = ctypes.c_bool
	def SetStaticSubnetMask(self, context, val):
		return LibLoader.lib.FliCblueOne_setStaticSubnetMask_V2(context, val.encode())

	#------------------------------------------------------------
	LibLoader.lib.FliCblueOne_getStaticDefaultGateway_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_size_t]
	LibLoader.lib.FliCblueOne_getStaticDefaultGateway_V2.restype = ctypes.c_bool
	def GetStaticDefaultGateway(self, context):
		res = LibLoader.lib.FliCblueOne_getStaticDefaultGateway_V2(context, charBuffer, bufferSize)
		return res, charBuffer.value.decode('utf-8', 'ignore')

	#------------------------------------------------------------
	LibLoader.lib.FliCblueOne_setStaticDefaultGateway_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
	LibLoader.lib.FliCblueOne_setStaticDefaultGateway_V2.restype = ctypes.c_bool
	def SetStaticDefaultGateway(self, context, val):
		return LibLoader.lib.FliCblueOne_setStaticDefaultGateway_V2(context, val.encode())

	#------------------------------------------------------------
	LibLoader.lib.FliCblueOne_getStaticDomainNameServer_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_size_t]
	LibLoader.lib.FliCblueOne_getStaticDomainNameServer_V2.restype = ctypes.c_bool
	def GetStaticDomainNameServer(self, context):
		res = LibLoader.lib.FliCblueOne_getStaticDomainNameServer_V2(context, charBuffer, bufferSize)
		return res, charBuffer.value.decode('utf-8', 'ignore')

	#------------------------------------------------------------
	LibLoader.lib.FliCblueOne_setStaticDomainNameServer_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
	LibLoader.lib.FliCblueOne_setStaticDomainNameServer_V2.restype = ctypes.c_bool
	def SetStaticDomainNameServer(self, context, val):
		return LibLoader.lib.FliCblueOne_setStaticDomainNameServer_V2(context, val.encode())

	#------------------------------------------------------------
	LibLoader.lib.FliCblueOne_getStaticAlternateDomainNameServer_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_size_t]
	LibLoader.lib.FliCblueOne_getStaticAlternateDomainNameServer_V2.restype = ctypes.c_bool
	def GetStaticAlternateDomainNameServer(self, context):
		res = LibLoader.lib.FliCblueOne_getStaticAlternateDomainNameServer_V2(context, charBuffer, bufferSize)
		return res, charBuffer.value.decode('utf-8', 'ignore')

	#------------------------------------------------------------
	LibLoader.lib.FliCblueOne_setStaticAlternateDomainNameServer_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
	LibLoader.lib.FliCblueOne_setStaticAlternateDomainNameServer_V2.restype = ctypes.c_bool
	def SetStaticAlternateDomainNameServer(self, context, val):
		return LibLoader.lib.FliCblueOne_setStaticAlternateDomainNameServer_V2(context, val.encode())

	#------------------------------------------------------------
	LibLoader.lib.FliCblueOne_getDeviceTecVoltage_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_double)]
	LibLoader.lib.FliCblueOne_getDeviceTecVoltage_V2.restype = ctypes.c_bool
	def GetDeviceTecVoltage(self, context):
		val = ctypes.c_double(0)
		res = LibLoader.lib.FliCblueOne_getDeviceTecVoltage_V2(context, ctypes.byref(val))
		return res, val.value

	#------------------------------------------------------------
	LibLoader.lib.FliCblueOne_getDeviceTecCurrent_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_double)]
	LibLoader.lib.FliCblueOne_getDeviceTecCurrent_V2.restype = ctypes.c_bool
	def GetDeviceTecCurrent(self, context):
		val = ctypes.c_double(0)
		res = LibLoader.lib.FliCblueOne_getDeviceTecCurrent_V2(context, ctypes.byref(val))
		return res, val.value

	#------------------------------------------------------------
	LibLoader.lib.FliCblueOne_getDeviceTecPower_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_double)]
	LibLoader.lib.FliCblueOne_getDeviceTecPower_V2.restype = ctypes.c_bool
	def GetDeviceTecPower(self, context):
		val = ctypes.c_double(0)
		res = LibLoader.lib.FliCblueOne_getDeviceTecPower_V2(context, ctypes.byref(val))
		return res, val.value

	#------------------------------------------------------------
	LibLoader.lib.FliCblueOne_getDeviceCoolingSetpoint_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_double)]
	LibLoader.lib.FliCblueOne_getDeviceCoolingSetpoint_V2.restype = ctypes.c_bool
	def GetDeviceCoolingSetpoint(self, context):
		val = ctypes.c_double(0)
		res = LibLoader.lib.FliCblueOne_getDeviceCoolingSetpoint_V2(context, ctypes.byref(val))
		return res, val.value

	#------------------------------------------------------------
	LibLoader.lib.FliCblueOne_setDeviceCoolingSetpoint_V2.argtypes = [ctypes.c_void_p, ctypes.c_double]
	LibLoader.lib.FliCblueOne_setDeviceCoolingSetpoint_V2.restype = ctypes.c_bool
	def SetDeviceCoolingSetpoint(self, context, val):
		return LibLoader.lib.FliCblueOne_setDeviceCoolingSetpoint_V2(context, val)

	#------------------------------------------------------------
	LibLoader.lib.FliCblueOne_getAcquisitionFrameRateMinReg_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_double)]
	LibLoader.lib.FliCblueOne_getAcquisitionFrameRateMinReg_V2.restype = ctypes.c_bool
	def GetAcquisitionFrameRateMinReg(self, context):
		val = ctypes.c_double(0)
		res = LibLoader.lib.FliCblueOne_getAcquisitionFrameRateMinReg_V2(context, ctypes.byref(val))
		return res, val.value

	#------------------------------------------------------------
	LibLoader.lib.FliCblueOne_getAcquisitionFrameRateMaxReg_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_double)]
	LibLoader.lib.FliCblueOne_getAcquisitionFrameRateMaxReg_V2.restype = ctypes.c_bool
	def GetAcquisitionFrameRateMaxReg(self, context):
		val = ctypes.c_double(0)
		res = LibLoader.lib.FliCblueOne_getAcquisitionFrameRateMaxReg_V2(context, ctypes.byref(val))
		return res, val.value

	#------------------------------------------------------------
	LibLoader.lib.FliCblueOne_getExposureTimeMinReg_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_double)]
	LibLoader.lib.FliCblueOne_getExposureTimeMinReg_V2.restype = ctypes.c_bool
	def GetExposureTimeMinReg(self, context):
		val = ctypes.c_double(0)
		res = LibLoader.lib.FliCblueOne_getExposureTimeMinReg_V2(context, ctypes.byref(val))
		return res, val.value

	#------------------------------------------------------------
	LibLoader.lib.FliCblueOne_getExposureTimeMaxReg_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_double)]
	LibLoader.lib.FliCblueOne_getExposureTimeMaxReg_V2.restype = ctypes.c_bool
	def GetExposureTimeMaxReg(self, context):
		val = ctypes.c_double(0)
		res = LibLoader.lib.FliCblueOne_getExposureTimeMaxReg_V2(context, ctypes.byref(val))
		return res, val.value

	#------------------------------------------------------------
	LibLoader.lib.FliCblueOne_getDeviceCoolingEnable_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_bool)]
	LibLoader.lib.FliCblueOne_getDeviceCoolingEnable_V2.restype = ctypes.c_bool
	def GetDeviceCoolingEnable(self, context):
		val = ctypes.c_bool(0)
		res = LibLoader.lib.FliCblueOne_getDeviceCoolingEnable_V2(context, ctypes.byref(val))
		return res, val.value

	#------------------------------------------------------------
	LibLoader.lib.FliCblueOne_setDeviceCoolingEnable_V2.argtypes = [ctypes.c_void_p, ctypes.c_bool]
	LibLoader.lib.FliCblueOne_setDeviceCoolingEnable_V2.restype = ctypes.c_bool
	def SetDeviceCoolingEnable(self, context, val):
		return LibLoader.lib.FliCblueOne_setDeviceCoolingEnable_V2(context, val)

	#------------------------------------------------------------
	LibLoader.lib.FliCblueOne_getSparse_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_bool)]
	LibLoader.lib.FliCblueOne_getSparse_V2.restype = ctypes.c_bool
	def GetSparse(self, context):
		val = ctypes.c_bool(0)
		res = LibLoader.lib.FliCblueOne_getSparse_V2(context, ctypes.byref(val))
		return res, val.value

	#------------------------------------------------------------
	LibLoader.lib.FliCblueOne_setSparse_V2.argtypes = [ctypes.c_void_p, ctypes.c_bool]
	LibLoader.lib.FliCblueOne_setSparse_V2.restype = ctypes.c_bool
	def SetSparse(self, context, val):
		return LibLoader.lib.FliCblueOne_setSparse_V2(context, val)

	#------------------------------------------------------------
	LibLoader.lib.FliCblueOne_executeDeviceShutdown_V2.restype = ctypes.c_bool
	def ExecuteDeviceShutdown(self, context):
		return LibLoader.lib.FliCblueOne_executeDeviceShutdown_V2(ctypes.c_void_p(context))

	#------------------------------------------------------------
	LibLoader.lib.FliCblueOne_executeFirmwareUpdateExecute_V2.restype = ctypes.c_bool
	def ExecuteFirmwareUpdateExecute(self, context):
		return LibLoader.lib.FliCblueOne_executeFirmwareUpdateExecute_V2(ctypes.c_void_p(context))

	#------------------------------------------------------------
	LibLoader.lib.FliCblueOne_executeFirmwareUpdateAbort_V2.restype = ctypes.c_bool
	def ExecuteFirmwareUpdateAbort(self, context):
		return LibLoader.lib.FliCblueOne_executeFirmwareUpdateAbort_V2(ctypes.c_void_p(context))

	#------------------------------------------------------------
	LibLoader.lib.FliCblueOne_executeFirmwareUpdateStatusRefresh_V2.restype = ctypes.c_bool
	def ExecuteFirmwareUpdateStatusRefresh(self, context):
		return LibLoader.lib.FliCblueOne_executeFirmwareUpdateStatusRefresh_V2(ctypes.c_void_p(context))

	#------------------------------------------------------------
	LibLoader.lib.FliCblueOne_executeLogCollect_V2.restype = ctypes.c_bool
	def ExecuteLogCollect(self, context):
		return LibLoader.lib.FliCblueOne_executeLogCollect_V2(ctypes.c_void_p(context))

	#------------------------------------------------------------
	LibLoader.lib.FliCblueOne_executeLogCollectAbort_V2.restype = ctypes.c_bool
	def ExecuteLogCollectAbort(self, context):
		return LibLoader.lib.FliCblueOne_executeLogCollectAbort_V2(ctypes.c_void_p(context))

	#------------------------------------------------------------
	LibLoader.lib.FliCblueOne_executeLogCollectStatusRefresh_V2.restype = ctypes.c_bool
	def ExecuteLogCollectStatusRefresh(self, context):
		return LibLoader.lib.FliCblueOne_executeLogCollectStatusRefresh_V2(ctypes.c_void_p(context))

	#------------------------------------------------------------
	LibLoader.lib.FliCblueOne_executeLogServe_V2.restype = ctypes.c_bool
	def ExecuteLogServe(self, context):
		return LibLoader.lib.FliCblueOne_executeLogServe_V2(ctypes.c_void_p(context))

	#------------------------------------------------------------
	LibLoader.lib.FliCblueOne_executeLogServeAbort_V2.restype = ctypes.c_bool
	def ExecuteLogServeAbort(self, context):
		return LibLoader.lib.FliCblueOne_executeLogServeAbort_V2(ctypes.c_void_p(context))

	#------------------------------------------------------------
	LibLoader.lib.FliCblueOne_executeIPReconfigure_V2.restype = ctypes.c_bool
	def ExecuteIPReconfigure(self, context):
		return LibLoader.lib.FliCblueOne_executeIPReconfigure_V2(ctypes.c_void_p(context))

