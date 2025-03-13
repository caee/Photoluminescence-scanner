import LibLoader
import ImageProcessing
import FliCblueOne
import FliCblueSfnc
import FliCred
import FliCredOne
import FliCredTwo
import FliCredTwoLite
import FliCredThree
import FliSerialCamera
import FliGenicamCamera
import FliOcam2K
import FliOcam2S
import ctypes
import numpy as np

class CroppingData(ctypes.Structure):
    _fields_ = [("col1", ctypes.c_int16),
                ("col2", ctypes.c_int16),
                ("row1", ctypes.c_int16),
                ("row2", ctypes.c_int16),
                ("cred1Cols", ctypes.c_bool * 10),
                ("cred1Rows", ctypes.c_bool * 256)]

class Mode:
    Full = 0
    GrabOnly = 1
    ConfigOnly = 2

CWRAPPER = ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.c_void_p)

bufferSize = ctypes.c_size_t(1000)
charBuffer = ctypes.create_string_buffer(bufferSize.value)

ImageProcessing = ImageProcessing.ImageProcessing()
FliCblueSfnc = FliCblueSfnc.FliCblueSfnc()
FliCblueOne = FliCblueOne.FliCblueOne()
FliCred = FliCred.FliCred()
FliCredOne = FliCredOne.FliCredOne()
FliCredTwo = FliCredTwo.FliCredTwo()
FliCredTwoLite = FliCredTwoLite.FliCredTwoLite()
FliCredThree = FliCredThree.FliCredThree()
FliSerialCamera = FliSerialCamera.FliSerialCamera()
FliGenicamCamera = FliGenicamCamera.FliGenicamCamera()
FliOcam2K = FliOcam2K.FliOcam2K()
FliOcam2S = FliOcam2S.FliOcam2S()

#-------------------------------------------------------------------#
LibLoader.lib.FliSdk_init_V2.restype = ctypes.c_void_p
def Init():
    return LibLoader.lib.FliSdk_init_V2()

#-------------------------------------------------------------------#
LibLoader.lib.FliSdk_exit_V2.argtypes = [ctypes.c_void_p]
def Exit(context):
    LibLoader.lib.FliSdk_exit_V2(context)

#-------------------------------------------------------------------#
LibLoader.lib.FliSdk_detectGrabbers_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_size_t]
def DetectGrabbers(context):
    LibLoader.lib.FliSdk_detectGrabbers_V2(context, charBuffer, bufferSize)
    return charBuffer.value.decode('utf-8', 'ignore').split(";")

#-------------------------------------------------------------------#
LibLoader.lib.FliSdk_getDetectedGrabbers_V2.argtypes = [
    ctypes.c_void_p, ctypes.c_char_p, ctypes.c_size_t]
def GetDetectedGrabbers(context):
    LibLoader.lib.FliSdk_getDetectedGrabbers_V2(context, charBuffer, bufferSize)
    return charBuffer.value.decode('utf-8', 'ignore').split(";")


#-------------------------------------------------------------------#
LibLoader.lib.FliSdk_detectCameras_V2.argtypes = [
    ctypes.c_void_p, ctypes.c_char_p, ctypes.c_size_t]
def DetectCameras(context):
    LibLoader.lib.FliSdk_detectCameras_V2(context, charBuffer, bufferSize)
    return charBuffer.value.decode('utf-8', 'ignore').split(";")

#-------------------------------------------------------------------#
LibLoader.lib.FliSdk_getDetectedCameras_V2.argtypes = [
    ctypes.c_void_p, ctypes.c_char_p, ctypes.c_size_t]
def GetDetectedCameras(context):
    LibLoader.lib.FliSdk_getDetectedCameras_V2(context, charBuffer, bufferSize)
    return charBuffer.value.decode('utf-8', 'ignore').split(";")

#-------------------------------------------------------------------#
LibLoader.lib.FliSdk_setGrabber_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
LibLoader.lib.FliSdk_setGrabber_V2.restype = ctypes.c_bool
def SetGrabber(context, grabberName):
    return LibLoader.lib.FliSdk_setGrabber_V2(context, grabberName.encode())

#-------------------------------------------------------------------#
LibLoader.lib.FliSdk_setCamera_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
LibLoader.lib.FliSdk_setCamera_V2.restype = ctypes.c_bool
def SetCamera(context, cameraName):
    return LibLoader.lib.FliSdk_setCamera_V2(context, cameraName.encode())

#------------------------------------------------------------
LibLoader.lib.FliSdk_getCurrentCameraName_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_size_t]
LibLoader.lib.FliSdk_getCurrentCameraName_V2.restype = ctypes.c_bool
def GetCurrentCameraName(context):
    res = LibLoader.lib.FliSdk_getCurrentCameraName_V2(context, charBuffer, bufferSize)
    return charBuffer.value.decode('utf-8', 'ignore')

#-------------------------------------------------------------------#
LibLoader.lib.FliSdk_setMode_V2.argtypes = [ctypes.c_void_p, ctypes.c_uint8]
def SetMode(context, mode):
    if mode != Mode.Full and mode != Mode.GrabOnly and mode != Mode.ConfigOnly:
        return False

    LibLoader.lib.FliSdk_setMode_V2(ctypes.c_void_p(context), mode)
    return True

#-------------------------------------------------------------------#
LibLoader.lib.FliSdk_setImageDimension_V2.argtypes = [ctypes.c_void_p, ctypes.c_uint16, ctypes.c_uint16]
def SetImageDimension(context, width, height):
    if width <= 0 or height <= 0:
        return False
    LibLoader.lib.FliSdk_setImageDimension_V2(ctypes.c_void_p(context), width, height)
    return True

#-------------------------------------------------------------------#
LibLoader.lib.FliSdk_update_V2.restype = ctypes.c_bool
def Update(context):
    return LibLoader.lib.FliSdk_update_V2(ctypes.c_void_p(context))

#-------------------------------------------------------------------#
LibLoader.lib.FliSdk_start_V2.restype = ctypes.c_bool
def Start(context):
    return LibLoader.lib.FliSdk_start_V2(ctypes.c_void_p(context))

#-------------------------------------------------------------------#
LibLoader.lib.FliSdk_stop_V2.restype = ctypes.c_bool
def Stop(context):
    return LibLoader.lib.FliSdk_stop_V2(ctypes.c_void_p(context))

#-------------------------------------------------------------------#
LibLoader.lib.FliSdk_isStarted_V2.restype = ctypes.c_bool
def IsStarted(context):
    return LibLoader.lib.FliSdk_isStarted_V2(ctypes.c_void_p(context))

#-------------------------------------------------------------------#
def GetCameraModel(context):
    LibLoader.lib.FliSdk_getCameraModelAsString_V2(
        ctypes.c_void_p(context), charBuffer, bufferSize)
    return charBuffer.value.decode("utf-8")

#-------------------------------------------------------------------#
LibLoader.lib.FliSdk_enableGrabN_V2.restype = ctypes.c_bool
def EnableGrabN(context, nbFrames):
    return LibLoader.lib.FliSdk_enableGrabN_V2(ctypes.c_void_p(context), nbFrames)

#-------------------------------------------------------------------#
LibLoader.lib.FliSdk_disableGrabN_V2.argtypes = [ctypes.c_void_p]
def DisableGrabN(context):
    return LibLoader.lib.FliSdk_disableGrabN_V2(ctypes.c_void_p(context))

#-------------------------------------------------------------------#
LibLoader.lib.FliSdk_isGrabNEnabled_V2.restype = ctypes.c_bool
def IsGrabNEnabled(context):
    return LibLoader.lib.FliSdk_isGrabNEnabled_V2(ctypes.c_void_p(context))


#-------------------------------------------------------------------#
LibLoader.lib.FliSdk_isGrabNFinished_V2.restype = ctypes.c_bool
def IsGrabNFinished(context):
    return LibLoader.lib.FliSdk_isGrabNFinished_V2(ctypes.c_void_p(context))

#-------------------------------------------------------------------#
LibLoader.lib.FliSdk_getRawImage_V2.argtypes = [ctypes.c_void_p, ctypes.c_int]
LibLoader.lib.FliSdk_getRawImage_V2.restype = ctypes.c_void_p
def GetRawImage(context, index):
    return LibLoader.lib.FliSdk_getRawImage_V2(context, index)

#-------------------------------------------------------------------#
LibLoader.lib.FliSdk_getRawImage_lv_V2.argtypes = [
    ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p]
def GetRawImageAsNumpyArray(context, index):
    width, height = GetCurrentImageDimension(context)
    buffer = np.zeros((height, width), dtype=np.uint16)
    LibLoader.lib.FliSdk_getRawImage_lv_V2(
        context, index, ctypes.c_void_p(
            buffer.ctypes.data))
    return buffer

#-------------------------------------------------------------------#
LibLoader.lib.FliSdk_display8bImage_V2.argtypes = [
    ctypes.c_void_p, ctypes.c_void_p, ctypes.c_char_p]
def Display8bImage(context, image, windowName):
    LibLoader.lib.FliSdk_display8bImage_V2(context, image, windowName.encode())

#-------------------------------------------------------------------#
LibLoader.lib.FliSdk_display16bImage_V2.argtypes = [
    ctypes.c_void_p,
    ctypes.c_void_p,
    ctypes.c_char_p,
    ctypes.c_bool]
def Display16bImage(context, image, windowName, unsignedPixel):
    LibLoader.lib.FliSdk_display16bImage_V2(
        context,
        image,
        windowName.encode(),
        unsignedPixel)

#-------------------------------------------------------------------#
LibLoader.lib.FliSdk_initLog_V2.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
def InitLog(context, appName):
    LibLoader.lib.FliSdk_initLog_V2(context, appName.encode())

#-------------------------------------------------------------------#
LibLoader.lib.FliSdk_getFps_V2.argtypes = [ctypes.c_void_p]
LibLoader.lib.FliSdk_getFps_V2.restype = ctypes.c_double
def GetImageReceivedRate(context):
    return LibLoader.lib.FliSdk_getFps_V2(ctypes.c_void_p(context))

#-------------------------------------------------------------------#
def AddCallbackNewImage(context, func, fps, beforeCopy, userContext):
    LibLoader.lib.FliSdk_addCallbackNewImage_V2(context, func, fps, beforeCopy, userContext)

#-------------------------------------------------------------------#
LibLoader.lib.FliSdk_getBufferFilling_V2.argtypes = [ctypes.c_void_p]
LibLoader.lib.FliSdk_getBufferFilling_V2.restype = ctypes.c_uint64
def GetBufferFilling(context):
    return LibLoader.lib.FliSdk_getBufferFilling_V2(ctypes.c_void_p(context))

#-------------------------------------------------------------------#
LibLoader.lib.FliSdk_setBufferSize_V2.argtypes = [ctypes.c_void_p, ctypes.c_uint32]
def SetBufferSize(context, sizeMo):
    LibLoader.lib.FliSdk_setBufferSize_V2(ctypes.c_void_p(context), sizeMo)

#-------------------------------------------------------------------#
LibLoader.lib.FliSdk_getBufferSize_V2.argtypes = [ctypes.c_void_p]
LibLoader.lib.FliSdk_getBufferSize_V2.restype = ctypes.c_uint64
def GetBufferSize(context):
    return LibLoader.lib.FliSdk_getBufferSize_V2(ctypes.c_void_p(context))

#-------------------------------------------------------------------#
LibLoader.lib.FliSdk_setBufferSizeInImages_V2.argtypes = [ctypes.c_void_p, ctypes.c_uint32]
def SetBufferSizeInImages(context, nbImages):
    LibLoader.lib.FliSdk_setBufferSizeInImages_V2(ctypes.c_void_p(context), nbImages)

#-------------------------------------------------------------------#
LibLoader.lib.FliSdk_loadBufferFromFile_V2.restype = ctypes.c_bool
LibLoader.lib.FliSdk_loadBufferFromFile_V2.argtypes = [
    ctypes.c_void_p, ctypes.c_char_p, ctypes.POINTER(CroppingData)]
def LoadBufferFromFile(context, path, bufferCrop):
    return LibLoader.lib.FliSdk_loadBufferFromFile_V2(
        context, path.encode(), ctypes.byref(bufferCrop))

#-------------------------------------------------------------------#
LibLoader.lib.FliSdk_loadBufferRaw_V2.argtypes = [
    ctypes.c_void_p, ctypes.c_char_p, ctypes.c_uint32]
def LoadBufferRaw(context, buffer, nbImages):
    return LibLoader.lib.FliSdk_loadBufferRaw_V2(context, buffer, nbImages)

#-------------------------------------------------------------------#
LibLoader.lib.FliSdk_resetBuffer_V2.argtypes = [ctypes.c_void_p]
def ResetBuffer(context):
    LibLoader.lib.FliSdk_resetBuffer_V2(ctypes.c_void_p(context))

#-------------------------------------------------------------------#
LibLoader.lib.FliSdk_saveBuffer_V2.restype = ctypes.c_bool
LibLoader.lib.FliSdk_saveBuffer_V2.argtypes = [
    ctypes.c_void_p,
    ctypes.c_char_p,
    ctypes.c_int,
    ctypes.c_int]
def SaveBuffer(context, path, startIndex, endIndex):
    return LibLoader.lib.FliSdk_saveBuffer_V2(
        context, path.encode(), startIndex, endIndex)

#-------------------------------------------------------------------#
LibLoader.lib.FliSdk_saveBufferWithOptions_V2.restype = ctypes.c_bool
def SaveBufferWithOptions(
        context,
        path,
        startIndex,
        endIndex,
        func,
        withMetadata,
        offset,
        forceUnsigned,
        decimation):
    return LibLoader.lib.FliSdk_saveBufferWithOptions_V2(
        ctypes.c_void_p(context),
        path.encode(),
        startIndex,
        endIndex,
        func,
        withMetadata,
        offset,
        forceUnsigned,
        decimation)

#-------------------------------------------------------------------#
LibLoader.lib.FliSdk_getImagesCapacity_V2.argtypes = [ctypes.c_void_p]
LibLoader.lib.FliSdk_getImagesCapacity_V2.restype = ctypes.c_uint32
def GetImagesCapacity(context):
    return LibLoader.lib.FliSdk_getImagesCapacity_V2(ctypes.c_void_p(context))

#-------------------------------------------------------------------#
LibLoader.lib.FliSdk_getProcessedImage_V2.argtypes = [ctypes.c_void_p, ctypes.c_int]
LibLoader.lib.FliSdk_getProcessedImage_V2.restype = ctypes.c_void_p
# return an address which can be used directly in Qt QImage
def GetProcessedImage(context, index):
    return LibLoader.lib.FliSdk_getProcessedImage_V2(context, index)

#-------------------------------------------------------------------#
LibLoader.lib.FliSdk_getProcessedImage_lv_V2.argtypes = [
    ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p]
def GetProcessedImageRGBANumpyArray(context, index):
    width, height = GetCurrentImageDimension(context)
    buffer = np.zeros((height, width), dtype=np.uint32)
    LibLoader.lib.FliSdk_getProcessedImage_lv_V2(
        context, index, ctypes.c_void_p(
            buffer.ctypes.data))
    return buffer

#-------------------------------------------------------------------#
LibLoader.lib.FliSdk_getProcessedImage16b_lv_V2.argtypes = [
    ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p]
def GetProcessedImageGrayscale16bNumpyArray(context, index):
    width, height = GetCurrentImageDimension(context)
    buffer = np.zeros((height, width), dtype=np.int16)
    LibLoader.lib.FliSdk_getProcessedImage16b_lv_V2(
        context, index, ctypes.c_void_p(
            buffer.ctypes.data))
    return buffer

#-------------------------------------------------------------------#
LibLoader.lib.FliSdk_isCroppingDataValid_V2.argtypes = [ctypes.c_void_p, CroppingData]
def IsCroppingDataValid(context, cropData):
    return LibLoader.lib.FliSdk_isCroppingDataValid_V2(context, cropData)

#-------------------------------------------------------------------#
LibLoader.lib.FliSdk_getCroppingState_V2.argtypes = [
    ctypes.c_void_p, ctypes.POINTER(
        ctypes.c_bool), ctypes.POINTER(CroppingData)]
def GetCroppingState(context):
    isEnabled = ctypes.c_bool(1)
    cropData = CroppingData(0, 0, 0, 0)
    res = LibLoader.lib.FliSdk_getCroppingState_V2(
        context, ctypes.byref(isEnabled), ctypes.byref(cropData))
    return res, isEnabled.value, cropData

#-------------------------------------------------------------------#
LibLoader.lib.FliSdk_setCroppingState_V2.argtypes = [
    ctypes.c_void_p, ctypes.c_bool, CroppingData]
def SetCroppingState(context, enable, cropData):
    return LibLoader.lib.FliSdk_setCroppingState_V2(context, enable, cropData)

#-------------------------------------------------------------------#
def GetCurrentImageDimension(context):
    width = ctypes.c_int(0)
    height = ctypes.c_int(0)
    LibLoader.lib.FliSdk_getCurrentImageDimension_V2(
        ctypes.c_void_p(context),
        ctypes.byref(width),
        ctypes.byref(height))
    return width.value, height.value

#-------------------------------------------------------------------#
LibLoader.lib.FliSdk_addCallbackNewImage_V2.restype = ctypes.c_void_p
def AddCallBackNewImage(context, func, fps, beforeCopy, ctx):
    return LibLoader.lib.FliSdk_addCallbackNewImage_V2(
        ctypes.c_void_p(context), func, ctypes.c_uint(fps), beforeCopy, ctypes.c_void_p(ctx))

#-------------------------------------------------------------------#
def RemoveCallBackNewImage(context, callbackCtx):
    LibLoader.lib.FliSdk_removeCallbackNewImage_V2(ctypes.c_void_p(context), callbackCtx)

#-------------------------------------------------------------------#
def SetFpsTrigger(context, callbackCtx, fps):
    LibLoader.lib.FliSdk_setFpsTrigger_V2(ctypes.c_void_p(context), callbackCtx, fps)

#-------------------------------------------------------------------#
LibLoader.lib.FliSdk_isCred_V2.restype = ctypes.c_bool
def IsCred(context):
    return LibLoader.lib.FliSdk_isCred_V2(ctypes.c_void_p(context))

#-------------------------------------------------------------------#
LibLoader.lib.FliSdk_isCredOne_V2.restype = ctypes.c_bool
def IsCredOne(context):
    return LibLoader.lib.FliSdk_isCredOne_V2(ctypes.c_void_p(context))

#-------------------------------------------------------------------#
LibLoader.lib.FliSdk_isCredTwo_V2.restype = ctypes.c_bool
def IsCredTwo(context):
    return LibLoader.lib.FliSdk_isCredTwo_V2(ctypes.c_void_p(context))

#-------------------------------------------------------------------#
LibLoader.lib.FliSdk_isCredTwoLite_V2.restype = ctypes.c_bool
def IsCredTwoLite(context):
    return LibLoader.lib.FliSdk_isCredTwoLite_V2(ctypes.c_void_p(context))

#-------------------------------------------------------------------#
LibLoader.lib.FliSdk_isCredThree_V2.restype = ctypes.c_bool
def IsCredThree(context):
    return LibLoader.lib.FliSdk_isCredThree_V2(ctypes.c_void_p(context))

#-------------------------------------------------------------------#
LibLoader.lib.FliSdk_isCblueOne_V2.restype = ctypes.c_bool
def IsCblueOne(context):
    return LibLoader.lib.FliSdk_isCblueOne_V2(ctypes.c_void_p(context))

#-------------------------------------------------------------------#
LibLoader.lib.FliSdk_isCblueTwo_V2.restype = ctypes.c_bool
def IsCblueOne(context):
    return LibLoader.lib.FliSdk_isCblueTwo_V2(ctypes.c_void_p(context))

#-------------------------------------------------------------------#
LibLoader.lib.FliSdk_isSerialCamera_V2.restype = ctypes.c_bool
def IsSerialCamera(context):
    return LibLoader.lib.FliSdk_isSerialCamera_V2(ctypes.c_void_p(context))

#-------------------------------------------------------------------#
LibLoader.lib.FliSdk_isCblueSfnc_V2.restype = ctypes.c_bool
def IsCblueSfnc(context):
    return LibLoader.lib.FliSdk_isCblueSfnc_V2(ctypes.c_void_p(context))

#-------------------------------------------------------------------#
LibLoader.lib.FliSdk_isOcam2k_V2.restype = ctypes.c_bool
def IsOcam2k(context):
    return LibLoader.lib.FliSdk_isOcam2k_V2(ctypes.c_void_p(context))

#-------------------------------------------------------------------#
LibLoader.lib.FliSdk_isOcam2s_V2.restype = ctypes.c_bool
def IsOcam2s(context):
    return LibLoader.lib.FliSdk_isOcam2s_V2(ctypes.c_void_p(context))

#-------------------------------------------------------------------#
def SetNbImagesPerBuffer(context, nbImages):
    LibLoader.lib.FliSdk_setNbImagesPerBuffer_V2(ctypes.c_void_p(context), nbImages)

#-------------------------------------------------------------------#
LibLoader.lib.FliSdk_isUnsignedPixel_V2.restype = ctypes.c_bool
def IsUnsignedPixel(context):
    return LibLoader.lib.FliSdk_isUnsignedPixel_V2(ctypes.c_void_p(context))

#-------------------------------------------------------------------#
LibLoader.lib.FliSdk_isMono8Pixel_V2.restype = ctypes.c_bool
def IsMono8Pixel(context):
    return LibLoader.lib.FliSdk_isMono8Pixel_V2(ctypes.c_void_p(context))

#-------------------------------------------------------------------#
def EnableUnsignedPixel(context, enable):
    LibLoader.lib.FliSdk_enableUnsignedPixel_V2(ctypes.c_void_p(context), enable)

#-------------------------------------------------------------------#
def EnableRingBuffer(context, enable):
    LibLoader.lib.FliSdk_enableRingBuffer_V2(ctypes.c_void_p(context), enable)

#-------------------------------------------------------------------#
LibLoader.lib.FliSdk_getAvailableSaveFormats_V2.argtypes = [
    ctypes.c_void_p,
    ctypes.c_char_p,
    ctypes.c_size_t,
    ctypes.c_char_p,
    ctypes.c_size_t]
def GetAvailableSaveFormats(context):
    fullName = ctypes.create_string_buffer(bufferSize)
    extension = ctypes.create_string_buffer(bufferSize)
    LibLoader.lib.FliSdk_getAvailableSaveFormats_V2(context, ctypes.byref(
        fullName), bufferSize, ctypes.byref(extension), bufferSize)
    fullNameList = fullName.value.decode("utf-8").split(";")
    extensionList = extension.value.decode("utf-8").split(";")
    return fullNameList, extensionList

#-------------------------------------------------------------------#
def GetNbCountError(context):
    return LibLoader.lib.FliSdk_getNbCountError_V2(ctypes.c_void_p(context))

#-------------------------------------------------------------------#
def GetOcamFrameNumber(context, index):
    return LibLoader.lib.FliSdk_getOcamFrameNumber_V2(ctypes.c_void_p(context), index)

#-------------------------------------------------------------------#
def SetOcamFrameNumberOffset(context, offset):
    LibLoader.lib.FliSdk_setOcamFrameNumberOffset_V2(ctypes.c_void_p(context), offset)

#-------------------------------------------------------------------#
def SetBurstFilter(context, id):
    LibLoader.lib.FliSdk_setBurstFilter_V2(ctypes.c_void_p(context), id)

#-------------------------------------------------------------------#
def GetBurstFilter(context):
    return LibLoader.lib.FliSdk_getBurstFilter_V2(ctypes.c_void_p(context))

#-------------------------------------------------------------------#
def EnableSubstractMode(context, enable):
    LibLoader.lib.FliSdk_enableSubstractMode_V2(ctypes.c_void_p(context), enable)

#-------------------------------------------------------------------#
def EnableFowlerProcessing(context, enable):
    LibLoader.lib.FliSdk_enableFowlerProcessing_V2(ctypes.c_void_p(context), enable)

#-------------------------------------------------------------------#
def SetFowlerOffset(context, offset):
    LibLoader.lib.FliSdk_setFowlerOffset_V2(ctypes.c_void_p(context), offset)

#-------------------------------------------------------------------#
def EnableFollowUptheRamp(context, enable):
    LibLoader.lib.FliSdk_enableFollowUpTheRamp_V2(ctypes.c_void_p(context), enable)

#-------------------------------------------------------------------#
LibLoader.lib.FliSdk_addEthernetCamera_V2.argtypes = [
    ctypes.c_void_p,
    ctypes.c_char_p,
    ctypes.c_char_p,
    ctypes.c_char_p,
    ctypes.c_char_p,
    ctypes.c_size_t]
def AddEthernetCamera(context, ip, userName, sshPassword):
    res = LibLoader.lib.FliSdk_addEthernetCamera_V2(
        context,
        ip,
        userName,
        sshPassword,
        ctypes.byref(charBuffer),
        bufferSize)
    return res, charBuffer.value.decode("utf-8")

#-------------------------------------------------------------------#
def AddImageProcessing(context):
    return LibLoader.lib.FliSdk_addImageProcessing_V2(ctypes.c_void_p(context))

#-------------------------------------------------------------------#
def RemoveImageProcessing(context, processingId):
    LibLoader.lib.FliSdk_removeImageProcessing_V2(context, processingId)

#-------------------------------------------------------------------#

""" 
######
OWN  WRAPPER FUNCTIONS
######
"""

def buildBiasNUC(context, nImages):
    LibLoader.lib.FliSdk_buildBiasNUC_V2(context,nImages)
