######################### DEPRECATED API PLEASE USE FLISDK_V2.PY ##############################

import ctypes
import os
import numpy as np

_DIRNAME = os.getenv('FLISDK_DIR')

if os.name == 'nt':
	lib = ctypes.cdll.LoadLibrary(_DIRNAME + "\\lib\\release\\FliSdk.dll")
	    
if os.name == 'posix':
	if "aarch64" in str(os.uname()):
		lib = ctypes.cdll.LoadLibrary(_DIRNAME + "/lib/libFliSdk.so")
	else:
		lib = ctypes.cdll.LoadLibrary(_DIRNAME + "/lib/release/libFliSdk.so")

class CroppingData(ctypes.Structure):
    _fields_=[("col1",ctypes.c_int16), ("col2",ctypes.c_int16), ("row1",ctypes.c_int16), ("row2",ctypes.c_int16), ("cred1Cols",ctypes.c_bool*10), ("cred1Rows",ctypes.c_bool*256)]

CWRAPPER = ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.c_void_p)

class Mode:
    Full = 0
    GrabOnly = 1
    ConfigOnly = 2

#-------------------------------------------------------------------#
lib.FliSdk_detectCameras.argtypes = [ctypes.POINTER(ctypes.c_int)]
lib.FliSdk_detectCameras.restype = ctypes.POINTER(ctypes.c_char_p)
def DetectCameras():
    nbCameras = ctypes.c_int(0)
    listOfCameras = lib.FliSdk_detectCameras(ctypes.byref(nbCameras))
    liste = []
    for i in range(nbCameras.value):
        liste.append(listOfCameras[i].decode("utf-8"))
    return liste, nbCameras.value

#-------------------------------------------------------------------#
lib.FliSdk_detectGrabbers.argtypes = [ctypes.POINTER(ctypes.c_int)]
lib.FliSdk_detectGrabbers.restype = ctypes.POINTER(ctypes.c_char_p)
def DetectGrabbers():
    nbGrabbers = ctypes.c_int(0)
    listOfGrabbers = lib.FliSdk_detectGrabbers(ctypes.byref(nbGrabbers))
    liste = []
    for i in range(nbGrabbers.value):
        liste.append(listOfGrabbers[i].decode("utf-8"))
    return liste, nbGrabbers.value

#-------------------------------------------------------------------#
lib.FliSdk_setGrabber.restype = ctypes.c_bool
def SetGrabber(grabberName):
    return lib.FliSdk_setGrabber(grabberName.encode())

#-------------------------------------------------------------------#
def SetMode(mode):
    if mode != Mode.Full and mode != Mode.GrabOnly and mode != Mode.ConfigOnly:
        return False

    lib.FliSdk_setMode(mode)
    return True

#-------------------------------------------------------------------#
def SetImageDimension(width, height):
    if width <= 0 or height <= 0:
        return False
    lib.FliSdk_setImageDimension(width, height)
    return True

#-------------------------------------------------------------------#
lib.FliSdk_update.restype = ctypes.c_bool
def Update():
    return lib.FliSdk_update()

#-------------------------------------------------------------------#
def Init():
    lib.FliSdk_init()

#-------------------------------------------------------------------#
def Exit():
    lib.FliSdk_exit()

#-------------------------------------------------------------------#
lib.FliSdk_display8bImage.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
def Display8bImage(image, windowName):
    lib.FliSdk_display8bImage(image, windowName.encode())

#-------------------------------------------------------------------#
lib.FliSdk_display16bImage.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
def Display16bImage(image, windowName):
    lib.FliSdk_display16bImage(image, windowName.encode())

#-------------------------------------------------------------------#
def SetCallBackNewImage(func, fps):
    lib.FliSdk_setCallbackNewImage(func, fps)

#-------------------------------------------------------------------#
lib.FliSdk_getDetectedCameras.argtypes = [ctypes.POINTER(ctypes.c_int)]
lib.FliSdk_getDetectedCameras.restype = ctypes.POINTER(ctypes.c_char_p)
def GetDetectedCameras():
    nbCameras = ctypes.c_int(0)
    listOfCameras = lib.FliSdk_getDetectedCameras(ctypes.byref(nbCameras))
    liste = []
    for i in range(nbCameras.value):
        liste.append(listOfCameras[i].decode("utf-8"))
    return liste, nbCameras.value

#-------------------------------------------------------------------#
lib.FliSdk_setCamera.restype = ctypes.c_bool
def SetCamera(cameraName):
    return lib.FliSdk_setCamera(cameraName.encode())

#-------------------------------------------------------------------#
lib.FliSdk_start.restype = ctypes.c_bool
def Start():
    return lib.FliSdk_start()

#-------------------------------------------------------------------#
lib.FliSdk_stop.restype = ctypes.c_bool
def Stop():
    return lib.FliSdk_stop()

#-------------------------------------------------------------------#
lib.FliSdk_isStarted.restype = ctypes.c_bool
def IsStarted():
    return lib.FliSdk_isStarted()

#-------------------------------------------------------------------#
lib.FliSdk_isCred.restype = ctypes.c_bool
def IsCred():
    return lib.FliSdk_isCred()

#-------------------------------------------------------------------#
lib.FliSdk_isCredOne.restype = ctypes.c_bool
def IsCredOne():
    return lib.FliSdk_isCredOne()

#-------------------------------------------------------------------#
lib.FliSdk_isCredTwo.restype = ctypes.c_bool
def IsCredTwo():
    return lib.FliSdk_isCredTwo()

#-------------------------------------------------------------------#
lib.FliSdk_isCredThree.restype = ctypes.c_bool
def IsCredThree():
    return lib.FliSdk_isCredThree()

#-------------------------------------------------------------------#
lib.FliSdk_isCblueOne.restype = ctypes.c_bool
def IsCblueOne():
    return lib.FliSdk_isCblueOne()

#-------------------------------------------------------------------#
lib.FliSdk_isSerialCamera.restype = ctypes.c_bool
def IsSerialCamera():
    return lib.FliSdk_isSerialCamera()

#-------------------------------------------------------------------#
lib.FliSdk_isCblueSfnc.restype = ctypes.c_bool
def IsCblueSfnc():
    return lib.FliSdk_isCblueSfnc()

#-------------------------------------------------------------------#
lib.FliSdk_isOcam2k.restype = ctypes.c_bool
def IsOcam2k():
    return lib.FliSdk_isOcam2k()

#-------------------------------------------------------------------#
lib.FliSdk_isOcam2s.restype = ctypes.c_bool
def IsOcam2s():
    return lib.FliSdk_isOcam2s()

#-------------------------------------------------------------------#
lib.FliSdk_getProcessedImage.argtypes = [ctypes.c_int]
lib.FliSdk_getProcessedImage.restype = ctypes.c_void_p
#return an address which can be used directly in Qt QImage
def GetProcessedImage(index):
    return lib.FliSdk_getProcessedImage(index)

#-------------------------------------------------------------------#
lib.FliSdk_getProcessedImage_lv.argtypes = [ctypes.c_int, ctypes.c_void_p]
def GetProcessedImageRGBANumpyArray(index):
    width, height = GetCurrentImageDimension()
    buffer = np.zeros((width,height), dtype=np.int)
    lib.FliSdk_getProcessedImage_lv(index, ctypes.c_void_p(buffer.ctypes.data))
    return buffer, width, height

#-------------------------------------------------------------------#
lib.FliSdk_getProcessedImage16b_lv.argtypes = [ctypes.c_int, ctypes.c_void_p]
def GetProcessedImageGrayscale16bNumpyArray(index):
    width, height = GetCurrentImageDimension()
    buffer = np.zeros((height,width), dtype=np.uint16)
    lib.FliSdk_getProcessedImage16b_lv(index, ctypes.c_void_p(buffer.ctypes.data))
    return buffer, width, height

#-------------------------------------------------------------------#
lib.FliSdk_getRawImage.argtypes = [ctypes.c_int]
lib.FliSdk_getRawImage.restype = ctypes.c_void_p
def GetRawImage(index):
    return lib.FliSdk_getRawImage(index)

#-------------------------------------------------------------------#
lib.FliSdk_getRawImage_lv.argtypes = [ctypes.c_int, ctypes.c_void_p]
def GetRawImageAsNumpyArray(index):
    width, height = GetCurrentImageDimension()
    buffer = np.zeros((height,width), dtype=np.uint16)
    lib.FliSdk_getRawImage_lv(index, ctypes.c_void_p(buffer.ctypes.data))
    return buffer, width, height

#-------------------------------------------------------------------#
def GetFps():
    return lib.FliSdk_getFps()

#-------------------------------------------------------------------#
lib.FliSdk_getCameraModelAsString.restype = ctypes.c_char_p
def GetCameraModel():
    return lib.FliSdk_getCameraModelAsString().decode('utf-8', 'ignore')

#-------------------------------------------------------------------#
lib.FliSdk_enableGrabN.restype = ctypes.c_bool
def EnableGrabN(nbFrames):
    return lib.FliSdk_enableGrabN(nbFrames)

#-------------------------------------------------------------------#
def DisableGrabN():
    return lib.FliSdk_disableGrabN()

#-------------------------------------------------------------------#
lib.FliSdk_isGrabNEnabled.restype = ctypes.c_bool
def IsGrabNEnabled():
    return lib.FliSdk_isGrabNEnabled()

#-------------------------------------------------------------------#
lib.FliSdk_isGrabNFinished.restype = ctypes.c_bool
def IsGrabNFinished():
    return lib.FliSdk_isGrabNFinished()

#-------------------------------------------------------------------#
def GetBufferFilling():
    return lib.FliSdk_getBufferFilling()

#-------------------------------------------------------------------#
def SetBufferSize(sizeMo):
    return lib.FliSdk_setBufferSize(sizeMo)

#-------------------------------------------------------------------#
def ResetBuffer():
    lib.FliSdk_resetBuffer()

#-------------------------------------------------------------------#
lib.FliSdk_saveBuffer.argtypes = [ctypes.c_char_p, ctypes.c_int, ctypes.c_int]
def SaveBuffer(path, startIndex, endIndex):
    return lib.FliSdk_saveBuffer(path.encode(), startIndex, endIndex)

#-------------------------------------------------------------------#
def GetImagesCapacity():
    return lib.FliSdk_getImagesCapacity()

#-------------------------------------------------------------------#
lib.FliSdk_getColormapList.argtypes = [ctypes.POINTER(ctypes.c_int)]
lib.FliSdk_getColormapList.restype = ctypes.POINTER(ctypes.c_char_p)
def GetColormapList():
    nbColormap = ctypes.c_int(0)
    listOfColormap = lib.FliSdk_getColormapList(ctypes.byref(nbColormap))
    liste = []
    for i in range(nbColormap.value):
        liste.append(listOfColormap[i].decode("utf-8"))
    return liste, nbColormap.value

#-------------------------------------------------------------------#
def SetColormap(colormap):
    return lib.FliSdk_setColorMap(colormap.encode())

#-------------------------------------------------------------------#
lib.FliSdk_getClippingList.argtypes = [ctypes.POINTER(ctypes.c_int)]
lib.FliSdk_getClippingList.restype = ctypes.POINTER(ctypes.c_char_p)
def GetClippingList():
    nbClipping = ctypes.c_int(0)
    listOfClipping = lib.FliSdk_getClippingList(ctypes.byref(nbClipping))
    liste = []
    for i in range(nbClipping.value):
        liste.append(listOfClipping[i].decode("utf-8"))
    return liste, nbClipping.value

#-------------------------------------------------------------------#
def SetClippingType(clipping):
    return lib.FliSdk_setClippingType(clipping.encode())

#-------------------------------------------------------------------#
lib.FliSdk_setGamma.argtypes = [ctypes.c_double]
def SetGamma(gamma):
    lib.FliSdk_setGamma(gamma)

#-------------------------------------------------------------------#
def Clip(x, y, width, height):
    lib.FliSdk_clip(x, y, width, height)

#-------------------------------------------------------------------#
def SetRotationAngle(angle):
    lib.FliSdk_setRotationAngle(angle)

#-------------------------------------------------------------------#
def EnableDisplayInfos(enable):
    lib.FliSdk_enableDisplayInfos(enable)

#-------------------------------------------------------------------#
def EnableSharpen(enable):
    lib.FliSdk_enableSharpen(enable)

#-------------------------------------------------------------------#
def GetCurrentImageDimension():
    width = ctypes.c_int(0)
    height = ctypes.c_int(0)
    lib.FliSdk_getCurrentImageDimension(ctypes.byref(width), ctypes.byref(height))
    return width.value, height.value

#-------------------------------------------------------------------#
lib.FliSdk_loadBuffer.argtypes = [ctypes.c_char_p, ctypes.POINTER(CroppingData)]
def LoadBuffer(path, bufferCrop):
    return lib.FliSdk_loadBuffer(path.encode(),bufferCrop)

#-------------------------------------------------------------------#
lib.FliSdk_isCroppingDataValid.argtypes = [CroppingData]
def IsCroppingDataValid(cropData):
    return lib.FliSdk_isCroppingDataValid(cropData)

#-------------------------------------------------------------------#
lib.FliSdk_getCroppingState.argtypes = [ctypes.POINTER(ctypes.c_bool), ctypes.POINTER(CroppingData)]
def GetCroppingState():
    isEnabled = ctypes.c_bool(1)
    cropData = CroppingData(0,0,0,0)
    res = lib.FliSdk_getCroppingState(ctypes.byref(isEnabled),ctypes.byref(cropData))
    return res, isEnabled.value, cropData

#-------------------------------------------------------------------#
lib.FliSdk_setCroppingState.argtypes = [ctypes.c_bool, CroppingData]
def SetCroppingState(enable, cropData):
    return lib.FliSdk_setCroppingState(enable,cropData)

#-------------------------------------------------------------------#
def SendCommand(command):
    response = ctypes.create_string_buffer(200)
    res = lib.FliCamera_sendCommand(command.encode(),ctypes.byref(response))
    return res, response.value.decode('utf-8', 'ignore')

#-------------------------------------------------------------------#
def GetAllTemp():
    cameraModel = GetCameraModel()
    if cameraModel == "Cred2":
        mbTemp = ctypes.c_double(0.0)
        feTemp = ctypes.c_double(0.0)
        pwTemp = ctypes.c_double(0.0)
        sensorTemp = ctypes.c_double(0.0)
        peltierTemp = ctypes.c_double(0.0)
        heatsinkTemp = ctypes.c_double(0.0)
        res = lib.Cred2_getAllTemp(ctypes.byref(mbTemp), ctypes.byref(feTemp), ctypes.byref(pwTemp), ctypes.byref(sensorTemp), ctypes.byref(peltierTemp), ctypes.byref(heatsinkTemp))
        return res, mbTemp.value, feTemp.value, pwTemp.value, sensorTemp.value, peltierTemp.value, heatsinkTemp.value
    elif cameraModel == "Cred3":
        cpu = ctypes.c_double(0.0)
        backend = ctypes.c_double(0.0)
        interface = ctypes.c_double(0.0)
        ambiant = ctypes.c_double(0.0)
        sensor = ctypes.c_double(0.0)
        res = lib.Cred3_getAllTemp(ctypes.byref(cpu), ctypes.byref(backend), ctypes.byref(interface), ctypes.byref(ambiant), ctypes.byref(sensor))
        return res, cpu.value, backend.value, interface.value, ambiant.value, sensor.value
    elif cameraModel == "Cred1":
        mb = ctypes.c_double(0.0)
        fe = ctypes.c_double(0.0)
        pw = ctypes.c_double(0.0)
        cryod = ctypes.c_double(0.0)
        cryopt = ctypes.c_double(0.0)
        water = ctypes.c_double(0.0)
        peltier = ctypes.c_double(0.0)
        ptmcu = ctypes.c_double(0.0)
        res = lib.Cred1_getAllTemp(ctypes.byref(mb), ctypes.byref(fe), ctypes.byref(pw), ctypes.byref(cryod), ctypes.byref(cryopt), ctypes.byref(water), ctypes.byref(peltier), ctypes.byref(ptmcu))
        return res, mb.value, fe.value, pw.value, cryod.value, cryopt.value, water.value, peltier.value, ptmcu.value
    return False, 0.0

#-------------------------------------------------------------------#
def GetMaxTintItr():
    res = False
    cameraModel = GetCameraModel()
    tint = ctypes.c_double(0.0)
    if cameraModel == "Cred2":
        res = lib.Cred2_getMaxTintItr(ctypes.byref(tint))
    elif cameraModel == "Cred3":
        res = lib.Cred2_getMaxTintItr(ctypes.byref(tint))
    return res, tint.value

#-------------------------------------------------------------------#
def GetTint():
    res = False
    cameraModel = GetCameraModel()
    tint = ctypes.c_double(0.0)
    if cameraModel == "Cred2":
        res = lib.Cred2_getTint(ctypes.byref(tint))
    elif cameraModel == "Cred3":
        res = lib.Cred3_getTint(ctypes.byref(tint))
    elif cameraModel == "Cred1":
        res, fps = GetFpsParameter()
        tint = 1/fps
    elif cameraModel == "Ocam2k":
        res, fps = GetFpsParameter()
        tint = 1/fps
    elif cameraModel == "Ocam2s":
        res, fps = GetFpsParameter()
        tint = 1/fps
    return res, tint.value

#-------------------------------------------------------------------#
lib.Cred2_setTint.argtypes = [ctypes.c_double]
lib.Cred3_setTint.argtypes = [ctypes.c_double]
def SetTint(tint):
    res = False
    cameraModel = GetCameraModel()
    if cameraModel == "Cred2":
        res = lib.Cred2_setTint(tint)
    elif cameraModel == "Cred3":
        res = lib.Cred3_setTint(tint)
    elif cameraModel == "Cred1":
        res = SetFpsParameter(1/tint)
    elif cameraModel == "Ocam2k":
        res = SetFpsParameter(1/tint)
    elif cameraModel == "Ocam2s":
        res = SetFpsParameter(1/tint)
    return res

#-------------------------------------------------------------------#
def GetConversionGain():
    res = False
    conversionGain = ctypes.create_string_buffer(50)
    cameraModel = GetCameraModel()
    if cameraModel == "Cred2":
        res = lib.Cred2_getSensibility(ctypes.byref(conversionGain))
    elif cameraModel == "Cred3":
        res = lib.Cred3_getSensibility(ctypes.byref(conversionGain))
    return res, conversionGain.value.decode('utf-8', 'ignore')

#-------------------------------------------------------------------#
def SetConversionGain(conversionGain):
    res = False
    cameraModel = GetCameraModel()
    if cameraModel == "Cred2":
        res = lib.Cred2_setSensibility(conversionGain.encode())
    elif cameraModel == "Cred3":
        res = lib.Cred3_setSensibility(conversionGain.encode())
    return res

#-------------------------------------------------------------------#
def GetTintMax():
    res = False
    tint = ctypes.c_double(0.0)
    cameraModel = GetCameraModel()
    if cameraModel == "Cred2":
        res = lib.Cred2_getTintMax(ctypes.byref(tint))
    elif cameraModel == "Cred3":
        res = lib.Cred3_getTintMax(ctypes.byref(tint))
    return res, tint.value

#-------------------------------------------------------------------#
def GetAntiBloomingState():
    res = False
    state = ctypes.c_bool(False)
    cameraModel = GetCameraModel()
    if cameraModel == "Cred2":
        res = lib.Cred2_getAntiBloomingState(ctypes.byref(state))
    elif cameraModel == "Cred3":
        res = lib.Cred3_getAntiBloomingState(ctypes.byref(state))
    return res, state.value

#-------------------------------------------------------------------#
def SetAntiBloomingState(enable):
    res = False
    cameraModel = GetCameraModel()
    if cameraModel == "Cred2":
        res = lib.Cred2_enableAntiBlooming(enable)
    elif cameraModel == "Cred3":
        res = lib.Cred3_enableAntiBlooming(enable)
    return res

#-------------------------------------------------------------------#
def GetBadPixelState():
    res = False
    state = ctypes.c_bool(False)
    cameraModel = GetCameraModel()
    if cameraModel == "Cred2":
        res = lib.Cred2_getBadPixelState(ctypes.byref(state))
    elif cameraModel == "Cred3":
        res = lib.Cred3_getBadPixelState(ctypes.byref(state))
    return res, state.value

#-------------------------------------------------------------------#
def SetBadPixelState(enable):
    res = False
    cameraModel = GetCameraModel()
    if cameraModel == "Cred2":
        res = lib.Cred2_enableBadPixel(enable)
    elif cameraModel == "Cred3":
        res = lib.Cred3_enableBadPixel(enable)
    return res

#-------------------------------------------------------------------#
def GetTempSnakeSetpoint():
    res = False
    temp = ctypes.c_double(0.0)
    cameraModel = GetCameraModel()
    if cameraModel == "Cred2":
        res = lib.Cred2_getTempSnakeSetPoint(ctypes.byref(temp))
    return res, temp.value

#-------------------------------------------------------------------#
lib.Cred2_setTempSnakeSetPoint.argtypes = [ctypes.c_double]
def SetTempSnakeSetpoint(temp):
    res = False
    cameraModel = GetCameraModel()
    if cameraModel == "Cred2":
        res = lib.Cred2_setTempSnakeSetPoint(temp)
    return res

#-------------------------------------------------------------------#
def GetFpsParameter():
    fps = ctypes.c_double(0.0)
    res = lib.FliSerialCamera_getFps(ctypes.byref(fps))
    return res, fps.value

#-------------------------------------------------------------------#
lib.FliSerialCamera_setFps.argtypes = [ctypes.c_double]
def SetFpsParameter(fps):
    return lib.FliSerialCamera_setFps(fps)

#-------------------------------------------------------------------#
def GetFpsMaxParameter():
    fps = ctypes.c_double(0.0)
    res = lib.FliSerialCamera_getFpsMax(ctypes.byref(fps))
    return res, fps.value

#-------------------------------------------------------------------#
def GetBiasState():
    state = ctypes.c_bool(False)
    res = lib.FliCamera_getBiasState(ctypes.byref(state))
    return res, state.value

#-------------------------------------------------------------------#
def SetBiasState(enable):
    return lib.FliSerialCamera_enableBias(enable)

#-------------------------------------------------------------------#
def BuildBias():
    return lib.FliCamera_buildBias()

#-------------------------------------------------------------------#
def ShutdownCamera():
    return lib.FliCamera_shutDown()

#-------------------------------------------------------------------#
def GetStatusDetailed():
    status = ctypes.create_string_buffer(50)
    diag = ctypes.create_string_buffer(50)
    res = lib.FliCamera_getStatusDetailed(ctypes.byref(status), ctypes.byref(diag))
    return res, status.value.decode('utf-8', 'ignore'), diag.value.decode('utf-8', 'ignore')

#-------------------------------------------------------------------#
def Ocam2_setStandardMode():
    return lib.Ocam2k_setStandardMode()

#-------------------------------------------------------------------#
def Ocam2_setBining2x2Mode():
    return lib.Ocam2k_setBinning2x2Mode()

#-------------------------------------------------------------------#
def Ocam2_setBining3x3Mode():
    return lib.Ocam2k_setBinning3x3Mode()

#-------------------------------------------------------------------#
def Ocam2_setBining4x4Mode():
    return lib.Ocam2k_setBinning4x4Mode()

#-------------------------------------------------------------------#
def Ocam2_setCropping240x120Mode():
    return lib.Ocam2k_setCropping240x120Mode()

#-------------------------------------------------------------------#
def Ocam2_setCropping240x128Mode():
    return lib.Ocam2k_setCropping240x128Mode()

#------------------------------------------------------------
lib.CblueSfnc_getDeviceScanType.argtypes = [ctypes.POINTER(ctypes.c_int)]
lib.CblueSfnc_getDeviceScanType.restype = ctypes.c_bool
def CblueSfnc_getDeviceScanType():
	val = ctypes.c_int(0)
	res = lib.CblueSfnc_getDeviceScanType(ctypes.byref(val))
	return res, val.value

#------------------------------------------------------------
lib.CblueSfnc_getDeviceIndicatorMode.argtypes = [ctypes.POINTER(ctypes.c_int)]
lib.CblueSfnc_getDeviceIndicatorMode.restype = ctypes.c_bool
def CblueSfnc_getDeviceIndicatorMode():
	val = ctypes.c_int(0)
	res = lib.CblueSfnc_getDeviceIndicatorMode(ctypes.byref(val))
	return res, val.value

#------------------------------------------------------------
lib.CblueSfnc_setDeviceIndicatorMode.argtypes = [ctypes.c_int]
lib.CblueSfnc_setDeviceIndicatorMode.restype = ctypes.c_bool
def CblueSfnc_setDeviceIndicatorMode(val):
	return lib.CblueSfnc_setDeviceIndicatorMode(val)

#------------------------------------------------------------
lib.Cblue1_getDeviceTemperatureSelector.argtypes = [ctypes.POINTER(ctypes.c_int)]
lib.Cblue1_getDeviceTemperatureSelector.restype = ctypes.c_bool
def Cblue1_getDeviceTemperatureSelector():
	val = ctypes.c_int(0)
	res = lib.Cblue1_getDeviceTemperatureSelector(ctypes.byref(val))
	return res, val.value

#------------------------------------------------------------
lib.Cblue1_setDeviceTemperatureSelector.argtypes = [ctypes.c_int]
lib.Cblue1_setDeviceTemperatureSelector.restype = ctypes.c_bool
def Cblue1_setDeviceTemperatureSelector(val):
	return lib.Cblue1_setDeviceTemperatureSelector(val)

#------------------------------------------------------------
lib.Cblue1_getDeviceTecSelector.argtypes = [ctypes.POINTER(ctypes.c_int)]
lib.Cblue1_getDeviceTecSelector.restype = ctypes.c_bool
def Cblue1_getDeviceTecSelector():
	val = ctypes.c_int(0)
	res = lib.Cblue1_getDeviceTecSelector(ctypes.byref(val))
	return res, val.value

#------------------------------------------------------------
lib.Cblue1_setDeviceTecSelector.argtypes = [ctypes.c_int]
lib.Cblue1_setDeviceTecSelector.restype = ctypes.c_bool
def Cblue1_setDeviceTecSelector(val):
	return lib.Cblue1_setDeviceTecSelector(val)

#------------------------------------------------------------
lib.Cblue1_getDeviceFanMode.argtypes = [ctypes.POINTER(ctypes.c_int)]
lib.Cblue1_getDeviceFanMode.restype = ctypes.c_bool
def Cblue1_getDeviceFanMode():
	val = ctypes.c_int(0)
	res = lib.Cblue1_getDeviceFanMode(ctypes.byref(val))
	return res, val.value

#------------------------------------------------------------
lib.Cblue1_setDeviceFanMode.argtypes = [ctypes.c_int]
lib.Cblue1_setDeviceFanMode.restype = ctypes.c_bool
def Cblue1_setDeviceFanMode(val):
	return lib.Cblue1_setDeviceFanMode(val)

#------------------------------------------------------------
lib.Cblue1_getFirmwareUpdateStatus.argtypes = [ctypes.POINTER(ctypes.c_int)]
lib.Cblue1_getFirmwareUpdateStatus.restype = ctypes.c_bool
def Cblue1_getFirmwareUpdateStatus():
	val = ctypes.c_int(0)
	res = lib.Cblue1_getFirmwareUpdateStatus(ctypes.byref(val))
	return res, val.value

#------------------------------------------------------------
lib.Cblue1_getLogCollectStatus.argtypes = [ctypes.POINTER(ctypes.c_int)]
lib.Cblue1_getLogCollectStatus.restype = ctypes.c_bool
def Cblue1_getLogCollectStatus():
	val = ctypes.c_int(0)
	res = lib.Cblue1_getLogCollectStatus(ctypes.byref(val))
	return res, val.value

#------------------------------------------------------------
lib.Cblue1_getIPMode.argtypes = [ctypes.POINTER(ctypes.c_int)]
lib.Cblue1_getIPMode.restype = ctypes.c_bool
def Cblue1_getIPMode():
	val = ctypes.c_int(0)
	res = lib.Cblue1_getIPMode(ctypes.byref(val))
	return res, val.value

#------------------------------------------------------------
lib.Cblue1_setIPMode.argtypes = [ctypes.c_int]
lib.Cblue1_setIPMode.restype = ctypes.c_bool
def Cblue1_setIPMode(val):
	return lib.Cblue1_setIPMode(val)

#------------------------------------------------------------
lib.CblueSfnc_getSensorShutterMode.argtypes = [ctypes.POINTER(ctypes.c_int)]
lib.CblueSfnc_getSensorShutterMode.restype = ctypes.c_bool
def CblueSfnc_getSensorShutterMode():
	val = ctypes.c_int(0)
	res = lib.CblueSfnc_getSensorShutterMode(ctypes.byref(val))
	return res, val.value

#------------------------------------------------------------
lib.CblueSfnc_getRegionSelector.argtypes = [ctypes.POINTER(ctypes.c_int)]
lib.CblueSfnc_getRegionSelector.restype = ctypes.c_bool
def CblueSfnc_getRegionSelector():
	val = ctypes.c_int(0)
	res = lib.CblueSfnc_getRegionSelector(ctypes.byref(val))
	return res, val.value

#------------------------------------------------------------
lib.CblueSfnc_setRegionSelector.argtypes = [ctypes.c_int]
lib.CblueSfnc_setRegionSelector.restype = ctypes.c_bool
def CblueSfnc_setRegionSelector(val):
	return lib.CblueSfnc_setRegionSelector(val)

#------------------------------------------------------------
lib.CblueSfnc_getRegionMode.argtypes = [ctypes.POINTER(ctypes.c_int)]
lib.CblueSfnc_getRegionMode.restype = ctypes.c_bool
def CblueSfnc_getRegionMode():
	val = ctypes.c_int(0)
	res = lib.CblueSfnc_getRegionMode(ctypes.byref(val))
	return res, val.value

#------------------------------------------------------------
lib.CblueSfnc_getRegionDestination.argtypes = [ctypes.POINTER(ctypes.c_int)]
lib.CblueSfnc_getRegionDestination.restype = ctypes.c_bool
def CblueSfnc_getRegionDestination():
	val = ctypes.c_int(0)
	res = lib.CblueSfnc_getRegionDestination(ctypes.byref(val))
	return res, val.value

#------------------------------------------------------------
lib.CblueSfnc_setRegionDestination.argtypes = [ctypes.c_int]
lib.CblueSfnc_setRegionDestination.restype = ctypes.c_bool
def CblueSfnc_setRegionDestination(val):
	return lib.CblueSfnc_setRegionDestination(val)

#------------------------------------------------------------
lib.Cblue1_getSparseSelector.argtypes = [ctypes.POINTER(ctypes.c_int)]
lib.Cblue1_getSparseSelector.restype = ctypes.c_bool
def Cblue1_getSparseSelector():
	val = ctypes.c_int(0)
	res = lib.Cblue1_getSparseSelector(ctypes.byref(val))
	return res, val.value

#------------------------------------------------------------
lib.Cblue1_setSparseSelector.argtypes = [ctypes.c_int]
lib.Cblue1_setSparseSelector.restype = ctypes.c_bool
def Cblue1_setSparseSelector(val):
	return lib.Cblue1_setSparseSelector(val)

#------------------------------------------------------------
lib.Cblue1_getSparseMode.argtypes = [ctypes.POINTER(ctypes.c_int)]
lib.Cblue1_getSparseMode.restype = ctypes.c_bool
def Cblue1_getSparseMode():
	val = ctypes.c_int(0)
	res = lib.Cblue1_getSparseMode(ctypes.byref(val))
	return res, val.value

#------------------------------------------------------------
lib.Cblue1_setSparseMode.argtypes = [ctypes.c_int]
lib.Cblue1_setSparseMode.restype = ctypes.c_bool
def Cblue1_setSparseMode(val):
	return lib.Cblue1_setSparseMode(val)

#------------------------------------------------------------
lib.CblueSfnc_getPixelFormat.argtypes = [ctypes.POINTER(ctypes.c_int)]
lib.CblueSfnc_getPixelFormat.restype = ctypes.c_bool
def CblueSfnc_getPixelFormat():
	val = ctypes.c_int(0)
	res = lib.CblueSfnc_getPixelFormat(ctypes.byref(val))
	return res, val.value

#------------------------------------------------------------
lib.CblueSfnc_setPixelFormat.argtypes = [ctypes.c_int]
lib.CblueSfnc_setPixelFormat.restype = ctypes.c_bool
def CblueSfnc_setPixelFormat(val):
	return lib.CblueSfnc_setPixelFormat(val)

#------------------------------------------------------------
lib.Cblue1_getTestPatternGeneratorSelector.argtypes = [ctypes.POINTER(ctypes.c_int)]
lib.Cblue1_getTestPatternGeneratorSelector.restype = ctypes.c_bool
def Cblue1_getTestPatternGeneratorSelector():
	val = ctypes.c_int(0)
	res = lib.Cblue1_getTestPatternGeneratorSelector(ctypes.byref(val))
	return res, val.value

#------------------------------------------------------------
lib.Cblue1_setTestPatternGeneratorSelector.argtypes = [ctypes.c_int]
lib.Cblue1_setTestPatternGeneratorSelector.restype = ctypes.c_bool
def Cblue1_setTestPatternGeneratorSelector(val):
	return lib.Cblue1_setTestPatternGeneratorSelector(val)

#------------------------------------------------------------
lib.Cblue1_getTestPattern.argtypes = [ctypes.POINTER(ctypes.c_int)]
lib.Cblue1_getTestPattern.restype = ctypes.c_bool
def Cblue1_getTestPattern():
	val = ctypes.c_int(0)
	res = lib.Cblue1_getTestPattern(ctypes.byref(val))
	return res, val.value

#------------------------------------------------------------
lib.Cblue1_setTestPattern.argtypes = [ctypes.c_int]
lib.Cblue1_setTestPattern.restype = ctypes.c_bool
def Cblue1_setTestPattern(val):
	return lib.Cblue1_setTestPattern(val)

#------------------------------------------------------------
lib.CblueSfnc_getAcquisitionMode.argtypes = [ctypes.POINTER(ctypes.c_int)]
lib.CblueSfnc_getAcquisitionMode.restype = ctypes.c_bool
def CblueSfnc_getAcquisitionMode():
	val = ctypes.c_int(0)
	res = lib.CblueSfnc_getAcquisitionMode(ctypes.byref(val))
	return res, val.value

#------------------------------------------------------------
lib.CblueSfnc_setAcquisitionMode.argtypes = [ctypes.c_int]
lib.CblueSfnc_setAcquisitionMode.restype = ctypes.c_bool
def CblueSfnc_setAcquisitionMode(val):
	return lib.CblueSfnc_setAcquisitionMode(val)

#------------------------------------------------------------
lib.CblueSfnc_getExposureMode.argtypes = [ctypes.POINTER(ctypes.c_int)]
lib.CblueSfnc_getExposureMode.restype = ctypes.c_bool
def CblueSfnc_getExposureMode():
	val = ctypes.c_int(0)
	res = lib.CblueSfnc_getExposureMode(ctypes.byref(val))
	return res, val.value

#------------------------------------------------------------
lib.CblueSfnc_setExposureMode.argtypes = [ctypes.c_int]
lib.CblueSfnc_setExposureMode.restype = ctypes.c_bool
def CblueSfnc_setExposureMode(val):
	return lib.CblueSfnc_setExposureMode(val)

#------------------------------------------------------------
lib.Cblue1_getGlowReduction.argtypes = [ctypes.POINTER(ctypes.c_int)]
lib.Cblue1_getGlowReduction.restype = ctypes.c_bool
def Cblue1_getGlowReduction():
	val = ctypes.c_int(0)
	res = lib.Cblue1_getGlowReduction(ctypes.byref(val))
	return res, val.value

#------------------------------------------------------------
lib.Cblue1_setGlowReduction.argtypes = [ctypes.c_int]
lib.Cblue1_setGlowReduction.restype = ctypes.c_bool
def Cblue1_setGlowReduction(val):
	return lib.Cblue1_setGlowReduction(val)

#------------------------------------------------------------
lib.CblueSfnc_getGainSelector.argtypes = [ctypes.POINTER(ctypes.c_int)]
lib.CblueSfnc_getGainSelector.restype = ctypes.c_bool
def CblueSfnc_getGainSelector():
	val = ctypes.c_int(0)
	res = lib.CblueSfnc_getGainSelector(ctypes.byref(val))
	return res, val.value

#------------------------------------------------------------
lib.CblueSfnc_setGainSelector.argtypes = [ctypes.c_int]
lib.CblueSfnc_setGainSelector.restype = ctypes.c_bool
def CblueSfnc_setGainSelector(val):
	return lib.CblueSfnc_setGainSelector(val)

#------------------------------------------------------------
lib.CblueSfnc_getBlackLevelSelector.argtypes = [ctypes.POINTER(ctypes.c_int)]
lib.CblueSfnc_getBlackLevelSelector.restype = ctypes.c_bool
def CblueSfnc_getBlackLevelSelector():
	val = ctypes.c_int(0)
	res = lib.CblueSfnc_getBlackLevelSelector(ctypes.byref(val))
	return res, val.value

#------------------------------------------------------------
lib.CblueSfnc_setBlackLevelSelector.argtypes = [ctypes.c_int]
lib.CblueSfnc_setBlackLevelSelector.restype = ctypes.c_bool
def CblueSfnc_setBlackLevelSelector(val):
	return lib.CblueSfnc_setBlackLevelSelector(val)

#------------------------------------------------------------
lib.CblueSfnc_getBlackLevelAuto.argtypes = [ctypes.POINTER(ctypes.c_int)]
lib.CblueSfnc_getBlackLevelAuto.restype = ctypes.c_bool
def CblueSfnc_getBlackLevelAuto():
	val = ctypes.c_int(0)
	res = lib.CblueSfnc_getBlackLevelAuto(ctypes.byref(val))
	return res, val.value

#------------------------------------------------------------
lib.CblueSfnc_setBlackLevelAuto.argtypes = [ctypes.c_int]
lib.CblueSfnc_setBlackLevelAuto.restype = ctypes.c_bool
def CblueSfnc_setBlackLevelAuto(val):
	return lib.CblueSfnc_setBlackLevelAuto(val)

#------------------------------------------------------------
lib.Cblue1_getConversionEfficiency.argtypes = [ctypes.POINTER(ctypes.c_int)]
lib.Cblue1_getConversionEfficiency.restype = ctypes.c_bool
def Cblue1_getConversionEfficiency():
	val = ctypes.c_int(0)
	res = lib.Cblue1_getConversionEfficiency(ctypes.byref(val))
	return res, val.value

#------------------------------------------------------------
lib.Cblue1_setConversionEfficiency.argtypes = [ctypes.c_int]
lib.Cblue1_setConversionEfficiency.restype = ctypes.c_bool
def Cblue1_setConversionEfficiency(val):
	return lib.Cblue1_setConversionEfficiency(val)

#------------------------------------------------------------
lib.Cblue1_getUserSetSelector.argtypes = [ctypes.POINTER(ctypes.c_int)]
lib.Cblue1_getUserSetSelector.restype = ctypes.c_bool
def Cblue1_getUserSetSelector():
	val = ctypes.c_int(0)
	res = lib.Cblue1_getUserSetSelector(ctypes.byref(val))
	return res, val.value

#------------------------------------------------------------
lib.Cblue1_setUserSetSelector.argtypes = [ctypes.c_int]
lib.Cblue1_setUserSetSelector.restype = ctypes.c_bool
def Cblue1_setUserSetSelector(val):
	return lib.Cblue1_setUserSetSelector(val)

#------------------------------------------------------------
lib.Cblue1_getUserSetDefault.argtypes = [ctypes.POINTER(ctypes.c_int)]
lib.Cblue1_getUserSetDefault.restype = ctypes.c_bool
def Cblue1_getUserSetDefault():
	val = ctypes.c_int(0)
	res = lib.Cblue1_getUserSetDefault(ctypes.byref(val))
	return res, val.value

#------------------------------------------------------------
lib.Cblue1_setUserSetDefault.argtypes = [ctypes.c_int]
lib.Cblue1_setUserSetDefault.restype = ctypes.c_bool
def Cblue1_setUserSetDefault(val):
	return lib.Cblue1_setUserSetDefault(val)

#------------------------------------------------------------
lib.CblueSfnc_getCxpLinkConfigurationStatus.argtypes = [ctypes.POINTER(ctypes.c_int)]
lib.CblueSfnc_getCxpLinkConfigurationStatus.restype = ctypes.c_bool
def CblueSfnc_getCxpLinkConfigurationStatus():
	val = ctypes.c_int(0)
	res = lib.CblueSfnc_getCxpLinkConfigurationStatus(ctypes.byref(val))
	return res, val.value

#------------------------------------------------------------
lib.CblueSfnc_getCxpLinkConfigurationPreferred.argtypes = [ctypes.POINTER(ctypes.c_int)]
lib.CblueSfnc_getCxpLinkConfigurationPreferred.restype = ctypes.c_bool
def CblueSfnc_getCxpLinkConfigurationPreferred():
	val = ctypes.c_int(0)
	res = lib.CblueSfnc_getCxpLinkConfigurationPreferred(ctypes.byref(val))
	return res, val.value

#------------------------------------------------------------
lib.CblueSfnc_getCxpLinkConfiguration.argtypes = [ctypes.POINTER(ctypes.c_int)]
lib.CblueSfnc_getCxpLinkConfiguration.restype = ctypes.c_bool
def CblueSfnc_getCxpLinkConfiguration():
	val = ctypes.c_int(0)
	res = lib.CblueSfnc_getCxpLinkConfiguration(ctypes.byref(val))
	return res, val.value

#------------------------------------------------------------
lib.CblueSfnc_getCxpConnectionTestMode.argtypes = [ctypes.POINTER(ctypes.c_int)]
lib.CblueSfnc_getCxpConnectionTestMode.restype = ctypes.c_bool
def CblueSfnc_getCxpConnectionTestMode():
	val = ctypes.c_int(0)
	res = lib.CblueSfnc_getCxpConnectionTestMode(ctypes.byref(val))
	return res, val.value

#------------------------------------------------------------
lib.CblueSfnc_setCxpConnectionTestMode.argtypes = [ctypes.c_int]
lib.CblueSfnc_setCxpConnectionTestMode.restype = ctypes.c_bool
def CblueSfnc_setCxpConnectionTestMode(val):
	return lib.CblueSfnc_setCxpConnectionTestMode(val)

#------------------------------------------------------------
lib.CblueSfnc_getCxpSendReceiveSelector.argtypes = [ctypes.POINTER(ctypes.c_int)]
lib.CblueSfnc_getCxpSendReceiveSelector.restype = ctypes.c_bool
def CblueSfnc_getCxpSendReceiveSelector():
	val = ctypes.c_int(0)
	res = lib.CblueSfnc_getCxpSendReceiveSelector(ctypes.byref(val))
	return res, val.value

#------------------------------------------------------------
lib.CblueSfnc_setCxpSendReceiveSelector.argtypes = [ctypes.c_int]
lib.CblueSfnc_setCxpSendReceiveSelector.restype = ctypes.c_bool
def CblueSfnc_setCxpSendReceiveSelector(val):
	return lib.CblueSfnc_setCxpSendReceiveSelector(val)

#------------------------------------------------------------
lib.CblueSfnc_getCxpErrorCounterSelector.argtypes = [ctypes.POINTER(ctypes.c_int)]
lib.CblueSfnc_getCxpErrorCounterSelector.restype = ctypes.c_bool
def CblueSfnc_getCxpErrorCounterSelector():
	val = ctypes.c_int(0)
	res = lib.CblueSfnc_getCxpErrorCounterSelector(ctypes.byref(val))
	return res, val.value

#------------------------------------------------------------
lib.CblueSfnc_setCxpErrorCounterSelector.argtypes = [ctypes.c_int]
lib.CblueSfnc_setCxpErrorCounterSelector.restype = ctypes.c_bool
def CblueSfnc_setCxpErrorCounterSelector(val):
	return lib.CblueSfnc_setCxpErrorCounterSelector(val)

#------------------------------------------------------------
lib.CblueSfnc_getCxpErrorCounterStatus.argtypes = [ctypes.POINTER(ctypes.c_int)]
lib.CblueSfnc_getCxpErrorCounterStatus.restype = ctypes.c_bool
def CblueSfnc_getCxpErrorCounterStatus():
	val = ctypes.c_int(0)
	res = lib.CblueSfnc_getCxpErrorCounterStatus(ctypes.byref(val))
	return res, val.value

#------------------------------------------------------------
lib.CblueSfnc_getSensorWidth.argtypes = [ctypes.POINTER(ctypes.c_int)]
lib.CblueSfnc_getSensorWidth.restype = ctypes.c_bool
def CblueSfnc_getSensorWidth():
	val = ctypes.c_int(0)
	res = lib.CblueSfnc_getSensorWidth(ctypes.byref(val))
	return res, val.value

#------------------------------------------------------------
lib.CblueSfnc_getSensorHeight.argtypes = [ctypes.POINTER(ctypes.c_int)]
lib.CblueSfnc_getSensorHeight.restype = ctypes.c_bool
def CblueSfnc_getSensorHeight():
	val = ctypes.c_int(0)
	res = lib.CblueSfnc_getSensorHeight(ctypes.byref(val))
	return res, val.value

#------------------------------------------------------------
lib.CblueSfnc_getWidthMax.argtypes = [ctypes.POINTER(ctypes.c_int)]
lib.CblueSfnc_getWidthMax.restype = ctypes.c_bool
def CblueSfnc_getWidthMax():
	val = ctypes.c_int(0)
	res = lib.CblueSfnc_getWidthMax(ctypes.byref(val))
	return res, val.value

#------------------------------------------------------------
lib.CblueSfnc_getHeightMax.argtypes = [ctypes.POINTER(ctypes.c_int)]
lib.CblueSfnc_getHeightMax.restype = ctypes.c_bool
def CblueSfnc_getHeightMax():
	val = ctypes.c_int(0)
	res = lib.CblueSfnc_getHeightMax(ctypes.byref(val))
	return res, val.value

#------------------------------------------------------------
lib.CblueSfnc_getWidth.argtypes = [ctypes.POINTER(ctypes.c_int)]
lib.CblueSfnc_getWidth.restype = ctypes.c_bool
def CblueSfnc_getWidth():
	val = ctypes.c_int(0)
	res = lib.CblueSfnc_getWidth(ctypes.byref(val))
	return res, val.value

#------------------------------------------------------------
lib.CblueSfnc_setWidth.argtypes = [ctypes.c_int]
lib.CblueSfnc_setWidth.restype = ctypes.c_bool
def CblueSfnc_setWidth(val):
	return lib.CblueSfnc_setWidth(val)

#------------------------------------------------------------
lib.CblueSfnc_getHeight.argtypes = [ctypes.POINTER(ctypes.c_int)]
lib.CblueSfnc_getHeight.restype = ctypes.c_bool
def CblueSfnc_getHeight():
	val = ctypes.c_int(0)
	res = lib.CblueSfnc_getHeight(ctypes.byref(val))
	return res, val.value

#------------------------------------------------------------
lib.CblueSfnc_setHeight.argtypes = [ctypes.c_int]
lib.CblueSfnc_setHeight.restype = ctypes.c_bool
def CblueSfnc_setHeight(val):
	return lib.CblueSfnc_setHeight(val)

#------------------------------------------------------------
lib.CblueSfnc_getOffsetX.argtypes = [ctypes.POINTER(ctypes.c_int)]
lib.CblueSfnc_getOffsetX.restype = ctypes.c_bool
def CblueSfnc_getOffsetX():
	val = ctypes.c_int(0)
	res = lib.CblueSfnc_getOffsetX(ctypes.byref(val))
	return res, val.value

#------------------------------------------------------------
lib.CblueSfnc_setOffsetX.argtypes = [ctypes.c_int]
lib.CblueSfnc_setOffsetX.restype = ctypes.c_bool
def CblueSfnc_setOffsetX(val):
	return lib.CblueSfnc_setOffsetX(val)

#------------------------------------------------------------
lib.CblueSfnc_getOffsetY.argtypes = [ctypes.POINTER(ctypes.c_int)]
lib.CblueSfnc_getOffsetY.restype = ctypes.c_bool
def CblueSfnc_getOffsetY():
	val = ctypes.c_int(0)
	res = lib.CblueSfnc_getOffsetY(ctypes.byref(val))
	return res, val.value

#------------------------------------------------------------
lib.CblueSfnc_setOffsetY.argtypes = [ctypes.c_int]
lib.CblueSfnc_setOffsetY.restype = ctypes.c_bool
def CblueSfnc_setOffsetY(val):
	return lib.CblueSfnc_setOffsetY(val)

#------------------------------------------------------------
lib.Cblue1_getSparseWidth.argtypes = [ctypes.POINTER(ctypes.c_int)]
lib.Cblue1_getSparseWidth.restype = ctypes.c_bool
def Cblue1_getSparseWidth():
	val = ctypes.c_int(0)
	res = lib.Cblue1_getSparseWidth(ctypes.byref(val))
	return res, val.value

#------------------------------------------------------------
lib.Cblue1_setSparseWidth.argtypes = [ctypes.c_int]
lib.Cblue1_setSparseWidth.restype = ctypes.c_bool
def Cblue1_setSparseWidth(val):
	return lib.Cblue1_setSparseWidth(val)

#------------------------------------------------------------
lib.Cblue1_getSparseHeight.argtypes = [ctypes.POINTER(ctypes.c_int)]
lib.Cblue1_getSparseHeight.restype = ctypes.c_bool
def Cblue1_getSparseHeight():
	val = ctypes.c_int(0)
	res = lib.Cblue1_getSparseHeight(ctypes.byref(val))
	return res, val.value

#------------------------------------------------------------
lib.Cblue1_setSparseHeight.argtypes = [ctypes.c_int]
lib.Cblue1_setSparseHeight.restype = ctypes.c_bool
def Cblue1_setSparseHeight(val):
	return lib.Cblue1_setSparseHeight(val)

#------------------------------------------------------------
lib.Cblue1_getSparseOffsetX.argtypes = [ctypes.POINTER(ctypes.c_int)]
lib.Cblue1_getSparseOffsetX.restype = ctypes.c_bool
def Cblue1_getSparseOffsetX():
	val = ctypes.c_int(0)
	res = lib.Cblue1_getSparseOffsetX(ctypes.byref(val))
	return res, val.value

#------------------------------------------------------------
lib.Cblue1_setSparseOffsetX.argtypes = [ctypes.c_int]
lib.Cblue1_setSparseOffsetX.restype = ctypes.c_bool
def Cblue1_setSparseOffsetX(val):
	return lib.Cblue1_setSparseOffsetX(val)

#------------------------------------------------------------
lib.Cblue1_getSparseOffsetY.argtypes = [ctypes.POINTER(ctypes.c_int)]
lib.Cblue1_getSparseOffsetY.restype = ctypes.c_bool
def Cblue1_getSparseOffsetY():
	val = ctypes.c_int(0)
	res = lib.Cblue1_getSparseOffsetY(ctypes.byref(val))
	return res, val.value

#------------------------------------------------------------
lib.Cblue1_setSparseOffsetY.argtypes = [ctypes.c_int]
lib.Cblue1_setSparseOffsetY.restype = ctypes.c_bool
def Cblue1_setSparseOffsetY(val):
	return lib.Cblue1_setSparseOffsetY(val)

#------------------------------------------------------------
lib.CblueSfnc_getAcquisitionFrameCount.argtypes = [ctypes.POINTER(ctypes.c_int)]
lib.CblueSfnc_getAcquisitionFrameCount.restype = ctypes.c_bool
def CblueSfnc_getAcquisitionFrameCount():
	val = ctypes.c_int(0)
	res = lib.CblueSfnc_getAcquisitionFrameCount(ctypes.byref(val))
	return res, val.value

#------------------------------------------------------------
lib.CblueSfnc_setAcquisitionFrameCount.argtypes = [ctypes.c_int]
lib.CblueSfnc_setAcquisitionFrameCount.restype = ctypes.c_bool
def CblueSfnc_setAcquisitionFrameCount(val):
	return lib.CblueSfnc_setAcquisitionFrameCount(val)

#------------------------------------------------------------
lib.CblueSfnc_getCxpConnectionSelector.argtypes = [ctypes.POINTER(ctypes.c_int)]
lib.CblueSfnc_getCxpConnectionSelector.restype = ctypes.c_bool
def CblueSfnc_getCxpConnectionSelector():
	val = ctypes.c_int(0)
	res = lib.CblueSfnc_getCxpConnectionSelector(ctypes.byref(val))
	return res, val.value

#------------------------------------------------------------
lib.CblueSfnc_setCxpConnectionSelector.argtypes = [ctypes.c_int]
lib.CblueSfnc_setCxpConnectionSelector.restype = ctypes.c_bool
def CblueSfnc_setCxpConnectionSelector(val):
	return lib.CblueSfnc_setCxpConnectionSelector(val)

#------------------------------------------------------------
lib.CblueSfnc_getCxpConnectionTestErrorCount.argtypes = [ctypes.POINTER(ctypes.c_int)]
lib.CblueSfnc_getCxpConnectionTestErrorCount.restype = ctypes.c_bool
def CblueSfnc_getCxpConnectionTestErrorCount():
	val = ctypes.c_int(0)
	res = lib.CblueSfnc_getCxpConnectionTestErrorCount(ctypes.byref(val))
	return res, val.value

#------------------------------------------------------------
lib.CblueSfnc_setCxpConnectionTestErrorCount.argtypes = [ctypes.c_int]
lib.CblueSfnc_setCxpConnectionTestErrorCount.restype = ctypes.c_bool
def CblueSfnc_setCxpConnectionTestErrorCount(val):
	return lib.CblueSfnc_setCxpConnectionTestErrorCount(val)

#------------------------------------------------------------
lib.CblueSfnc_getCxpConnectionTestPacketCount.argtypes = [ctypes.POINTER(ctypes.c_int)]
lib.CblueSfnc_getCxpConnectionTestPacketCount.restype = ctypes.c_bool
def CblueSfnc_getCxpConnectionTestPacketCount():
	val = ctypes.c_int(0)
	res = lib.CblueSfnc_getCxpConnectionTestPacketCount(ctypes.byref(val))
	return res, val.value

#------------------------------------------------------------
lib.CblueSfnc_setCxpConnectionTestPacketCount.argtypes = [ctypes.c_int]
lib.CblueSfnc_setCxpConnectionTestPacketCount.restype = ctypes.c_bool
def CblueSfnc_setCxpConnectionTestPacketCount(val):
	return lib.CblueSfnc_setCxpConnectionTestPacketCount(val)

#------------------------------------------------------------
lib.CblueSfnc_getCxpErrorCounterValue.argtypes = [ctypes.POINTER(ctypes.c_int)]
lib.CblueSfnc_getCxpErrorCounterValue.restype = ctypes.c_bool
def CblueSfnc_getCxpErrorCounterValue():
	val = ctypes.c_int(0)
	res = lib.CblueSfnc_getCxpErrorCounterValue(ctypes.byref(val))
	return res, val.value

#------------------------------------------------------------
lib.CblueSfnc_setCxpErrorCounterValue.argtypes = [ctypes.c_int]
lib.CblueSfnc_setCxpErrorCounterValue.restype = ctypes.c_bool
def CblueSfnc_setCxpErrorCounterValue(val):
	return lib.CblueSfnc_setCxpErrorCounterValue(val)

#------------------------------------------------------------
lib.Cblue1_getDeviceFanSpeed.argtypes = [ctypes.POINTER(ctypes.c_int)]
lib.Cblue1_getDeviceFanSpeed.restype = ctypes.c_bool
def Cblue1_getDeviceFanSpeed():
	val = ctypes.c_int(0)
	res = lib.Cblue1_getDeviceFanSpeed(ctypes.byref(val))
	return res, val.value

#------------------------------------------------------------
lib.Cblue1_setDeviceFanSpeed.argtypes = [ctypes.c_int]
lib.Cblue1_setDeviceFanSpeed.restype = ctypes.c_bool
def Cblue1_setDeviceFanSpeed(val):
	return lib.Cblue1_setDeviceFanSpeed(val)

#------------------------------------------------------------
lib.Cblue1_getLogHistoryDepth.argtypes = [ctypes.POINTER(ctypes.c_int)]
lib.Cblue1_getLogHistoryDepth.restype = ctypes.c_bool
def Cblue1_getLogHistoryDepth():
	val = ctypes.c_int(0)
	res = lib.Cblue1_getLogHistoryDepth(ctypes.byref(val))
	return res, val.value

#------------------------------------------------------------
lib.Cblue1_setLogHistoryDepth.argtypes = [ctypes.c_int]
lib.Cblue1_setLogHistoryDepth.restype = ctypes.c_bool
def Cblue1_setLogHistoryDepth(val):
	return lib.Cblue1_setLogHistoryDepth(val)

#------------------------------------------------------------
lib.CblueSfnc_getTLParamsLocked.argtypes = [ctypes.POINTER(ctypes.c_int)]
lib.CblueSfnc_getTLParamsLocked.restype = ctypes.c_bool
def CblueSfnc_getTLParamsLocked():
	val = ctypes.c_int(0)
	res = lib.CblueSfnc_getTLParamsLocked(ctypes.byref(val))
	return res, val.value

#------------------------------------------------------------
lib.CblueSfnc_setTLParamsLocked.argtypes = [ctypes.c_int]
lib.CblueSfnc_setTLParamsLocked.restype = ctypes.c_bool
def CblueSfnc_setTLParamsLocked(val):
	return lib.CblueSfnc_setTLParamsLocked(val)

#------------------------------------------------------------
lib.CblueSfnc_getDeviceVendorName.restype = ctypes.c_bool
def CblueSfnc_getDeviceVendorName():
	val = ctypes.create_string_buffer(200)
	res = lib.CblueSfnc_getDeviceVendorName(ctypes.byref(val))
	return res, val.value.decode('utf-8', 'ignore')

#------------------------------------------------------------
lib.CblueSfnc_getDeviceModelName.restype = ctypes.c_bool
def CblueSfnc_getDeviceModelName():
	val = ctypes.create_string_buffer(200)
	res = lib.CblueSfnc_getDeviceModelName(ctypes.byref(val))
	return res, val.value.decode('utf-8', 'ignore')

#------------------------------------------------------------
lib.CblueSfnc_getDeviceManufacturerInfo.restype = ctypes.c_bool
def CblueSfnc_getDeviceManufacturerInfo():
	val = ctypes.create_string_buffer(200)
	res = lib.CblueSfnc_getDeviceManufacturerInfo(ctypes.byref(val))
	return res, val.value.decode('utf-8', 'ignore')

#------------------------------------------------------------
lib.CblueSfnc_getDeviceVersion.restype = ctypes.c_bool
def CblueSfnc_getDeviceVersion():
	val = ctypes.create_string_buffer(200)
	res = lib.CblueSfnc_getDeviceVersion(ctypes.byref(val))
	return res, val.value.decode('utf-8', 'ignore')

#------------------------------------------------------------
lib.CblueSfnc_getDeviceFirmwareVersion.restype = ctypes.c_bool
def CblueSfnc_getDeviceFirmwareVersion():
	val = ctypes.create_string_buffer(200)
	res = lib.CblueSfnc_getDeviceFirmwareVersion(ctypes.byref(val))
	return res, val.value.decode('utf-8', 'ignore')

#------------------------------------------------------------
lib.CblueSfnc_getDeviceSerialNumber.restype = ctypes.c_bool
def CblueSfnc_getDeviceSerialNumber():
	val = ctypes.create_string_buffer(200)
	res = lib.CblueSfnc_getDeviceSerialNumber(ctypes.byref(val))
	return res, val.value.decode('utf-8', 'ignore')

#------------------------------------------------------------
lib.CblueSfnc_getDeviceUserID.restype = ctypes.c_bool
def CblueSfnc_getDeviceUserID():
	val = ctypes.create_string_buffer(200)
	res = lib.CblueSfnc_getDeviceUserID(ctypes.byref(val))
	return res, val.value.decode('utf-8', 'ignore')

#------------------------------------------------------------
lib.CblueSfnc_setDeviceUserID.restype = ctypes.c_bool
def CblueSfnc_setDeviceUserID(val):
	return lib.CblueSfnc_setDeviceUserID(val.encode())

#------------------------------------------------------------
lib.Cblue1_getDeviceStatus.restype = ctypes.c_bool
def Cblue1_getDeviceStatus():
	val = ctypes.create_string_buffer(200)
	res = lib.Cblue1_getDeviceStatus(ctypes.byref(val))
	return res, val.value.decode('utf-8', 'ignore')

#------------------------------------------------------------
lib.Cblue1_getDeviceStatusDetailed.restype = ctypes.c_bool
def Cblue1_getDeviceStatusDetailed():
	val = ctypes.create_string_buffer(200)
	res = lib.Cblue1_getDeviceStatusDetailed(ctypes.byref(val))
	return res, val.value.decode('utf-8', 'ignore')

#------------------------------------------------------------
lib.Cblue1_getFirmwareUpdateUri.restype = ctypes.c_bool
def Cblue1_getFirmwareUpdateUri():
	val = ctypes.create_string_buffer(200)
	res = lib.Cblue1_getFirmwareUpdateUri(ctypes.byref(val))
	return res, val.value.decode('utf-8', 'ignore')

#------------------------------------------------------------
lib.Cblue1_setFirmwareUpdateUri.restype = ctypes.c_bool
def Cblue1_setFirmwareUpdateUri(val):
	return lib.Cblue1_setFirmwareUpdateUri(val.encode())

#------------------------------------------------------------
lib.Cblue1_getLogServeUri.restype = ctypes.c_bool
def Cblue1_getLogServeUri():
	val = ctypes.create_string_buffer(200)
	res = lib.Cblue1_getLogServeUri(ctypes.byref(val))
	return res, val.value.decode('utf-8', 'ignore')

#------------------------------------------------------------
lib.Cblue1_getCurrentIPAddress.restype = ctypes.c_bool
def Cblue1_getCurrentIPAddress():
	val = ctypes.create_string_buffer(200)
	res = lib.Cblue1_getCurrentIPAddress(ctypes.byref(val))
	return res, val.value.decode('utf-8', 'ignore')

#------------------------------------------------------------
lib.Cblue1_getCurrentSubnetMask.restype = ctypes.c_bool
def Cblue1_getCurrentSubnetMask():
	val = ctypes.create_string_buffer(200)
	res = lib.Cblue1_getCurrentSubnetMask(ctypes.byref(val))
	return res, val.value.decode('utf-8', 'ignore')

#------------------------------------------------------------
lib.Cblue1_getStaticIPAddress.restype = ctypes.c_bool
def Cblue1_getStaticIPAddress():
	val = ctypes.create_string_buffer(200)
	res = lib.Cblue1_getStaticIPAddress(ctypes.byref(val))
	return res, val.value.decode('utf-8', 'ignore')

#------------------------------------------------------------
lib.Cblue1_setStaticIPAddress.restype = ctypes.c_bool
def Cblue1_setStaticIPAddress(val):
	return lib.Cblue1_setStaticIPAddress(val.encode())

#------------------------------------------------------------
lib.Cblue1_getStaticSubnetMask.restype = ctypes.c_bool
def Cblue1_getStaticSubnetMask():
	val = ctypes.create_string_buffer(200)
	res = lib.Cblue1_getStaticSubnetMask(ctypes.byref(val))
	return res, val.value.decode('utf-8', 'ignore')

#------------------------------------------------------------
lib.Cblue1_setStaticSubnetMask.restype = ctypes.c_bool
def Cblue1_setStaticSubnetMask(val):
	return lib.Cblue1_setStaticSubnetMask(val.encode())

#------------------------------------------------------------
lib.Cblue1_getStaticDefaultGateway.restype = ctypes.c_bool
def Cblue1_getStaticDefaultGateway():
	val = ctypes.create_string_buffer(200)
	res = lib.Cblue1_getStaticDefaultGateway(ctypes.byref(val))
	return res, val.value.decode('utf-8', 'ignore')

#------------------------------------------------------------
lib.Cblue1_setStaticDefaultGateway.restype = ctypes.c_bool
def Cblue1_setStaticDefaultGateway(val):
	return lib.Cblue1_setStaticDefaultGateway(val.encode())

#------------------------------------------------------------
lib.Cblue1_getStaticDomainNameServer.restype = ctypes.c_bool
def Cblue1_getStaticDomainNameServer():
	val = ctypes.create_string_buffer(200)
	res = lib.Cblue1_getStaticDomainNameServer(ctypes.byref(val))
	return res, val.value.decode('utf-8', 'ignore')

#------------------------------------------------------------
lib.Cblue1_setStaticDomainNameServer.restype = ctypes.c_bool
def Cblue1_setStaticDomainNameServer(val):
	return lib.Cblue1_setStaticDomainNameServer(val.encode())

#------------------------------------------------------------
lib.Cblue1_getStaticAlternateDomainNameServer.restype = ctypes.c_bool
def Cblue1_getStaticAlternateDomainNameServer():
	val = ctypes.create_string_buffer(200)
	res = lib.Cblue1_getStaticAlternateDomainNameServer(ctypes.byref(val))
	return res, val.value.decode('utf-8', 'ignore')

#------------------------------------------------------------
lib.Cblue1_setStaticAlternateDomainNameServer.restype = ctypes.c_bool
def Cblue1_setStaticAlternateDomainNameServer(val):
	return lib.Cblue1_setStaticAlternateDomainNameServer(val.encode())

#------------------------------------------------------------
lib.CblueSfnc_getDeviceTemperature.argtypes = [ctypes.POINTER(ctypes.c_double)]
lib.CblueSfnc_getDeviceTemperature.restype = ctypes.c_bool
def CblueSfnc_getDeviceTemperature():
	val = ctypes.c_double(0)
	res = lib.CblueSfnc_getDeviceTemperature(ctypes.byref(val))
	return res, val.value

#------------------------------------------------------------
lib.Cblue1_getDeviceTecVoltage.argtypes = [ctypes.POINTER(ctypes.c_double)]
lib.Cblue1_getDeviceTecVoltage.restype = ctypes.c_bool
def Cblue1_getDeviceTecVoltage():
	val = ctypes.c_double(0)
	res = lib.Cblue1_getDeviceTecVoltage(ctypes.byref(val))
	return res, val.value

#------------------------------------------------------------
lib.Cblue1_getDeviceTecCurrent.argtypes = [ctypes.POINTER(ctypes.c_double)]
lib.Cblue1_getDeviceTecCurrent.restype = ctypes.c_bool
def Cblue1_getDeviceTecCurrent():
	val = ctypes.c_double(0)
	res = lib.Cblue1_getDeviceTecCurrent(ctypes.byref(val))
	return res, val.value

#------------------------------------------------------------
lib.Cblue1_getDeviceTecPower.argtypes = [ctypes.POINTER(ctypes.c_double)]
lib.Cblue1_getDeviceTecPower.restype = ctypes.c_bool
def Cblue1_getDeviceTecPower():
	val = ctypes.c_double(0)
	res = lib.Cblue1_getDeviceTecPower(ctypes.byref(val))
	return res, val.value

#------------------------------------------------------------
lib.Cblue1_getDeviceCoolingSetpoint.argtypes = [ctypes.POINTER(ctypes.c_double)]
lib.Cblue1_getDeviceCoolingSetpoint.restype = ctypes.c_bool
def Cblue1_getDeviceCoolingSetpoint():
	val = ctypes.c_double(0)
	res = lib.Cblue1_getDeviceCoolingSetpoint(ctypes.byref(val))
	return res, val.value

#------------------------------------------------------------
lib.Cblue1_setDeviceCoolingSetpoint.argtypes = [ctypes.c_double]
lib.Cblue1_setDeviceCoolingSetpoint.restype = ctypes.c_bool
def Cblue1_setDeviceCoolingSetpoint(val):
	return lib.Cblue1_setDeviceCoolingSetpoint(val)

#------------------------------------------------------------
lib.Cblue1_getAcquisitionFrameRateMinReg.argtypes = [ctypes.POINTER(ctypes.c_double)]
lib.Cblue1_getAcquisitionFrameRateMinReg.restype = ctypes.c_bool
def Cblue1_getAcquisitionFrameRateMinReg():
	val = ctypes.c_double(0)
	res = lib.Cblue1_getAcquisitionFrameRateMinReg(ctypes.byref(val))
	return res, val.value

#------------------------------------------------------------
lib.Cblue1_getAcquisitionFrameRateMaxReg.argtypes = [ctypes.POINTER(ctypes.c_double)]
lib.Cblue1_getAcquisitionFrameRateMaxReg.restype = ctypes.c_bool
def Cblue1_getAcquisitionFrameRateMaxReg():
	val = ctypes.c_double(0)
	res = lib.Cblue1_getAcquisitionFrameRateMaxReg(ctypes.byref(val))
	return res, val.value

#------------------------------------------------------------
lib.Cblue1_getExposureTimeMinReg.argtypes = [ctypes.POINTER(ctypes.c_double)]
lib.Cblue1_getExposureTimeMinReg.restype = ctypes.c_bool
def Cblue1_getExposureTimeMinReg():
	val = ctypes.c_double(0)
	res = lib.Cblue1_getExposureTimeMinReg(ctypes.byref(val))
	return res, val.value

#------------------------------------------------------------
lib.Cblue1_getExposureTimeMaxReg.argtypes = [ctypes.POINTER(ctypes.c_double)]
lib.Cblue1_getExposureTimeMaxReg.restype = ctypes.c_bool
def Cblue1_getExposureTimeMaxReg():
	val = ctypes.c_double(0)
	res = lib.Cblue1_getExposureTimeMaxReg(ctypes.byref(val))
	return res, val.value

#------------------------------------------------------------
lib.CblueSfnc_getSensorPixelWidth.argtypes = [ctypes.POINTER(ctypes.c_double)]
lib.CblueSfnc_getSensorPixelWidth.restype = ctypes.c_bool
def CblueSfnc_getSensorPixelWidth():
	val = ctypes.c_double(0)
	res = lib.CblueSfnc_getSensorPixelWidth(ctypes.byref(val))
	return res, val.value

#------------------------------------------------------------
lib.CblueSfnc_getSensorPixelHeight.argtypes = [ctypes.POINTER(ctypes.c_double)]
lib.CblueSfnc_getSensorPixelHeight.restype = ctypes.c_bool
def CblueSfnc_getSensorPixelHeight():
	val = ctypes.c_double(0)
	res = lib.CblueSfnc_getSensorPixelHeight(ctypes.byref(val))
	return res, val.value

#------------------------------------------------------------
lib.CblueSfnc_getAcquisitionFrameRate.argtypes = [ctypes.POINTER(ctypes.c_double)]
lib.CblueSfnc_getAcquisitionFrameRate.restype = ctypes.c_bool
def CblueSfnc_getAcquisitionFrameRate():
	val = ctypes.c_double(0)
	res = lib.CblueSfnc_getAcquisitionFrameRate(ctypes.byref(val))
	return res, val.value

#------------------------------------------------------------
lib.CblueSfnc_setAcquisitionFrameRate.argtypes = [ctypes.c_double]
lib.CblueSfnc_setAcquisitionFrameRate.restype = ctypes.c_bool
def CblueSfnc_setAcquisitionFrameRate(val):
	return lib.CblueSfnc_setAcquisitionFrameRate(val)

#------------------------------------------------------------
lib.CblueSfnc_getAcquisitionFrameRateMin.argtypes = [ctypes.POINTER(ctypes.c_double)]
lib.CblueSfnc_getAcquisitionFrameRateMin.restype = ctypes.c_bool
def CblueSfnc_getAcquisitionFrameRateMin():
	val = ctypes.c_double(0)
	res = lib.CblueSfnc_getAcquisitionFrameRateMin(ctypes.byref(val))
	return res, val.value

#------------------------------------------------------------
lib.CblueSfnc_getAcquisitionFrameRateMax.argtypes = [ctypes.POINTER(ctypes.c_double)]
lib.CblueSfnc_getAcquisitionFrameRateMax.restype = ctypes.c_bool
def CblueSfnc_getAcquisitionFrameRateMax():
	val = ctypes.c_double(0)
	res = lib.CblueSfnc_getAcquisitionFrameRateMax(ctypes.byref(val))
	return res, val.value

#------------------------------------------------------------
lib.CblueSfnc_getExposureTime.argtypes = [ctypes.POINTER(ctypes.c_double)]
lib.CblueSfnc_getExposureTime.restype = ctypes.c_bool
def CblueSfnc_getExposureTime():
	val = ctypes.c_double(0)
	res = lib.CblueSfnc_getExposureTime(ctypes.byref(val))
	return res, val.value

#------------------------------------------------------------
lib.CblueSfnc_setExposureTime.argtypes = [ctypes.c_double]
lib.CblueSfnc_setExposureTime.restype = ctypes.c_bool
def CblueSfnc_setExposureTime(val):
	return lib.CblueSfnc_setExposureTime(val)

#------------------------------------------------------------
lib.CblueSfnc_getExposureTimeMin.argtypes = [ctypes.POINTER(ctypes.c_double)]
lib.CblueSfnc_getExposureTimeMin.restype = ctypes.c_bool
def CblueSfnc_getExposureTimeMin():
	val = ctypes.c_double(0)
	res = lib.CblueSfnc_getExposureTimeMin(ctypes.byref(val))
	return res, val.value

#------------------------------------------------------------
lib.CblueSfnc_getExposureTimeMax.argtypes = [ctypes.POINTER(ctypes.c_double)]
lib.CblueSfnc_getExposureTimeMax.restype = ctypes.c_bool
def CblueSfnc_getExposureTimeMax():
	val = ctypes.c_double(0)
	res = lib.CblueSfnc_getExposureTimeMax(ctypes.byref(val))
	return res, val.value

#------------------------------------------------------------
lib.CblueSfnc_getGain.argtypes = [ctypes.POINTER(ctypes.c_double)]
lib.CblueSfnc_getGain.restype = ctypes.c_bool
def CblueSfnc_getGain():
	val = ctypes.c_double(0)
	res = lib.CblueSfnc_getGain(ctypes.byref(val))
	return res, val.value

#------------------------------------------------------------
lib.CblueSfnc_setGain.argtypes = [ctypes.c_double]
lib.CblueSfnc_setGain.restype = ctypes.c_bool
def CblueSfnc_setGain(val):
	return lib.CblueSfnc_setGain(val)

#------------------------------------------------------------
lib.CblueSfnc_getGainMin.argtypes = [ctypes.POINTER(ctypes.c_double)]
lib.CblueSfnc_getGainMin.restype = ctypes.c_bool
def CblueSfnc_getGainMin():
	val = ctypes.c_double(0)
	res = lib.CblueSfnc_getGainMin(ctypes.byref(val))
	return res, val.value

#------------------------------------------------------------
lib.CblueSfnc_getGainMax.argtypes = [ctypes.POINTER(ctypes.c_double)]
lib.CblueSfnc_getGainMax.restype = ctypes.c_bool
def CblueSfnc_getGainMax():
	val = ctypes.c_double(0)
	res = lib.CblueSfnc_getGainMax(ctypes.byref(val))
	return res, val.value

#------------------------------------------------------------
lib.CblueSfnc_getBlackLevel.argtypes = [ctypes.POINTER(ctypes.c_double)]
lib.CblueSfnc_getBlackLevel.restype = ctypes.c_bool
def CblueSfnc_getBlackLevel():
	val = ctypes.c_double(0)
	res = lib.CblueSfnc_getBlackLevel(ctypes.byref(val))
	return res, val.value

#------------------------------------------------------------
lib.CblueSfnc_setBlackLevel.argtypes = [ctypes.c_double]
lib.CblueSfnc_setBlackLevel.restype = ctypes.c_bool
def CblueSfnc_setBlackLevel(val):
	return lib.CblueSfnc_setBlackLevel(val)

#------------------------------------------------------------
lib.Cblue1_getDeviceCoolingEnable.argtypes = [ctypes.POINTER(ctypes.c_bool)]
lib.Cblue1_getDeviceCoolingEnable.restype = ctypes.c_bool
def Cblue1_getDeviceCoolingEnable():
	val = ctypes.c_bool(0)
	res = lib.Cblue1_getDeviceCoolingEnable(ctypes.byref(val))
	return res, val.value

#------------------------------------------------------------
lib.Cblue1_setDeviceCoolingEnable.argtypes = [ctypes.c_bool]
lib.Cblue1_setDeviceCoolingEnable.restype = ctypes.c_bool
def Cblue1_setDeviceCoolingEnable(val):
	return lib.Cblue1_setDeviceCoolingEnable(val)

#------------------------------------------------------------
lib.Cblue1_getSparse.argtypes = [ctypes.POINTER(ctypes.c_bool)]
lib.Cblue1_getSparse.restype = ctypes.c_bool
def Cblue1_getSparse():
	val = ctypes.c_bool(0)
	res = lib.Cblue1_getSparse(ctypes.byref(val))
	return res, val.value

#------------------------------------------------------------
lib.Cblue1_setSparse.argtypes = [ctypes.c_bool]
lib.Cblue1_setSparse.restype = ctypes.c_bool
def Cblue1_setSparse(val):
	return lib.Cblue1_setSparse(val)

#------------------------------------------------------------
lib.CblueSfnc_getReverseX.argtypes = [ctypes.POINTER(ctypes.c_bool)]
lib.CblueSfnc_getReverseX.restype = ctypes.c_bool
def CblueSfnc_getReverseX():
	val = ctypes.c_bool(0)
	res = lib.CblueSfnc_getReverseX(ctypes.byref(val))
	return res, val.value

#------------------------------------------------------------
lib.CblueSfnc_setReverseX.argtypes = [ctypes.c_bool]
lib.CblueSfnc_setReverseX.restype = ctypes.c_bool
def CblueSfnc_setReverseX(val):
	return lib.CblueSfnc_setReverseX(val)

#------------------------------------------------------------
lib.CblueSfnc_getReverseY.argtypes = [ctypes.POINTER(ctypes.c_bool)]
lib.CblueSfnc_getReverseY.restype = ctypes.c_bool
def CblueSfnc_getReverseY():
	val = ctypes.c_bool(0)
	res = lib.CblueSfnc_getReverseY(ctypes.byref(val))
	return res, val.value

#------------------------------------------------------------
lib.CblueSfnc_setReverseY.argtypes = [ctypes.c_bool]
lib.CblueSfnc_setReverseY.restype = ctypes.c_bool
def CblueSfnc_setReverseY(val):
	return lib.CblueSfnc_setReverseY(val)

#------------------------------------------------------------
lib.CblueSfnc_executeDeviceReset.restype = ctypes.c_bool
def CblueSfnc_executeDeviceReset():
	return lib.CblueSfnc_executeDeviceReset()

#------------------------------------------------------------
lib.Cblue1_executeDeviceShutdown.restype = ctypes.c_bool
def Cblue1_executeDeviceShutdown():
	return lib.Cblue1_executeDeviceShutdown()

#------------------------------------------------------------
lib.Cblue1_executeFirmwareUpdateExecute.restype = ctypes.c_bool
def Cblue1_executeFirmwareUpdateExecute():
	return lib.Cblue1_executeFirmwareUpdateExecute()

#------------------------------------------------------------
lib.Cblue1_executeFirmwareUpdateAbort.restype = ctypes.c_bool
def Cblue1_executeFirmwareUpdateAbort():
	return lib.Cblue1_executeFirmwareUpdateAbort()

#------------------------------------------------------------
lib.Cblue1_executeFirmwareUpdateStatusRefresh.restype = ctypes.c_bool
def Cblue1_executeFirmwareUpdateStatusRefresh():
	return lib.Cblue1_executeFirmwareUpdateStatusRefresh()

#------------------------------------------------------------
lib.Cblue1_executeLogCollect.restype = ctypes.c_bool
def Cblue1_executeLogCollect():
	return lib.Cblue1_executeLogCollect()

#------------------------------------------------------------
lib.Cblue1_executeLogCollectAbort.restype = ctypes.c_bool
def Cblue1_executeLogCollectAbort():
	return lib.Cblue1_executeLogCollectAbort()

#------------------------------------------------------------
lib.Cblue1_executeLogCollectStatusRefresh.restype = ctypes.c_bool
def Cblue1_executeLogCollectStatusRefresh():
	return lib.Cblue1_executeLogCollectStatusRefresh()

#------------------------------------------------------------
lib.Cblue1_executeLogServe.restype = ctypes.c_bool
def Cblue1_executeLogServe():
	return lib.Cblue1_executeLogServe()

#------------------------------------------------------------
lib.Cblue1_executeLogServeAbort.restype = ctypes.c_bool
def Cblue1_executeLogServeAbort():
	return lib.Cblue1_executeLogServeAbort()

#------------------------------------------------------------
lib.Cblue1_executeIPReconfigure.restype = ctypes.c_bool
def Cblue1_executeIPReconfigure():
	return lib.Cblue1_executeIPReconfigure()

#------------------------------------------------------------
lib.CblueSfnc_executeAcquisitionStart.restype = ctypes.c_bool
def CblueSfnc_executeAcquisitionStart():
	return lib.CblueSfnc_executeAcquisitionStart()

#------------------------------------------------------------
lib.CblueSfnc_executeAcquisitionStop.restype = ctypes.c_bool
def CblueSfnc_executeAcquisitionStop():
	return lib.CblueSfnc_executeAcquisitionStop()

#------------------------------------------------------------
lib.CblueSfnc_executeAcquisitionAbort.restype = ctypes.c_bool
def CblueSfnc_executeAcquisitionAbort():
	return lib.CblueSfnc_executeAcquisitionAbort()

#------------------------------------------------------------
lib.CblueSfnc_executeUserSetLoad.restype = ctypes.c_bool
def CblueSfnc_executeUserSetLoad():
	return lib.CblueSfnc_executeUserSetLoad()

#------------------------------------------------------------
lib.CblueSfnc_executeUserSetSave.restype = ctypes.c_bool
def CblueSfnc_executeUserSetSave():
	return lib.CblueSfnc_executeUserSetSave()

#------------------------------------------------------------
lib.CblueSfnc_executeCxpErrorCounterReset.restype = ctypes.c_bool
def CblueSfnc_executeCxpErrorCounterReset():
	return lib.CblueSfnc_executeCxpErrorCounterReset()
