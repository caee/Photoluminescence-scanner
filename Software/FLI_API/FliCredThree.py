import LibLoader
import ctypes
import numpy as np

bufferSize = ctypes.c_size_t(1000)
charBuffer = ctypes.create_string_buffer(bufferSize.value)

class FliCredThree:
	#------------------------------------------------------------
	LibLoader.lib.FliCredThree_getAllTemp_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double)]
	LibLoader.lib.FliCredThree_getAllTemp_V2.restype = ctypes.c_bool
	def GetAllTemp(self, context):
		cpu = ctypes.c_double(0)
		backend = ctypes.c_double(0)
		interfaceTemp = ctypes.c_double(0)
		ambiant = ctypes.c_double(0)
		sensor = ctypes.c_double(0)
		res = LibLoader.lib.FliCredThree_getAllTemp_V2(context, ctypes.byref(cpu), ctypes.byref(backend), ctypes.byref(interfaceTemp), ctypes.byref(ambiant), ctypes.byref(sensor))
		return res, cpu.value, backend.value, interfaceTemp.value, ambiant.value, sensor.value

	#------------------------------------------------------------
	LibLoader.lib.FliCredThree_getTint_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_double)]
	LibLoader.lib.FliCredThree_getTint_V2.restype = ctypes.c_bool
	def GetTint(self, context):
		tint = ctypes.c_double(0)
		res = LibLoader.lib.FliCredThree_getTint_V2(context, ctypes.byref(tint))
		return res, tint.value

	#------------------------------------------------------------
	LibLoader.lib.FliCredThree_getTintMax_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_double)]
	LibLoader.lib.FliCredThree_getTintMax_V2.restype = ctypes.c_bool
	def GetTintMax(self, context):
		tintMax = ctypes.c_double(0)
		res = LibLoader.lib.FliCredThree_getTintMax_V2(context, ctypes.byref(tintMax))
		return res, tintMax.value

	#------------------------------------------------------------
	LibLoader.lib.FliCredThree_getAntiBloomingState_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_bool)]
	LibLoader.lib.FliCredThree_getAntiBloomingState_V2.restype = ctypes.c_bool
	def GetAntiBloomingState(self, context):
		enabled = ctypes.c_bool(0)
		res = LibLoader.lib.FliCredThree_getAntiBloomingState_V2(context, ctypes.byref(enabled))
		return res, enabled.value

	#------------------------------------------------------------
	LibLoader.lib.FliCredThree_getBadPixelState_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_bool)]
	LibLoader.lib.FliCredThree_getBadPixelState_V2.restype = ctypes.c_bool
	def GetBadPixelState(self, context):
		enabled = ctypes.c_bool(0)
		res = LibLoader.lib.FliCredThree_getBadPixelState_V2(context, ctypes.byref(enabled))
		return res, enabled.value

	#------------------------------------------------------------
	LibLoader.lib.FliCredThree_getTempAmbiant_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_double)]
	LibLoader.lib.FliCredThree_getTempAmbiant_V2.restype = ctypes.c_bool
	def GetTempAmbiant(self, context):
		temp = ctypes.c_double(0)
		res = LibLoader.lib.FliCredThree_getTempAmbiant_V2(context, ctypes.byref(temp))
		return res, temp.value

	#------------------------------------------------------------
	LibLoader.lib.FliCredThree_getTempBackEnd_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_double)]
	LibLoader.lib.FliCredThree_getTempBackEnd_V2.restype = ctypes.c_bool
	def GetTempBackEnd(self, context):
		temp = ctypes.c_double(0)
		res = LibLoader.lib.FliCredThree_getTempBackEnd_V2(context, ctypes.byref(temp))
		return res, temp.value

	#------------------------------------------------------------
	LibLoader.lib.FliCredThree_getTempCpu_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_double)]
	LibLoader.lib.FliCredThree_getTempCpu_V2.restype = ctypes.c_bool
	def GetTempCpu(self, context):
		temp = ctypes.c_double(0)
		res = LibLoader.lib.FliCredThree_getTempCpu_V2(context, ctypes.byref(temp))
		return res, temp.value

	#------------------------------------------------------------
	LibLoader.lib.FliCredThree_getTempInterface_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_double)]
	LibLoader.lib.FliCredThree_getTempInterface_V2.restype = ctypes.c_bool
	def GetTempInterface(self, context):
		temp = ctypes.c_double(0)
		res = LibLoader.lib.FliCredThree_getTempInterface_V2(context, ctypes.byref(temp))
		return res, temp.value

	#------------------------------------------------------------
	LibLoader.lib.FliCredThree_getTempSnake_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_double)]
	LibLoader.lib.FliCredThree_getTempSnake_V2.restype = ctypes.c_bool
	def GetTempSnake(self, context):
		temp = ctypes.c_double(0)
		res = LibLoader.lib.FliCredThree_getTempSnake_V2(context, ctypes.byref(temp))
		return res, temp.value

	#------------------------------------------------------------
	LibLoader.lib.FliCredThree_getTintRange_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double)]
	LibLoader.lib.FliCredThree_getTintRange_V2.restype = ctypes.c_bool
	def GetTintRange(self, context):
		tintMin = ctypes.c_double(0)
		tintMax = ctypes.c_double(0)
		res = LibLoader.lib.FliCredThree_getTintRange_V2(context, ctypes.byref(tintMin), ctypes.byref(tintMax))
		return res, tintMin.value, tintMax.value

	#------------------------------------------------------------
	LibLoader.lib.FliCredThree_getAdaptBiasState_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_bool)]
	LibLoader.lib.FliCredThree_getAdaptBiasState_V2.restype = ctypes.c_bool
	def GetAdaptBiasState(self, context):
		enabled = ctypes.c_bool(0)
		res = LibLoader.lib.FliCredThree_getAdaptBiasState_V2(context, ctypes.byref(enabled))
		return res, enabled.value

	#------------------------------------------------------------
	LibLoader.lib.FliCredThree_getAgcState_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_bool)]
	LibLoader.lib.FliCredThree_getAgcState_V2.restype = ctypes.c_bool
	def GetAgcState(self, context):
		enabled = ctypes.c_bool(0)
		res = LibLoader.lib.FliCredThree_getAgcState_V2(context, ctypes.byref(enabled))
		return res, enabled.value

	#------------------------------------------------------------
	LibLoader.lib.FliCredThree_getAgcPriority_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_size_t]
	LibLoader.lib.FliCredThree_getAgcPriority_V2.restype = ctypes.c_bool
	def GetAgcPriority(self, context):
		res = LibLoader.lib.FliCredThree_getAgcPriority_V2(context, charBuffer, bufferSize)
		return res, charBuffer.value.decode('utf-8', 'ignore')

	#------------------------------------------------------------
	LibLoader.lib.FliCredThree_getAgcRoi_V2.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int]
	LibLoader.lib.FliCredThree_getAgcRoi_V2.restype = ctypes.c_bool
	def GetAgcRoi(self, context, col1, row1, col2, row2):
		res = LibLoader.lib.FliCredThree_getAgcRoi_V2(context, col1, row1, col2, row2)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredThree_getDarkOptimLevel_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_int)]
	LibLoader.lib.FliCredThree_getDarkOptimLevel_V2.restype = ctypes.c_bool
	def GetDarkOptimLevel(self, context):
		level = ctypes.c_int(0)
		res = LibLoader.lib.FliCredThree_getDarkOptimLevel_V2(context, ctypes.byref(level))
		return res, level.value

	#------------------------------------------------------------
	LibLoader.lib.FliCredThree_getExtSynchroExposure_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_size_t]
	LibLoader.lib.FliCredThree_getExtSynchroExposure_V2.restype = ctypes.c_bool
	def GetExtSynchroExposure(self, context):
		res = LibLoader.lib.FliCredThree_getExtSynchroExposure_V2(context, charBuffer, bufferSize)
		return res, charBuffer.value.decode('utf-8', 'ignore')

	#------------------------------------------------------------
	LibLoader.lib.FliCredThree_getExtSynchroPolarity_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_size_t]
	LibLoader.lib.FliCredThree_getExtSynchroPolarity_V2.restype = ctypes.c_bool
	def GetExtSynchroPolarity(self, context):
		res = LibLoader.lib.FliCredThree_getExtSynchroPolarity_V2(context, charBuffer, bufferSize)
		return res, charBuffer.value.decode('utf-8', 'ignore')

	#------------------------------------------------------------
	LibLoader.lib.FliCredThree_getHdrState_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_bool)]
	LibLoader.lib.FliCredThree_getHdrState_V2.restype = ctypes.c_bool
	def GetHdrState(self, context):
		enabled = ctypes.c_bool(0)
		res = LibLoader.lib.FliCredThree_getHdrState_V2(context, ctypes.byref(enabled))
		return res, enabled.value

	#------------------------------------------------------------
	LibLoader.lib.FliCredThree_getHdrCalibrationMode_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_size_t]
	LibLoader.lib.FliCredThree_getHdrCalibrationMode_V2.restype = ctypes.c_bool
	def GetHdrCalibrationMode(self, context):
		res = LibLoader.lib.FliCredThree_getHdrCalibrationMode_V2(context, charBuffer, bufferSize)
		return res, charBuffer.value.decode('utf-8', 'ignore')

	#------------------------------------------------------------
	LibLoader.lib.FliCredThree_getHdrExtendedState_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_bool)]
	LibLoader.lib.FliCredThree_getHdrExtendedState_V2.restype = ctypes.c_bool
	def GetHdrExtendedState(self, context):
		enabled = ctypes.c_bool(0)
		res = LibLoader.lib.FliCredThree_getHdrExtendedState_V2(context, ctypes.byref(enabled))
		return res, enabled.value

	#------------------------------------------------------------
	LibLoader.lib.FliCredThree_getLicenses_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_size_t]
	LibLoader.lib.FliCredThree_getLicenses_V2.restype = ctypes.c_bool
	def GetLicenses(self, context):
		res = LibLoader.lib.FliCredThree_getLicenses_V2(context, charBuffer, bufferSize)
		return res, charBuffer.value.decode('utf-8', 'ignore')

	#------------------------------------------------------------
	LibLoader.lib.FliCredThree_getMaxFpsUsb_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_double)]
	LibLoader.lib.FliCredThree_getMaxFpsUsb_V2.restype = ctypes.c_bool
	def GetMaxFpsUsb(self, context):
		maxFpsUsb = ctypes.c_double(0)
		res = LibLoader.lib.FliCredThree_getMaxFpsUsb_V2(context, ctypes.byref(maxFpsUsb))
		return res, maxFpsUsb.value

	#------------------------------------------------------------
	LibLoader.lib.FliCredThree_getMaxSyncDelay_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_double)]
	LibLoader.lib.FliCredThree_getMaxSyncDelay_V2.restype = ctypes.c_bool
	def GetMaxSyncDelay(self, context):
		maxSyncDelay = ctypes.c_double(0)
		res = LibLoader.lib.FliCredThree_getMaxSyncDelay_V2(context, ctypes.byref(maxSyncDelay))
		return res, maxSyncDelay.value

	#------------------------------------------------------------
	LibLoader.lib.FliCredThree_getMinSyncDelay_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_double)]
	LibLoader.lib.FliCredThree_getMinSyncDelay_V2.restype = ctypes.c_bool
	def GetMinSyncDelay(self, context):
		minSyncDelay = ctypes.c_double(0)
		res = LibLoader.lib.FliCredThree_getMinSyncDelay_V2(context, ctypes.byref(minSyncDelay))
		return res, minSyncDelay.value

	#------------------------------------------------------------
	LibLoader.lib.FliCredThree_getMaxTintItr_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_double)]
	LibLoader.lib.FliCredThree_getMaxTintItr_V2.restype = ctypes.c_bool
	def GetMaxTintItr(self, context):
		maxTintItr = ctypes.c_double(0)
		res = LibLoader.lib.FliCredThree_getMaxTintItr_V2(context, ctypes.byref(maxTintItr))
		return res, maxTintItr.value

	#------------------------------------------------------------
	LibLoader.lib.FliCredThree_getMinFps_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_double)]
	LibLoader.lib.FliCredThree_getMinFps_V2.restype = ctypes.c_bool
	def GetMinFps(self, context):
		minFps = ctypes.c_double(0)
		res = LibLoader.lib.FliCredThree_getMinFps_V2(context, ctypes.byref(minFps))
		return res, minFps.value

	#------------------------------------------------------------
	LibLoader.lib.FliCredThree_getNbFramesPerSwTrig_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_int)]
	LibLoader.lib.FliCredThree_getNbFramesPerSwTrig_V2.restype = ctypes.c_bool
	def GetNbFramesPerSwTrig(self, context):
		nbFrames = ctypes.c_int(0)
		res = LibLoader.lib.FliCredThree_getNbFramesPerSwTrig_V2(context, ctypes.byref(nbFrames))
		return res, nbFrames.value

	#------------------------------------------------------------
	LibLoader.lib.FliCredThree_getPreset_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_int)]
	LibLoader.lib.FliCredThree_getPreset_V2.restype = ctypes.c_bool
	def GetPreset(self, context):
		preset = ctypes.c_int(0)
		res = LibLoader.lib.FliCredThree_getPreset_V2(context, ctypes.byref(preset))
		return res, preset.value

	#------------------------------------------------------------
	LibLoader.lib.FliCredThree_getRemoteMaintenanceState_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_bool)]
	LibLoader.lib.FliCredThree_getRemoteMaintenanceState_V2.restype = ctypes.c_bool
	def GetRemoteMaintenanceState(self, context):
		enabled = ctypes.c_bool(0)
		res = LibLoader.lib.FliCredThree_getRemoteMaintenanceState_V2(context, ctypes.byref(enabled))
		return res, enabled.value

	#------------------------------------------------------------
	LibLoader.lib.FliCredThree_getStepSyncDelay_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_double)]
	LibLoader.lib.FliCredThree_getStepSyncDelay_V2.restype = ctypes.c_bool
	def GetStepSyncDelay(self, context):
		delay = ctypes.c_double(0)
		res = LibLoader.lib.FliCredThree_getStepSyncDelay_V2(context, ctypes.byref(delay))
		return res, delay.value

	#------------------------------------------------------------
	LibLoader.lib.FliCredThree_getSwSynchroState_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_bool)]
	LibLoader.lib.FliCredThree_getSwSynchroState_V2.restype = ctypes.c_bool
	def GetSwSynchroState(self, context):
		enabled = ctypes.c_bool(0)
		res = LibLoader.lib.FliCredThree_getSwSynchroState_V2(context, ctypes.byref(enabled))
		return res, enabled.value

	#------------------------------------------------------------
	LibLoader.lib.FliCredThree_getSyncDelay_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_double)]
	LibLoader.lib.FliCredThree_getSyncDelay_V2.restype = ctypes.c_bool
	def GetSyncDelay(self, context):
		delay = ctypes.c_double(0)
		res = LibLoader.lib.FliCredThree_getSyncDelay_V2(context, ctypes.byref(delay))
		return res, delay.value

	#------------------------------------------------------------
	LibLoader.lib.FliCredThree_getTcdsAdjustState_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_bool)]
	LibLoader.lib.FliCredThree_getTcdsAdjustState_V2.restype = ctypes.c_bool
	def GetTcdsAdjustState(self, context):
		enabled = ctypes.c_bool(0)
		res = LibLoader.lib.FliCredThree_getTcdsAdjustState_V2(context, ctypes.byref(enabled))
		return res, enabled.value

	#------------------------------------------------------------
	LibLoader.lib.FliCredThree_getTelnetState_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_bool)]
	LibLoader.lib.FliCredThree_getTelnetState_V2.restype = ctypes.c_bool
	def GetTelnetState(self, context):
		enabled = ctypes.c_bool(0)
		res = LibLoader.lib.FliCredThree_getTelnetState_V2(context, ctypes.byref(enabled))
		return res, enabled.value

	#------------------------------------------------------------
	LibLoader.lib.FliCredThree_getTintGranularityState_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_bool)]
	LibLoader.lib.FliCredThree_getTintGranularityState_V2.restype = ctypes.c_bool
	def GetTintGranularityState(self, context):
		enabled = ctypes.c_bool(0)
		res = LibLoader.lib.FliCredThree_getTintGranularityState_V2(context, ctypes.byref(enabled))
		return res, enabled.value

	#------------------------------------------------------------
	LibLoader.lib.FliCredThree_getTlsydel_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_int)]
	LibLoader.lib.FliCredThree_getTlsydel_V2.restype = ctypes.c_bool
	def GetTlsydel(self, context):
		val = ctypes.c_int(0)
		res = LibLoader.lib.FliCredThree_getTlsydel_V2(context, ctypes.byref(val))
		return res, val.value

	#------------------------------------------------------------
	LibLoader.lib.FliCredThree_getVrefAdjustState_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_bool)]
	LibLoader.lib.FliCredThree_getVrefAdjustState_V2.restype = ctypes.c_bool
	def GetVrefAdjustState(self, context):
		enabled = ctypes.c_bool(0)
		res = LibLoader.lib.FliCredThree_getVrefAdjustState_V2(context, ctypes.byref(enabled))
		return res, enabled.value

	#------------------------------------------------------------
	LibLoader.lib.FliCredThree_getAgcParam_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_double)]
	LibLoader.lib.FliCredThree_getAgcParam_V2.restype = ctypes.c_bool
	def GetAgcParam(self, context):
		value = ctypes.c_double(0)
		res = LibLoader.lib.FliCredThree_getAgcParam_V2(context, ctypes.byref(value))
		return res, value.value

	#------------------------------------------------------------
	LibLoader.lib.FliCredThree_getIpAlternateDns_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_size_t]
	LibLoader.lib.FliCredThree_getIpAlternateDns_V2.restype = ctypes.c_bool
	def GetIpAlternateDns(self, context):
		res = LibLoader.lib.FliCredThree_getIpAlternateDns_V2(context, charBuffer, bufferSize)
		return res, charBuffer.value.decode('utf-8', 'ignore')

	#------------------------------------------------------------
	LibLoader.lib.FliCredThree_getIpDns_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_size_t]
	LibLoader.lib.FliCredThree_getIpDns_V2.restype = ctypes.c_bool
	def GetIpDns(self, context):
		res = LibLoader.lib.FliCredThree_getIpDns_V2(context, charBuffer, bufferSize)
		return res, charBuffer.value.decode('utf-8', 'ignore')

	#------------------------------------------------------------
	LibLoader.lib.FliCredThree_getIpGateway_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_size_t]
	LibLoader.lib.FliCredThree_getIpGateway_V2.restype = ctypes.c_bool
	def GetIpGateway(self, context):
		res = LibLoader.lib.FliCredThree_getIpGateway_V2(context, charBuffer, bufferSize)
		return res, charBuffer.value.decode('utf-8', 'ignore')

	#------------------------------------------------------------
	LibLoader.lib.FliCredThree_getIpMode_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_size_t]
	LibLoader.lib.FliCredThree_getIpMode_V2.restype = ctypes.c_bool
	def GetIpMode(self, context):
		res = LibLoader.lib.FliCredThree_getIpMode_V2(context, charBuffer, bufferSize)
		return res, charBuffer.value.decode('utf-8', 'ignore')

	#------------------------------------------------------------
	LibLoader.lib.FliCredThree_getIpNetmask_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_size_t]
	LibLoader.lib.FliCredThree_getIpNetmask_V2.restype = ctypes.c_bool
	def GetIpNetmask(self, context):
		res = LibLoader.lib.FliCredThree_getIpNetmask_V2(context, charBuffer, bufferSize)
		return res, charBuffer.value.decode('utf-8', 'ignore')

	#------------------------------------------------------------
	LibLoader.lib.FliCredThree_getIpAddress_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_size_t]
	LibLoader.lib.FliCredThree_getIpAddress_V2.restype = ctypes.c_bool
	def GetIpAddress(self, context):
		res = LibLoader.lib.FliCredThree_getIpAddress_V2(context, charBuffer, bufferSize)
		return res, charBuffer.value.decode('utf-8', 'ignore')

	#------------------------------------------------------------
	LibLoader.lib.FliCredThree_getSnakeParam_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_int]
	LibLoader.lib.FliCredThree_getSnakeParam_V2.restype = ctypes.c_bool
	def GetSnakeParam(self, context, parameter, value):
		res = LibLoader.lib.FliCredThree_getSnakeParam_V2(context, parameter.encode(), value)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredThree_getUploadFirmwareConnectionInfo_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_size_t, ctypes.c_int]
	LibLoader.lib.FliCredThree_getUploadFirmwareConnectionInfo_V2.restype = ctypes.c_bool
	def GetUploadFirmwareConnectionInfo(self, context, port):
		res = LibLoader.lib.FliCredThree_getUploadFirmwareConnectionInfo_V2(context, charBuffer, bufferSize, port)
		return res, charBuffer.value.decode('utf-8', 'ignore')

	#------------------------------------------------------------
	LibLoader.lib.FliCredThree_getConversionGain_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_size_t]
	LibLoader.lib.FliCredThree_getConversionGain_V2.restype = ctypes.c_bool
	def GetConversionGain(self, context):
		res = LibLoader.lib.FliCredThree_getConversionGain_V2(context, charBuffer, bufferSize)
		return res, charBuffer.value.decode('utf-8', 'ignore')

	#------------------------------------------------------------
	LibLoader.lib.FliCredThree_getTintStep_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_double)]
	LibLoader.lib.FliCredThree_getTintStep_V2.restype = ctypes.c_bool
	def GetTintStep(self, context):
		step = ctypes.c_double(0)
		res = LibLoader.lib.FliCredThree_getTintStep_V2(context, ctypes.byref(step))
		return res, step.value

	#------------------------------------------------------------
	LibLoader.lib.FliCredThree_getImagePattern_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_size_t]
	LibLoader.lib.FliCredThree_getImagePattern_V2.restype = ctypes.c_bool
	def GetImagePattern(self, context):
		res = LibLoader.lib.FliCredThree_getImagePattern_V2(context, charBuffer, bufferSize)
		return res, charBuffer.value.decode('utf-8', 'ignore')

	#------------------------------------------------------------
	LibLoader.lib.FliCredThree_getDate_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_size_t]
	LibLoader.lib.FliCredThree_getDate_V2.restype = ctypes.c_bool
	def GetDate(self, context):
		res = LibLoader.lib.FliCredThree_getDate_V2(context, charBuffer, bufferSize)
		return res, charBuffer.value.decode('utf-8', 'ignore')

	#------------------------------------------------------------
	LibLoader.lib.FliCredThree_getUptime_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_size_t]
	LibLoader.lib.FliCredThree_getUptime_V2.restype = ctypes.c_bool
	def GetUptime(self, context):
		res = LibLoader.lib.FliCredThree_getUptime_V2(context, charBuffer, bufferSize)
		return res, charBuffer.value.decode('utf-8', 'ignore')

	#------------------------------------------------------------
	LibLoader.lib.FliCredThree_getAccumulatedUptime_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_size_t]
	LibLoader.lib.FliCredThree_getAccumulatedUptime_V2.restype = ctypes.c_bool
	def GetAccumulatedUptime(self, context):
		res = LibLoader.lib.FliCredThree_getAccumulatedUptime_V2(context, charBuffer, bufferSize)
		return res, charBuffer.value.decode('utf-8', 'ignore')

	#------------------------------------------------------------
	LibLoader.lib.FliCredThree_getTotalUptime_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_size_t]
	LibLoader.lib.FliCredThree_getTotalUptime_V2.restype = ctypes.c_bool
	def GetTotalUptime(self, context):
		res = LibLoader.lib.FliCredThree_getTotalUptime_V2(context, charBuffer, bufferSize)
		return res, charBuffer.value.decode('utf-8', 'ignore')

	#------------------------------------------------------------
	LibLoader.lib.FliCredThree_getRawImagesState_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_bool)]
	LibLoader.lib.FliCredThree_getRawImagesState_V2.restype = ctypes.c_bool
	def GetRawImagesState(self, context):
		enabled = ctypes.c_bool(0)
		res = LibLoader.lib.FliCredThree_getRawImagesState_V2(context, ctypes.byref(enabled))
		return res, enabled.value

	#------------------------------------------------------------
	LibLoader.lib.FliCredThree_getUnsignedPixelsState_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_bool)]
	LibLoader.lib.FliCredThree_getUnsignedPixelsState_V2.restype = ctypes.c_bool
	def GetUnsignedPixelsState(self, context):
		enabled = ctypes.c_bool(0)
		res = LibLoader.lib.FliCredThree_getUnsignedPixelsState_V2(context, ctypes.byref(enabled))
		return res, enabled.value

	#------------------------------------------------------------
	LibLoader.lib.FliCredThree_setTint_V2.argtypes = [ctypes.c_void_p, ctypes.c_double]
	LibLoader.lib.FliCredThree_setTint_V2.restype = ctypes.c_bool
	def SetTint(self, context, tint):
		res = LibLoader.lib.FliCredThree_setTint_V2(context, tint)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredThree_setConversionGain_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
	LibLoader.lib.FliCredThree_setConversionGain_V2.restype = ctypes.c_bool
	def SetConversionGain(self, context, gain):
		res = LibLoader.lib.FliCredThree_setConversionGain_V2(context, gain.encode())
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredThree_setAgcPriorityNone_V2.argtypes = [ctypes.c_void_p]
	LibLoader.lib.FliCredThree_setAgcPriorityNone_V2.restype = ctypes.c_bool
	def SetAgcPriorityNone(self, context):
		res = LibLoader.lib.FliCredThree_setAgcPriorityNone_V2(context)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredThree_setAgcPriorityOverExposed_V2.argtypes = [ctypes.c_void_p]
	LibLoader.lib.FliCredThree_setAgcPriorityOverExposed_V2.restype = ctypes.c_bool
	def SetAgcPriorityOverExposed(self, context):
		res = LibLoader.lib.FliCredThree_setAgcPriorityOverExposed_V2(context)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredThree_setAgcPriorityUnderExposed_V2.argtypes = [ctypes.c_void_p]
	LibLoader.lib.FliCredThree_setAgcPriorityUnderExposed_V2.restype = ctypes.c_bool
	def SetAgcPriorityUnderExposed(self, context):
		res = LibLoader.lib.FliCredThree_setAgcPriorityUnderExposed_V2(context)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredThree_setDarkOptimLevel_V2.argtypes = [ctypes.c_void_p, ctypes.c_int]
	LibLoader.lib.FliCredThree_setDarkOptimLevel_V2.restype = ctypes.c_bool
	def SetDarkOptimLevel(self, context, level):
		res = LibLoader.lib.FliCredThree_setDarkOptimLevel_V2(context, level)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredThree_setExtSynchroExposureInternal_V2.argtypes = [ctypes.c_void_p]
	LibLoader.lib.FliCredThree_setExtSynchroExposureInternal_V2.restype = ctypes.c_bool
	def SetExtSynchroExposureInternal(self, context):
		res = LibLoader.lib.FliCredThree_setExtSynchroExposureInternal_V2(context)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredThree_setExtSynchroExposureExternal_V2.argtypes = [ctypes.c_void_p]
	LibLoader.lib.FliCredThree_setExtSynchroExposureExternal_V2.restype = ctypes.c_bool
	def SetExtSynchroExposureExternal(self, context):
		res = LibLoader.lib.FliCredThree_setExtSynchroExposureExternal_V2(context)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredThree_setExtSynchroPolarityInverted_V2.argtypes = [ctypes.c_void_p]
	LibLoader.lib.FliCredThree_setExtSynchroPolarityInverted_V2.restype = ctypes.c_bool
	def SetExtSynchroPolarityInverted(self, context):
		res = LibLoader.lib.FliCredThree_setExtSynchroPolarityInverted_V2(context)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredThree_setExtSynchroPolarityStandard_V2.argtypes = [ctypes.c_void_p]
	LibLoader.lib.FliCredThree_setExtSynchroPolarityStandard_V2.restype = ctypes.c_bool
	def SetExtSynchroPolarityStandard(self, context):
		res = LibLoader.lib.FliCredThree_setExtSynchroPolarityStandard_V2(context)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredThree_setHdrCalibrationC1_V2.argtypes = [ctypes.c_void_p]
	LibLoader.lib.FliCredThree_setHdrCalibrationC1_V2.restype = ctypes.c_bool
	def SetHdrCalibrationC1(self, context):
		res = LibLoader.lib.FliCredThree_setHdrCalibrationC1_V2(context)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredThree_setHdrCalibrationC2_V2.argtypes = [ctypes.c_void_p]
	LibLoader.lib.FliCredThree_setHdrCalibrationC2_V2.restype = ctypes.c_bool
	def SetHdrCalibrationC2(self, context):
		res = LibLoader.lib.FliCredThree_setHdrCalibrationC2_V2(context)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredThree_setHdrCalibrationOff_V2.argtypes = [ctypes.c_void_p]
	LibLoader.lib.FliCredThree_setHdrCalibrationOff_V2.restype = ctypes.c_bool
	def SetHdrCalibrationOff(self, context):
		res = LibLoader.lib.FliCredThree_setHdrCalibrationOff_V2(context)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredThree_setNbFramesPerSwTrig_V2.argtypes = [ctypes.c_void_p, ctypes.c_int]
	LibLoader.lib.FliCredThree_setNbFramesPerSwTrig_V2.restype = ctypes.c_bool
	def SetNbFramesPerSwTrig(self, context, nbFrames):
		res = LibLoader.lib.FliCredThree_setNbFramesPerSwTrig_V2(context, nbFrames)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredThree_setSyncDelay_V2.argtypes = [ctypes.c_void_p, ctypes.c_int]
	LibLoader.lib.FliCredThree_setSyncDelay_V2.restype = ctypes.c_bool
	def SetSyncDelay(self, context, delay):
		res = LibLoader.lib.FliCredThree_setSyncDelay_V2(context, delay)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredThree_setTlsyDel_V2.argtypes = [ctypes.c_void_p, ctypes.c_int]
	LibLoader.lib.FliCredThree_setTlsyDel_V2.restype = ctypes.c_bool
	def SetTlsyDel(self, context, val):
		res = LibLoader.lib.FliCredThree_setTlsyDel_V2(context, val)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredThree_setVoltageVref_V2.argtypes = [ctypes.c_void_p, ctypes.c_double]
	LibLoader.lib.FliCredThree_setVoltageVref_V2.restype = ctypes.c_bool
	def SetVoltageVref(self, context, vref):
		res = LibLoader.lib.FliCredThree_setVoltageVref_V2(context, vref)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredThree_setAgcRoi_V2.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int]
	LibLoader.lib.FliCredThree_setAgcRoi_V2.restype = ctypes.c_bool
	def SetAgcRoi(self, context, col1, row1, col2, row2):
		res = LibLoader.lib.FliCredThree_setAgcRoi_V2(context, col1, row1, col2, row2)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredThree_setAgcParam_V2.argtypes = [ctypes.c_void_p, ctypes.c_double]
	LibLoader.lib.FliCredThree_setAgcParam_V2.restype = ctypes.c_bool
	def SetAgcParam(self, context, value):
		res = LibLoader.lib.FliCredThree_setAgcParam_V2(context, value)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredThree_setPreset_V2.argtypes = [ctypes.c_void_p]
	LibLoader.lib.FliCredThree_setPreset_V2.restype = ctypes.c_bool
	def SetPreset(self, context):
		res = LibLoader.lib.FliCredThree_setPreset_V2(context)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredThree_setPresetNumber_V2.argtypes = [ctypes.c_void_p, ctypes.c_int]
	LibLoader.lib.FliCredThree_setPresetNumber_V2.restype = ctypes.c_bool
	def SetPresetNumber(self, context, presetNumber):
		res = LibLoader.lib.FliCredThree_setPresetNumber_V2(context, presetNumber)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredThree_setSnakeParam_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_int]
	LibLoader.lib.FliCredThree_setSnakeParam_V2.restype = ctypes.c_bool
	def SetSnakeParam(self, context, parameter, value):
		res = LibLoader.lib.FliCredThree_setSnakeParam_V2(context, parameter.encode(), value)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredThree_setImagePatternRamp_V2.argtypes = [ctypes.c_void_p]
	LibLoader.lib.FliCredThree_setImagePatternRamp_V2.restype = ctypes.c_bool
	def SetImagePatternRamp(self, context):
		res = LibLoader.lib.FliCredThree_setImagePatternRamp_V2(context)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredThree_setImagePatternConstant_V2.argtypes = [ctypes.c_void_p, ctypes.c_int]
	LibLoader.lib.FliCredThree_setImagePatternConstant_V2.restype = ctypes.c_bool
	def SetImagePatternConstant(self, context, val):
		res = LibLoader.lib.FliCredThree_setImagePatternConstant_V2(context, val)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredThree_setImagePatternOff_V2.argtypes = [ctypes.c_void_p]
	LibLoader.lib.FliCredThree_setImagePatternOff_V2.restype = ctypes.c_bool
	def SetImagePatternOff(self, context):
		res = LibLoader.lib.FliCredThree_setImagePatternOff_V2(context)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredThree_enableAntiBlooming_V2.argtypes = [ctypes.c_void_p, ctypes.c_bool]
	LibLoader.lib.FliCredThree_enableAntiBlooming_V2.restype = ctypes.c_bool
	def EnableAntiBlooming(self, context, enabled):
		res = LibLoader.lib.FliCredThree_enableAntiBlooming_V2(context, enabled)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredThree_enableBadPixel_V2.argtypes = [ctypes.c_void_p, ctypes.c_bool]
	LibLoader.lib.FliCredThree_enableBadPixel_V2.restype = ctypes.c_bool
	def EnableBadPixel(self, context, enabled):
		res = LibLoader.lib.FliCredThree_enableBadPixel_V2(context, enabled)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredThree_enableAdaptbias_V2.argtypes = [ctypes.c_void_p, ctypes.c_bool]
	LibLoader.lib.FliCredThree_enableAdaptbias_V2.restype = ctypes.c_bool
	def EnableAdaptbias(self, context, enable):
		res = LibLoader.lib.FliCredThree_enableAdaptbias_V2(context, enable)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredThree_enableAgc_V2.argtypes = [ctypes.c_void_p, ctypes.c_bool]
	LibLoader.lib.FliCredThree_enableAgc_V2.restype = ctypes.c_bool
	def EnableAgc(self, context, enable):
		res = LibLoader.lib.FliCredThree_enableAgc_V2(context, enable)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredThree_enableHdrExtended_V2.argtypes = [ctypes.c_void_p, ctypes.c_bool]
	LibLoader.lib.FliCredThree_enableHdrExtended_V2.restype = ctypes.c_bool
	def EnableHdrExtended(self, context, enable):
		res = LibLoader.lib.FliCredThree_enableHdrExtended_V2(context, enable)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredThree_enableHdr_V2.argtypes = [ctypes.c_void_p, ctypes.c_bool]
	LibLoader.lib.FliCredThree_enableHdr_V2.restype = ctypes.c_bool
	def EnableHdr(self, context, enable):
		res = LibLoader.lib.FliCredThree_enableHdr_V2(context, enable)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredThree_enableRemoteMaintenance_V2.argtypes = [ctypes.c_void_p, ctypes.c_bool]
	LibLoader.lib.FliCredThree_enableRemoteMaintenance_V2.restype = ctypes.c_bool
	def EnableRemoteMaintenance(self, context, enable):
		res = LibLoader.lib.FliCredThree_enableRemoteMaintenance_V2(context, enable)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredThree_enableSwSynchro_V2.argtypes = [ctypes.c_void_p, ctypes.c_bool]
	LibLoader.lib.FliCredThree_enableSwSynchro_V2.restype = ctypes.c_bool
	def EnableSwSynchro(self, context, enable):
		res = LibLoader.lib.FliCredThree_enableSwSynchro_V2(context, enable)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredThree_enableTcdsAdjust_V2.argtypes = [ctypes.c_void_p, ctypes.c_bool]
	LibLoader.lib.FliCredThree_enableTcdsAdjust_V2.restype = ctypes.c_bool
	def EnableTcdsAdjust(self, context, enable):
		res = LibLoader.lib.FliCredThree_enableTcdsAdjust_V2(context, enable)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredThree_enableTintGranularity_V2.argtypes = [ctypes.c_void_p, ctypes.c_bool]
	LibLoader.lib.FliCredThree_enableTintGranularity_V2.restype = ctypes.c_bool
	def EnableTintGranularity(self, context, enable):
		res = LibLoader.lib.FliCredThree_enableTintGranularity_V2(context, enable)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredThree_enableVrefAdjust_V2.argtypes = [ctypes.c_void_p, ctypes.c_bool]
	LibLoader.lib.FliCredThree_enableVrefAdjust_V2.restype = ctypes.c_bool
	def EnableVrefAdjust(self, context, enable):
		res = LibLoader.lib.FliCredThree_enableVrefAdjust_V2(context, enable)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredThree_enableRawImages_V2.argtypes = [ctypes.c_void_p, ctypes.c_bool]
	LibLoader.lib.FliCredThree_enableRawImages_V2.restype = ctypes.c_bool
	def EnableRawImages(self, context, enable):
		res = LibLoader.lib.FliCredThree_enableRawImages_V2(context, enable)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredThree_enableUnsignedPixels_V2.argtypes = [ctypes.c_void_p, ctypes.c_bool]
	LibLoader.lib.FliCredThree_enableUnsignedPixels_V2.restype = ctypes.c_bool
	def EnableUnsignedPixels(self, context, enable):
		res = LibLoader.lib.FliCredThree_enableUnsignedPixels_V2(context, enable)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredThree_reboot_V2.argtypes = [ctypes.c_void_p]
	LibLoader.lib.FliCredThree_reboot_V2.restype = ctypes.c_bool
	def Reboot(self, context):
		res = LibLoader.lib.FliCredThree_reboot_V2(context)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredThree_buildFlatHdrC1_V2.argtypes = [ctypes.c_void_p]
	LibLoader.lib.FliCredThree_buildFlatHdrC1_V2.restype = ctypes.c_bool
	def BuildFlatHdrC1(self, context):
		res = LibLoader.lib.FliCredThree_buildFlatHdrC1_V2(context)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredThree_buildFlatHdrC2_V2.argtypes = [ctypes.c_void_p]
	LibLoader.lib.FliCredThree_buildFlatHdrC2_V2.restype = ctypes.c_bool
	def BuildFlatHdrC2(self, context):
		res = LibLoader.lib.FliCredThree_buildFlatHdrC2_V2(context)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredThree_sendBiasHdrC1FromUrl_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
	LibLoader.lib.FliCredThree_sendBiasHdrC1FromUrl_V2.restype = ctypes.c_bool
	def SendBiasHdrC1FromUrl(self, context, url):
		res = LibLoader.lib.FliCredThree_sendBiasHdrC1FromUrl_V2(context, url.encode())
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredThree_sendBiasHdrC2FromUrl_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
	LibLoader.lib.FliCredThree_sendBiasHdrC2FromUrl_V2.restype = ctypes.c_bool
	def SendBiasHdrC2FromUrl(self, context, url):
		res = LibLoader.lib.FliCredThree_sendBiasHdrC2FromUrl_V2(context, url.encode())
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredThree_sendFlatHdrC1FromUrl_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
	LibLoader.lib.FliCredThree_sendFlatHdrC1FromUrl_V2.restype = ctypes.c_bool
	def SendFlatHdrC1FromUrl(self, context, url):
		res = LibLoader.lib.FliCredThree_sendFlatHdrC1FromUrl_V2(context, url.encode())
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredThree_sendFlatHdrC2FromUrl_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
	LibLoader.lib.FliCredThree_sendFlatHdrC2FromUrl_V2.restype = ctypes.c_bool
	def SendFlatHdrC2FromUrl(self, context, url):
		res = LibLoader.lib.FliCredThree_sendFlatHdrC2FromUrl_V2(context, url.encode())
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredThree_sendBiasHdrC1File_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
	LibLoader.lib.FliCredThree_sendBiasHdrC1File_V2.restype = ctypes.c_bool
	def SendBiasHdrC1File(self, context, filePath):
		res = LibLoader.lib.FliCredThree_sendBiasHdrC1File_V2(context, filePath.encode())
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredThree_sendBiasHdrC2File_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
	LibLoader.lib.FliCredThree_sendBiasHdrC2File_V2.restype = ctypes.c_bool
	def SendBiasHdrC2File(self, context, filePath):
		res = LibLoader.lib.FliCredThree_sendBiasHdrC2File_V2(context, filePath.encode())
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredThree_sendFlatHdrC1File_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
	LibLoader.lib.FliCredThree_sendFlatHdrC1File_V2.restype = ctypes.c_bool
	def SendFlatHdrC1File(self, context, filePath):
		res = LibLoader.lib.FliCredThree_sendFlatHdrC1File_V2(context, filePath.encode())
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredThree_sendFlatHdrC2File_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
	LibLoader.lib.FliCredThree_sendFlatHdrC2File_V2.restype = ctypes.c_bool
	def SendFlatHdrC2File(self, context, filePath):
		res = LibLoader.lib.FliCredThree_sendFlatHdrC2File_V2(context, filePath.encode())
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredThree_xSendBiasFile_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
	LibLoader.lib.FliCredThree_xSendBiasFile_V2.restype = ctypes.c_bool
	def XSendBiasFile(self, context, filePath):
		res = LibLoader.lib.FliCredThree_xSendBiasFile_V2(context, filePath.encode())
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredThree_xSendBiasHdrC1File_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
	LibLoader.lib.FliCredThree_xSendBiasHdrC1File_V2.restype = ctypes.c_bool
	def XSendBiasHdrC1File(self, context, filePath):
		res = LibLoader.lib.FliCredThree_xSendBiasHdrC1File_V2(context, filePath.encode())
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredThree_xSendBiasHdrC2File_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
	LibLoader.lib.FliCredThree_xSendBiasHdrC2File_V2.restype = ctypes.c_bool
	def XSendBiasHdrC2File(self, context, filePath):
		res = LibLoader.lib.FliCredThree_xSendBiasHdrC2File_V2(context, filePath.encode())
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredThree_xSendFlatFile_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
	LibLoader.lib.FliCredThree_xSendFlatFile_V2.restype = ctypes.c_bool
	def XSendFlatFile(self, context, filePath):
		res = LibLoader.lib.FliCredThree_xSendFlatFile_V2(context, filePath.encode())
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredThree_xSendFlatHdrC1File_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
	LibLoader.lib.FliCredThree_xSendFlatHdrC1File_V2.restype = ctypes.c_bool
	def XSendFlatHdrC1File(self, context, filePath):
		res = LibLoader.lib.FliCredThree_xSendFlatHdrC1File_V2(context, filePath.encode())
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredThree_xSendFlatHdrC2File_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
	LibLoader.lib.FliCredThree_xSendFlatHdrC2File_V2.restype = ctypes.c_bool
	def XSendFlatHdrC2File(self, context, filePath):
		res = LibLoader.lib.FliCredThree_xSendFlatHdrC2File_V2(context, filePath.encode())
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredThree_sendLicenseFile_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_char_p]
	LibLoader.lib.FliCredThree_sendLicenseFile_V2.restype = ctypes.c_bool
	def SendLicenseFile(self, context, filePath, fileName):
		res = LibLoader.lib.FliCredThree_sendLicenseFile_V2(context, filePath.encode(), fileName.encode())
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredThree_deleteLicense_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
	LibLoader.lib.FliCredThree_deleteLicense_V2.restype = ctypes.c_bool
	def DeleteLicense(self, context, licenseName):
		res = LibLoader.lib.FliCredThree_deleteLicense_V2(context, licenseName.encode())
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredThree_disableLicense_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
	LibLoader.lib.FliCredThree_disableLicense_V2.restype = ctypes.c_bool
	def DisableLicense(self, context, licenseName):
		res = LibLoader.lib.FliCredThree_disableLicense_V2(context, licenseName.encode())
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredThree_enableLicense_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
	LibLoader.lib.FliCredThree_enableLicense_V2.restype = ctypes.c_bool
	def EnableLicense(self, context, licenseName):
		res = LibLoader.lib.FliCredThree_enableLicense_V2(context, licenseName.encode())
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredThree_softwareTrig_V2.argtypes = [ctypes.c_void_p]
	LibLoader.lib.FliCredThree_softwareTrig_V2.restype = ctypes.c_bool
	def SoftwareTrig(self, context):
		res = LibLoader.lib.FliCredThree_softwareTrig_V2(context)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredThree_startHttpServer_V2.argtypes = [ctypes.c_void_p]
	LibLoader.lib.FliCredThree_startHttpServer_V2.restype = ctypes.c_bool
	def StartHttpServer(self, context):
		res = LibLoader.lib.FliCredThree_startHttpServer_V2(context)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredThree_stopHttpServer_V2.argtypes = [ctypes.c_void_p]
	LibLoader.lib.FliCredThree_stopHttpServer_V2.restype = ctypes.c_bool
	def StopHttpServer(self, context):
		res = LibLoader.lib.FliCredThree_stopHttpServer_V2(context)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredThree_startEthernetGrabber_V2.argtypes = [ctypes.c_void_p]
	LibLoader.lib.FliCredThree_startEthernetGrabber_V2.restype = ctypes.c_bool
	def StartEthernetGrabber(self, context):
		res = LibLoader.lib.FliCredThree_startEthernetGrabber_V2(context)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredThree_stopEthernetGrabber_V2.argtypes = [ctypes.c_void_p]
	LibLoader.lib.FliCredThree_stopEthernetGrabber_V2.restype = ctypes.c_bool
	def StopEthernetGrabber(self, context):
		res = LibLoader.lib.FliCredThree_stopEthernetGrabber_V2(context)
		return res
	""" 
	######
	OWN  WRAPPER FUNCTIONS
	######
	"""
	#------------------------------------------------------------
	# Unfortunately, NUC for C-RED3 does not exist in SDK Python Wrapper???
	# LibLoader.lib.FliCredThree_buildBiasNuc.argtypes = [ctypes.c_void_p]
	# LibLoader.lib.FliCredThree_buildBiasNuc.restype = ctypes.c_bool
	# def BuildBiasNUC(self, context):
	# 	res = LibLoader.lib.FliCredThree_buildBiasNuc(context)
	# 	return res

	
