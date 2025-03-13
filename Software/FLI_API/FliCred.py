import LibLoader
import ctypes
import numpy as np

bufferSize = ctypes.c_size_t(1000)
charBuffer = ctypes.create_string_buffer(bufferSize.value)

class FliCred:
	#------------------------------------------------------------
	LibLoader.lib.FliCred_getAduOffset_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_int)]
	LibLoader.lib.FliCred_getAduOffset_V2.restype = ctypes.c_bool
	def GetAduOffset(self, context):
		aduOffset = ctypes.c_int(0)
		res = LibLoader.lib.FliCred_getAduOffset_V2(context, ctypes.byref(aduOffset))
		return res, aduOffset.value

	#------------------------------------------------------------
	LibLoader.lib.FliCred_getBiasState_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_bool)]
	LibLoader.lib.FliCred_getBiasState_V2.restype = ctypes.c_bool
	def GetBiasState(self, context):
		enabled = ctypes.c_bool(0)
		res = LibLoader.lib.FliCred_getBiasState_V2(context, ctypes.byref(enabled))
		return res, enabled.value

	#------------------------------------------------------------
	LibLoader.lib.FliCred_getFlatState_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_bool)]
	LibLoader.lib.FliCred_getFlatState_V2.restype = ctypes.c_bool
	def GetFlatState(self, context):
		enabled = ctypes.c_bool(0)
		res = LibLoader.lib.FliCred_getFlatState_V2(context, ctypes.byref(enabled))
		return res, enabled.value

	#------------------------------------------------------------
	LibLoader.lib.FliCred_getEventsState_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_bool)]
	LibLoader.lib.FliCred_getEventsState_V2.restype = ctypes.c_bool
	def GetEventsState(self, context):
		enabled = ctypes.c_bool(0)
		res = LibLoader.lib.FliCred_getEventsState_V2(context, ctypes.byref(enabled))
		return res, enabled.value

	#------------------------------------------------------------
	LibLoader.lib.FliCred_getCameraType_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_size_t]
	LibLoader.lib.FliCred_getCameraType_V2.restype = ctypes.c_bool
	def GetCameraType(self, context):
		res = LibLoader.lib.FliCred_getCameraType_V2(context, charBuffer, bufferSize)
		return res, charBuffer.value.decode('utf-8', 'ignore')

	#------------------------------------------------------------
	LibLoader.lib.FliCred_getHwuid_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_size_t]
	LibLoader.lib.FliCred_getHwuid_V2.restype = ctypes.c_bool
	def GetHwuid(self, context):
		res = LibLoader.lib.FliCred_getHwuid_V2(context, charBuffer, bufferSize)
		return res, charBuffer.value.decode('utf-8', 'ignore')

	#------------------------------------------------------------
	LibLoader.lib.FliCred_getImageTagsState_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_bool)]
	LibLoader.lib.FliCred_getImageTagsState_V2.restype = ctypes.c_bool
	def GetImageTagsState(self, context):
		enabled = ctypes.c_bool(0)
		res = LibLoader.lib.FliCred_getImageTagsState_V2(context, ctypes.byref(enabled))
		return res, enabled.value

	#------------------------------------------------------------
	LibLoader.lib.FliCred_getLedState_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_bool)]
	LibLoader.lib.FliCred_getLedState_V2.restype = ctypes.c_bool
	def GetLedState(self, context):
		enabled = ctypes.c_bool(0)
		res = LibLoader.lib.FliCred_getLedState_V2(context, ctypes.byref(enabled))
		return res, enabled.value

	#------------------------------------------------------------
	LibLoader.lib.FliCred_getSshPassword_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_size_t]
	LibLoader.lib.FliCred_getSshPassword_V2.restype = ctypes.c_bool
	def GetSshPassword(self, context):
		res = LibLoader.lib.FliCred_getSshPassword_V2(context, charBuffer, bufferSize)
		return res, charBuffer.value.decode('utf-8', 'ignore')

	#------------------------------------------------------------
	LibLoader.lib.FliCred_getExtSynchroState_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_bool)]
	LibLoader.lib.FliCred_getExtSynchroState_V2.restype = ctypes.c_bool
	def GetExtSynchroState(self, context):
		enabled = ctypes.c_bool(0)
		res = LibLoader.lib.FliCred_getExtSynchroState_V2(context, ctypes.byref(enabled))
		return res, enabled.value

	#------------------------------------------------------------
	LibLoader.lib.FliCred_getIpConfig_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_size_t, ctypes.c_char_p, ctypes.c_size_t, ctypes.c_char_p, ctypes.c_size_t, ctypes.POINTER(ctypes.c_bool)]
	LibLoader.lib.FliCred_getIpConfig_V2.restype = ctypes.c_bool
	def GetIpConfig(self, context):
		established = ctypes.c_bool(0)
		res = LibLoader.lib.FliCred_getIpConfig_V2(context, charBuffer, bufferSize, charBuffer, bufferSize, charBuffer, bufferSize, ctypes.byref(established))
		return res, charBuffer.value.decode('utf-8', 'ignore'), charBuffer.value.decode('utf-8', 'ignore'), charBuffer.value.decode('utf-8', 'ignore'), established.value

	#------------------------------------------------------------
	LibLoader.lib.FliCred_getStatusDetailed_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_size_t, ctypes.c_char_p, ctypes.c_size_t]
	LibLoader.lib.FliCred_getStatusDetailed_V2.restype = ctypes.c_bool
	def GetStatusDetailed(self, context):
		res = LibLoader.lib.FliCred_getStatusDetailed_V2(context, charBuffer, bufferSize, charBuffer, bufferSize)
		return res, charBuffer.value.decode('utf-8', 'ignore'), charBuffer.value.decode('utf-8', 'ignore')

	#------------------------------------------------------------
	LibLoader.lib.FliCred_getStatus_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_size_t]
	LibLoader.lib.FliCred_getStatus_V2.restype = ctypes.c_bool
	def GetStatus(self, context):
		res = LibLoader.lib.FliCred_getStatus_V2(context, charBuffer, bufferSize)
		return res, charBuffer.value.decode('utf-8', 'ignore')

	#------------------------------------------------------------
	LibLoader.lib.FliCred_getVersions_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_size_t, ctypes.c_char_p, ctypes.c_size_t, ctypes.c_char_p, ctypes.c_size_t]
	LibLoader.lib.FliCred_getVersions_V2.restype = ctypes.c_bool
	def GetVersions(self, context):
		res = LibLoader.lib.FliCred_getVersions_V2(context, charBuffer, bufferSize, charBuffer, bufferSize, charBuffer, bufferSize)
		return res, charBuffer.value.decode('utf-8', 'ignore'), charBuffer.value.decode('utf-8', 'ignore'), charBuffer.value.decode('utf-8', 'ignore')

	#------------------------------------------------------------
	LibLoader.lib.FliCred_getVersionFirmware_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_size_t]
	LibLoader.lib.FliCred_getVersionFirmware_V2.restype = ctypes.c_bool
	def GetVersionFirmware(self, context):
		res = LibLoader.lib.FliCred_getVersionFirmware_V2(context, charBuffer, bufferSize)
		return res, charBuffer.value.decode('utf-8', 'ignore')

	#------------------------------------------------------------
	LibLoader.lib.FliCred_getVersionFirmwareBuild_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_size_t]
	LibLoader.lib.FliCred_getVersionFirmwareBuild_V2.restype = ctypes.c_bool
	def GetVersionFirmwareBuild(self, context):
		res = LibLoader.lib.FliCred_getVersionFirmwareBuild_V2(context, charBuffer, bufferSize)
		return res, charBuffer.value.decode('utf-8', 'ignore')

	#------------------------------------------------------------
	LibLoader.lib.FliCred_getVersionFirmwareDetailed_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_size_t]
	LibLoader.lib.FliCred_getVersionFirmwareDetailed_V2.restype = ctypes.c_bool
	def GetVersionFirmwareDetailed(self, context):
		res = LibLoader.lib.FliCred_getVersionFirmwareDetailed_V2(context, charBuffer, bufferSize)
		return res, charBuffer.value.decode('utf-8', 'ignore')

	#------------------------------------------------------------
	LibLoader.lib.FliCred_getVersionFpga_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_size_t]
	LibLoader.lib.FliCred_getVersionFpga_V2.restype = ctypes.c_bool
	def GetVersionFpga(self, context):
		res = LibLoader.lib.FliCred_getVersionFpga_V2(context, charBuffer, bufferSize)
		return res, charBuffer.value.decode('utf-8', 'ignore')

	#------------------------------------------------------------
	LibLoader.lib.FliCred_getVersionHardware_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_size_t]
	LibLoader.lib.FliCred_getVersionHardware_V2.restype = ctypes.c_bool
	def GetVersionHardware(self, context):
		res = LibLoader.lib.FliCred_getVersionHardware_V2(context, charBuffer, bufferSize)
		return res, charBuffer.value.decode('utf-8', 'ignore')

	#------------------------------------------------------------
	LibLoader.lib.FliCred_enableExtSynchro_V2.argtypes = [ctypes.c_void_p, ctypes.c_bool]
	LibLoader.lib.FliCred_enableExtSynchro_V2.restype = ctypes.c_bool
	def EnableExtSynchro(self, context, enable):
		res = LibLoader.lib.FliCred_enableExtSynchro_V2(context, enable)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCred_enableImageTags_V2.argtypes = [ctypes.c_void_p, ctypes.c_bool]
	LibLoader.lib.FliCred_enableImageTags_V2.restype = ctypes.c_bool
	def EnableImageTags(self, context, enable):
		res = LibLoader.lib.FliCred_enableImageTags_V2(context, enable)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCred_enableEvents_V2.argtypes = [ctypes.c_void_p, ctypes.c_bool]
	LibLoader.lib.FliCred_enableEvents_V2.restype = ctypes.c_bool
	def EnableEvents(self, context, enable):
		res = LibLoader.lib.FliCred_enableEvents_V2(context, enable)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCred_enableLed_V2.argtypes = [ctypes.c_void_p, ctypes.c_bool]
	LibLoader.lib.FliCred_enableLed_V2.restype = ctypes.c_bool
	def EnableLed(self, context, enable):
		res = LibLoader.lib.FliCred_enableLed_V2(context, enable)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCred_enableTelnet_V2.argtypes = [ctypes.c_void_p, ctypes.c_bool]
	LibLoader.lib.FliCred_enableTelnet_V2.restype = ctypes.c_bool
	def EnableTelnet(self, context, enable):
		res = LibLoader.lib.FliCred_enableTelnet_V2(context, enable)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCred_setIpAddress_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
	LibLoader.lib.FliCred_setIpAddress_V2.restype = ctypes.c_bool
	def SetIpAddress(self, context, ip):
		res = LibLoader.lib.FliCred_setIpAddress_V2(context, ip.encode())
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCred_setIpAlternateDns_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
	LibLoader.lib.FliCred_setIpAlternateDns_V2.restype = ctypes.c_bool
	def SetIpAlternateDns(self, context, dns):
		res = LibLoader.lib.FliCred_setIpAlternateDns_V2(context, dns.encode())
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCred_setIpDns_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
	LibLoader.lib.FliCred_setIpDns_V2.restype = ctypes.c_bool
	def SetIpDns(self, context, dns):
		res = LibLoader.lib.FliCred_setIpDns_V2(context, dns.encode())
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCred_setIpGateway_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
	LibLoader.lib.FliCred_setIpGateway_V2.restype = ctypes.c_bool
	def SetIpGateway(self, context, gateway):
		res = LibLoader.lib.FliCred_setIpGateway_V2(context, gateway.encode())
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCred_setIpAutomatic_V2.argtypes = [ctypes.c_void_p]
	LibLoader.lib.FliCred_setIpAutomatic_V2.restype = ctypes.c_bool
	def SetIpAutomatic(self, context):
		res = LibLoader.lib.FliCred_setIpAutomatic_V2(context)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCred_setIpManual_V2.argtypes = [ctypes.c_void_p]
	LibLoader.lib.FliCred_setIpManual_V2.restype = ctypes.c_bool
	def SetIpManual(self, context):
		res = LibLoader.lib.FliCred_setIpManual_V2(context)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCred_setIpRefresh_V2.argtypes = [ctypes.c_void_p]
	LibLoader.lib.FliCred_setIpRefresh_V2.restype = ctypes.c_bool
	def SetIpRefresh(self, context):
		res = LibLoader.lib.FliCred_setIpRefresh_V2(context)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCred_setIpNetmask_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
	LibLoader.lib.FliCred_setIpNetmask_V2.restype = ctypes.c_bool
	def SetIpNetmask(self, context, netmask):
		res = LibLoader.lib.FliCred_setIpNetmask_V2(context, netmask.encode())
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCred_setPassword_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
	LibLoader.lib.FliCred_setPassword_V2.restype = ctypes.c_bool
	def SetPassword(self, context, password):
		res = LibLoader.lib.FliCred_setPassword_V2(context, password.encode())
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCred_setAduOffset_V2.argtypes = [ctypes.c_void_p, ctypes.c_int]
	LibLoader.lib.FliCred_setAduOffset_V2.restype = ctypes.c_bool
	def SetAduOffset(self, context, aduOffset):
		res = LibLoader.lib.FliCred_setAduOffset_V2(context, aduOffset)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCred_saveCameraSettings_V2.argtypes = [ctypes.c_void_p]
	LibLoader.lib.FliCred_saveCameraSettings_V2.restype = ctypes.c_bool
	def SaveCameraSettings(self, context):
		res = LibLoader.lib.FliCred_saveCameraSettings_V2(context)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCred_continueStarting_V2.argtypes = [ctypes.c_void_p]
	LibLoader.lib.FliCred_continueStarting_V2.restype = ctypes.c_bool
	def ContinueStarting(self, context):
		res = LibLoader.lib.FliCred_continueStarting_V2(context)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCred_getLogs_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_size_t]
	LibLoader.lib.FliCred_getLogs_V2.restype = ctypes.c_bool
	def GetLogs(self, context):
		res = LibLoader.lib.FliCred_getLogs_V2(context, charBuffer, bufferSize)
		return res, charBuffer.value.decode('utf-8', 'ignore')

	#------------------------------------------------------------
	LibLoader.lib.FliCred_shutDown_V2.argtypes = [ctypes.c_void_p]
	LibLoader.lib.FliCred_shutDown_V2.restype = ctypes.c_bool
	def ShutDown(self, context):
		res = LibLoader.lib.FliCred_shutDown_V2(context)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCred_getLogsFrom_V2.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_char_p, ctypes.c_size_t]
	LibLoader.lib.FliCred_getLogsFrom_V2.restype = ctypes.c_bool
	def GetLogsFrom(self, context, nbDays):
		res = LibLoader.lib.FliCred_getLogsFrom_V2(context, nbDays, charBuffer, bufferSize)
		return res, charBuffer.value.decode('utf-8', 'ignore')

	#------------------------------------------------------------
	LibLoader.lib.FliCred_buildFlat_V2.argtypes = [ctypes.c_void_p]
	LibLoader.lib.FliCred_buildFlat_V2.restype = ctypes.c_bool
	def BuildFlat(self, context):
		res = LibLoader.lib.FliCred_buildFlat_V2(context)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCred_buildBias_V2.argtypes = [ctypes.c_void_p]
	LibLoader.lib.FliCred_buildBias_V2.restype = ctypes.c_bool
	def BuildBias(self, context):
		res = LibLoader.lib.FliCred_buildBias_V2(context)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCred_restoreFactory_V2.argtypes = [ctypes.c_void_p]
	LibLoader.lib.FliCred_restoreFactory_V2.restype = ctypes.c_bool
	def RestoreFactory(self, context):
		res = LibLoader.lib.FliCred_restoreFactory_V2(context)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCred_upgradeFirmware_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
	LibLoader.lib.FliCred_upgradeFirmware_V2.restype = ctypes.c_bool
	def UpgradeFirmware(self, context, url):
		res = LibLoader.lib.FliCred_upgradeFirmware_V2(context, url.encode())
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCred_sendBiasFromUrl_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
	LibLoader.lib.FliCred_sendBiasFromUrl_V2.restype = ctypes.c_bool
	def SendBiasFromUrl(self, context, url):
		res = LibLoader.lib.FliCred_sendBiasFromUrl_V2(context, url.encode())
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCred_sendFlatFromUrl_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
	LibLoader.lib.FliCred_sendFlatFromUrl_V2.restype = ctypes.c_bool
	def SendFlatFromUrl(self, context, url):
		res = LibLoader.lib.FliCred_sendFlatFromUrl_V2(context, url.encode())
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCred_sendBiasFile_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
	LibLoader.lib.FliCred_sendBiasFile_V2.restype = ctypes.c_bool
	def SendBiasFile(self, context, filePath):
		res = LibLoader.lib.FliCred_sendBiasFile_V2(context, filePath.encode())
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCred_sendFlatFile_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
	LibLoader.lib.FliCred_sendFlatFile_V2.restype = ctypes.c_bool
	def SendFlatFile(self, context, filePath):
		res = LibLoader.lib.FliCred_sendFlatFile_V2(context, filePath.encode())
		return res

