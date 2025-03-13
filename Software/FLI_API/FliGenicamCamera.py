import LibLoader
import ctypes

bufferSize = ctypes.c_size_t(1000)
charBuffer = ctypes.create_string_buffer(bufferSize.value)

class FliGenicamCamera:
	#------------------------------------------------------------
	LibLoader.lib.FliGenicamCamera_getStringFeature_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_size_t]
	LibLoader.lib.FliGenicamCamera_getStringFeature_V2.restype = ctypes.c_bool
	def GetStringFeature(self, context, feature):
		fps = ctypes.c_double(0)
		res = LibLoader.lib.FliGenicamCamera_getStringFeature_V2(context, feature.encode(), charBuffer, bufferSize)
		return res, charBuffer.value.decode('utf-8', 'ignore')

    #------------------------------------------------------------
	LibLoader.lib.FliGenicamCamera_setStringFeature_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_char_p]
	LibLoader.lib.FliGenicamCamera_setStringFeature_V2.restype = ctypes.c_bool
	def SetStringFeature(self, context, feature, val):
		fps = ctypes.c_double(0)
		res = LibLoader.lib.FliGenicamCamera_setStringFeature_V2(context, feature.encode(), val.encode())
		return res

    #------------------------------------------------------------
	LibLoader.lib.FliGenicamCamera_getDoubleFeature_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.POINTER(ctypes.c_double)]
	LibLoader.lib.FliGenicamCamera_getDoubleFeature_V2.restype = ctypes.c_bool
	def GetDoubleFeature(self, context, feature):
		val = ctypes.c_double(0)
		res = LibLoader.lib.FliGenicamCamera_getDoubleFeature_V2(context, feature.encode(), ctypes.byref(val))
		return res, val.value

    #------------------------------------------------------------
	LibLoader.lib.FliGenicamCamera_setDoubleFeature_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_double]
	LibLoader.lib.FliGenicamCamera_setDoubleFeature_V2.restype = ctypes.c_bool
	def SetDoubleFeature(self, context, feature, val):
		res = LibLoader.lib.FliGenicamCamera_setDoubleFeature_V2(context, feature.encode(), val)
		return res

    #------------------------------------------------------------
	LibLoader.lib.FliGenicamCamera_getIntegerFeature_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.POINTER(ctypes.c_int64)]
	LibLoader.lib.FliGenicamCamera_getIntegerFeature_V2.restype = ctypes.c_bool
	def GetIntegerFeature(self, context, feature):
		val = ctypes.c_int64(0)
		res = LibLoader.lib.FliGenicamCamera_getIntegerFeature_V2(context, feature.encode(), ctypes.byref(val))
		return res, val.value

    #------------------------------------------------------------
	LibLoader.lib.FliGenicamCamera_setIntegerFeature_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_int64]
	LibLoader.lib.FliGenicamCamera_setIntegerFeature_V2.restype = ctypes.c_bool
	def SetIntegerFeature(self, context, feature, val):
		res = LibLoader.lib.FliGenicamCamera_setIntegerFeature_V2(context, feature.encode(), val)
		return res

    #------------------------------------------------------------
	LibLoader.lib.FliGenicamCamera_getBooleanFeature_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.POINTER(ctypes.c_bool)]
	LibLoader.lib.FliGenicamCamera_getBooleanFeature_V2.restype = ctypes.c_bool
	def GetBooleanFeature(self, context, feature):
		val = ctypes.c_bool(0)
		res = LibLoader.lib.FliGenicamCamera_getBooleanFeature_V2(context, feature.encode(), ctypes.byref(val))
		return res, val.value

    #------------------------------------------------------------
	LibLoader.lib.FliGenicamCamera_setBooleanFeature_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_bool]
	LibLoader.lib.FliGenicamCamera_setBooleanFeature_V2.restype = ctypes.c_bool
	def SetBooleanFeature(self, context, feature, val):
		res = LibLoader.lib.FliGenicamCamera_setBooleanFeature_V2(context, feature.encode(), val)
		return res

    #------------------------------------------------------------
	LibLoader.lib.FliGenicamCamera_executeFeature_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
	LibLoader.lib.FliGenicamCamera_executeFeature_V2.restype = ctypes.c_bool
	def ExecuteFeature(self, context, feature):
		res = LibLoader.lib.FliGenicamCamera_executeFeature_V2(context, feature.encode())
		return res

    #------------------------------------------------------------
	LibLoader.lib.FliGenicamCamera_getDoubleMinFeature_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.POINTER(ctypes.c_double)]
	LibLoader.lib.FliGenicamCamera_getDoubleMinFeature_V2.restype = ctypes.c_bool
	def GetDoubleMinFeature(self, context, feature):
		val = ctypes.c_double(0)
		res = LibLoader.lib.FliGenicamCamera_getDoubleMinFeature_V2(context, feature.encode(), ctypes.byref(val))
		return res, val.value

    #------------------------------------------------------------
	LibLoader.lib.FliGenicamCamera_getDoubleMaxFeature_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.POINTER(ctypes.c_double)]
	LibLoader.lib.FliGenicamCamera_getDoubleMaxFeature_V2.restype = ctypes.c_bool
	def GetDoubleMaxFeature(self, context, feature):
		val = ctypes.c_double(0)
		res = LibLoader.lib.FliGenicamCamera_getDoubleMaxFeature_V2(context, feature.encode(), ctypes.byref(val))
		return res, val.value

    #------------------------------------------------------------
	LibLoader.lib.FliGenicamCamera_getIntegerMinFeature_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.POINTER(ctypes.c_int64)]
	LibLoader.lib.FliGenicamCamera_getIntegerMinFeature_V2.restype = ctypes.c_bool
	def GetIntegerMinFeature(self, context, feature):
		val = ctypes.c_int64(0)
		res = LibLoader.lib.FliGenicamCamera_getIntegerMinFeature_V2(context, feature.encode(), ctypes.byref(val))
		return res, val.value
    
    #------------------------------------------------------------
	LibLoader.lib.FliGenicamCamera_getIntegerMaxFeature_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.POINTER(ctypes.c_int64)]
	LibLoader.lib.FliGenicamCamera_getIntegerMaxFeature_V2.restype = ctypes.c_bool
	def GetIntegerMaxFeature(self, context, feature):
		val = ctypes.c_int64(0)
		res = LibLoader.lib.FliGenicamCamera_getIntegerMaxFeature_V2(context, feature.encode(), ctypes.byref(val))
		return res, val.value

    #------------------------------------------------------------
	LibLoader.lib.FliGenicamCamera_getDoubleIncrementFeature_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.POINTER(ctypes.c_double)]
	LibLoader.lib.FliGenicamCamera_getDoubleIncrementFeature_V2.restype = ctypes.c_bool
	def GetDoubleIncrementFeature(self, context, feature):
		val = ctypes.c_double(0)
		res = LibLoader.lib.FliGenicamCamera_getDoubleIncrementFeature_V2(context, feature.encode(), ctypes.byref(val))
		return res, val.value

    #------------------------------------------------------------
	LibLoader.lib.FliGenicamCamera_getIntegerIncrementFeature_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.POINTER(ctypes.c_int64)]
	LibLoader.lib.FliGenicamCamera_getIntegerIncrementFeature_V2.restype = ctypes.c_bool
	def GetIntegerIncrementFeature(self, context, feature):
		val = ctypes.c_int64(0)
		res = LibLoader.lib.FliGenicamCamera_getIntegerIncrementFeature_V2(context, feature.encode(), ctypes.byref(val))
		return res, val.value

    #------------------------------------------------------------
	LibLoader.lib.FliGenicamCamera_getPollingInterval_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.POINTER(ctypes.c_int64)]
	LibLoader.lib.FliGenicamCamera_getPollingInterval_V2.restype = ctypes.c_bool
	def GetPollingInterval(self, context, feature):
		val = ctypes.c_int64(0)
		res = LibLoader.lib.FliGenicamCamera_getPollingInterval_V2(context, feature.encode(), ctypes.byref(val))
		return res, val.value
