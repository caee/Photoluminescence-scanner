import LibLoader
import ctypes
import numpy as np

bufferSize = ctypes.c_size_t(1000)
charBuffer = ctypes.create_string_buffer(bufferSize.value)

class CredTwoLite_CoolingMode:
    Manual = 0
    Automatic = 1
    Custom_steps = 2

class FliCredTwoLite:
	#------------------------------------------------------------
	LibLoader.lib.FliCredTwoLite_getAllTemp_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double)]
	LibLoader.lib.FliCredTwoLite_getAllTemp_V2.restype = ctypes.c_bool
	def GetAllTemp(self, context):
		cpu = ctypes.c_double(0)
		backend = ctypes.c_double(0)
		interfaceTemp = ctypes.c_double(0)
		ambiant = ctypes.c_double(0)
		sensor = ctypes.c_double(0)
		res = LibLoader.lib.FliCredTwoLite_getAllTemp_V2(context, ctypes.byref(cpu), ctypes.byref(backend), ctypes.byref(interfaceTemp), ctypes.byref(ambiant), ctypes.byref(sensor))
		return res, cpu.value, backend.value, interfaceTemp.value, ambiant.value, sensor.value

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwoLite_getTint_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_double)]
	LibLoader.lib.FliCredTwoLite_getTint_V2.restype = ctypes.c_bool
	def GetTint(self, context):
		tint = ctypes.c_double(0)
		res = LibLoader.lib.FliCredTwoLite_getTint_V2(context, ctypes.byref(tint))
		return res, tint.value

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwoLite_getTintMax_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_double)]
	LibLoader.lib.FliCredTwoLite_getTintMax_V2.restype = ctypes.c_bool
	def GetTintMax(self, context):
		tintMax = ctypes.c_double(0)
		res = LibLoader.lib.FliCredTwoLite_getTintMax_V2(context, ctypes.byref(tintMax))
		return res, tintMax.value

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwoLite_getAntiBloomingState_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_bool)]
	LibLoader.lib.FliCredTwoLite_getAntiBloomingState_V2.restype = ctypes.c_bool
	def GetAntiBloomingState(self, context):
		enabled = ctypes.c_bool(0)
		res = LibLoader.lib.FliCredTwoLite_getAntiBloomingState_V2(context, ctypes.byref(enabled))
		return res, enabled.value

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwoLite_getBadPixelState_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_bool)]
	LibLoader.lib.FliCredTwoLite_getBadPixelState_V2.restype = ctypes.c_bool
	def GetBadPixelState(self, context):
		enabled = ctypes.c_bool(0)
		res = LibLoader.lib.FliCredTwoLite_getBadPixelState_V2(context, ctypes.byref(enabled))
		return res, enabled.value

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwoLite_getTempAmbiant_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_double)]
	LibLoader.lib.FliCredTwoLite_getTempAmbiant_V2.restype = ctypes.c_bool
	def GetTempAmbiant(self, context):
		temp = ctypes.c_double(0)
		res = LibLoader.lib.FliCredTwoLite_getTempAmbiant_V2(context, ctypes.byref(temp))
		return res, temp.value

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwoLite_getTempBackEnd_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_double)]
	LibLoader.lib.FliCredTwoLite_getTempBackEnd_V2.restype = ctypes.c_bool
	def GetTempBackEnd(self, context):
		temp = ctypes.c_double(0)
		res = LibLoader.lib.FliCredTwoLite_getTempBackEnd_V2(context, ctypes.byref(temp))
		return res, temp.value

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwoLite_getTempCpu_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_double)]
	LibLoader.lib.FliCredTwoLite_getTempCpu_V2.restype = ctypes.c_bool
	def GetTempCpu(self, context):
		temp = ctypes.c_double(0)
		res = LibLoader.lib.FliCredTwoLite_getTempCpu_V2(context, ctypes.byref(temp))
		return res, temp.value

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwoLite_getTempInterface_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_double)]
	LibLoader.lib.FliCredTwoLite_getTempInterface_V2.restype = ctypes.c_bool
	def GetTempInterface(self, context):
		temp = ctypes.c_double(0)
		res = LibLoader.lib.FliCredTwoLite_getTempInterface_V2(context, ctypes.byref(temp))
		return res, temp.value

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwoLite_getTempSnake_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_double)]
	LibLoader.lib.FliCredTwoLite_getTempSnake_V2.restype = ctypes.c_bool
	def GetTempSnake(self, context):
		temp = ctypes.c_double(0)
		res = LibLoader.lib.FliCredTwoLite_getTempSnake_V2(context, ctypes.byref(temp))
		return res, temp.value

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwoLite_getTintRange_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double)]
	LibLoader.lib.FliCredTwoLite_getTintRange_V2.restype = ctypes.c_bool
	def GetTintRange(self, context):
		tintMin = ctypes.c_double(0)
		tintMax = ctypes.c_double(0)
		res = LibLoader.lib.FliCredTwoLite_getTintRange_V2(context, ctypes.byref(tintMin), ctypes.byref(tintMax))
		return res, tintMin.value, tintMax.value

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwoLite_getAdaptBiasState_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_bool)]
	LibLoader.lib.FliCredTwoLite_getAdaptBiasState_V2.restype = ctypes.c_bool
	def GetAdaptBiasState(self, context):
		enabled = ctypes.c_bool(0)
		res = LibLoader.lib.FliCredTwoLite_getAdaptBiasState_V2(context, ctypes.byref(enabled))
		return res, enabled.value

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwoLite_getAgcState_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_bool)]
	LibLoader.lib.FliCredTwoLite_getAgcState_V2.restype = ctypes.c_bool
	def GetAgcState(self, context):
		enabled = ctypes.c_bool(0)
		res = LibLoader.lib.FliCredTwoLite_getAgcState_V2(context, ctypes.byref(enabled))
		return res, enabled.value

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwoLite_getAgcPriority_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_size_t]
	LibLoader.lib.FliCredTwoLite_getAgcPriority_V2.restype = ctypes.c_bool
	def GetAgcPriority(self, context):
		res = LibLoader.lib.FliCredTwoLite_getAgcPriority_V2(context, charBuffer, bufferSize)
		return res, charBuffer.value.decode('utf-8', 'ignore')

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwoLite_getAgcRoi_V2.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int]
	LibLoader.lib.FliCredTwoLite_getAgcRoi_V2.restype = ctypes.c_bool
	def GetAgcRoi(self, context, col1, row1, col2, row2):
		res = LibLoader.lib.FliCredTwoLite_getAgcRoi_V2(context, col1, row1, col2, row2)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwoLite_getDarkOptimLevel_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_int)]
	LibLoader.lib.FliCredTwoLite_getDarkOptimLevel_V2.restype = ctypes.c_bool
	def GetDarkOptimLevel(self, context):
		level = ctypes.c_int(0)
		res = LibLoader.lib.FliCredTwoLite_getDarkOptimLevel_V2(context, ctypes.byref(level))
		return res, level.value

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwoLite_getExtSynchroExposure_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_size_t]
	LibLoader.lib.FliCredTwoLite_getExtSynchroExposure_V2.restype = ctypes.c_bool
	def GetExtSynchroExposure(self, context):
		res = LibLoader.lib.FliCredTwoLite_getExtSynchroExposure_V2(context, charBuffer, bufferSize)
		return res, charBuffer.value.decode('utf-8', 'ignore')

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwoLite_getExtSynchroPolarity_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_size_t]
	LibLoader.lib.FliCredTwoLite_getExtSynchroPolarity_V2.restype = ctypes.c_bool
	def GetExtSynchroPolarity(self, context):
		res = LibLoader.lib.FliCredTwoLite_getExtSynchroPolarity_V2(context, charBuffer, bufferSize)
		return res, charBuffer.value.decode('utf-8', 'ignore')

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwoLite_getHdrState_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_bool)]
	LibLoader.lib.FliCredTwoLite_getHdrState_V2.restype = ctypes.c_bool
	def GetHdrState(self, context):
		enabled = ctypes.c_bool(0)
		res = LibLoader.lib.FliCredTwoLite_getHdrState_V2(context, ctypes.byref(enabled))
		return res, enabled.value

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwoLite_getHdrCalibrationMode_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_size_t]
	LibLoader.lib.FliCredTwoLite_getHdrCalibrationMode_V2.restype = ctypes.c_bool
	def GetHdrCalibrationMode(self, context):
		res = LibLoader.lib.FliCredTwoLite_getHdrCalibrationMode_V2(context, charBuffer, bufferSize)
		return res, charBuffer.value.decode('utf-8', 'ignore')

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwoLite_getHdrExtendedState_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_bool)]
	LibLoader.lib.FliCredTwoLite_getHdrExtendedState_V2.restype = ctypes.c_bool
	def GetHdrExtendedState(self, context):
		enabled = ctypes.c_bool(0)
		res = LibLoader.lib.FliCredTwoLite_getHdrExtendedState_V2(context, ctypes.byref(enabled))
		return res, enabled.value

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwoLite_getLicenses_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_size_t]
	LibLoader.lib.FliCredTwoLite_getLicenses_V2.restype = ctypes.c_bool
	def GetLicenses(self, context):
		res = LibLoader.lib.FliCredTwoLite_getLicenses_V2(context, charBuffer, bufferSize)
		return res, charBuffer.value.decode('utf-8', 'ignore')

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwoLite_getMaxFpsUsb_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_double)]
	LibLoader.lib.FliCredTwoLite_getMaxFpsUsb_V2.restype = ctypes.c_bool
	def GetMaxFpsUsb(self, context):
		maxFpsUsb = ctypes.c_double(0)
		res = LibLoader.lib.FliCredTwoLite_getMaxFpsUsb_V2(context, ctypes.byref(maxFpsUsb))
		return res, maxFpsUsb.value

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwoLite_getMaxSyncDelay_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_double)]
	LibLoader.lib.FliCredTwoLite_getMaxSyncDelay_V2.restype = ctypes.c_bool
	def GetMaxSyncDelay(self, context):
		maxSyncDelay = ctypes.c_double(0)
		res = LibLoader.lib.FliCredTwoLite_getMaxSyncDelay_V2(context, ctypes.byref(maxSyncDelay))
		return res, maxSyncDelay.value

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwoLite_getMinSyncDelay_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_double)]
	LibLoader.lib.FliCredTwoLite_getMinSyncDelay_V2.restype = ctypes.c_bool
	def GetMinSyncDelay(self, context):
		minSyncDelay = ctypes.c_double(0)
		res = LibLoader.lib.FliCredTwoLite_getMinSyncDelay_V2(context, ctypes.byref(minSyncDelay))
		return res, minSyncDelay.value

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwoLite_getMaxTintItr_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_double)]
	LibLoader.lib.FliCredTwoLite_getMaxTintItr_V2.restype = ctypes.c_bool
	def GetMaxTintItr(self, context):
		maxTintItr = ctypes.c_double(0)
		res = LibLoader.lib.FliCredTwoLite_getMaxTintItr_V2(context, ctypes.byref(maxTintItr))
		return res, maxTintItr.value

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwoLite_getMinFps_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_double)]
	LibLoader.lib.FliCredTwoLite_getMinFps_V2.restype = ctypes.c_bool
	def GetMinFps(self, context):
		minFps = ctypes.c_double(0)
		res = LibLoader.lib.FliCredTwoLite_getMinFps_V2(context, ctypes.byref(minFps))
		return res, minFps.value

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwoLite_getNbFramesPerSwTrig_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_int)]
	LibLoader.lib.FliCredTwoLite_getNbFramesPerSwTrig_V2.restype = ctypes.c_bool
	def GetNbFramesPerSwTrig(self, context):
		nbFrames = ctypes.c_int(0)
		res = LibLoader.lib.FliCredTwoLite_getNbFramesPerSwTrig_V2(context, ctypes.byref(nbFrames))
		return res, nbFrames.value

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwoLite_getPreset_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_int)]
	LibLoader.lib.FliCredTwoLite_getPreset_V2.restype = ctypes.c_bool
	def GetPreset(self, context):
		preset = ctypes.c_int(0)
		res = LibLoader.lib.FliCredTwoLite_getPreset_V2(context, ctypes.byref(preset))
		return res, preset.value

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwoLite_getRemoteMaintenanceState_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_bool)]
	LibLoader.lib.FliCredTwoLite_getRemoteMaintenanceState_V2.restype = ctypes.c_bool
	def GetRemoteMaintenanceState(self, context):
		enabled = ctypes.c_bool(0)
		res = LibLoader.lib.FliCredTwoLite_getRemoteMaintenanceState_V2(context, ctypes.byref(enabled))
		return res, enabled.value

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwoLite_getStepSyncDelay_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_double)]
	LibLoader.lib.FliCredTwoLite_getStepSyncDelay_V2.restype = ctypes.c_bool
	def GetStepSyncDelay(self, context):
		delay = ctypes.c_double(0)
		res = LibLoader.lib.FliCredTwoLite_getStepSyncDelay_V2(context, ctypes.byref(delay))
		return res, delay.value

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwoLite_getSwSynchroState_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_bool)]
	LibLoader.lib.FliCredTwoLite_getSwSynchroState_V2.restype = ctypes.c_bool
	def GetSwSynchroState(self, context):
		enabled = ctypes.c_bool(0)
		res = LibLoader.lib.FliCredTwoLite_getSwSynchroState_V2(context, ctypes.byref(enabled))
		return res, enabled.value

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwoLite_getSyncDelay_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_double)]
	LibLoader.lib.FliCredTwoLite_getSyncDelay_V2.restype = ctypes.c_bool
	def GetSyncDelay(self, context):
		delay = ctypes.c_double(0)
		res = LibLoader.lib.FliCredTwoLite_getSyncDelay_V2(context, ctypes.byref(delay))
		return res, delay.value

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwoLite_getTcdsAdjustState_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_bool)]
	LibLoader.lib.FliCredTwoLite_getTcdsAdjustState_V2.restype = ctypes.c_bool
	def GetTcdsAdjustState(self, context):
		enabled = ctypes.c_bool(0)
		res = LibLoader.lib.FliCredTwoLite_getTcdsAdjustState_V2(context, ctypes.byref(enabled))
		return res, enabled.value

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwoLite_getTelnetState_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_bool)]
	LibLoader.lib.FliCredTwoLite_getTelnetState_V2.restype = ctypes.c_bool
	def GetTelnetState(self, context):
		enabled = ctypes.c_bool(0)
		res = LibLoader.lib.FliCredTwoLite_getTelnetState_V2(context, ctypes.byref(enabled))
		return res, enabled.value

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwoLite_getTintGranularityState_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_bool)]
	LibLoader.lib.FliCredTwoLite_getTintGranularityState_V2.restype = ctypes.c_bool
	def GetTintGranularityState(self, context):
		enabled = ctypes.c_bool(0)
		res = LibLoader.lib.FliCredTwoLite_getTintGranularityState_V2(context, ctypes.byref(enabled))
		return res, enabled.value

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwoLite_getTlsydel_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_int)]
	LibLoader.lib.FliCredTwoLite_getTlsydel_V2.restype = ctypes.c_bool
	def GetTlsydel(self, context):
		val = ctypes.c_int(0)
		res = LibLoader.lib.FliCredTwoLite_getTlsydel_V2(context, ctypes.byref(val))
		return res, val.value

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwoLite_getVrefAdjustState_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_bool)]
	LibLoader.lib.FliCredTwoLite_getVrefAdjustState_V2.restype = ctypes.c_bool
	def GetVrefAdjustState(self, context):
		enabled = ctypes.c_bool(0)
		res = LibLoader.lib.FliCredTwoLite_getVrefAdjustState_V2(context, ctypes.byref(enabled))
		return res, enabled.value

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwoLite_getAgcParam_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_double)]
	LibLoader.lib.FliCredTwoLite_getAgcParam_V2.restype = ctypes.c_bool
	def GetAgcParam(self, context):
		value = ctypes.c_double(0)
		res = LibLoader.lib.FliCredTwoLite_getAgcParam_V2(context, ctypes.byref(value))
		return res, value.value

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwoLite_getIpAlternateDns_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_size_t]
	LibLoader.lib.FliCredTwoLite_getIpAlternateDns_V2.restype = ctypes.c_bool
	def GetIpAlternateDns(self, context):
		res = LibLoader.lib.FliCredTwoLite_getIpAlternateDns_V2(context, charBuffer, bufferSize)
		return res, charBuffer.value.decode('utf-8', 'ignore')

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwoLite_getIpDns_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_size_t]
	LibLoader.lib.FliCredTwoLite_getIpDns_V2.restype = ctypes.c_bool
	def GetIpDns(self, context):
		res = LibLoader.lib.FliCredTwoLite_getIpDns_V2(context, charBuffer, bufferSize)
		return res, charBuffer.value.decode('utf-8', 'ignore')

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwoLite_getIpGateway_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_size_t]
	LibLoader.lib.FliCredTwoLite_getIpGateway_V2.restype = ctypes.c_bool
	def GetIpGateway(self, context):
		res = LibLoader.lib.FliCredTwoLite_getIpGateway_V2(context, charBuffer, bufferSize)
		return res, charBuffer.value.decode('utf-8', 'ignore')

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwoLite_getIpMode_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_size_t]
	LibLoader.lib.FliCredTwoLite_getIpMode_V2.restype = ctypes.c_bool
	def GetIpMode(self, context):
		res = LibLoader.lib.FliCredTwoLite_getIpMode_V2(context, charBuffer, bufferSize)
		return res, charBuffer.value.decode('utf-8', 'ignore')

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwoLite_getIpNetmask_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_size_t]
	LibLoader.lib.FliCredTwoLite_getIpNetmask_V2.restype = ctypes.c_bool
	def GetIpNetmask(self, context):
		res = LibLoader.lib.FliCredTwoLite_getIpNetmask_V2(context, charBuffer, bufferSize)
		return res, charBuffer.value.decode('utf-8', 'ignore')

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwoLite_getIpAddress_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_size_t]
	LibLoader.lib.FliCredTwoLite_getIpAddress_V2.restype = ctypes.c_bool
	def GetIpAddress(self, context):
		res = LibLoader.lib.FliCredTwoLite_getIpAddress_V2(context, charBuffer, bufferSize)
		return res, charBuffer.value.decode('utf-8', 'ignore')

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwoLite_getSnakeParam_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_int]
	LibLoader.lib.FliCredTwoLite_getSnakeParam_V2.restype = ctypes.c_bool
	def GetSnakeParam(self, context, parameter, value):
		res = LibLoader.lib.FliCredTwoLite_getSnakeParam_V2(context, parameter.encode(), value)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwoLite_getUploadFirmwareConnectionInfo_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_size_t, ctypes.c_int]
	LibLoader.lib.FliCredTwoLite_getUploadFirmwareConnectionInfo_V2.restype = ctypes.c_bool
	def GetUploadFirmwareConnectionInfo(self, context, port):
		res = LibLoader.lib.FliCredTwoLite_getUploadFirmwareConnectionInfo_V2(context, charBuffer, bufferSize, port)
		return res, charBuffer.value.decode('utf-8', 'ignore')

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwoLite_getConversionGain_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_size_t]
	LibLoader.lib.FliCredTwoLite_getConversionGain_V2.restype = ctypes.c_bool
	def GetConversionGain(self, context):
		res = LibLoader.lib.FliCredTwoLite_getConversionGain_V2(context, charBuffer, bufferSize)
		return res, charBuffer.value.decode('utf-8', 'ignore')

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwoLite_getTintStep_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_double)]
	LibLoader.lib.FliCredTwoLite_getTintStep_V2.restype = ctypes.c_bool
	def GetTintStep(self, context):
		step = ctypes.c_double(0)
		res = LibLoader.lib.FliCredTwoLite_getTintStep_V2(context, ctypes.byref(step))
		return res, step.value

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwoLite_getImagePattern_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_size_t]
	LibLoader.lib.FliCredTwoLite_getImagePattern_V2.restype = ctypes.c_bool
	def GetImagePattern(self, context):
		res = LibLoader.lib.FliCredTwoLite_getImagePattern_V2(context, charBuffer, bufferSize)
		return res, charBuffer.value.decode('utf-8', 'ignore')

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwoLite_getDate_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_size_t]
	LibLoader.lib.FliCredTwoLite_getDate_V2.restype = ctypes.c_bool
	def GetDate(self, context):
		res = LibLoader.lib.FliCredTwoLite_getDate_V2(context, charBuffer, bufferSize)
		return res, charBuffer.value.decode('utf-8', 'ignore')

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwoLite_getUptime_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_size_t]
	LibLoader.lib.FliCredTwoLite_getUptime_V2.restype = ctypes.c_bool
	def GetUptime(self, context):
		res = LibLoader.lib.FliCredTwoLite_getUptime_V2(context, charBuffer, bufferSize)
		return res, charBuffer.value.decode('utf-8', 'ignore')

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwoLite_getAccumulatedUptime_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_size_t]
	LibLoader.lib.FliCredTwoLite_getAccumulatedUptime_V2.restype = ctypes.c_bool
	def GetAccumulatedUptime(self, context):
		res = LibLoader.lib.FliCredTwoLite_getAccumulatedUptime_V2(context, charBuffer, bufferSize)
		return res, charBuffer.value.decode('utf-8', 'ignore')

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwoLite_getTotalUptime_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_size_t]
	LibLoader.lib.FliCredTwoLite_getTotalUptime_V2.restype = ctypes.c_bool
	def GetTotalUptime(self, context):
		res = LibLoader.lib.FliCredTwoLite_getTotalUptime_V2(context, charBuffer, bufferSize)
		return res, charBuffer.value.decode('utf-8', 'ignore')

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwoLite_getRawImagesState_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_bool)]
	LibLoader.lib.FliCredTwoLite_getRawImagesState_V2.restype = ctypes.c_bool
	def GetRawImagesState(self, context):
		enabled = ctypes.c_bool(0)
		res = LibLoader.lib.FliCredTwoLite_getRawImagesState_V2(context, ctypes.byref(enabled))
		return res, enabled.value

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwoLite_getUnsignedPixelsState_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_bool)]
	LibLoader.lib.FliCredTwoLite_getUnsignedPixelsState_V2.restype = ctypes.c_bool
	def GetUnsignedPixelsState(self, context):
		enabled = ctypes.c_bool(0)
		res = LibLoader.lib.FliCredTwoLite_getUnsignedPixelsState_V2(context, ctypes.byref(enabled))
		return res, enabled.value

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwoLite_getCoolingMode_V2.argtypes = [ctypes.c_void_p]
	LibLoader.lib.FliCredTwoLite_getCoolingMode_V2.restype = ctypes.c_bool
	def GetCoolingMode(self, context):
		res = LibLoader.lib.FliCredTwoLite_getCoolingMode_V2(context)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwoLite_getCoolingFirstPoint_V2.argtypes = [ctypes.c_void_p, ctypes.c_int]
	LibLoader.lib.FliCredTwoLite_getCoolingFirstPoint_V2.restype = ctypes.c_bool
	def GetCoolingFirstPoint(self, context, firstPoint):
		res = LibLoader.lib.FliCredTwoLite_getCoolingFirstPoint_V2(context, firstPoint)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwoLite_getCoolingStepWidth_V2.argtypes = [ctypes.c_void_p, ctypes.c_int]
	LibLoader.lib.FliCredTwoLite_getCoolingStepWidth_V2.restype = ctypes.c_bool
	def GetCoolingStepWidth(self, context, stepWidth):
		res = LibLoader.lib.FliCredTwoLite_getCoolingStepWidth_V2(context, stepWidth)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwoLite_getSensorSetpoint_V2.argtypes = [ctypes.c_void_p, ctypes.c_int]
	LibLoader.lib.FliCredTwoLite_getSensorSetpoint_V2.restype = ctypes.c_bool
	def GetSensorSetpoint(self, context, temp):
		res = LibLoader.lib.FliCredTwoLite_getSensorSetpoint_V2(context, temp)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwoLite_getTecPower_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double)]
	LibLoader.lib.FliCredTwoLite_getTecPower_V2.restype = ctypes.c_bool
	def GetTecPower(self, context):
		current = ctypes.c_double(0)
		voltage = ctypes.c_double(0)
		power = ctypes.c_double(0)
		res = LibLoader.lib.FliCredTwoLite_getTecPower_V2(context, ctypes.byref(current), ctypes.byref(voltage), ctypes.byref(power))
		return res, current.value, voltage.value, power.value

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwoLite_getCoolingState_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_bool)]
	LibLoader.lib.FliCredTwoLite_getCoolingState_V2.restype = ctypes.c_bool
	def GetCoolingState(self, context):
		enabled = ctypes.c_bool(0)
		res = LibLoader.lib.FliCredTwoLite_getCoolingState_V2(context, ctypes.byref(enabled))
		return res, enabled.value

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwoLite_getCurrentStep_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_size_t]
	LibLoader.lib.FliCredTwoLite_getCurrentStep_V2.restype = ctypes.c_bool
	def GetCurrentStep(self, context):
		res = LibLoader.lib.FliCredTwoLite_getCurrentStep_V2(context, charBuffer, bufferSize)
		return res, charBuffer.value.decode('utf-8', 'ignore')

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwoLite_setTint_V2.argtypes = [ctypes.c_void_p, ctypes.c_double]
	LibLoader.lib.FliCredTwoLite_setTint_V2.restype = ctypes.c_bool
	def SetTint(self, context, tint):
		res = LibLoader.lib.FliCredTwoLite_setTint_V2(context, tint)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwoLite_setConversionGain_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
	LibLoader.lib.FliCredTwoLite_setConversionGain_V2.restype = ctypes.c_bool
	def SetConversionGain(self, context, gain):
		res = LibLoader.lib.FliCredTwoLite_setConversionGain_V2(context, gain.encode())
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwoLite_setAgcPriorityNone_V2.argtypes = [ctypes.c_void_p]
	LibLoader.lib.FliCredTwoLite_setAgcPriorityNone_V2.restype = ctypes.c_bool
	def SetAgcPriorityNone(self, context):
		res = LibLoader.lib.FliCredTwoLite_setAgcPriorityNone_V2(context)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwoLite_setAgcPriorityOverExposed_V2.argtypes = [ctypes.c_void_p]
	LibLoader.lib.FliCredTwoLite_setAgcPriorityOverExposed_V2.restype = ctypes.c_bool
	def SetAgcPriorityOverExposed(self, context):
		res = LibLoader.lib.FliCredTwoLite_setAgcPriorityOverExposed_V2(context)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwoLite_setAgcPriorityUnderExposed_V2.argtypes = [ctypes.c_void_p]
	LibLoader.lib.FliCredTwoLite_setAgcPriorityUnderExposed_V2.restype = ctypes.c_bool
	def SetAgcPriorityUnderExposed(self, context):
		res = LibLoader.lib.FliCredTwoLite_setAgcPriorityUnderExposed_V2(context)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwoLite_setDarkOptimLevel_V2.argtypes = [ctypes.c_void_p, ctypes.c_int]
	LibLoader.lib.FliCredTwoLite_setDarkOptimLevel_V2.restype = ctypes.c_bool
	def SetDarkOptimLevel(self, context, level):
		res = LibLoader.lib.FliCredTwoLite_setDarkOptimLevel_V2(context, level)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwoLite_setExtSynchroExposureInternal_V2.argtypes = [ctypes.c_void_p]
	LibLoader.lib.FliCredTwoLite_setExtSynchroExposureInternal_V2.restype = ctypes.c_bool
	def SetExtSynchroExposureInternal(self, context):
		res = LibLoader.lib.FliCredTwoLite_setExtSynchroExposureInternal_V2(context)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwoLite_setExtSynchroExposureExternal_V2.argtypes = [ctypes.c_void_p]
	LibLoader.lib.FliCredTwoLite_setExtSynchroExposureExternal_V2.restype = ctypes.c_bool
	def SetExtSynchroExposureExternal(self, context):
		res = LibLoader.lib.FliCredTwoLite_setExtSynchroExposureExternal_V2(context)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwoLite_setExtSynchroPolarityInverted_V2.argtypes = [ctypes.c_void_p]
	LibLoader.lib.FliCredTwoLite_setExtSynchroPolarityInverted_V2.restype = ctypes.c_bool
	def SetExtSynchroPolarityInverted(self, context):
		res = LibLoader.lib.FliCredTwoLite_setExtSynchroPolarityInverted_V2(context)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwoLite_setExtSynchroPolarityStandard_V2.argtypes = [ctypes.c_void_p]
	LibLoader.lib.FliCredTwoLite_setExtSynchroPolarityStandard_V2.restype = ctypes.c_bool
	def SetExtSynchroPolarityStandard(self, context):
		res = LibLoader.lib.FliCredTwoLite_setExtSynchroPolarityStandard_V2(context)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwoLite_setHdrCalibrationC1_V2.argtypes = [ctypes.c_void_p]
	LibLoader.lib.FliCredTwoLite_setHdrCalibrationC1_V2.restype = ctypes.c_bool
	def SetHdrCalibrationC1(self, context):
		res = LibLoader.lib.FliCredTwoLite_setHdrCalibrationC1_V2(context)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwoLite_setHdrCalibrationC2_V2.argtypes = [ctypes.c_void_p]
	LibLoader.lib.FliCredTwoLite_setHdrCalibrationC2_V2.restype = ctypes.c_bool
	def SetHdrCalibrationC2(self, context):
		res = LibLoader.lib.FliCredTwoLite_setHdrCalibrationC2_V2(context)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwoLite_setHdrCalibrationOff_V2.argtypes = [ctypes.c_void_p]
	LibLoader.lib.FliCredTwoLite_setHdrCalibrationOff_V2.restype = ctypes.c_bool
	def SetHdrCalibrationOff(self, context):
		res = LibLoader.lib.FliCredTwoLite_setHdrCalibrationOff_V2(context)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwoLite_setNbFramesPerSwTrig_V2.argtypes = [ctypes.c_void_p, ctypes.c_int]
	LibLoader.lib.FliCredTwoLite_setNbFramesPerSwTrig_V2.restype = ctypes.c_bool
	def SetNbFramesPerSwTrig(self, context, nbFrames):
		res = LibLoader.lib.FliCredTwoLite_setNbFramesPerSwTrig_V2(context, nbFrames)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwoLite_setSyncDelay_V2.argtypes = [ctypes.c_void_p, ctypes.c_int]
	LibLoader.lib.FliCredTwoLite_setSyncDelay_V2.restype = ctypes.c_bool
	def SetSyncDelay(self, context, delay):
		res = LibLoader.lib.FliCredTwoLite_setSyncDelay_V2(context, delay)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwoLite_setTlsyDel_V2.argtypes = [ctypes.c_void_p, ctypes.c_int]
	LibLoader.lib.FliCredTwoLite_setTlsyDel_V2.restype = ctypes.c_bool
	def SetTlsyDel(self, context, val):
		res = LibLoader.lib.FliCredTwoLite_setTlsyDel_V2(context, val)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwoLite_setVoltageVref_V2.argtypes = [ctypes.c_void_p, ctypes.c_double]
	LibLoader.lib.FliCredTwoLite_setVoltageVref_V2.restype = ctypes.c_bool
	def SetVoltageVref(self, context, vref):
		res = LibLoader.lib.FliCredTwoLite_setVoltageVref_V2(context, vref)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwoLite_setAgcRoi_V2.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int]
	LibLoader.lib.FliCredTwoLite_setAgcRoi_V2.restype = ctypes.c_bool
	def SetAgcRoi(self, context, col1, row1, col2, row2):
		res = LibLoader.lib.FliCredTwoLite_setAgcRoi_V2(context, col1, row1, col2, row2)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwoLite_setAgcParam_V2.argtypes = [ctypes.c_void_p, ctypes.c_double]
	LibLoader.lib.FliCredTwoLite_setAgcParam_V2.restype = ctypes.c_bool
	def SetAgcParam(self, context, value):
		res = LibLoader.lib.FliCredTwoLite_setAgcParam_V2(context, value)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwoLite_setPreset_V2.argtypes = [ctypes.c_void_p]
	LibLoader.lib.FliCredTwoLite_setPreset_V2.restype = ctypes.c_bool
	def SetPreset(self, context):
		res = LibLoader.lib.FliCredTwoLite_setPreset_V2(context)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwoLite_setPresetNumber_V2.argtypes = [ctypes.c_void_p, ctypes.c_int]
	LibLoader.lib.FliCredTwoLite_setPresetNumber_V2.restype = ctypes.c_bool
	def SetPresetNumber(self, context, presetNumber):
		res = LibLoader.lib.FliCredTwoLite_setPresetNumber_V2(context, presetNumber)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwoLite_setSnakeParam_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_int]
	LibLoader.lib.FliCredTwoLite_setSnakeParam_V2.restype = ctypes.c_bool
	def SetSnakeParam(self, context, parameter, value):
		res = LibLoader.lib.FliCredTwoLite_setSnakeParam_V2(context, parameter.encode(), value)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwoLite_setImagePatternRamp_V2.argtypes = [ctypes.c_void_p]
	LibLoader.lib.FliCredTwoLite_setImagePatternRamp_V2.restype = ctypes.c_bool
	def SetImagePatternRamp(self, context):
		res = LibLoader.lib.FliCredTwoLite_setImagePatternRamp_V2(context)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwoLite_setImagePatternConstant_V2.argtypes = [ctypes.c_void_p, ctypes.c_int]
	LibLoader.lib.FliCredTwoLite_setImagePatternConstant_V2.restype = ctypes.c_bool
	def SetImagePatternConstant(self, context, val):
		res = LibLoader.lib.FliCredTwoLite_setImagePatternConstant_V2(context, val)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwoLite_setImagePatternOff_V2.argtypes = [ctypes.c_void_p]
	LibLoader.lib.FliCredTwoLite_setImagePatternOff_V2.restype = ctypes.c_bool
	def SetImagePatternOff(self, context):
		res = LibLoader.lib.FliCredTwoLite_setImagePatternOff_V2(context)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwoLite_setCoolingState_V2.argtypes = [ctypes.c_void_p, ctypes.c_bool]
	LibLoader.lib.FliCredTwoLite_setCoolingState_V2.restype = ctypes.c_bool
	def SetCoolingState(self, context, enable):
		res = LibLoader.lib.FliCredTwoLite_setCoolingState_V2(context, enable)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwoLite_setCoolingMode_V2.argtypes = [ctypes.c_void_p]
	LibLoader.lib.FliCredTwoLite_setCoolingMode_V2.restype = ctypes.c_bool
	def SetCoolingMode(self, context):
		res = LibLoader.lib.FliCredTwoLite_setCoolingMode_V2(context)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwoLite_setCoolingFirstPoint_V2.argtypes = [ctypes.c_void_p, ctypes.c_int]
	LibLoader.lib.FliCredTwoLite_setCoolingFirstPoint_V2.restype = ctypes.c_bool
	def SetCoolingFirstPoint(self, context, firstPoint):
		res = LibLoader.lib.FliCredTwoLite_setCoolingFirstPoint_V2(context, firstPoint)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwoLite_setCoolingStepWidth_V2.argtypes = [ctypes.c_void_p, ctypes.c_int]
	LibLoader.lib.FliCredTwoLite_setCoolingStepWidth_V2.restype = ctypes.c_bool
	def SetCoolingStepWidth(self, context, stepWidth):
		res = LibLoader.lib.FliCredTwoLite_setCoolingStepWidth_V2(context, stepWidth)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwoLite_setSensorSetpoint_V2.argtypes = [ctypes.c_void_p, ctypes.c_int]
	LibLoader.lib.FliCredTwoLite_setSensorSetpoint_V2.restype = ctypes.c_bool
	def SetSensorSetpoint(self, context, temp):
		res = LibLoader.lib.FliCredTwoLite_setSensorSetpoint_V2(context, temp)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwoLite_enableAntiBlooming_V2.argtypes = [ctypes.c_void_p, ctypes.c_bool]
	LibLoader.lib.FliCredTwoLite_enableAntiBlooming_V2.restype = ctypes.c_bool
	def EnableAntiBlooming(self, context, enabled):
		res = LibLoader.lib.FliCredTwoLite_enableAntiBlooming_V2(context, enabled)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwoLite_enableBadPixel_V2.argtypes = [ctypes.c_void_p, ctypes.c_bool]
	LibLoader.lib.FliCredTwoLite_enableBadPixel_V2.restype = ctypes.c_bool
	def EnableBadPixel(self, context, enabled):
		res = LibLoader.lib.FliCredTwoLite_enableBadPixel_V2(context, enabled)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwoLite_enableAdaptbias_V2.argtypes = [ctypes.c_void_p, ctypes.c_bool]
	LibLoader.lib.FliCredTwoLite_enableAdaptbias_V2.restype = ctypes.c_bool
	def EnableAdaptbias(self, context, enable):
		res = LibLoader.lib.FliCredTwoLite_enableAdaptbias_V2(context, enable)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwoLite_enableAgc_V2.argtypes = [ctypes.c_void_p, ctypes.c_bool]
	LibLoader.lib.FliCredTwoLite_enableAgc_V2.restype = ctypes.c_bool
	def EnableAgc(self, context, enable):
		res = LibLoader.lib.FliCredTwoLite_enableAgc_V2(context, enable)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwoLite_enableHdrExtended_V2.argtypes = [ctypes.c_void_p, ctypes.c_bool]
	LibLoader.lib.FliCredTwoLite_enableHdrExtended_V2.restype = ctypes.c_bool
	def EnableHdrExtended(self, context, enable):
		res = LibLoader.lib.FliCredTwoLite_enableHdrExtended_V2(context, enable)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwoLite_enableHdr_V2.argtypes = [ctypes.c_void_p, ctypes.c_bool]
	LibLoader.lib.FliCredTwoLite_enableHdr_V2.restype = ctypes.c_bool
	def EnableHdr(self, context, enable):
		res = LibLoader.lib.FliCredTwoLite_enableHdr_V2(context, enable)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwoLite_enableRemoteMaintenance_V2.argtypes = [ctypes.c_void_p, ctypes.c_bool]
	LibLoader.lib.FliCredTwoLite_enableRemoteMaintenance_V2.restype = ctypes.c_bool
	def EnableRemoteMaintenance(self, context, enable):
		res = LibLoader.lib.FliCredTwoLite_enableRemoteMaintenance_V2(context, enable)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwoLite_enableSwSynchro_V2.argtypes = [ctypes.c_void_p, ctypes.c_bool]
	LibLoader.lib.FliCredTwoLite_enableSwSynchro_V2.restype = ctypes.c_bool
	def EnableSwSynchro(self, context, enable):
		res = LibLoader.lib.FliCredTwoLite_enableSwSynchro_V2(context, enable)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwoLite_enableTcdsAdjust_V2.argtypes = [ctypes.c_void_p, ctypes.c_bool]
	LibLoader.lib.FliCredTwoLite_enableTcdsAdjust_V2.restype = ctypes.c_bool
	def EnableTcdsAdjust(self, context, enable):
		res = LibLoader.lib.FliCredTwoLite_enableTcdsAdjust_V2(context, enable)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwoLite_enableTintGranularity_V2.argtypes = [ctypes.c_void_p, ctypes.c_bool]
	LibLoader.lib.FliCredTwoLite_enableTintGranularity_V2.restype = ctypes.c_bool
	def EnableTintGranularity(self, context, enable):
		res = LibLoader.lib.FliCredTwoLite_enableTintGranularity_V2(context, enable)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwoLite_enableVrefAdjust_V2.argtypes = [ctypes.c_void_p, ctypes.c_bool]
	LibLoader.lib.FliCredTwoLite_enableVrefAdjust_V2.restype = ctypes.c_bool
	def EnableVrefAdjust(self, context, enable):
		res = LibLoader.lib.FliCredTwoLite_enableVrefAdjust_V2(context, enable)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwoLite_enableRawImages_V2.argtypes = [ctypes.c_void_p, ctypes.c_bool]
	LibLoader.lib.FliCredTwoLite_enableRawImages_V2.restype = ctypes.c_bool
	def EnableRawImages(self, context, enable):
		res = LibLoader.lib.FliCredTwoLite_enableRawImages_V2(context, enable)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwoLite_enableUnsignedPixels_V2.argtypes = [ctypes.c_void_p, ctypes.c_bool]
	LibLoader.lib.FliCredTwoLite_enableUnsignedPixels_V2.restype = ctypes.c_bool
	def EnableUnsignedPixels(self, context, enable):
		res = LibLoader.lib.FliCredTwoLite_enableUnsignedPixels_V2(context, enable)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwoLite_reboot_V2.argtypes = [ctypes.c_void_p]
	LibLoader.lib.FliCredTwoLite_reboot_V2.restype = ctypes.c_bool
	def Reboot(self, context):
		res = LibLoader.lib.FliCredTwoLite_reboot_V2(context)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwoLite_buildFlatHdrC1_V2.argtypes = [ctypes.c_void_p]
	LibLoader.lib.FliCredTwoLite_buildFlatHdrC1_V2.restype = ctypes.c_bool
	def BuildFlatHdrC1(self, context):
		res = LibLoader.lib.FliCredTwoLite_buildFlatHdrC1_V2(context)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwoLite_buildFlatHdrC2_V2.argtypes = [ctypes.c_void_p]
	LibLoader.lib.FliCredTwoLite_buildFlatHdrC2_V2.restype = ctypes.c_bool
	def BuildFlatHdrC2(self, context):
		res = LibLoader.lib.FliCredTwoLite_buildFlatHdrC2_V2(context)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwoLite_sendBiasHdrC1FromUrl_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
	LibLoader.lib.FliCredTwoLite_sendBiasHdrC1FromUrl_V2.restype = ctypes.c_bool
	def SendBiasHdrC1FromUrl(self, context, url):
		res = LibLoader.lib.FliCredTwoLite_sendBiasHdrC1FromUrl_V2(context, url.encode())
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwoLite_sendBiasHdrC2FromUrl_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
	LibLoader.lib.FliCredTwoLite_sendBiasHdrC2FromUrl_V2.restype = ctypes.c_bool
	def SendBiasHdrC2FromUrl(self, context, url):
		res = LibLoader.lib.FliCredTwoLite_sendBiasHdrC2FromUrl_V2(context, url.encode())
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwoLite_sendFlatHdrC1FromUrl_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
	LibLoader.lib.FliCredTwoLite_sendFlatHdrC1FromUrl_V2.restype = ctypes.c_bool
	def SendFlatHdrC1FromUrl(self, context, url):
		res = LibLoader.lib.FliCredTwoLite_sendFlatHdrC1FromUrl_V2(context, url.encode())
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwoLite_sendFlatHdrC2FromUrl_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
	LibLoader.lib.FliCredTwoLite_sendFlatHdrC2FromUrl_V2.restype = ctypes.c_bool
	def SendFlatHdrC2FromUrl(self, context, url):
		res = LibLoader.lib.FliCredTwoLite_sendFlatHdrC2FromUrl_V2(context, url.encode())
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwoLite_sendBiasHdrC1File_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
	LibLoader.lib.FliCredTwoLite_sendBiasHdrC1File_V2.restype = ctypes.c_bool
	def SendBiasHdrC1File(self, context, filePath):
		res = LibLoader.lib.FliCredTwoLite_sendBiasHdrC1File_V2(context, filePath.encode())
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwoLite_sendBiasHdrC2File_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
	LibLoader.lib.FliCredTwoLite_sendBiasHdrC2File_V2.restype = ctypes.c_bool
	def SendBiasHdrC2File(self, context, filePath):
		res = LibLoader.lib.FliCredTwoLite_sendBiasHdrC2File_V2(context, filePath.encode())
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwoLite_sendFlatHdrC1File_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
	LibLoader.lib.FliCredTwoLite_sendFlatHdrC1File_V2.restype = ctypes.c_bool
	def SendFlatHdrC1File(self, context, filePath):
		res = LibLoader.lib.FliCredTwoLite_sendFlatHdrC1File_V2(context, filePath.encode())
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwoLite_sendFlatHdrC2File_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
	LibLoader.lib.FliCredTwoLite_sendFlatHdrC2File_V2.restype = ctypes.c_bool
	def SendFlatHdrC2File(self, context, filePath):
		res = LibLoader.lib.FliCredTwoLite_sendFlatHdrC2File_V2(context, filePath.encode())
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwoLite_xSendBiasFile_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
	LibLoader.lib.FliCredTwoLite_xSendBiasFile_V2.restype = ctypes.c_bool
	def XSendBiasFile(self, context, filePath):
		res = LibLoader.lib.FliCredTwoLite_xSendBiasFile_V2(context, filePath.encode())
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwoLite_xSendBiasHdrC1File_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
	LibLoader.lib.FliCredTwoLite_xSendBiasHdrC1File_V2.restype = ctypes.c_bool
	def XSendBiasHdrC1File(self, context, filePath):
		res = LibLoader.lib.FliCredTwoLite_xSendBiasHdrC1File_V2(context, filePath.encode())
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwoLite_xSendBiasHdrC2File_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
	LibLoader.lib.FliCredTwoLite_xSendBiasHdrC2File_V2.restype = ctypes.c_bool
	def XSendBiasHdrC2File(self, context, filePath):
		res = LibLoader.lib.FliCredTwoLite_xSendBiasHdrC2File_V2(context, filePath.encode())
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwoLite_xSendFlatFile_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
	LibLoader.lib.FliCredTwoLite_xSendFlatFile_V2.restype = ctypes.c_bool
	def XSendFlatFile(self, context, filePath):
		res = LibLoader.lib.FliCredTwoLite_xSendFlatFile_V2(context, filePath.encode())
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwoLite_xSendFlatHdrC1File_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
	LibLoader.lib.FliCredTwoLite_xSendFlatHdrC1File_V2.restype = ctypes.c_bool
	def XSendFlatHdrC1File(self, context, filePath):
		res = LibLoader.lib.FliCredTwoLite_xSendFlatHdrC1File_V2(context, filePath.encode())
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwoLite_xSendFlatHdrC2File_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
	LibLoader.lib.FliCredTwoLite_xSendFlatHdrC2File_V2.restype = ctypes.c_bool
	def XSendFlatHdrC2File(self, context, filePath):
		res = LibLoader.lib.FliCredTwoLite_xSendFlatHdrC2File_V2(context, filePath.encode())
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwoLite_sendLicenseFile_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_char_p]
	LibLoader.lib.FliCredTwoLite_sendLicenseFile_V2.restype = ctypes.c_bool
	def SendLicenseFile(self, context, filePath, fileName):
		res = LibLoader.lib.FliCredTwoLite_sendLicenseFile_V2(context, filePath.encode(), fileName.encode())
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwoLite_deleteLicense_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
	LibLoader.lib.FliCredTwoLite_deleteLicense_V2.restype = ctypes.c_bool
	def DeleteLicense(self, context, licenseName):
		res = LibLoader.lib.FliCredTwoLite_deleteLicense_V2(context, licenseName.encode())
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwoLite_disableLicense_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
	LibLoader.lib.FliCredTwoLite_disableLicense_V2.restype = ctypes.c_bool
	def DisableLicense(self, context, licenseName):
		res = LibLoader.lib.FliCredTwoLite_disableLicense_V2(context, licenseName.encode())
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwoLite_enableLicense_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
	LibLoader.lib.FliCredTwoLite_enableLicense_V2.restype = ctypes.c_bool
	def EnableLicense(self, context, licenseName):
		res = LibLoader.lib.FliCredTwoLite_enableLicense_V2(context, licenseName.encode())
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwoLite_softwareTrig_V2.argtypes = [ctypes.c_void_p]
	LibLoader.lib.FliCredTwoLite_softwareTrig_V2.restype = ctypes.c_bool
	def SoftwareTrig(self, context):
		res = LibLoader.lib.FliCredTwoLite_softwareTrig_V2(context)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwoLite_startHttpServer_V2.argtypes = [ctypes.c_void_p]
	LibLoader.lib.FliCredTwoLite_startHttpServer_V2.restype = ctypes.c_bool
	def StartHttpServer(self, context):
		res = LibLoader.lib.FliCredTwoLite_startHttpServer_V2(context)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwoLite_stopHttpServer_V2.argtypes = [ctypes.c_void_p]
	LibLoader.lib.FliCredTwoLite_stopHttpServer_V2.restype = ctypes.c_bool
	def StopHttpServer(self, context):
		res = LibLoader.lib.FliCredTwoLite_stopHttpServer_V2(context)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwoLite_startEthernetGrabber_V2.argtypes = [ctypes.c_void_p]
	LibLoader.lib.FliCredTwoLite_startEthernetGrabber_V2.restype = ctypes.c_bool
	def StartEthernetGrabber(self, context):
		res = LibLoader.lib.FliCredTwoLite_startEthernetGrabber_V2(context)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwoLite_stopEthernetGrabber_V2.argtypes = [ctypes.c_void_p]
	LibLoader.lib.FliCredTwoLite_stopEthernetGrabber_V2.restype = ctypes.c_bool
	def StopEthernetGrabber(self, context):
		res = LibLoader.lib.FliCredTwoLite_stopEthernetGrabber_V2(context)
		return res

