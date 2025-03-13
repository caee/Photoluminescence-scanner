import LibLoader
import ctypes
import numpy as np

bufferSize = ctypes.c_size_t(1000)
charBuffer = ctypes.create_string_buffer(bufferSize.value)

class ImageProcessing:
    #-------------------------------------------------------------------#
    def EnableIndependentMode(self, context, processingId, enable):
        LibLoader.lib.FliImageProcessing_enableIndependentMode_V2(
            ctypes.c_void_p(context), processingId, enable)

    #-------------------------------------------------------------------#
    LibLoader.lib.FliImageProcessing_isIndependent_V2.restype = ctypes.c_bool

    def IsIndependent(self, context, processingId):
        return LibLoader.lib.FliImageProcessing_isIndependent_V2(
            ctypes.c_void_p(context), processingId)

    #-------------------------------------------------------------------#
    LibLoader.lib.FliImageProcessing_getColormapList_V2.argtypes = [
        ctypes.c_void_p, ctypes.c_int, ctypes.c_char_p, ctypes.c_size_t]

    def GetColorMapList(self, context, processingId):
        LibLoader.lib.FliImageProcessing_getColormapList_V2(
            context, processingId, charBuffer, bufferSize)
        return charBuffer.value.decode('utf-8', 'ignore').split(";")

    #-------------------------------------------------------------------#
    LibLoader.lib.FliImageProcessing_setColorMap_V2.argtypes = [
        ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p]

    def SetColorMap(self, context, processingId, colormap):
        LibLoader.lib.FliImageProcessing_setColorMap_V2(
            context, processingId, colormap.encode())

    #-------------------------------------------------------------------#
    LibLoader.lib.FliImageProcessing_getClippingList_V2.argtypes = [
        ctypes.c_void_p, ctypes.c_int, ctypes.c_char_p, ctypes.c_size_t]

    def GetClippingList(self, context, processingId):
        LibLoader.lib.FliImageProcessing_getClippingList_V2(
            context, processingId, charBuffer, bufferSize)
        return charBuffer.value.decode('utf-8', 'ignore').split(";")

    #-------------------------------------------------------------------#
    LibLoader.lib.FliImageProcessing_setClippingType_V2.argtypes = [
        ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p]

    def SetClippingType(self, context, processingId, clipping):
        LibLoader.lib.FliImageProcessing_setClippingType_V2(
            context, processingId, clipping.encode())

    #-------------------------------------------------------------------#
    LibLoader.lib.FliImageProcessing_setDimension_V2.argtypes = [
        ctypes.c_void_p, ctypes.c_int, ctypes.c_uint, ctypes.c_uint]

    def SetDimension(self, context, processingId, width, height):
        LibLoader.lib.FliImageProcessing_setDimension_V2(
            context, processingId, width, height)

    #-------------------------------------------------------------------#
    LibLoader.lib.FliImageProcessing_setGamma_V2.argtypes = [
        ctypes.c_void_p, ctypes.c_int, ctypes.c_double]

    def SetGamma(self, context, processingId, gamma):
        LibLoader.lib.FliImageProcessing_setGamma_V2(context, processingId, gamma)

    #-------------------------------------------------------------------#
    LibLoader.lib.FliImageProcessing_setRotationAngle_V2.argtypes = [
        ctypes.c_void_p, ctypes.c_int, ctypes.c_uint]

    def SetRotationAngle(self, context, processingId, angle):
        LibLoader.lib.FliImageProcessing_setRotationAngle_V2(
            context, processingId, angle)

    #-------------------------------------------------------------------#
    LibLoader.lib.FliImageProcessing_enableDisplayInfos_V2.argtypes = [
        ctypes.c_void_p, ctypes.c_int, ctypes.c_bool]

    def EnableDisplayInfos(self, context, processingId, enable):
        LibLoader.lib.FliImageProcessing_enableDisplayInfos_V2(
            context, processingId, enable)

    #-------------------------------------------------------------------#
    LibLoader.lib.FliImageProcessing_getMean16b_V2.argtypes = [
        ctypes.c_void_p, ctypes.c_int]
    LibLoader.lib.FliImageProcessing_getMean16b_V2.restype = ctypes.c_double

    def GetMean16b(self, context, processingId):
        return LibLoader.lib.FliImageProcessing_getMean16b_V2(context, processingId)

    #-------------------------------------------------------------------#
    LibLoader.lib.FliImageProcessing_getSpatialStdDev16b_V2.argtypes = [
        ctypes.c_void_p, ctypes.c_int]
    LibLoader.lib.FliImageProcessing_getSpatialStdDev16b_V2.restype = ctypes.c_double

    def GetSpatialStdDev16b(self, context, processingId):
        return LibLoader.lib.FliImageProcessing_getSpatialStdDev16b_V2(
            context, processingId)

    #-------------------------------------------------------------------#
    LibLoader.lib.FliImageProcessing_getMean8b_V2.argtypes = [
        ctypes.c_void_p, ctypes.c_int]
    LibLoader.lib.FliImageProcessing_getMean8b_V2.restype = ctypes.c_double

    def GetMean8b(self, context, processingId):
        return LibLoader.lib.FliImageProcessing_getMean8b_V2(context, processingId)

    #-------------------------------------------------------------------#
    LibLoader.lib.FliImageProcessing_getSpatialStdDev8b_V2.argtypes = [
        ctypes.c_void_p, ctypes.c_int]
    LibLoader.lib.FliImageProcessing_getSpatialStdDev8b_V2.restype = ctypes.c_double

    def GetSpatialStdDev8b(self, context, processingId):
        return LibLoader.lib.FliImageProcessing_getSpatialStdDev8b_V2(
            context, processingId)

    #-------------------------------------------------------------------#
    LibLoader.lib.FliImageProcessing_getClipBlack_V2.argtypes = [
        ctypes.c_void_p, ctypes.c_int]
    LibLoader.lib.FliImageProcessing_getClipBlack_V2.restype = ctypes.c_double

    def GetClipBlack(self, context, processingId):
        return LibLoader.lib.FliImageProcessing_getClipBlack_V2(context, processingId)

    #-------------------------------------------------------------------#
    LibLoader.lib.FliImageProcessing_setClipBlack_V2.argtypes = [
        ctypes.c_void_p, ctypes.c_int, ctypes.c_int16]

    def SetClipBlack(self, context, processingId, val):
        LibLoader.lib.FliImageProcessing_setClipBlack_V2(context, processingId, val)

    #-------------------------------------------------------------------#
    LibLoader.lib.FliImageProcessing_getClipWhite_V2.argtypes = [
        ctypes.c_void_p, ctypes.c_int]
    LibLoader.lib.FliImageProcessing_getClipWhite_V2.restype = ctypes.c_double

    def GetClipWhite(self, context, processingId):
        return LibLoader.lib.FliImageProcessing_getClipWhite_V2(context, processingId)

    #-------------------------------------------------------------------#
    LibLoader.lib.FliImageProcessing_setClipWhite_V2.argtypes = [
        ctypes.c_void_p, ctypes.c_int, ctypes.c_int16]

    def SetClipWhite(self, context, processingId, val):
        LibLoader.lib.FliImageProcessing_setClipWhite_V2(context, processingId, val)

    #-------------------------------------------------------------------#
    LibLoader.lib.FliImageProcessing_getMinVal_V2.argtypes = [
        ctypes.c_void_p, ctypes.c_int]
    LibLoader.lib.FliImageProcessing_getMinVal_V2.restype = ctypes.c_int16

    def GetMinVal(self, context, processingId):
        return LibLoader.lib.FliImageProcessing_getMinVal_V2(context, processingId)

    #-------------------------------------------------------------------#
    LibLoader.lib.FliImageProcessing_getMaxVal_V2.argtypes = [
        ctypes.c_void_p, ctypes.c_int]
    LibLoader.lib.FliImageProcessing_getMaxVal_V2.restype = ctypes.c_int32

    def GetMaxVal(self, context, processingId):
        return LibLoader.lib.FliImageProcessing_getMaxVal_V2(context, processingId)

    #-------------------------------------------------------------------#
    LibLoader.lib.FliImageProcessing_getHistogram8b_V2.argtypes = [
        ctypes.c_void_p, ctypes.c_int, ctypes.POINTER(ctypes.c_size_t)]
    LibLoader.lib.FliImageProcessing_getHistogram8b_V2.restype = ctypes.POINTER(
        ctypes.c_uint64 * 256)

    def GetHistogram8b(self, context, processingId):
        size = ctypes.c_size_t(0)
        ptr = LibLoader.lib.FliImageProcessing_getHistogram8b_V2(
            context, processingId, ctypes.byref(size))
        liste = []
        for i in ptr.contents:
            liste.append(i)
        return liste

    #-------------------------------------------------------------------#
    LibLoader.lib.FliImageProcessing_getHistogram16b_V2.argtypes = [
        ctypes.c_void_p, ctypes.c_int, ctypes.POINTER(ctypes.c_size_t)]
    LibLoader.lib.FliImageProcessing_getHistogram16b_V2.restype = ctypes.POINTER(
        ctypes.c_uint64 * 16386)

    def GetHistogram16b(self, context, processingId):
        size = ctypes.c_size_t(0)
        ptr = LibLoader.lib.FliImageProcessing_getHistogram16b_V2(
            context, processingId, ctypes.byref(size))
        liste = []
        for i in ptr.contents:
            liste.append(i)
        return liste

    #-------------------------------------------------------------------#
    LibLoader.lib.FliImageProcessing_getHistogram16bNegative_V2.argtypes = [
        ctypes.c_void_p, ctypes.c_int, ctypes.POINTER(ctypes.c_size_t)]
    LibLoader.lib.FliImageProcessing_getHistogram16bNegative_V2.restype = ctypes.POINTER(
        ctypes.c_uint64 * 16386)

    def GetHistogram16bNegative(self, context, processingId):
        size = ctypes.c_size_t(0)
        ptr = LibLoader.lib.FliImageProcessing_getHistogram16bNegative_V2(
            context, processingId, ctypes.byref(size))
        liste = []
        for i in ptr.contents:
            liste.append(i)
        return liste

    #-------------------------------------------------------------------#
    LibLoader.lib.FliImageProcessing_clip_V2.argtypes = [
        ctypes.c_void_p,
        ctypes.c_int,
        ctypes.c_int,
        ctypes.c_int,
        ctypes.c_int,
        ctypes.c_int]

    def Clip(self, context, processingId, x, y, width, height):
        LibLoader.lib.FliImageProcessing_clip_V2(
            context, processingId, x, y, width, height)

    #-------------------------------------------------------------------#
    def EnableAutoClip(self, context, processingId, enable):
        LibLoader.lib.FliImageProcessing_enableAutoClip_V2(
            ctypes.c_void_p(context), processingId, enable)

    #-------------------------------------------------------------------#
    def EnableAutoExposure(self, context, processingId, enable):
        LibLoader.lib.FliImageProcessing_enableAutoExposure_V2(
            ctypes.c_void_p(context), processingId, enable)

    #-------------------------------------------------------------------#
    def UpdateAutoExposureParam(self, context, processingId):
        LibLoader.lib.FliImageProcessing_updateAutoExposureParam_V2(
            ctypes.c_void_p(context), processingId)

    #-------------------------------------------------------------------#
    def EnableFilters(self, context, processingId, enable):
        LibLoader.lib.FliImageProcessing_enableFilters_V2(
            ctypes.c_void_p(context), processingId, enable)

    #-------------------------------------------------------------------#
    LibLoader.lib.FliImageProcessing_getCoeffA_V2.argtypes = [
        ctypes.c_void_p, ctypes.c_int]
    LibLoader.lib.FliImageProcessing_getCoeffA_V2.restype = ctypes.c_double

    def GetCoeffA(self, context, processingId):
        return LibLoader.lib.FliImageProcessing_getCoeffA_V2(context, processingId)

    #-------------------------------------------------------------------#
    LibLoader.lib.FliImageProcessing_getCoeffB_V2.argtypes = [
        ctypes.c_void_p, ctypes.c_int]
    LibLoader.lib.FliImageProcessing_getCoeffB_V2.restype = ctypes.c_double

    def GetCoeffB(self, context, processingId):
        return LibLoader.lib.FliImageProcessing_getCoeffB_V2(context, processingId)

    #-------------------------------------------------------------------#
    LibLoader.lib.FliImageProcessing_setStdDevAndMeanSelection_V2.argtypes = [
        ctypes.c_void_p,
        ctypes.c_int,
        ctypes.c_uint16,
        ctypes.c_uint16,
        ctypes.c_uint16,
        ctypes.c_uint16]

    def setAnalysisSelection(self, context, processingId, x, y, width, height):
        LibLoader.lib.FliImageProcessing_setStdDevAndMeanSelection_V2(
            context, processingId, x, y, width, height)

    #-------------------------------------------------------------------#
    def EnableDenoising(self, context, processingId, enable):
        LibLoader.lib.FliImageProcessing_enableDenoising_V2(
            ctypes.c_void_p(context), processingId, enable)

    #-------------------------------------------------------------------#
    LibLoader.lib.FliImageProcessing_setDenoisingH_V2.argtypes = [
        ctypes.c_void_p, ctypes.c_int, ctypes.c_float]

    def SetDenoisingH(self, context, processingId, val):
        LibLoader.lib.FliImageProcessing_setDenoisingH_V2(context, processingId, val)

    #-------------------------------------------------------------------#
    LibLoader.lib.FliImageProcessing_setDenoisingTemplateWindowSize_V2.argtypes = [
        ctypes.c_void_p, ctypes.c_int, ctypes.c_int]

    def SetDenoisingTemplateWindowSize(self, context, processingId, val):
        LibLoader.lib.FliImageProcessing_setDenoisingTemplateWindowSize_V2(
            context, processingId, val)

    #-------------------------------------------------------------------#
    LibLoader.lib.FliImageProcessing_setDenoisingSearchWindowSize_V2.argtypes = [
        ctypes.c_void_p, ctypes.c_int, ctypes.c_int]

    def SetDenoisingSearchWindowSize(self, context, processingId, val):
        LibLoader.lib.FliImageProcessing_setDenoisingSearchWindowSize_V2(
            context, processingId, val)

    #-------------------------------------------------------------------#
    def EnableSmoothImage(self, context, processingId, enable):
        LibLoader.lib.FliImageProcessing_enableSmoothImage_V2(
            ctypes.c_void_p(context), processingId, enable)

    #-------------------------------------------------------------------#
    def EnableManualClippingCoeff(self, context, processingId, enable):
        LibLoader.lib.FliImageProcessing_enableManualClippingCoeff_V2(
            ctypes.c_void_p(context), processingId, enable)

    #-------------------------------------------------------------------#
    LibLoader.lib.FliImageProcessing_setClippingAlpha_V2.argtypes = [
        ctypes.c_void_p, ctypes.c_int, ctypes.c_double]

    def SetClippingAlpha(self, context, processingId, val):
        LibLoader.lib.FliImageProcessing_setClippingAlpha_V2(context, processingId, val)

    #-------------------------------------------------------------------#
    LibLoader.lib.FliImageProcessing_setClippingBeta_V2.argtypes = [
        ctypes.c_void_p, ctypes.c_int, ctypes.c_double]

    def SetClippingBeta(self, context, processingId, val):
        LibLoader.lib.FliImageProcessing_setClippingBeta_V2(context, processingId, val)

    #-------------------------------------------------------------------#
    def EnableSharpen(self, context, processingId, enable):
        LibLoader.lib.FliImageProcessing_enableSharpen_V2(
            ctypes.c_void_p(context), processingId, enable)

    #-------------------------------------------------------------------#
    LibLoader.lib.FliImageProcessing_setSharpenKsize_V2.argtypes = [
        ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_int]

    def SetSharpenKsize(self, context, processingId, width, height):
        LibLoader.lib.FliImageProcessing_setSharpenKsize_V2(
            context, processingId, width, height)

    #-------------------------------------------------------------------#
    LibLoader.lib.FliImageProcessing_setSharpenSigmaX_V2.argtypes = [
        ctypes.c_void_p, ctypes.c_int, ctypes.c_double]

    def SetSharpenSigmaX(self, context, processingId, val):
        LibLoader.lib.FliImageProcessing_setSharpenSigmaX_V2(context, processingId, val)

    #-------------------------------------------------------------------#
    LibLoader.lib.FliImageProcessing_setSharpenSigmaY_V2.argtypes = [
        ctypes.c_void_p, ctypes.c_int, ctypes.c_double]

    def SetSharpenSigmaY(self, context, processingId, val):
        LibLoader.lib.FliImageProcessing_setSharpenSigmaY_V2(context, processingId, val)

    #-------------------------------------------------------------------#
    LibLoader.lib.FliImageProcessing_setSharpenAlpha_V2.argtypes = [
        ctypes.c_void_p, ctypes.c_int, ctypes.c_double]

    def SetSharpenAlpha(self, context, processingId, val):
        LibLoader.lib.FliImageProcessing_setSharpenAlpha_V2(context, processingId, val)

    #-------------------------------------------------------------------#
    LibLoader.lib.FliImageProcessing_setSharpenBeta_V2.argtypes = [
        ctypes.c_void_p, ctypes.c_int, ctypes.c_double]

    def SetSharpenBeta(self, context, processingId, val):
        LibLoader.lib.FliImageProcessing_setSharpenBeta_V2(context, processingId, val)

    #-------------------------------------------------------------------#
    LibLoader.lib.FliImageProcessing_setSharpenGamma_V2.argtypes = [
        ctypes.c_void_p, ctypes.c_int, ctypes.c_double]

    def SetSharpenGamma(self, context, processingId, val):
        LibLoader.lib.FliImageProcessing_setSharpenGamma_V2(context, processingId, val)

    #-------------------------------------------------------------------#
    def EnableClahe(self, context, processingId, enable):
        LibLoader.lib.FliImageProcessing_enableClahe_V2(
            ctypes.c_void_p(context), processingId, enable)

    #-------------------------------------------------------------------#
    LibLoader.lib.FliImageProcessing_setClaheCliplimit_V2.argtypes = [
        ctypes.c_void_p, ctypes.c_int, ctypes.c_double]

    def SetClaheCliplimit(self, context, processingId, val):
        LibLoader.lib.FliImageProcessing_setClaheCliplimit_V2(context, processingId, val)

    #-------------------------------------------------------------------#
    LibLoader.lib.FliImageProcessing_setClaheTileGridSize_V2.argtypes = [
        ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_int]

    def SetClaheTileGridSize(self, context, processingId, width, height):
        LibLoader.lib.FliImageProcessing_setClaheTileGridSize_V2(
            context, processingId, width, height)

    #-------------------------------------------------------------------#
    def EnableImagesAccumulation(self, context, processingId, enable):
        LibLoader.lib.FliImageProcessing_enableImagesAccumulation_V2(
            ctypes.c_void_p(context), processingId, enable)

    #-------------------------------------------------------------------#
    LibLoader.lib.FliImageProcessing_setNbImagesAccumulation_V2.argtypes = [
        ctypes.c_void_p, ctypes.c_int, ctypes.c_uint8]

    def SetNbImagesAccumulation(self, context, processingId, val):
        LibLoader.lib.FliImageProcessing_setNbImagesAccumulation_V2(
            context, processingId, val)

    #-------------------------------------------------------------------#
    def FlipVertically(self, context, processingId):
        LibLoader.lib.FliImageProcessing_flipVertically_V2(
            ctypes.c_void_p(context), processingId)

    #-------------------------------------------------------------------#
    def FlipHorizontally(self, context, processingId):
        LibLoader.lib.FliImageProcessing_flipHorizontally_V2(
            ctypes.c_void_p(context), processingId)

    #-------------------------------------------------------------------#
    LibLoader.lib.FliImageProcessing_flipHorizontally_V2.restype = ctypes.c_bool

    def IsFlippedHorizontally(self, context, processingId):
        return LibLoader.lib.FliImageProcessing_isFlippedHorizontally_V2(
            ctypes.c_void_p(context), processingId)

    #-------------------------------------------------------------------#
    LibLoader.lib.FliImageProcessing_isFlippedVertically_V2.restype = ctypes.c_bool

    def IsFlippedVertically(self, context, processingId):
        return LibLoader.lib.FliImageProcessing_isFlippedVertically_V2(
            ctypes.c_void_p(context), processingId)

    #-------------------------------------------------------------------#
    def SetToneMappingNormal(self, context, processingId):
        LibLoader.lib.FliImageProcessing_setToneMappingNormal_V2(
            ctypes.c_void_p(context), processingId)

    #-------------------------------------------------------------------#
    def SetToneMappingDrago(self, context, processingId):
        LibLoader.lib.FliImageProcessing_setToneMappingDrago_V2(
            ctypes.c_void_p(context), processingId)

    #-------------------------------------------------------------------#
    def SetToneMappingReinhard(self, context, processingId):
        LibLoader.lib.FliImageProcessing_setToneMappingReinhard_V2(
            ctypes.c_void_p(context), processingId)

    #-------------------------------------------------------------------#
    def SetToneMappingMantiuk(self, context, processingId):
        LibLoader.lib.FliImageProcessing_setToneMappingMantiuk_V2(
            ctypes.c_void_p(context), processingId)

    #-------------------------------------------------------------------#
    LibLoader.lib.FliImageProcessing_setDragoGamma_V2.argtypes = [
        ctypes.c_void_p, ctypes.c_int, ctypes.c_float]

    def SetDragoGamma(self, context, processingId, val):
        LibLoader.lib.FliImageProcessing_setDragoGamma_V2(context, processingId, val)

    #-------------------------------------------------------------------#
    LibLoader.lib.FliImageProcessing_setDragoSaturation_V2.argtypes = [
        ctypes.c_void_p, ctypes.c_int, ctypes.c_float]

    def SetDragoSaturation(self, context, processingId, val):
        LibLoader.lib.FliImageProcessing_setDragoSaturation_V2(
            context, processingId, val)

    #-------------------------------------------------------------------#
    LibLoader.lib.FliImageProcessing_setDragoBias_V2.argtypes = [
        ctypes.c_void_p, ctypes.c_int, ctypes.c_float]

    def SetDragoBias(self, context, processingId, val):
        LibLoader.lib.FliImageProcessing_setDragoBias_V2(context, processingId, val)

    #-------------------------------------------------------------------#
    LibLoader.lib.FliImageProcessing_setDragoMultiplicator_V2.argtypes = [
        ctypes.c_void_p, ctypes.c_int, ctypes.c_uint8]

    def SetDragoMultiplicator(self, context, processingId, val):
        LibLoader.lib.FliImageProcessing_setDragoMultiplicator_V2(
            context, processingId, val)

    #-------------------------------------------------------------------#
    LibLoader.lib.FliImageProcessing_setReinhardGamma_V2.argtypes = [
        ctypes.c_void_p, ctypes.c_int, ctypes.c_float]

    def SetReinhardGamma(self, context, processingId, val):
        LibLoader.lib.FliImageProcessing_setReinhardGamma_V2(context, processingId, val)

    #-------------------------------------------------------------------#
    LibLoader.lib.FliImageProcessing_setReinhardIntensity_V2.argtypes = [
        ctypes.c_void_p, ctypes.c_int, ctypes.c_float]

    def SetReinhardIntensity(self, context, processingId, val):
        LibLoader.lib.FliImageProcessing_setReinhardIntensity_V2(
            context, processingId, val)

    #-------------------------------------------------------------------#
    LibLoader.lib.FliImageProcessing_setReinhardLightAdapt_V2.argtypes = [
        ctypes.c_void_p, ctypes.c_int, ctypes.c_float]

    def SetReinhardLightAdapt(self, context, processingId, val):
        LibLoader.lib.FliImageProcessing_setReinhardLightAdapt_V2(
            context, processingId, val)

    #-------------------------------------------------------------------#
    LibLoader.lib.FliImageProcessing_setReinhardColorAdapt_V2.argtypes = [
        ctypes.c_void_p, ctypes.c_int, ctypes.c_float]

    def SetReinhardColorAdapt(self, context, processingId, val):
        LibLoader.lib.FliImageProcessing_setReinhardColorAdapt_V2(
            context, processingId, val)

    #-------------------------------------------------------------------#
    LibLoader.lib.FliImageProcessing_setMantiukGamma_V2.argtypes = [
        ctypes.c_void_p, ctypes.c_int, ctypes.c_float]

    def SetMantiukGamma(self, context, processingId, val):
        LibLoader.lib.FliImageProcessing_setMantiukGamma_V2(context, processingId, val)

    #-------------------------------------------------------------------#
    LibLoader.lib.FliImageProcessing_setMantiukScale_V2.argtypes = [
        ctypes.c_void_p, ctypes.c_int, ctypes.c_float]

    def SetMantiukScale(self, context, processingId, val):
        LibLoader.lib.FliImageProcessing_setMantiukScale_V2(context, processingId, val)

    #-------------------------------------------------------------------#
    LibLoader.lib.FliImageProcessing_setMantiukSaturation_V2.argtypes = [
        ctypes.c_void_p, ctypes.c_int, ctypes.c_float]

    def SetMantiukSaturation(self, context, processingId, val):
        LibLoader.lib.FliImageProcessing_setMantiukSaturation_V2(
            context, processingId, val)

    #-------------------------------------------------------------------#
    LibLoader.lib.FliImageProcessing_setMantiukMultiplicator_V2.argtypes = [
        ctypes.c_void_p, ctypes.c_int, ctypes.c_uint8]

    def SetMantiukMultiplicator(self, context, processingId, val):
        LibLoader.lib.FliImageProcessing_setMantiukMultiplicator_V2(
            context, processingId, val)

    #-------------------------------------------------------------------#
    LibLoader.lib.FliImageProcessing_setBadPixelsCarto_V2.argtypes = [
        ctypes.c_void_p, ctypes.c_int, ctypes.POINTER(
            ctypes.c_bool), ctypes.c_size_t]

    def SetBadPixelsCarto(self, context, processingId, carto):
        LibLoader.lib.FliImageProcessing_setBadPixelsCarto_V2(
            context, processingId, ctypes.byref(carto), len(carto))

    #-------------------------------------------------------------------#
    def EnableBadPixelsCarto(self, context, processingId, enable):
        LibLoader.lib.FliImageProcessing_enableBadPixelsCarto_V2(
            ctypes.c_void_p(context), processingId, enable)

    #-------------------------------------------------------------------#
    LibLoader.lib.FliImageProcessing_badPixelsCartoLoaded_V2.restype = ctypes.c_bool

    def BadPixelsCartoLoaded(self, context, processingId):
        return LibLoader.lib.FliImageProcessing_badPixelsCartoLoaded_V2(
            ctypes.c_void_p(context), processingId)