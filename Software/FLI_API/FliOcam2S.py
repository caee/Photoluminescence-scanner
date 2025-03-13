import LibLoader
import ctypes
import numpy as np

bufferSize = ctypes.c_size_t(1000)
charBuffer = ctypes.create_string_buffer(bufferSize.value)

class FliOcam2S:
	#------------------------------------------------------------
	LibLoader.lib.FliOcam2s_enableShutter_V2.argtypes = [ctypes.c_void_p, ctypes.c_bool]
	LibLoader.lib.FliOcam2s_enableShutter_V2.restype = ctypes.c_bool
	def EnableShutter(self, context, enable):
		res = LibLoader.lib.FliOcam2s_enableShutter_V2(context, enable)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliOcam2s_setShutterInternal_V2.argtypes = [ctypes.c_void_p]
	LibLoader.lib.FliOcam2s_setShutterInternal_V2.restype = ctypes.c_bool
	def SetShutterInternal(self, context):
		res = LibLoader.lib.FliOcam2s_setShutterInternal_V2(context)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliOcam2s_setShutterExternal_V2.argtypes = [ctypes.c_void_p]
	LibLoader.lib.FliOcam2s_setShutterExternal_V2.restype = ctypes.c_bool
	def SetShutterExternal(self, context):
		res = LibLoader.lib.FliOcam2s_setShutterExternal_V2(context)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliOcam2s_setShutterSingle_V2.argtypes = [ctypes.c_void_p]
	LibLoader.lib.FliOcam2s_setShutterSingle_V2.restype = ctypes.c_bool
	def SetShutterSingle(self, context):
		res = LibLoader.lib.FliOcam2s_setShutterSingle_V2(context)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliOcam2s_setShutterBurst_V2.argtypes = [ctypes.c_void_p]
	LibLoader.lib.FliOcam2s_setShutterBurst_V2.restype = ctypes.c_bool
	def SetShutterBurst(self, context):
		res = LibLoader.lib.FliOcam2s_setShutterBurst_V2(context)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliOcam2s_setShutterSweepMode_V2.argtypes = [ctypes.c_void_p, ctypes.c_int]
	LibLoader.lib.FliOcam2s_setShutterSweepMode_V2.restype = ctypes.c_bool
	def SetShutterSweepMode(self, context, int):
		res = LibLoader.lib.FliOcam2s_setShutterSweepMode_V2(context, int)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliOcam2s_setShutterPulseWidth_V2.argtypes = [ctypes.c_void_p, ctypes.c_int]
	LibLoader.lib.FliOcam2s_setShutterPulseWidth_V2.restype = ctypes.c_bool
	def SetShutterPulseWidth(self, context, int):
		res = LibLoader.lib.FliOcam2s_setShutterPulseWidth_V2(context, int)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliOcam2s_setShutterBlanking_V2.argtypes = [ctypes.c_void_p, ctypes.c_int]
	LibLoader.lib.FliOcam2s_setShutterBlanking_V2.restype = ctypes.c_bool
	def SetShutterBlanking(self, context, int):
		res = LibLoader.lib.FliOcam2s_setShutterBlanking_V2(context, int)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliOcam2s_setShutterPulsePosition_V2.argtypes = [ctypes.c_void_p, ctypes.c_int]
	LibLoader.lib.FliOcam2s_setShutterPulsePosition_V2.restype = ctypes.c_bool
	def SetShutterPulsePosition(self, context, int):
		res = LibLoader.lib.FliOcam2s_setShutterPulsePosition_V2(context, int)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliOcam2s_setShutterStep_V2.argtypes = [ctypes.c_void_p, ctypes.c_int]
	LibLoader.lib.FliOcam2s_setShutterStep_V2.restype = ctypes.c_bool
	def SetShutterStep(self, context, int):
		res = LibLoader.lib.FliOcam2s_setShutterStep_V2(context, int)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliOcam2s_setShutterEnd_V2.argtypes = [ctypes.c_void_p, ctypes.c_int]
	LibLoader.lib.FliOcam2s_setShutterEnd_V2.restype = ctypes.c_bool
	def SetShutterEnd(self, context, int):
		res = LibLoader.lib.FliOcam2s_setShutterEnd_V2(context, int)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliOcam2s_setShutterPulseCount_V2.argtypes = [ctypes.c_void_p, ctypes.c_int]
	LibLoader.lib.FliOcam2s_setShutterPulseCount_V2.restype = ctypes.c_bool
	def SetShutterPulseCount(self, context, int):
		res = LibLoader.lib.FliOcam2s_setShutterPulseCount_V2(context, int)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliOcam2s_enableShutterBlockOnRead_V2.argtypes = [ctypes.c_void_p, ctypes.c_bool]
	LibLoader.lib.FliOcam2s_enableShutterBlockOnRead_V2.restype = ctypes.c_bool
	def EnableShutterBlockOnRead(self, context, enable):
		res = LibLoader.lib.FliOcam2s_enableShutterBlockOnRead_V2(context, enable)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliOcam2s_enableShutterCorrectGlitch_V2.argtypes = [ctypes.c_void_p, ctypes.c_bool]
	LibLoader.lib.FliOcam2s_enableShutterCorrectGlitch_V2.restype = ctypes.c_bool
	def EnableShutterCorrectGlitch(self, context, enable):
		res = LibLoader.lib.FliOcam2s_enableShutterCorrectGlitch_V2(context, enable)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliOcam2s_sendShutterBias_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
	LibLoader.lib.FliOcam2s_sendShutterBias_V2.restype = ctypes.c_bool
	def SendShutterBias(self, context, file):
		res = LibLoader.lib.FliOcam2s_sendShutterBias_V2(context, file.encode())
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliOcam2s_getShutterState_V2.argtypes = [ctypes.c_void_p]
	LibLoader.lib.FliOcam2s_getShutterState_V2.restype = ctypes.c_bool
	def GetShutterState(self, context):
		res = LibLoader.lib.FliOcam2s_getShutterState_V2(context)
		return res

