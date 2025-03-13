import LibLoader
import ctypes
import numpy as np

bufferSize = ctypes.c_size_t(1000)
charBuffer = ctypes.create_string_buffer(bufferSize.value)

class FliSerialCamera:
	#------------------------------------------------------------
	LibLoader.lib.FliSerialCamera_getFps_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_double)]
	LibLoader.lib.FliSerialCamera_getFps_V2.restype = ctypes.c_bool
	def GetFps(self, context):
		fps = ctypes.c_double(0)
		res = LibLoader.lib.FliSerialCamera_getFps_V2(context, ctypes.byref(fps))
		return res, fps.value

	#------------------------------------------------------------
	LibLoader.lib.FliSerialCamera_setFps_V2.argtypes = [ctypes.c_void_p, ctypes.c_double]
	LibLoader.lib.FliSerialCamera_setFps_V2.restype = ctypes.c_bool
	def SetFps(self, context, fps):
		res = LibLoader.lib.FliSerialCamera_setFps_V2(context, fps)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliSerialCamera_getFpsMax_V2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_double)]
	LibLoader.lib.FliSerialCamera_getFpsMax_V2.restype = ctypes.c_bool
	def GetFpsMax(self, context):
		fps = ctypes.c_double(0)
		res = LibLoader.lib.FliSerialCamera_getFpsMax_V2(context, ctypes.byref(fps))
		return res, fps.value

	#------------------------------------------------------------
	LibLoader.lib.FliSerialCamera_sendCommand_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_size_t]
	LibLoader.lib.FliSerialCamera_sendCommand_V2.restype = ctypes.c_bool
	def SendCommand(self, context, command):
		res = LibLoader.lib.FliSerialCamera_sendCommand_V2(context, command.encode(), charBuffer, bufferSize)
		return res, charBuffer.value.decode('utf-8', 'ignore')

	#------------------------------------------------------------
	LibLoader.lib.FliSerialCamera_enableBias_V2.argtypes = [ctypes.c_void_p, ctypes.c_bool]
	LibLoader.lib.FliSerialCamera_enableBias_V2.restype = ctypes.c_bool
	def EnableBias(self, context, enable):
		res = LibLoader.lib.FliSerialCamera_enableBias_V2(context, enable)
		return res

	#------------------------------------------------------------
	LibLoader.lib.FliSerialCamera_enableFlat_V2.argtypes = [ctypes.c_void_p, ctypes.c_bool]
	LibLoader.lib.FliSerialCamera_enableFlat_V2.restype = ctypes.c_bool
	def EnableFlat(self, context, enable):
		res = LibLoader.lib.FliSerialCamera_enableFlat_V2(context, enable)
		return res

