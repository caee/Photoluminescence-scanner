from FLI_API import FliSdk_V2
import os
import sys
import cv2
import time
#sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
def setFPS(context,val):
    try:
        valFloat = float(val)
        if FliSdk_V2.IsSerialCamera(context):
            FliSdk_V2.FliSerialCamera.SetFps(context, valFloat)
        elif FliSdk_V2.IsCblueSfnc(context):
            FliSdk_V2.FliCblueSfnc.SetAcquisitionFrameRate(context, valFloat)
    except:
        print("Value is not a float")
def initCamera(context,frameRate,tintVal,conversionGain="Medium"):
    """
    Initialize the FLI camera.

    Parameters:
    context (object): The FLI SDK context.
    frameRate (float): The desired frame rate for the camera.
    tintVal (float): The desired exposure time (tint) for the camera in milliseconds.
    conversionGain (str): The desired conversion gain for the camera. Allowed values are "low", "medium", "high".

    Returns:
    None
    """
    print("Detection of grabbers...")
    listOfGrabbers = FliSdk_V2.DetectGrabbers(context)

    if len(listOfGrabbers) == 0:
        print("No grabber detected, exit.")
        exit()

    print("Done.")
    print("List of detected grabber(s):")

    for s in listOfGrabbers:
        print("- " + s)

    print("Detection of cameras...")
    listOfCameras = FliSdk_V2.DetectCameras(context)

    if len(listOfCameras) == 0:
        print("No camera detected, exit.")
        exit()

    print("Done.")
    print("List of detected camera(s):")

    i = 0
    for s in listOfCameras:
        print("- " + str(i) + " -> " + s)
        i = i + 1

    cameraIndex = int(input("Which camera to use? (0, 1, ...) "))
    print("Setting camera: " + listOfCameras[cameraIndex])
    ok = FliSdk_V2.SetCamera(context, listOfCameras[cameraIndex])

    if not ok:
        print("Error while setting camera.")
        exit()

    print("Setting mode full.")
    FliSdk_V2.SetMode(context, FliSdk_V2.Mode.Full)

    print("Updating...")
    ok = FliSdk_V2.Update(context)

    if not ok:
        print("Error while updating SDK.")
        exit()

    print("Done.")

    fps = 0

    if FliSdk_V2.IsSerialCamera(context):
        res, fps = FliSdk_V2.FliSerialCamera.GetFps(context)
    elif FliSdk_V2.IsCblueSfnc(context):
        res, fps = FliSdk_V2.FliCblueSfnc.GetAcquisitionFrameRate(context)
    print("Previous camera FPS: " + str(fps))

    # val = input("FPS to set? ")
    val = frameRate
    setFPS(context,val)
    # try:
    #     valFloat = float(val)
    #     if FliSdk_V2.IsSerialCamera(context):
    #         FliSdk_V2.FliSerialCamera.SetFps(context, valFloat)
    #     elif FliSdk_V2.IsCblueSfnc(context):
    #         FliSdk_V2.FliCblueSfnc.SetAcquisitionFrameRate(context, valFloat)
    # except:
    #     print("Value is not a float")

    if FliSdk_V2.IsSerialCamera(context):
        res, fps = FliSdk_V2.FliSerialCamera.GetFps(context)
    elif FliSdk_V2.IsCblueSfnc(context):
        res, fps = FliSdk_V2.FliCblueSfnc.GetAcquisitionFrameRate(context)
    print("New FPS read: " + str(fps))

    if FliSdk_V2.IsCredTwo(context) or FliSdk_V2.IsCredThree(context) or FliSdk_V2.IsCredTwoLite(context):
        res, response = FliSdk_V2.FliSerialCamera.SendCommand(
            context, "mintint raw")
        minTint = float(response)

        res, response = FliSdk_V2.FliSerialCamera.SendCommand(
            context, "maxtint raw")
        maxTint = float(response)

        res, response = FliSdk_V2.FliSerialCamera.SendCommand(context, "tint raw")

        print("Previous camera tint: " + str(float(response)*1000) + "ms")

        # val = input("Tint to set? (between " + str(minTint*1000) +
        #            "ms and " + str(maxTint*1000) + "ms) ")
        val = tintVal
        try:
            valFloat = float(val)
            res, response = FliSdk_V2.FliSerialCamera.SendCommand(
                context, "set tint " + str(valFloat/1000))
        except:
            print("Value is not a float")

        res, response = FliSdk_V2.FliSerialCamera.SendCommand(context, "tint raw")
        print("Current new camera tint: " + str(float(response)*1000) + "ms")
    elif FliSdk_V2.IsCblueSfnc(context):
        res, tint = FliSdk_V2.FliCblueSfnc.GetExposureTime(context)
        print("Current new camera tint: " + str(tint/1000) + "ms")

    res,conversionGain=FliSdk_V2.FliCredThree.GetConversionGain(context)
    print("Previous conversion gain: " + str(conversionGain))

    val = input("Conversion gain to set? (Low, Medium, High). Default is Medium")
    setConversionGain(context,val)
    
    #Setting buffer size (in acquisition now...?)
    #val = input("How many images to read? ")
    #val = float(bufferSize)
    # if not val.isnumeric():
    #     val = 600
def FramerateResolution(gantrySpeed,framerate,H,H_IR):
    """
    TODO:
    Calculate the resolution of x, given framerate of the camera along axis given a certain speed.
    Should just be geometry
    """
    # d_PF=speed/framerate
    pass
def acquireImage(context,bufferSize,framerate,nImages=4,savePath=0, fileName=0,disp=False):
    """
    Acquire raw images (.TIFF) from FLI C-RED 3. Signed int16?

    Parameters:
    context (object): The FLI SDK context.
    bufferSize (int): The buffer size for the camera.
    nImages (int): The number of images to capture. Default is 4.
    savePath (str): The path to save the images. Default is the current working directory.
    fileName (str): The name of the file to save the images. Default is "Test.tiff".

    Returns:
    None

    Saves .TIFF in the specified savePath (str)
    """

    if fileName==0:
        #standard file name
        fileName="Test.tiff"
    if savePath==0:
        #Standard save path
        savePath=os.path.join(os.getcwd(),fileName)
        #savePath="C:\\Users\\carle\\OneDrive - Danmarks Tekniske Universitet\\THESIS\\Work Files\\Camera\\Acquisition"+fileName
    else:
        
        savePath=os.path.join(savePath,fileName+".tiff")

    
    
    FliSdk_V2.ImageProcessing.SetColorMap(context, -1, "RAINBOW")

    FliSdk_V2.Start(context)

    #Enable auto clip after start
    FliSdk_V2.ImageProcessing.EnableAutoClip(context, -1, True)


    #For showing images
    val=bufferSize
    if disp:
        for i in range(int(val)):
            # -1 to get the last image in the buffer
            image = FliSdk_V2.GetProcessedImage(context, -1)
            FliSdk_V2.Display8bImage(context, image, "image 8b")
            image = FliSdk_V2.GetRawImage(context, -1)
            FliSdk_V2.Display16bImage(context, image, "image 16b", False)
        
    print("buffer at start:")
    print(FliSdk_V2.GetBufferFilling(context))
    print("Filling buffer")
    time.sleep(bufferSize/framerate+1) #Wait for images to be captured
    print("buffer at end:")
    print(FliSdk_V2.GetBufferFilling(context)) #DEBUG: Buffer filling

    lastImageIndex = FliSdk_V2.GetBufferFilling(context) - 1 #Find the buffer size
    numImages = bufferSize #Define the total number of images wanted
    if lastImageIndex<numImages:
        print("Error: Number of images exceeds buffer size. Increase buffer or decrease nImages")
        exit()

    #Get last image as np array and show it
    # fig=plt.figure()
    # buffer = FliSdk_V2.GetRawImageAsNumpyArray(context, -1)
    # plt.imshow(buffer, cmap='gray', vmin=0, vmax=65535)
    # plt.colorbar()

    # cv2.imshow("testImage",buffer)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    #Save last nImages of buffer as .tiff
    print("LastImageIndex:",lastImageIndex)
    print("Number of images:",numImages)
    print("savePath:",savePath)
    FliSdk_V2.SaveBuffer(
        context, savePath, lastImageIndex-numImages, lastImageIndex-1)

def justShowImage(context):
    """
    Display images from the FLI camera in real-time.

    Parameters:
    context (object): The FLI SDK context.

    Returns:
    None
    """  
    FliSdk_V2.ImageProcessing.EnableAutoClip(context, -1, True)
    FliSdk_V2.ImageProcessing.SetColorMap(context, -1, "RAINBOW")

    FliSdk_V2.Start(context)
    
    while True:
        # -1 to get the last image in the buffer
        image = FliSdk_V2.GetProcessedImage(context, -1)
        FliSdk_V2.Display8bImage(context, image, "image 8b")
        image = FliSdk_V2.GetRawImage(context, -1)
        FliSdk_V2.Display16bImage(context, image, "image 16b", False)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            #Break if q is pressed
            break
    # plt.figure()
    # buffer = FliSdk_V2.GetRawImageAsNumpyArray(context, -1)
    # plt.imshow(buffer, cmap='gray', vmin=0, vmax=65535)
    # plt.colorbar()
#---------------------------------
"""
BIAS FUNCTIONS
"""
def BuildNUCBias(context):
    """
    Build NUC Bias for FLI C-RED 3.

    Parameters:
    context (object): The FLI SDK context.

    Returns:
    None
    """
    print("NUC Bias correction for FLI C-RED 3 started.....") 
    nImages=256
    #nImages=input("How many images to use? (default 256)")
    print("[DEBUGGING]getting current bias state")
    res,state= FliSdk_V2.FliCred.GetBiasState(context)
    if state:
        #Change bias to false to generate new bias. Not sure if necessary but do it anyway?
        FliSdk_V2.FliSerialCamera.EnableBias(context, False)
    res,state= FliSdk_V2.FliCred.GetBiasState(context)
    print("[DEBUGGING] State before correction: (should be false)")
    print(state)
    
    val = input("Cover lens and press any button...")
    print("Building bias")
    res = FliSdk_V2.FliCred.BuildBias(context)
    if not res:
        print("Error while building bias.")
        exit()
    print("Bias built! Enabling...")
    FliSdk_V2.FliSerialCamera.EnableBias(context, True)
    print("Bias Enabled!")
    print("[DEBUGGING]getting new bias state (should be true")
    res,state= FliSdk_V2.FliCred.GetBiasState(context)
    #print(res)
    print(state)
    input("Bias correction applied. Press enter to continue...")
# def buildOwnBiasNuc(context):
#     #TODO:Own NUC Bias implementation??
#     print("Bias correction for FLI C-RED 3 started.....") 
#     nImages=256
#     #nImages=input("How many images to use? (default 256)")
#     val = input("Cover lens and press any button...")
#     FliCredThree.BuildBiasNuc(context,nImages)
#     print("Bias built!")

def EnableAdaptBias(context):
    """
    Enable Adaptive Bias for FLI C-RED 3.

    Parameters:
    context (object): The FLI SDK context.

    Returns:
    None
    """
    print("Adaptive bias correction for FLI C-RED 3 started.....") 
    #Check if bias is enables´d
    res,state= FliSdk_V2.FliCredThree.GetAdaptBiasState(context)
    if state:
        #Change bias to false to generate new bias. Not sure if necessary but do it anyway?
        FliSdk_V2.FliSerialCamera.EnableBias(context, False)
    FliSdk_V2.FliCredThree.EnableAdaptbias(context,True)
    print("Bias enabled!")

# def EnableSerialBias(context):
#     #Serial camera bias? NUC?
#     print("Bias correction for FLI C-RED 3 started.....") 
#     nImages=256
#     #nImages=input("How many images to use? (default 256)")
#     val = input("Cover lens and press any button...")
#     FliCredThree.BuildBiasNuc(context,nImages)
#     print("Bias built!")

def setConversionGain(context,conversionGain):
    """
    Sets the conversion gain for the given context.

    Parameters:
    context (object): The context in which to set the conversion gain.
    conversionGain (str): The desired conversion gain level. 
                            Accepted values are "low", "medium", and "high".

    Returns:
    None

    Prints a message indicating whether the conversion gain was successfully set.
    If an invalid conversion gain is provided, it defaults to "medium" and prints a warning message.
    """
    if conversionGain.lower()=="low":
        res =FliSdk_V2.FliCredThree.SetConversionGain(context, conversionGain.lower())
    elif conversionGain.lower()=="medium": 
        res=FliSdk_V2.FliCredThree.SetConversionGain(context, conversionGain.lower())
    elif conversionGain.lower()=="high":
        res=FliSdk_V2.FliCredThree.SetConversionGain(context, conversionGain.lower())
    else:
        print("Conversion gain not set. Default is Medium")
        conversionGain="medium"
        res=FliSdk_V2.FliCredThree.SetConversionGain(context, conversionGain.lower())
    if res:
        print("Conversion gain succesfully set to:",conversionGain)
def PixelCorrect(context,state=True):
    """
    Correct bad pixels.

    Parameters:
    context (object): The FLI SDK context.
    state (bool): The state to set for bad pixel correction. Default is True.

    Returns:
    None
    """
    val = input("Bad pixel correction?[y/n]")
    res,state=FliSdk_V2.FliCredThree.GetBadPixelState(context)
    FliSdk_V2.FliCredThree.EnableBadPixel(context,False) #Set default value to false
    if state:
        FliSdk_V2.FliCredThree.EnableBadPixel(context,True)

