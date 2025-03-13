import LibLoader
import ctypes
import numpy as np

bufferSize = ctypes.c_size_t(1000)
charBuffer = ctypes.create_string_buffer(bufferSize.value)

class FliCredOne:
	#------------------------------------------------------------
	LibLoader.lib.FliCredOne_getAllTemp_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double)]
	LibLoader.lib.FliCredOne_getAllTemp_V2.restype = ctypes.c_bool
	def GetAllTemp(self, context):
		mb = ctypes.c_double(0)
		fe = ctypes.c_double(0)
		pw = ctypes.c_double(0)
		cryod = ctypes.c_double(0)
		cryopt = ctypes.c_double(0)
		water = ctypes.c_double(0)
		peltier = ctypes.c_double(0)
		ptmcu = ctypes.c_double(0)
		res = LibLoader.lib.FliCredOne_getAllTemp_V2(context, ctypes.byref(mb), ctypes.byref(fe), ctypes.byref(pw), ctypes.byref(cryod), ctypes.byref(cryopt), ctypes.byref(water), ctypes.byref(peltier), ctypes.byref(ptmcu))
		return res, mb.value, fe.value, pw.value, cryod.value, cryopt.value, water.value, peltier.value, ptmcu.value

	#------------------------------------------------------------
	LibLoader.lib.FliCredOne_getNbReadWoReset_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_int)]
	LibLoader.lib.FliCredOne_getNbReadWoReset_V2.restype = ctypes.c_bool
	def GetNbReadWoReset(self, context):
		nbRead = ctypes.c_int(0)
		res = LibLoader.lib.FliCredOne_getNbReadWoReset_V2(context, ctypes.byref(nbRead))
		return res, nbRead.value

	#------------------------------------------------------------
	LibLoader.lib.FliCredOne_getRawImagesState_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_bool)]
	LibLoader.lib.FliCredOne_getRawImagesState_V2.restype = ctypes.c_bool
	def GetRawImagesState(self, context):
		enabled = ctypes.c_bool(0)
		res = LibLoader.lib.FliCredOne_getRawImagesState_V2(context, ctypes.byref(enabled))
		return res, enabled.value

	#------------------------------------------------------------
	LibLoader.lib.FliCredOne_getTempFrontEnd_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_double)]
	LibLoader.lib.FliCredOne_getTempFrontEnd_V2.restype = ctypes.c_bool
	def GetTempFrontEnd(self, context):
		temp = ctypes.c_double(0)
		res = LibLoader.lib.FliCredOne_getTempFrontEnd_V2(context, ctypes.byref(temp))
		return res, temp.value

	#------------------------------------------------------------
	LibLoader.lib.FliCredOne_getTempMotherBoard_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_double)]
	LibLoader.lib.FliCredOne_getTempMotherBoard_V2.restype = ctypes.c_bool
	def GetTempMotherBoard(self, context):
		temp = ctypes.c_double(0)
		res = LibLoader.lib.FliCredOne_getTempMotherBoard_V2(context, ctypes.byref(temp))
		return res, temp.value

	#------------------------------------------------------------
	LibLoader.lib.FliCredOne_getTempPowerBoard_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_double)]
	LibLoader.lib.FliCredOne_getTempPowerBoard_V2.restype = ctypes.c_bool
	def GetTempPowerBoard(self, context):
		temp = ctypes.c_double(0)
		res = LibLoader.lib.FliCredOne_getTempPowerBoard_V2(context, ctypes.byref(temp))
		return res, temp.value

	#------------------------------------------------------------
	LibLoader.lib.FliCredOne_getTempDiode_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_double)]
	LibLoader.lib.FliCredOne_getTempDiode_V2.restype = ctypes.c_bool
	def GetTempDiode(self, context):
		temp = ctypes.c_double(0)
		res = LibLoader.lib.FliCredOne_getTempDiode_V2(context, ctypes.byref(temp))
		return res, temp.value

	#------------------------------------------------------------
	LibLoader.lib.FliCredOne_getTempPtController_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_double)]
	LibLoader.lib.FliCredOne_getTempPtController_V2.restype = ctypes.c_bool
	def GetTempPtController(self, context):
		temp = ctypes.c_double(0)
		res = LibLoader.lib.FliCredOne_getTempPtController_V2(context, ctypes.byref(temp))
		return res, temp.value

	#------------------------------------------------------------
	LibLoader.lib.FliCredOne_getTempSetpoint_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_double)]
	LibLoader.lib.FliCredOne_getTempSetpoint_V2.restype = ctypes.c_bool
	def GetTempSetpoint(self, context):
		temp = ctypes.c_double(0)
		res = LibLoader.lib.FliCredOne_getTempSetpoint_V2(context, ctypes.byref(temp))
		return res, temp.value

	#------------------------------------------------------------
	LibLoader.lib.FliCredOne_getTempPtMcu_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_double)]
	LibLoader.lib.FliCredOne_getTempPtMcu_V2.restype = ctypes.c_bool
	def GetTempPtMcu(self, context):
		temp = ctypes.c_double(0)
		res = LibLoader.lib.FliCredOne_getTempPtMcu_V2(context, ctypes.byref(temp))
		return res, temp.value

	#------------------------------------------------------------
	LibLoader.lib.FliCredOne_getTempWater_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_double)]
	LibLoader.lib.FliCredOne_getTempWater_V2.restype = ctypes.c_bool
	def GetTempWater(self, context):
		temp = ctypes.c_double(0)
		res = LibLoader.lib.FliCredOne_getTempWater_V2(context, ctypes.byref(temp))
		return res, temp.value

	#------------------------------------------------------------
	LibLoader.lib.FliCredOne_getVersionFpgaDetailed_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_size_t]
	LibLoader.lib.FliCredOne_getVersionFpgaDetailed_V2.restype = ctypes.c_bool
	def GetVersionFpgaDetailed(self, context):
		res = LibLoader.lib.FliCredOne_getVersionFpgaDetailed_V2(context, charBuffer, bufferSize)
		return res, charBuffer.value.decode('utf-8', 'ignore')

	#------------------------------------------------------------
	LibLoader.lib.FliCredOne_getAll_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_size_t]
	LibLoader.lib.FliCredOne_getAll_V2.restype = ctypes.c_bool
	def GetAll(self, context):
		res = LibLoader.lib.FliCredOne_getAll_V2(context, charBuffer, bufferSize)
		return res, charBuffer.value.decode('utf-8', 'ignore')

	#------------------------------------------------------------
	LibLoader.lib.FliCredOne_getCoolingState_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_bool)]
	LibLoader.lib.FliCredOne_getCoolingState_V2.restype = ctypes.c_bool
	def GetCoolingState(self, context):
		enabled = ctypes.c_bool(0)
		res = LibLoader.lib.FliCredOne_getCoolingState_V2(context, ctypes.byref(enabled))
		return res, enabled.value

	#------------------------------------------------------------
	LibLoader.lib.FliCredOne_getGain_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_double)]
	LibLoader.lib.FliCredOne_getGain_V2.restype = ctypes.c_bool
	def GetGain(self, context):
		gain = ctypes.c_double(0)
		res = LibLoader.lib.FliCredOne_getGain_V2(context, ctypes.byref(gain))
		return res, gain.value

	#------------------------------------------------------------
	LibLoader.lib.FliCredOne_getNbRegenGetter_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_size_t]
	LibLoader.lib.FliCredOne_getNbRegenGetter_V2.restype = ctypes.c_bool
	def GetNbRegenGetter(self, context):
		res = LibLoader.lib.FliCredOne_getNbRegenGetter_V2(context, charBuffer, bufferSize)
		return res, charBuffer.value.decode('utf-8', 'ignore')

	#------------------------------------------------------------
	LibLoader.lib.FliCredOne_getRegenRemainingTime_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_int)]
	LibLoader.lib.FliCredOne_getRegenRemainingTime_V2.restype = ctypes.c_bool
	def GetRegenRemainingTime(self, context):
		time = ctypes.c_int(0)
		res = LibLoader.lib.FliCredOne_getRegenRemainingTime_V2(context, ctypes.byref(time))
		return res, time.value

	#------------------------------------------------------------
	LibLoader.lib.FliCredOne_getReadOutMode_V2.argtypes = [ctypes.c_void_p]
	LibLoader.lib.FliCredOne_getReadOutMode_V2.restype = ctypes.c_bool
	def GetReadOutMode(self, context):
		res = LibLoader.lib.FliCredOne_getReadOutMode_V2(context)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredOne_getNloop_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_int)]
	LibLoader.lib.FliCredOne_getNloop_V2.restype = ctypes.c_bool
	def GetNloop(self, context):
		nLoop = ctypes.c_int(0)
		res = LibLoader.lib.FliCredOne_getNloop_V2(context, ctypes.byref(nLoop))
		return res, nLoop.value

	#------------------------------------------------------------
	LibLoader.lib.FliCredOne_getNbSamplePixel_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_int)]
	LibLoader.lib.FliCredOne_getNbSamplePixel_V2.restype = ctypes.c_bool
	def GetNbSamplePixel(self, context):
		nSample = ctypes.c_int(0)
		res = LibLoader.lib.FliCredOne_getNbSamplePixel_V2(context, ctypes.byref(nSample))
		return res, nSample.value

	#------------------------------------------------------------
	LibLoader.lib.FliCredOne_getPhotoCurrent_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_double)]
	LibLoader.lib.FliCredOne_getPhotoCurrent_V2.restype = ctypes.c_bool
	def GetPhotoCurrent(self, context):
		photocurrent = ctypes.c_double(0)
		res = LibLoader.lib.FliCredOne_getPhotoCurrent_V2(context, ctypes.byref(photocurrent))
		return res, photocurrent.value

	#------------------------------------------------------------
	LibLoader.lib.FliCredOne_getPowers_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double)]
	LibLoader.lib.FliCredOne_getPowers_V2.restype = ctypes.c_bool
	def GetPowers(self, context):
		getter = ctypes.c_double(0)
		peltier = ctypes.c_double(0)
		pulseTube = ctypes.c_double(0)
		res = LibLoader.lib.FliCredOne_getPowers_V2(context, ctypes.byref(getter), ctypes.byref(peltier), ctypes.byref(pulseTube))
		return res, getter.value, peltier.value, pulseTube.value

	#------------------------------------------------------------
	LibLoader.lib.FliCredOne_getPowerGetter_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_double)]
	LibLoader.lib.FliCredOne_getPowerGetter_V2.restype = ctypes.c_bool
	def GetPowerGetter(self, context):
		getter = ctypes.c_double(0)
		res = LibLoader.lib.FliCredOne_getPowerGetter_V2(context, ctypes.byref(getter))
		return res, getter.value

	#------------------------------------------------------------
	LibLoader.lib.FliCredOne_getPowerPulseTube_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_double)]
	LibLoader.lib.FliCredOne_getPowerPulseTube_V2.restype = ctypes.c_bool
	def GetPowerPulseTube(self, context):
		pulseTube = ctypes.c_double(0)
		res = LibLoader.lib.FliCredOne_getPowerPulseTube_V2(context, ctypes.byref(pulseTube))
		return res, pulseTube.value

	#------------------------------------------------------------
	LibLoader.lib.FliCredOne_getPressure_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_size_t]
	LibLoader.lib.FliCredOne_getPressure_V2.restype = ctypes.c_bool
	def GetPressure(self, context):
		res = LibLoader.lib.FliCredOne_getPressure_V2(context, charBuffer, bufferSize)
		return res, charBuffer.value.decode('utf-8', 'ignore')

	#------------------------------------------------------------
	LibLoader.lib.FliCredOne_getPulseTubeReady_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_size_t]
	LibLoader.lib.FliCredOne_getPulseTubeReady_V2.restype = ctypes.c_bool
	def GetPulseTubeReady(self, context):
		res = LibLoader.lib.FliCredOne_getPulseTubeReady_V2(context, charBuffer, bufferSize)
		return res, charBuffer.value.decode('utf-8', 'ignore')

	#------------------------------------------------------------
	LibLoader.lib.FliCredOne_getRemoteMaintenanceState_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_size_t]
	LibLoader.lib.FliCredOne_getRemoteMaintenanceState_V2.restype = ctypes.c_bool
	def GetRemoteMaintenanceState(self, context):
		res = LibLoader.lib.FliCredOne_getRemoteMaintenanceState_V2(context, charBuffer, bufferSize)
		return res, charBuffer.value.decode('utf-8', 'ignore')

	#------------------------------------------------------------
	LibLoader.lib.FliCredOne_getResetWidth_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_int)]
	LibLoader.lib.FliCredOne_getResetWidth_V2.restype = ctypes.c_bool
	def GetResetWidth(self, context):
		width = ctypes.c_int(0)
		res = LibLoader.lib.FliCredOne_getResetWidth_V2(context, ctypes.byref(width))
		return res, width.value

	#------------------------------------------------------------
	LibLoader.lib.FliCredOne_getStandbyState_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_bool)]
	LibLoader.lib.FliCredOne_getStandbyState_V2.restype = ctypes.c_bool
	def GetStandbyState(self, context):
		enabled = ctypes.c_bool(0)
		res = LibLoader.lib.FliCredOne_getStandbyState_V2(context, ctypes.byref(enabled))
		return res, enabled.value

	#------------------------------------------------------------
	LibLoader.lib.FliCredOne_getTestPatternState_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_bool)]
	LibLoader.lib.FliCredOne_getTestPatternState_V2.restype = ctypes.c_bool
	def GetTestPatternState(self, context):
		enabled = ctypes.c_bool(0)
		res = LibLoader.lib.FliCredOne_getTestPatternState_V2(context, ctypes.byref(enabled))
		return res, enabled.value

	#------------------------------------------------------------
	LibLoader.lib.FliCredOne_getTelnetState_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_bool)]
	LibLoader.lib.FliCredOne_getTelnetState_V2.restype = ctypes.c_bool
	def GetTelnetState(self, context):
		enabled = ctypes.c_bool(0)
		res = LibLoader.lib.FliCredOne_getTelnetState_V2(context, ctypes.byref(enabled))
		return res, enabled.value

	#------------------------------------------------------------
	LibLoader.lib.FliCredOne_getFowlerState_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_bool)]
	LibLoader.lib.FliCredOne_getFowlerState_V2.restype = ctypes.c_bool
	def GetFowlerState(self, context):
		enabled = ctypes.c_bool(0)
		res = LibLoader.lib.FliCredOne_getFowlerState_V2(context, ctypes.byref(enabled))
		return res, enabled.value

	#------------------------------------------------------------
	LibLoader.lib.FliCredOne_setNbReadWoReset_V2.argtypes = [ctypes.c_void_p, ctypes.c_int]
	LibLoader.lib.FliCredOne_setNbReadWoReset_V2.restype = ctypes.c_bool
	def SetNbReadWoReset(self, context, nbRead):
		res = LibLoader.lib.FliCredOne_setNbReadWoReset_V2(context, nbRead)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredOne_setGain_V2.argtypes = [ctypes.c_void_p, ctypes.c_double]
	LibLoader.lib.FliCredOne_setGain_V2.restype = ctypes.c_bool
	def SetGain(self, context, gain):
		res = LibLoader.lib.FliCredOne_setGain_V2(context, gain)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredOne_setMode_V2.argtypes = [ctypes.c_void_p]
	LibLoader.lib.FliCredOne_setMode_V2.restype = ctypes.c_bool
	def SetMode(self, context):
		res = LibLoader.lib.FliCredOne_setMode_V2(context)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredOne_setNloop_V2.argtypes = [ctypes.c_void_p, ctypes.c_int]
	LibLoader.lib.FliCredOne_setNloop_V2.restype = ctypes.c_bool
	def SetNloop(self, context, nLoop):
		res = LibLoader.lib.FliCredOne_setNloop_V2(context, nLoop)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredOne_setNsamplePixel_V2.argtypes = [ctypes.c_void_p, ctypes.c_int]
	LibLoader.lib.FliCredOne_setNsamplePixel_V2.restype = ctypes.c_bool
	def SetNsamplePixel(self, context, nSample):
		res = LibLoader.lib.FliCredOne_setNsamplePixel_V2(context, nSample)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredOne_setResetWidth_V2.argtypes = [ctypes.c_void_p, ctypes.c_int]
	LibLoader.lib.FliCredOne_setResetWidth_V2.restype = ctypes.c_bool
	def SetResetWidth(self, context, resetWidth):
		res = LibLoader.lib.FliCredOne_setResetWidth_V2(context, resetWidth)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredOne_enableRawImages_V2.argtypes = [ctypes.c_void_p, ctypes.c_bool]
	LibLoader.lib.FliCredOne_enableRawImages_V2.restype = ctypes.c_bool
	def EnableRawImages(self, context, enable):
		res = LibLoader.lib.FliCredOne_enableRawImages_V2(context, enable)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredOne_enableRemoteMaintenance_V2.argtypes = [ctypes.c_void_p, ctypes.c_bool]
	LibLoader.lib.FliCredOne_enableRemoteMaintenance_V2.restype = ctypes.c_bool
	def EnableRemoteMaintenance(self, context, enable):
		res = LibLoader.lib.FliCredOne_enableRemoteMaintenance_V2(context, enable)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredOne_enableCooling_V2.argtypes = [ctypes.c_void_p, ctypes.c_bool]
	LibLoader.lib.FliCredOne_enableCooling_V2.restype = ctypes.c_bool
	def EnableCooling(self, context, enable):
		res = LibLoader.lib.FliCredOne_enableCooling_V2(context, enable)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredOne_enableStandby_V2.argtypes = [ctypes.c_void_p, ctypes.c_bool]
	LibLoader.lib.FliCredOne_enableStandby_V2.restype = ctypes.c_bool
	def EnableStandby(self, context, enable):
		res = LibLoader.lib.FliCredOne_enableStandby_V2(context, enable)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredOne_enableTestPattern_V2.argtypes = [ctypes.c_void_p, ctypes.c_bool]
	LibLoader.lib.FliCredOne_enableTestPattern_V2.restype = ctypes.c_bool
	def EnableTestPattern(self, context, enable):
		res = LibLoader.lib.FliCredOne_enableTestPattern_V2(context, enable)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredOne_enableFowler_V2.argtypes = [ctypes.c_void_p, ctypes.c_bool]
	LibLoader.lib.FliCredOne_enableFowler_V2.restype = ctypes.c_bool
	def EnableFowler(self, context, enable):
		res = LibLoader.lib.FliCredOne_enableFowler_V2(context, enable)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredOne_startVacuumRegen_V2.argtypes = [ctypes.c_void_p]
	LibLoader.lib.FliCredOne_startVacuumRegen_V2.restype = ctypes.c_bool
	def StartVacuumRegen(self, context):
		res = LibLoader.lib.FliCredOne_startVacuumRegen_V2(context)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredOne_sendTestPatternFromUrl_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
	LibLoader.lib.FliCredOne_sendTestPatternFromUrl_V2.restype = ctypes.c_bool
	def SendTestPatternFromUrl(self, context, url):
		res = LibLoader.lib.FliCredOne_sendTestPatternFromUrl_V2(context, url.encode())
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliCredOne_reboot_V2.argtypes = [ctypes.c_void_p]
	LibLoader.lib.FliCredOne_reboot_V2.restype = ctypes.c_bool
	def Reboot(self, context):
		res = LibLoader.lib.FliCredOne_reboot_V2(context)
		return res

