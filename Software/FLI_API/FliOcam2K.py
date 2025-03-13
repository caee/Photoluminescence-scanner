import LibLoader
import ctypes
import numpy as np

bufferSize = ctypes.c_size_t(1000)
charBuffer = ctypes.create_string_buffer(bufferSize.value)

class FliOcam2K:
	#------------------------------------------------------------
	LibLoader.lib.FliOcam2k_getAllTemp_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double)]
	LibLoader.lib.FliOcam2k_getAllTemp_V2.restype = ctypes.c_bool
	def GetAllTemp(self, context):
		ccdTemp = ctypes.c_double(0)
		cpuTemp = ctypes.c_double(0)
		powerTemp = ctypes.c_double(0)
		biasTemp = ctypes.c_double(0)
		waterTemp = ctypes.c_double(0)
		leftTemp = ctypes.c_double(0)
		rightTemp = ctypes.c_double(0)
		setTemp = ctypes.c_double(0)
		res = LibLoader.lib.FliOcam2k_getAllTemp_V2(context, ctypes.byref(ccdTemp), ctypes.byref(cpuTemp), ctypes.byref(powerTemp), ctypes.byref(biasTemp), ctypes.byref(waterTemp), ctypes.byref(leftTemp), ctypes.byref(rightTemp), ctypes.byref(setTemp))
		return res, ccdTemp.value, cpuTemp.value, powerTemp.value, biasTemp.value, waterTemp.value, leftTemp.value, rightTemp.value, setTemp.value

	#------------------------------------------------------------
	LibLoader.lib.FliOcam2k_setWorkMode_V2.argtypes = [ctypes.c_void_p]
	LibLoader.lib.FliOcam2k_setWorkMode_V2.restype = ctypes.c_bool
	def SetWorkMode(self, context):
		res = LibLoader.lib.FliOcam2k_setWorkMode_V2(context)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliOcam2k_setStandardMode_V2.argtypes = [ctypes.c_void_p]
	LibLoader.lib.FliOcam2k_setStandardMode_V2.restype = ctypes.c_bool
	def SetStandardMode(self, context):
		res = LibLoader.lib.FliOcam2k_setStandardMode_V2(context)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliOcam2k_setCropping240x120Mode_V2.argtypes = [ctypes.c_void_p]
	LibLoader.lib.FliOcam2k_setCropping240x120Mode_V2.restype = ctypes.c_bool
	def SetCropping240x120Mode(self, context):
		res = LibLoader.lib.FliOcam2k_setCropping240x120Mode_V2(context)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliOcam2k_setCropping240x128Mode_V2.argtypes = [ctypes.c_void_p]
	LibLoader.lib.FliOcam2k_setCropping240x128Mode_V2.restype = ctypes.c_bool
	def SetCropping240x128Mode(self, context):
		res = LibLoader.lib.FliOcam2k_setCropping240x128Mode_V2(context)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliOcam2k_setBinning2x2Mode_V2.argtypes = [ctypes.c_void_p]
	LibLoader.lib.FliOcam2k_setBinning2x2Mode_V2.restype = ctypes.c_bool
	def SetBinning2x2Mode(self, context):
		res = LibLoader.lib.FliOcam2k_setBinning2x2Mode_V2(context)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliOcam2k_setBinning3x3Mode_V2.argtypes = [ctypes.c_void_p]
	LibLoader.lib.FliOcam2k_setBinning3x3Mode_V2.restype = ctypes.c_bool
	def SetBinning3x3Mode(self, context):
		res = LibLoader.lib.FliOcam2k_setBinning3x3Mode_V2(context)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliOcam2k_setBinning4x4Mode_V2.argtypes = [ctypes.c_void_p]
	LibLoader.lib.FliOcam2k_setBinning4x4Mode_V2.restype = ctypes.c_bool
	def SetBinning4x4Mode(self, context):
		res = LibLoader.lib.FliOcam2k_setBinning4x4Mode_V2(context)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliOcam2k_getConf_V2.argtypes = [ctypes.c_void_p]
	LibLoader.lib.FliOcam2k_getConf_V2.restype = ctypes.c_bool
	def GetConf(self, context):
		res = LibLoader.lib.FliOcam2k_getConf_V2(context)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliOcam2k_protectionReset_V2.argtypes = [ctypes.c_void_p]
	LibLoader.lib.FliOcam2k_protectionReset_V2.restype = ctypes.c_bool
	def ProtectionReset(self, context):
		res = LibLoader.lib.FliOcam2k_protectionReset_V2(context)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliOcam2k_setBiasOffset_V2.argtypes = [ctypes.c_void_p, ctypes.c_int]
	LibLoader.lib.FliOcam2k_setBiasOffset_V2.restype = ctypes.c_bool
	def SetBiasOffset(self, context, int):
		res = LibLoader.lib.FliOcam2k_setBiasOffset_V2(context, int)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliOcam2k_setFpsMax_V2.argtypes = [ctypes.c_void_p]
	LibLoader.lib.FliOcam2k_setFpsMax_V2.restype = ctypes.c_bool
	def SetFpsMax(self, context):
		res = LibLoader.lib.FliOcam2k_setFpsMax_V2(context)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliOcam2k_setGain_V2.argtypes = [ctypes.c_void_p, ctypes.c_int]
	LibLoader.lib.FliOcam2k_setGain_V2.restype = ctypes.c_bool
	def SetGain(self, context, int):
		res = LibLoader.lib.FliOcam2k_setGain_V2(context, int)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliOcam2k_sendBiasFile_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
	LibLoader.lib.FliOcam2k_sendBiasFile_V2.restype = ctypes.c_bool
	def SendBiasFile(self, context, file):
		res = LibLoader.lib.FliOcam2k_sendBiasFile_V2(context, file.encode())
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliOcam2k_sendFlatFile_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
	LibLoader.lib.FliOcam2k_sendFlatFile_V2.restype = ctypes.c_bool
	def SendFlatFile(self, context, file):
		res = LibLoader.lib.FliOcam2k_sendFlatFile_V2(context, file.encode())
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliOcam2k_getCoolingState_V2.argtypes = [ctypes.c_void_p]
	LibLoader.lib.FliOcam2k_getCoolingState_V2.restype = ctypes.c_bool
	def GetCoolingState(self, context):
		res = LibLoader.lib.FliOcam2k_getCoolingState_V2(context)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliOcam2k_getCoolingValue_V2.argtypes = [ctypes.c_void_p, ctypes.c_int]
	LibLoader.lib.FliOcam2k_getCoolingValue_V2.restype = ctypes.c_bool
	def GetCoolingValue(self, context, val):
		res = LibLoader.lib.FliOcam2k_getCoolingValue_V2(context, val)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliOcam2k_setCoolingValue_V2.argtypes = [ctypes.c_void_p, ctypes.c_int]
	LibLoader.lib.FliOcam2k_setCoolingValue_V2.restype = ctypes.c_bool
	def SetCoolingValue(self, context, val):
		res = LibLoader.lib.FliOcam2k_setCoolingValue_V2(context, val)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliOcam2k_resetCoolingAlarm_V2.argtypes = [ctypes.c_void_p]
	LibLoader.lib.FliOcam2k_resetCoolingAlarm_V2.restype = ctypes.c_bool
	def ResetCoolingAlarm(self, context):
		res = LibLoader.lib.FliOcam2k_resetCoolingAlarm_V2(context)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliOcam2k_disableCooling_V2.argtypes = [ctypes.c_void_p]
	LibLoader.lib.FliOcam2k_disableCooling_V2.restype = ctypes.c_bool
	def DisableCooling(self, context):
		res = LibLoader.lib.FliOcam2k_disableCooling_V2(context)
		return res

