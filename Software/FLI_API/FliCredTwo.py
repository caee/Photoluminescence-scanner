import LibLoader
import ctypes
import numpy as np

bufferSize = ctypes.c_size_t(1000)
charBuffer = ctypes.create_string_buffer(bufferSize.value)

class FliCredTwo:
	#------------------------------------------------------------
	LibLoader.lib.FliCredTwo_getAllTemp_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double)]
	LibLoader.lib.FliCredTwo_getAllTemp_V2.restype = ctypes.c_bool
	def GetAllTemp(self, context):
		mb = ctypes.c_double(0)
		fe = ctypes.c_double(0)
		pw = ctypes.c_double(0)
		sensor = ctypes.c_double(0)
		peltier = ctypes.c_double(0)
		heatsink = ctypes.c_double(0)
		res = LibLoader.lib.FliCredTwo_getAllTemp_V2(context, ctypes.byref(mb), ctypes.byref(fe), ctypes.byref(pw), ctypes.byref(sensor), ctypes.byref(peltier), ctypes.byref(heatsink))
		return res, mb.value, fe.value, pw.value, sensor.value, peltier.value, heatsink.value

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwo_getTint_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_double)]
	LibLoader.lib.FliCredTwo_getTint_V2.restype = ctypes.c_bool
	def GetTint(self, context):
		tint = ctypes.c_double(0)
		res = LibLoader.lib.FliCredTwo_getTint_V2(context, ctypes.byref(tint))
		return res, tint.value

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwo_getTintMax_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_double)]
	LibLoader.lib.FliCredTwo_getTintMax_V2.restype = ctypes.c_bool
	def GetTintMax(self, context):
		tintMax = ctypes.c_double(0)
		res = LibLoader.lib.FliCredTwo_getTintMax_V2(context, ctypes.byref(tintMax))
		return res, tintMax.value

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwo_getAntiBloomingState_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_bool)]
	LibLoader.lib.FliCredTwo_getAntiBloomingState_V2.restype = ctypes.c_bool
	def GetAntiBloomingState(self, context):
		enabled = ctypes.c_bool(0)
		res = LibLoader.lib.FliCredTwo_getAntiBloomingState_V2(context, ctypes.byref(enabled))
		return res, enabled.value

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwo_getBadPixelState_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_bool)]
	LibLoader.lib.FliCredTwo_getBadPixelState_V2.restype = ctypes.c_bool
	def GetBadPixelState(self, context):
		enabled = ctypes.c_bool(0)
		res = LibLoader.lib.FliCredTwo_getBadPixelState_V2(context, ctypes.byref(enabled))
		return res, enabled.value

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwo_getTempSnakeSetPoint_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_double)]
	LibLoader.lib.FliCredTwo_getTempSnakeSetPoint_V2.restype = ctypes.c_bool
	def GetTempSnakeSetPoint(self, context):
		temp = ctypes.c_double(0)
		res = LibLoader.lib.FliCredTwo_getTempSnakeSetPoint_V2(context, ctypes.byref(temp))
		return res, temp.value

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwo_getNbReadWoReset_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_int)]
	LibLoader.lib.FliCredTwo_getNbReadWoReset_V2.restype = ctypes.c_bool
	def GetNbReadWoReset(self, context):
		nbread = ctypes.c_int(0)
		res = LibLoader.lib.FliCredTwo_getNbReadWoReset_V2(context, ctypes.byref(nbread))
		return res, nbread.value

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwo_getRawImagesState_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_bool)]
	LibLoader.lib.FliCredTwo_getRawImagesState_V2.restype = ctypes.c_bool
	def GetRawImagesState(self, context):
		enabled = ctypes.c_bool(0)
		res = LibLoader.lib.FliCredTwo_getRawImagesState_V2(context, ctypes.byref(enabled))
		return res, enabled.value

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwo_getTempFrontEnd_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_double)]
	LibLoader.lib.FliCredTwo_getTempFrontEnd_V2.restype = ctypes.c_bool
	def GetTempFrontEnd(self, context):
		temp = ctypes.c_double(0)
		res = LibLoader.lib.FliCredTwo_getTempFrontEnd_V2(context, ctypes.byref(temp))
		return res, temp.value

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwo_getTempMotherBoard_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_double)]
	LibLoader.lib.FliCredTwo_getTempMotherBoard_V2.restype = ctypes.c_bool
	def GetTempMotherBoard(self, context):
		temp = ctypes.c_double(0)
		res = LibLoader.lib.FliCredTwo_getTempMotherBoard_V2(context, ctypes.byref(temp))
		return res, temp.value

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwo_getTempPowerBoard_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_double)]
	LibLoader.lib.FliCredTwo_getTempPowerBoard_V2.restype = ctypes.c_bool
	def GetTempPowerBoard(self, context):
		temp = ctypes.c_double(0)
		res = LibLoader.lib.FliCredTwo_getTempPowerBoard_V2(context, ctypes.byref(temp))
		return res, temp.value

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwo_getTempHeatSink_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_double)]
	LibLoader.lib.FliCredTwo_getTempHeatSink_V2.restype = ctypes.c_bool
	def GetTempHeatSink(self, context):
		temp = ctypes.c_double(0)
		res = LibLoader.lib.FliCredTwo_getTempHeatSink_V2(context, ctypes.byref(temp))
		return res, temp.value

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwo_getTempPeltier_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_double)]
	LibLoader.lib.FliCredTwo_getTempPeltier_V2.restype = ctypes.c_bool
	def GetTempPeltier(self, context):
		temp = ctypes.c_double(0)
		res = LibLoader.lib.FliCredTwo_getTempPeltier_V2(context, ctypes.byref(temp))
		return res, temp.value

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwo_getTempSnake_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_double)]
	LibLoader.lib.FliCredTwo_getTempSnake_V2.restype = ctypes.c_bool
	def GetTempSnake(self, context):
		temp = ctypes.c_double(0)
		res = LibLoader.lib.FliCredTwo_getTempSnake_V2(context, ctypes.byref(temp))
		return res, temp.value

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwo_getTintRange_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double)]
	LibLoader.lib.FliCredTwo_getTintRange_V2.restype = ctypes.c_bool
	def GetTintRange(self, context):
		tintMin = ctypes.c_double(0)
		tintMax = ctypes.c_double(0)
		res = LibLoader.lib.FliCredTwo_getTintRange_V2(context, ctypes.byref(tintMin), ctypes.byref(tintMax))
		return res, tintMin.value, tintMax.value

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwo_getDarkOptimLevel_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_int)]
	LibLoader.lib.FliCredTwo_getDarkOptimLevel_V2.restype = ctypes.c_bool
	def GetDarkOptimLevel(self, context):
		level = ctypes.c_int(0)
		res = LibLoader.lib.FliCredTwo_getDarkOptimLevel_V2(context, ctypes.byref(level))
		return res, level.value

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwo_getFanMode_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_size_t]
	LibLoader.lib.FliCredTwo_getFanMode_V2.restype = ctypes.c_bool
	def GetFanMode(self, context):
		res = LibLoader.lib.FliCredTwo_getFanMode_V2(context, charBuffer, bufferSize)
		return res, charBuffer.value.decode('utf-8', 'ignore')

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwo_getExtSynchroExposure_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_size_t]
	LibLoader.lib.FliCredTwo_getExtSynchroExposure_V2.restype = ctypes.c_bool
	def GetExtSynchroExposure(self, context):
		res = LibLoader.lib.FliCredTwo_getExtSynchroExposure_V2(context, charBuffer, bufferSize)
		return res, charBuffer.value.decode('utf-8', 'ignore')

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwo_getExtSynchroPolarity_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_size_t]
	LibLoader.lib.FliCredTwo_getExtSynchroPolarity_V2.restype = ctypes.c_bool
	def GetExtSynchroPolarity(self, context):
		res = LibLoader.lib.FliCredTwo_getExtSynchroPolarity_V2(context, charBuffer, bufferSize)
		return res, charBuffer.value.decode('utf-8', 'ignore')

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwo_getFanSpeed_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_int)]
	LibLoader.lib.FliCredTwo_getFanSpeed_V2.restype = ctypes.c_bool
	def GetFanSpeed(self, context):
		speed = ctypes.c_int(0)
		res = LibLoader.lib.FliCredTwo_getFanSpeed_V2(context, ctypes.byref(speed))
		return res, speed.value

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwo_getHdrState_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_bool)]
	LibLoader.lib.FliCredTwo_getHdrState_V2.restype = ctypes.c_bool
	def GetHdrState(self, context):
		enabled = ctypes.c_bool(0)
		res = LibLoader.lib.FliCredTwo_getHdrState_V2(context, ctypes.byref(enabled))
		return res, enabled.value

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwo_getHdrCalibrationMode_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_size_t]
	LibLoader.lib.FliCredTwo_getHdrCalibrationMode_V2.restype = ctypes.c_bool
	def GetHdrCalibrationMode(self, context):
		res = LibLoader.lib.FliCredTwo_getHdrCalibrationMode_V2(context, charBuffer, bufferSize)
		return res, charBuffer.value.decode('utf-8', 'ignore')

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwo_getHdrExtendedState_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_bool)]
	LibLoader.lib.FliCredTwo_getHdrExtendedState_V2.restype = ctypes.c_bool
	def GetHdrExtendedState(self, context):
		enabled = ctypes.c_bool(0)
		res = LibLoader.lib.FliCredTwo_getHdrExtendedState_V2(context, ctypes.byref(enabled))
		return res, enabled.value

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwo_getLicenses_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_size_t]
	LibLoader.lib.FliCredTwo_getLicenses_V2.restype = ctypes.c_bool
	def GetLicenses(self, context):
		res = LibLoader.lib.FliCredTwo_getLicenses_V2(context, charBuffer, bufferSize)
		return res, charBuffer.value.decode('utf-8', 'ignore')

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwo_getMaxFpsUsb_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_double)]
	LibLoader.lib.FliCredTwo_getMaxFpsUsb_V2.restype = ctypes.c_bool
	def GetMaxFpsUsb(self, context):
		maxFpsUsb = ctypes.c_double(0)
		res = LibLoader.lib.FliCredTwo_getMaxFpsUsb_V2(context, ctypes.byref(maxFpsUsb))
		return res, maxFpsUsb.value

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwo_getMaxSyncDelay_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_double)]
	LibLoader.lib.FliCredTwo_getMaxSyncDelay_V2.restype = ctypes.c_bool
	def GetMaxSyncDelay(self, context):
		maxSyncDelay = ctypes.c_double(0)
		res = LibLoader.lib.FliCredTwo_getMaxSyncDelay_V2(context, ctypes.byref(maxSyncDelay))
		return res, maxSyncDelay.value

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwo_getMinSyncDelay_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_double)]
	LibLoader.lib.FliCredTwo_getMinSyncDelay_V2.restype = ctypes.c_bool
	def GetMinSyncDelay(self, context):
		minSyncDelay = ctypes.c_double(0)
		res = LibLoader.lib.FliCredTwo_getMinSyncDelay_V2(context, ctypes.byref(minSyncDelay))
		return res, minSyncDelay.value

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwo_getMaxTintItr_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_double)]
	LibLoader.lib.FliCredTwo_getMaxTintItr_V2.restype = ctypes.c_bool
	def GetMaxTintItr(self, context):
		maxTintItr = ctypes.c_double(0)
		res = LibLoader.lib.FliCredTwo_getMaxTintItr_V2(context, ctypes.byref(maxTintItr))
		return res, maxTintItr.value

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwo_getVoltageVref_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_double)]
	LibLoader.lib.FliCredTwo_getVoltageVref_V2.restype = ctypes.c_bool
	def GetVoltageVref(self, context):
		vref = ctypes.c_double(0)
		res = LibLoader.lib.FliCredTwo_getVoltageVref_V2(context, ctypes.byref(vref))
		return res, vref.value

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwo_getMinFps_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_double)]
	LibLoader.lib.FliCredTwo_getMinFps_V2.restype = ctypes.c_bool
	def GetMinFps(self, context):
		minFps = ctypes.c_double(0)
		res = LibLoader.lib.FliCredTwo_getMinFps_V2(context, ctypes.byref(minFps))
		return res, minFps.value

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwo_getNbFramesPerSwTrig_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_int)]
	LibLoader.lib.FliCredTwo_getNbFramesPerSwTrig_V2.restype = ctypes.c_bool
	def GetNbFramesPerSwTrig(self, context):
		nbFrames = ctypes.c_int(0)
		res = LibLoader.lib.FliCredTwo_getNbFramesPerSwTrig_V2(context, ctypes.byref(nbFrames))
		return res, nbFrames.value

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwo_getTlsydel_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_int)]
	LibLoader.lib.FliCredTwo_getTlsydel_V2.restype = ctypes.c_bool
	def GetTlsydel(self, context):
		val = ctypes.c_int(0)
		res = LibLoader.lib.FliCredTwo_getTlsydel_V2(context, ctypes.byref(val))
		return res, val.value

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwo_getPreset_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_int)]
	LibLoader.lib.FliCredTwo_getPreset_V2.restype = ctypes.c_bool
	def GetPreset(self, context):
		preset = ctypes.c_int(0)
		res = LibLoader.lib.FliCredTwo_getPreset_V2(context, ctypes.byref(preset))
		return res, preset.value

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwo_getRemoteMaintenanceState_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_bool)]
	LibLoader.lib.FliCredTwo_getRemoteMaintenanceState_V2.restype = ctypes.c_bool
	def GetRemoteMaintenanceState(self, context):
		enabled = ctypes.c_bool(0)
		res = LibLoader.lib.FliCredTwo_getRemoteMaintenanceState_V2(context, ctypes.byref(enabled))
		return res, enabled.value

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwo_getSwSynchroState_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_bool)]
	LibLoader.lib.FliCredTwo_getSwSynchroState_V2.restype = ctypes.c_bool
	def GetSwSynchroState(self, context):
		enabled = ctypes.c_bool(0)
		res = LibLoader.lib.FliCredTwo_getSwSynchroState_V2(context, ctypes.byref(enabled))
		return res, enabled.value

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwo_getTcdsAdjustState_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_bool)]
	LibLoader.lib.FliCredTwo_getTcdsAdjustState_V2.restype = ctypes.c_bool
	def GetTcdsAdjustState(self, context):
		enabled = ctypes.c_bool(0)
		res = LibLoader.lib.FliCredTwo_getTcdsAdjustState_V2(context, ctypes.byref(enabled))
		return res, enabled.value

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwo_getTelnetState_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_bool)]
	LibLoader.lib.FliCredTwo_getTelnetState_V2.restype = ctypes.c_bool
	def GetTelnetState(self, context):
		enabled = ctypes.c_bool(0)
		res = LibLoader.lib.FliCredTwo_getTelnetState_V2(context, ctypes.byref(enabled))
		return res, enabled.value

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwo_getTintGranularityState_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_bool)]
	LibLoader.lib.FliCredTwo_getTintGranularityState_V2.restype = ctypes.c_bool
	def GetTintGranularityState(self, context):
		enabled = ctypes.c_bool(0)
		res = LibLoader.lib.FliCredTwo_getTintGranularityState_V2(context, ctypes.byref(enabled))
		return res, enabled.value

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwo_getVrefAdjustState_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_bool)]
	LibLoader.lib.FliCredTwo_getVrefAdjustState_V2.restype = ctypes.c_bool
	def GetVrefAdjustState(self, context):
		enabled = ctypes.c_bool(0)
		res = LibLoader.lib.FliCredTwo_getVrefAdjustState_V2(context, ctypes.byref(enabled))
		return res, enabled.value

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwo_getStepSyncDelay_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_double)]
	LibLoader.lib.FliCredTwo_getStepSyncDelay_V2.restype = ctypes.c_bool
	def GetStepSyncDelay(self, context):
		delay = ctypes.c_double(0)
		res = LibLoader.lib.FliCredTwo_getStepSyncDelay_V2(context, ctypes.byref(delay))
		return res, delay.value

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwo_getSyncDelay_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_double)]
	LibLoader.lib.FliCredTwo_getSyncDelay_V2.restype = ctypes.c_bool
	def GetSyncDelay(self, context):
		delay = ctypes.c_double(0)
		res = LibLoader.lib.FliCredTwo_getSyncDelay_V2(context, ctypes.byref(delay))
		return res, delay.value

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwo_getSynchronization_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_size_t]
	LibLoader.lib.FliCredTwo_getSynchronization_V2.restype = ctypes.c_bool
	def GetSynchronization(self, context):
		res = LibLoader.lib.FliCredTwo_getSynchronization_V2(context, charBuffer, bufferSize)
		return res, charBuffer.value.decode('utf-8', 'ignore')

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwo_getIpAlternateDns_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_size_t]
	LibLoader.lib.FliCredTwo_getIpAlternateDns_V2.restype = ctypes.c_bool
	def GetIpAlternateDns(self, context):
		res = LibLoader.lib.FliCredTwo_getIpAlternateDns_V2(context, charBuffer, bufferSize)
		return res, charBuffer.value.decode('utf-8', 'ignore')

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwo_getIpDns_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_size_t]
	LibLoader.lib.FliCredTwo_getIpDns_V2.restype = ctypes.c_bool
	def GetIpDns(self, context):
		res = LibLoader.lib.FliCredTwo_getIpDns_V2(context, charBuffer, bufferSize)
		return res, charBuffer.value.decode('utf-8', 'ignore')

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwo_getIpGateway_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_size_t]
	LibLoader.lib.FliCredTwo_getIpGateway_V2.restype = ctypes.c_bool
	def GetIpGateway(self, context):
		res = LibLoader.lib.FliCredTwo_getIpGateway_V2(context, charBuffer, bufferSize)
		return res, charBuffer.value.decode('utf-8', 'ignore')

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwo_getIpMode_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_size_t]
	LibLoader.lib.FliCredTwo_getIpMode_V2.restype = ctypes.c_bool
	def GetIpMode(self, context):
		res = LibLoader.lib.FliCredTwo_getIpMode_V2(context, charBuffer, bufferSize)
		return res, charBuffer.value.decode('utf-8', 'ignore')

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwo_getIpNetmask_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_size_t]
	LibLoader.lib.FliCredTwo_getIpNetmask_V2.restype = ctypes.c_bool
	def GetIpNetmask(self, context):
		res = LibLoader.lib.FliCredTwo_getIpNetmask_V2(context, charBuffer, bufferSize)
		return res, charBuffer.value.decode('utf-8', 'ignore')

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwo_getIpAddress_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_size_t]
	LibLoader.lib.FliCredTwo_getIpAddress_V2.restype = ctypes.c_bool
	def GetIpAddress(self, context):
		res = LibLoader.lib.FliCredTwo_getIpAddress_V2(context, charBuffer, bufferSize)
		return res, charBuffer.value.decode('utf-8', 'ignore')

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwo_getSnakeParam_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_int]
	LibLoader.lib.FliCredTwo_getSnakeParam_V2.restype = ctypes.c_bool
	def GetSnakeParam(self, context, parameter, value):
		res = LibLoader.lib.FliCredTwo_getSnakeParam_V2(context, parameter.encode(), value)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwo_getPowers_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double), ctypes.c_int, ctypes.c_int, ctypes.c_int]
	LibLoader.lib.FliCredTwo_getPowers_V2.restype = ctypes.c_bool
	def GetPowers(self, context, intPeltierCurrent, intPeltierVoltage, intPeltierPower):
		extPeltierCurrent = ctypes.c_double(0)
		extPeltierVoltage = ctypes.c_double(0)
		extPeltierPower = ctypes.c_double(0)
		intPeltierCurrent = ctypes.c_double(0)
		intPeltierVoltage = ctypes.c_double(0)
		intPeltierPower = ctypes.c_double(0)
		res = LibLoader.lib.FliCredTwo_getPowers_V2(context, ctypes.byref(extPeltierCurrent), ctypes.byref(extPeltierVoltage), ctypes.byref(extPeltierPower), ctypes.byref(intPeltierCurrent), ctypes.byref(intPeltierVoltage), ctypes.byref(intPeltierPower))
		return res, extPeltierCurrent.value, extPeltierVoltage.value, extPeltierPower.value, intPeltierCurrent.value, intPeltierVoltage.value, intPeltierPower.value

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwo_getPowerExternalPeltier_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double)]
	LibLoader.lib.FliCredTwo_getPowerExternalPeltier_V2.restype = ctypes.c_bool
	def GetPowerExternalPeltier(self, context):
		current = ctypes.c_double(0)
		voltage = ctypes.c_double(0)
		power = ctypes.c_double(0)
		res = LibLoader.lib.FliCredTwo_getPowerExternalPeltier_V2(context, ctypes.byref(current), ctypes.byref(voltage), ctypes.byref(power))
		return res, current.value, voltage.value, power.value

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwo_getPowerSensor_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double)]
	LibLoader.lib.FliCredTwo_getPowerSensor_V2.restype = ctypes.c_bool
	def GetPowerSensor(self, context):
		current = ctypes.c_double(0)
		voltage = ctypes.c_double(0)
		power = ctypes.c_double(0)
		res = LibLoader.lib.FliCredTwo_getPowerSensor_V2(context, ctypes.byref(current), ctypes.byref(voltage), ctypes.byref(power))
		return res, current.value, voltage.value, power.value

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwo_getUploadFirmwareConnectionInfo_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_size_t, ctypes.c_int]
	LibLoader.lib.FliCredTwo_getUploadFirmwareConnectionInfo_V2.restype = ctypes.c_bool
	def GetUploadFirmwareConnectionInfo(self, context, port):
		res = LibLoader.lib.FliCredTwo_getUploadFirmwareConnectionInfo_V2(context, charBuffer, bufferSize, port)
		return res, charBuffer.value.decode('utf-8', 'ignore')

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwo_getConversionGain_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_size_t]
	LibLoader.lib.FliCredTwo_getConversionGain_V2.restype = ctypes.c_bool
	def GetConversionGain(self, context):
		res = LibLoader.lib.FliCredTwo_getConversionGain_V2(context, charBuffer, bufferSize)
		return res, charBuffer.value.decode('utf-8', 'ignore')

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwo_getTintStep_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_double)]
	LibLoader.lib.FliCredTwo_getTintStep_V2.restype = ctypes.c_bool
	def GetTintStep(self, context):
		step = ctypes.c_double(0)
		res = LibLoader.lib.FliCredTwo_getTintStep_V2(context, ctypes.byref(step))
		return res, step.value

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwo_getImagePattern_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_size_t]
	LibLoader.lib.FliCredTwo_getImagePattern_V2.restype = ctypes.c_bool
	def GetImagePattern(self, context):
		res = LibLoader.lib.FliCredTwo_getImagePattern_V2(context, charBuffer, bufferSize)
		return res, charBuffer.value.decode('utf-8', 'ignore')

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwo_getDate_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_size_t]
	LibLoader.lib.FliCredTwo_getDate_V2.restype = ctypes.c_bool
	def GetDate(self, context):
		res = LibLoader.lib.FliCredTwo_getDate_V2(context, charBuffer, bufferSize)
		return res, charBuffer.value.decode('utf-8', 'ignore')

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwo_getUptime_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_size_t]
	LibLoader.lib.FliCredTwo_getUptime_V2.restype = ctypes.c_bool
	def GetUptime(self, context):
		res = LibLoader.lib.FliCredTwo_getUptime_V2(context, charBuffer, bufferSize)
		return res, charBuffer.value.decode('utf-8', 'ignore')

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwo_getAccumulatedUptime_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_size_t]
	LibLoader.lib.FliCredTwo_getAccumulatedUptime_V2.restype = ctypes.c_bool
	def GetAccumulatedUptime(self, context):
		res = LibLoader.lib.FliCredTwo_getAccumulatedUptime_V2(context, charBuffer, bufferSize)
		return res, charBuffer.value.decode('utf-8', 'ignore')

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwo_getTotalUptime_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_size_t]
	LibLoader.lib.FliCredTwo_getTotalUptime_V2.restype = ctypes.c_bool
	def GetTotalUptime(self, context):
		res = LibLoader.lib.FliCredTwo_getTotalUptime_V2(context, charBuffer, bufferSize)
		return res, charBuffer.value.decode('utf-8', 'ignore')

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwo_getUnsignedPixelsState_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_bool)]
	LibLoader.lib.FliCredTwo_getUnsignedPixelsState_V2.restype = ctypes.c_bool
	def GetUnsignedPixelsState(self, context):
		enabled = ctypes.c_bool(0)
		res = LibLoader.lib.FliCredTwo_getUnsignedPixelsState_V2(context, ctypes.byref(enabled))
		return res, enabled.value

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwo_setTint_V2.argtypes = [ctypes.c_void_p, ctypes.c_double]
	LibLoader.lib.FliCredTwo_setTint_V2.restype = ctypes.c_bool
	def SetTint(self, context, tint):
		res = LibLoader.lib.FliCredTwo_setTint_V2(context, tint)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwo_setConversionGain_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
	LibLoader.lib.FliCredTwo_setConversionGain_V2.restype = ctypes.c_bool
	def SetConversionGain(self, context, gain):
		res = LibLoader.lib.FliCredTwo_setConversionGain_V2(context, gain.encode())
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwo_setNbReadWoReset_V2.argtypes = [ctypes.c_void_p, ctypes.c_int]
	LibLoader.lib.FliCredTwo_setNbReadWoReset_V2.restype = ctypes.c_bool
	def SetNbReadWoReset(self, context, nbRead):
		res = LibLoader.lib.FliCredTwo_setNbReadWoReset_V2(context, nbRead)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwo_setNbFramesPerSwTrig_V2.argtypes = [ctypes.c_void_p, ctypes.c_int]
	LibLoader.lib.FliCredTwo_setNbFramesPerSwTrig_V2.restype = ctypes.c_bool
	def SetNbFramesPerSwTrig(self, context, nbFrames):
		res = LibLoader.lib.FliCredTwo_setNbFramesPerSwTrig_V2(context, nbFrames)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwo_setDarkOptimLevel_V2.argtypes = [ctypes.c_void_p, ctypes.c_int]
	LibLoader.lib.FliCredTwo_setDarkOptimLevel_V2.restype = ctypes.c_bool
	def SetDarkOptimLevel(self, context, level):
		res = LibLoader.lib.FliCredTwo_setDarkOptimLevel_V2(context, level)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwo_setSensorTemp_V2.argtypes = [ctypes.c_void_p, ctypes.c_double]
	LibLoader.lib.FliCredTwo_setSensorTemp_V2.restype = ctypes.c_bool
	def SetSensorTemp(self, context, temp):
		res = LibLoader.lib.FliCredTwo_setSensorTemp_V2(context, temp)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwo_setExtSynchroExposureInternal_V2.argtypes = [ctypes.c_void_p]
	LibLoader.lib.FliCredTwo_setExtSynchroExposureInternal_V2.restype = ctypes.c_bool
	def SetExtSynchroExposureInternal(self, context):
		res = LibLoader.lib.FliCredTwo_setExtSynchroExposureInternal_V2(context)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwo_setExtSynchroExposureExternal_V2.argtypes = [ctypes.c_void_p]
	LibLoader.lib.FliCredTwo_setExtSynchroExposureExternal_V2.restype = ctypes.c_bool
	def SetExtSynchroExposureExternal(self, context):
		res = LibLoader.lib.FliCredTwo_setExtSynchroExposureExternal_V2(context)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwo_setExtSynchroPolarityInverted_V2.argtypes = [ctypes.c_void_p]
	LibLoader.lib.FliCredTwo_setExtSynchroPolarityInverted_V2.restype = ctypes.c_bool
	def SetExtSynchroPolarityInverted(self, context):
		res = LibLoader.lib.FliCredTwo_setExtSynchroPolarityInverted_V2(context)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwo_setExtSynchroPolarityStandard_V2.argtypes = [ctypes.c_void_p]
	LibLoader.lib.FliCredTwo_setExtSynchroPolarityStandard_V2.restype = ctypes.c_bool
	def SetExtSynchroPolarityStandard(self, context):
		res = LibLoader.lib.FliCredTwo_setExtSynchroPolarityStandard_V2(context)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwo_setFanSpeed_V2.argtypes = [ctypes.c_void_p, ctypes.c_int]
	LibLoader.lib.FliCredTwo_setFanSpeed_V2.restype = ctypes.c_bool
	def SetFanSpeed(self, context, speed):
		res = LibLoader.lib.FliCredTwo_setFanSpeed_V2(context, speed)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwo_setSyncDelay_V2.argtypes = [ctypes.c_void_p, ctypes.c_int]
	LibLoader.lib.FliCredTwo_setSyncDelay_V2.restype = ctypes.c_bool
	def SetSyncDelay(self, context, delay):
		res = LibLoader.lib.FliCredTwo_setSyncDelay_V2(context, delay)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwo_setTlsyDel_V2.argtypes = [ctypes.c_void_p, ctypes.c_int]
	LibLoader.lib.FliCredTwo_setTlsyDel_V2.restype = ctypes.c_bool
	def SetTlsyDel(self, context, val):
		res = LibLoader.lib.FliCredTwo_setTlsyDel_V2(context, val)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwo_setVoltageVref_V2.argtypes = [ctypes.c_void_p, ctypes.c_double]
	LibLoader.lib.FliCredTwo_setVoltageVref_V2.restype = ctypes.c_bool
	def SetVoltageVref(self, context, vref):
		res = LibLoader.lib.FliCredTwo_setVoltageVref_V2(context, vref)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwo_setFanModeAutomatic_V2.argtypes = [ctypes.c_void_p]
	LibLoader.lib.FliCredTwo_setFanModeAutomatic_V2.restype = ctypes.c_bool
	def SetFanModeAutomatic(self, context):
		res = LibLoader.lib.FliCredTwo_setFanModeAutomatic_V2(context)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwo_setFanModeManual_V2.argtypes = [ctypes.c_void_p]
	LibLoader.lib.FliCredTwo_setFanModeManual_V2.restype = ctypes.c_bool
	def SetFanModeManual(self, context):
		res = LibLoader.lib.FliCredTwo_setFanModeManual_V2(context)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwo_setHdrCalibrationC1_V2.argtypes = [ctypes.c_void_p]
	LibLoader.lib.FliCredTwo_setHdrCalibrationC1_V2.restype = ctypes.c_bool
	def SetHdrCalibrationC1(self, context):
		res = LibLoader.lib.FliCredTwo_setHdrCalibrationC1_V2(context)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwo_setHdrCalibrationC2_V2.argtypes = [ctypes.c_void_p]
	LibLoader.lib.FliCredTwo_setHdrCalibrationC2_V2.restype = ctypes.c_bool
	def SetHdrCalibrationC2(self, context):
		res = LibLoader.lib.FliCredTwo_setHdrCalibrationC2_V2(context)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwo_setHdrCalibrationOff_V2.argtypes = [ctypes.c_void_p]
	LibLoader.lib.FliCredTwo_setHdrCalibrationOff_V2.restype = ctypes.c_bool
	def SetHdrCalibrationOff(self, context):
		res = LibLoader.lib.FliCredTwo_setHdrCalibrationOff_V2(context)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwo_setSynchronizationCmos_V2.argtypes = [ctypes.c_void_p]
	LibLoader.lib.FliCredTwo_setSynchronizationCmos_V2.restype = ctypes.c_bool
	def SetSynchronizationCmos(self, context):
		res = LibLoader.lib.FliCredTwo_setSynchronizationCmos_V2(context)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwo_setSynchronizationFullCmos_V2.argtypes = [ctypes.c_void_p]
	LibLoader.lib.FliCredTwo_setSynchronizationFullCmos_V2.restype = ctypes.c_bool
	def SetSynchronizationFullCmos(self, context):
		res = LibLoader.lib.FliCredTwo_setSynchronizationFullCmos_V2(context)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwo_setSynchronizationLvds_V2.argtypes = [ctypes.c_void_p]
	LibLoader.lib.FliCredTwo_setSynchronizationLvds_V2.restype = ctypes.c_bool
	def SetSynchronizationLvds(self, context):
		res = LibLoader.lib.FliCredTwo_setSynchronizationLvds_V2(context)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwo_setPreset_V2.argtypes = [ctypes.c_void_p]
	LibLoader.lib.FliCredTwo_setPreset_V2.restype = ctypes.c_bool
	def SetPreset(self, context):
		res = LibLoader.lib.FliCredTwo_setPreset_V2(context)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwo_setPresetNumber_V2.argtypes = [ctypes.c_void_p, ctypes.c_int]
	LibLoader.lib.FliCredTwo_setPresetNumber_V2.restype = ctypes.c_bool
	def SetPresetNumber(self, context, presetNumber):
		res = LibLoader.lib.FliCredTwo_setPresetNumber_V2(context, presetNumber)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwo_setSnakeParam_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_int]
	LibLoader.lib.FliCredTwo_setSnakeParam_V2.restype = ctypes.c_bool
	def SetSnakeParam(self, context, parameter, value):
		res = LibLoader.lib.FliCredTwo_setSnakeParam_V2(context, parameter.encode(), value)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwo_setTempSnakeSetPoint_V2.argtypes = [ctypes.c_void_p, ctypes.c_double]
	LibLoader.lib.FliCredTwo_setTempSnakeSetPoint_V2.restype = ctypes.c_bool
	def SetTempSnakeSetPoint(self, context, temp):
		res = LibLoader.lib.FliCredTwo_setTempSnakeSetPoint_V2(context, temp)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwo_setImagePatternRamp_V2.argtypes = [ctypes.c_void_p]
	LibLoader.lib.FliCredTwo_setImagePatternRamp_V2.restype = ctypes.c_bool
	def SetImagePatternRamp(self, context):
		res = LibLoader.lib.FliCredTwo_setImagePatternRamp_V2(context)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwo_setImagePatternConstant_V2.argtypes = [ctypes.c_void_p, ctypes.c_int]
	LibLoader.lib.FliCredTwo_setImagePatternConstant_V2.restype = ctypes.c_bool
	def SetImagePatternConstant(self, context, val):
		res = LibLoader.lib.FliCredTwo_setImagePatternConstant_V2(context, val)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwo_setImagePatternOff_V2.argtypes = [ctypes.c_void_p]
	LibLoader.lib.FliCredTwo_setImagePatternOff_V2.restype = ctypes.c_bool
	def SetImagePatternOff(self, context):
		res = LibLoader.lib.FliCredTwo_setImagePatternOff_V2(context)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwo_enableRawImages_V2.argtypes = [ctypes.c_void_p, ctypes.c_bool]
	LibLoader.lib.FliCredTwo_enableRawImages_V2.restype = ctypes.c_bool
	def EnableRawImages(self, context, enable):
		res = LibLoader.lib.FliCredTwo_enableRawImages_V2(context, enable)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwo_enableBadPixel_V2.argtypes = [ctypes.c_void_p, ctypes.c_bool]
	LibLoader.lib.FliCredTwo_enableBadPixel_V2.restype = ctypes.c_bool
	def EnableBadPixel(self, context, enable):
		res = LibLoader.lib.FliCredTwo_enableBadPixel_V2(context, enable)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwo_enableHdr_V2.argtypes = [ctypes.c_void_p, ctypes.c_bool]
	LibLoader.lib.FliCredTwo_enableHdr_V2.restype = ctypes.c_bool
	def EnableHdr(self, context, enable):
		res = LibLoader.lib.FliCredTwo_enableHdr_V2(context, enable)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwo_enableAntiBlooming_V2.argtypes = [ctypes.c_void_p, ctypes.c_bool]
	LibLoader.lib.FliCredTwo_enableAntiBlooming_V2.restype = ctypes.c_bool
	def EnableAntiBlooming(self, context, enable):
		res = LibLoader.lib.FliCredTwo_enableAntiBlooming_V2(context, enable)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwo_enableHdrExtended_V2.argtypes = [ctypes.c_void_p, ctypes.c_bool]
	LibLoader.lib.FliCredTwo_enableHdrExtended_V2.restype = ctypes.c_bool
	def EnableHdrExtended(self, context, enable):
		res = LibLoader.lib.FliCredTwo_enableHdrExtended_V2(context, enable)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwo_enableRemoteMaintenance_V2.argtypes = [ctypes.c_void_p, ctypes.c_bool]
	LibLoader.lib.FliCredTwo_enableRemoteMaintenance_V2.restype = ctypes.c_bool
	def EnableRemoteMaintenance(self, context, enable):
		res = LibLoader.lib.FliCredTwo_enableRemoteMaintenance_V2(context, enable)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwo_enableSwSynchro_V2.argtypes = [ctypes.c_void_p, ctypes.c_bool]
	LibLoader.lib.FliCredTwo_enableSwSynchro_V2.restype = ctypes.c_bool
	def EnableSwSynchro(self, context, enable):
		res = LibLoader.lib.FliCredTwo_enableSwSynchro_V2(context, enable)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwo_enableTcdsAdjust_V2.argtypes = [ctypes.c_void_p, ctypes.c_bool]
	LibLoader.lib.FliCredTwo_enableTcdsAdjust_V2.restype = ctypes.c_bool
	def EnableTcdsAdjust(self, context, enable):
		res = LibLoader.lib.FliCredTwo_enableTcdsAdjust_V2(context, enable)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwo_enableTintGranularity_V2.argtypes = [ctypes.c_void_p, ctypes.c_bool]
	LibLoader.lib.FliCredTwo_enableTintGranularity_V2.restype = ctypes.c_bool
	def EnableTintGranularity(self, context, enable):
		res = LibLoader.lib.FliCredTwo_enableTintGranularity_V2(context, enable)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwo_enableVrefAdjust_V2.argtypes = [ctypes.c_void_p, ctypes.c_bool]
	LibLoader.lib.FliCredTwo_enableVrefAdjust_V2.restype = ctypes.c_bool
	def EnableVrefAdjust(self, context, enable):
		res = LibLoader.lib.FliCredTwo_enableVrefAdjust_V2(context, enable)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwo_enableUnsignedPixels_V2.argtypes = [ctypes.c_void_p, ctypes.c_bool]
	LibLoader.lib.FliCredTwo_enableUnsignedPixels_V2.restype = ctypes.c_bool
	def EnableUnsignedPixels(self, context, enable):
		res = LibLoader.lib.FliCredTwo_enableUnsignedPixels_V2(context, enable)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwo_reboot_V2.argtypes = [ctypes.c_void_p]
	LibLoader.lib.FliCredTwo_reboot_V2.restype = ctypes.c_bool
	def Reboot(self, context):
		res = LibLoader.lib.FliCredTwo_reboot_V2(context)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwo_buildFlatHdrC1_V2.argtypes = [ctypes.c_void_p]
	LibLoader.lib.FliCredTwo_buildFlatHdrC1_V2.restype = ctypes.c_bool
	def BuildFlatHdrC1(self, context):
		res = LibLoader.lib.FliCredTwo_buildFlatHdrC1_V2(context)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwo_buildFlatHdrC2_V2.argtypes = [ctypes.c_void_p]
	LibLoader.lib.FliCredTwo_buildFlatHdrC2_V2.restype = ctypes.c_bool
	def BuildFlatHdrC2(self, context):
		res = LibLoader.lib.FliCredTwo_buildFlatHdrC2_V2(context)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwo_sendBiasHdrC1FromUrl_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
	LibLoader.lib.FliCredTwo_sendBiasHdrC1FromUrl_V2.restype = ctypes.c_bool
	def SendBiasHdrC1FromUrl(self, context, url):
		res = LibLoader.lib.FliCredTwo_sendBiasHdrC1FromUrl_V2(context, url.encode())
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwo_sendBiasHdrC2FromUrl_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
	LibLoader.lib.FliCredTwo_sendBiasHdrC2FromUrl_V2.restype = ctypes.c_bool
	def SendBiasHdrC2FromUrl(self, context, url):
		res = LibLoader.lib.FliCredTwo_sendBiasHdrC2FromUrl_V2(context, url.encode())
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwo_sendFlatHdrC1FromUrl_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
	LibLoader.lib.FliCredTwo_sendFlatHdrC1FromUrl_V2.restype = ctypes.c_bool
	def SendFlatHdrC1FromUrl(self, context, url):
		res = LibLoader.lib.FliCredTwo_sendFlatHdrC1FromUrl_V2(context, url.encode())
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwo_sendFlatHdrC2FromUrl_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
	LibLoader.lib.FliCredTwo_sendFlatHdrC2FromUrl_V2.restype = ctypes.c_bool
	def SendFlatHdrC2FromUrl(self, context, url):
		res = LibLoader.lib.FliCredTwo_sendFlatHdrC2FromUrl_V2(context, url.encode())
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwo_sendBiasHdrC1File_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
	LibLoader.lib.FliCredTwo_sendBiasHdrC1File_V2.restype = ctypes.c_bool
	def SendBiasHdrC1File(self, context, filePath):
		res = LibLoader.lib.FliCredTwo_sendBiasHdrC1File_V2(context, filePath.encode())
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwo_sendBiasHdrC2File_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
	LibLoader.lib.FliCredTwo_sendBiasHdrC2File_V2.restype = ctypes.c_bool
	def SendBiasHdrC2File(self, context, filePath):
		res = LibLoader.lib.FliCredTwo_sendBiasHdrC2File_V2(context, filePath.encode())
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwo_sendFlatHdrC1File_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
	LibLoader.lib.FliCredTwo_sendFlatHdrC1File_V2.restype = ctypes.c_bool
	def SendFlatHdrC1File(self, context, filePath):
		res = LibLoader.lib.FliCredTwo_sendFlatHdrC1File_V2(context, filePath.encode())
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwo_sendFlatHdrC2File_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
	LibLoader.lib.FliCredTwo_sendFlatHdrC2File_V2.restype = ctypes.c_bool
	def SendFlatHdrC2File(self, context, filePath):
		res = LibLoader.lib.FliCredTwo_sendFlatHdrC2File_V2(context, filePath.encode())
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwo_xSendBiasFile_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
	LibLoader.lib.FliCredTwo_xSendBiasFile_V2.restype = ctypes.c_bool
	def XSendBiasFile(self, context, filePath):
		res = LibLoader.lib.FliCredTwo_xSendBiasFile_V2(context, filePath.encode())
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwo_xSendBiasHdrC1File_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
	LibLoader.lib.FliCredTwo_xSendBiasHdrC1File_V2.restype = ctypes.c_bool
	def XSendBiasHdrC1File(self, context, filePath):
		res = LibLoader.lib.FliCredTwo_xSendBiasHdrC1File_V2(context, filePath.encode())
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwo_xSendBiasHdrC2File_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
	LibLoader.lib.FliCredTwo_xSendBiasHdrC2File_V2.restype = ctypes.c_bool
	def XSendBiasHdrC2File(self, context, filePath):
		res = LibLoader.lib.FliCredTwo_xSendBiasHdrC2File_V2(context, filePath.encode())
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwo_xSendFlatFile_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
	LibLoader.lib.FliCredTwo_xSendFlatFile_V2.restype = ctypes.c_bool
	def XSendFlatFile(self, context, filePath):
		res = LibLoader.lib.FliCredTwo_xSendFlatFile_V2(context, filePath.encode())
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwo_xSendFlatHdrC1File_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
	LibLoader.lib.FliCredTwo_xSendFlatHdrC1File_V2.restype = ctypes.c_bool
	def XSendFlatHdrC1File(self, context, filePath):
		res = LibLoader.lib.FliCredTwo_xSendFlatHdrC1File_V2(context, filePath.encode())
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwo_xSendFlatHdrC2File_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
	LibLoader.lib.FliCredTwo_xSendFlatHdrC2File_V2.restype = ctypes.c_bool
	def XSendFlatHdrC2File(self, context, filePath):
		res = LibLoader.lib.FliCredTwo_xSendFlatHdrC2File_V2(context, filePath.encode())
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwo_sendLicenseFile_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_char_p]
	LibLoader.lib.FliCredTwo_sendLicenseFile_V2.restype = ctypes.c_bool
	def SendLicenseFile(self, context, filePath, fileName):
		res = LibLoader.lib.FliCredTwo_sendLicenseFile_V2(context, filePath.encode(), fileName.encode())
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwo_deleteLicense_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
	LibLoader.lib.FliCredTwo_deleteLicense_V2.restype = ctypes.c_bool
	def DeleteLicense(self, context, licenseName):
		res = LibLoader.lib.FliCredTwo_deleteLicense_V2(context, licenseName.encode())
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwo_disableLicense_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
	LibLoader.lib.FliCredTwo_disableLicense_V2.restype = ctypes.c_bool
	def DisableLicense(self, context, licenseName):
		res = LibLoader.lib.FliCredTwo_disableLicense_V2(context, licenseName.encode())
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwo_enableLicense_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
	LibLoader.lib.FliCredTwo_enableLicense_V2.restype = ctypes.c_bool
	def EnableLicense(self, context, licenseName):
		res = LibLoader.lib.FliCredTwo_enableLicense_V2(context, licenseName.encode())
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwo_softwareTrig_V2.argtypes = [ctypes.c_void_p]
	LibLoader.lib.FliCredTwo_softwareTrig_V2.restype = ctypes.c_bool
	def SoftwareTrig(self, context):
		res = LibLoader.lib.FliCredTwo_softwareTrig_V2(context)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwo_startHttpServer_V2.argtypes = [ctypes.c_void_p]
	LibLoader.lib.FliCredTwo_startHttpServer_V2.restype = ctypes.c_bool
	def StartHttpServer(self, context):
		res = LibLoader.lib.FliCredTwo_startHttpServer_V2(context)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwo_stopHttpServer_V2.argtypes = [ctypes.c_void_p]
	LibLoader.lib.FliCredTwo_stopHttpServer_V2.restype = ctypes.c_bool
	def StopHttpServer(self, context):
		res = LibLoader.lib.FliCredTwo_stopHttpServer_V2(context)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwo_startEthernetGrabber_V2.argtypes = [ctypes.c_void_p]
	LibLoader.lib.FliCredTwo_startEthernetGrabber_V2.restype = ctypes.c_bool
	def StartEthernetGrabber(self, context):
		res = LibLoader.lib.FliCredTwo_startEthernetGrabber_V2(context)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredTwo_stopEthernetGrabber_V2.argtypes = [ctypes.c_void_p]
	LibLoader.lib.FliCredTwo_stopEthernetGrabber_V2.restype = ctypes.c_bool
	def StopEthernetGrabber(self, context):
		res = LibLoader.lib.FliCredTwo_stopEthernetGrabber_V2(context)
		return res

