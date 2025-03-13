import os
import sys
sys.path.append('FLI_API')
sys.path.append('Stitching')
sys.path.append('Acquisition')
sys.path.append('lib')
from lib import ProcessInGaAs
from lib import imageAcquisition
from lib import gCodeHandler
from lib import stitchImages
import cv2

import datetime
import FLI_API
import tifffile
from FLI_API import FliSdk_V2


cwd = os.getcwd() #current working directory

def calibrateLoad(calpath):
    width, height = 640, 512  # Example dimensions, adjust as necessary
    K,P,DIM=ProcessInGaAs.loadCal(calpath,width,height)
    return K,P,DIM

def calibrateCamera(frameRate, tintVal, disp=False):
    # Initialize camera
    context = FliSdk_V2.Init()
    imageAcquisition.initCamera(context, frameRate, tintVal)

    # Set bad pixel correction
    imageAcquisition.PixelCorrect(context, True)

    # Buidling bias correction. Choose between NUC calibrated bias and FLI's adaptive bias (only C-RED3?)
    val=input("Build standard bias [y/n]?")
    if val=="y":
        imageAcquisition.BuildNUCBias(context)
        val=input("Also enable Adaptive Bias[y/n]?")
        if val=="y":
            imageAcquisition.EnableAdaptBias(context)
    elif not val=="y":
        val=input("Enable Adaptive bias instead [y/n]?")
        if val=="y":
            imageAcquisition.EnableAdaptBias(context)
    #TODO: Flat correction. Fixing non-uniformity response of pixels [OPTIONAL]
    #https://andor.oxinst.com/learning/view/article/how-to-use-the-hdr-mode
    # val=input("Do flat correction?[y/n]")
    # if val=="y":

    #Enable anti-blooming
    FliSdk_V2.FliCredThree.EnableAntiBlooming(context, True)
    print("Anti-blooming enabled")
    #Enable auto clip. Only after starting acquisition?????
    FliSdk_V2.ImageProcessing.EnableAutoClip(context, -1, True)
    print("Auto clip enabled")
    # Debugging display
    if disp:
        imageAcquisition.justShowImage(context)
    return context
def calibrateGantry(gcode_handler):
    """
    Calibration method for parallel X Y gantry. First, check if end stops are functional, even if they are triggered. Then, home the gantry.
    """
    #First make sure no end stops are triggered:
    try:
        endStop= ["M120", #enable end stops
            "M119", #Check end stop status
        ]
        t=gcode_handler.send_gcode(endStop)
        axis_trig = []
        count = 0  # count for error. Do not loop forever, max two times for each axis
        while any("TRIGGERED" in line for line in t) and count < 2:
            #Check end stops
            axis_trig = []
            for line in t:
                    if "TRIGGERED" in line:
                        axis = line.split("_")[0]  # Get the axis letter (X, Y, Z, etc.)
                        axis_trig.append(axis)
            print(f"End stop for axis(es) {', '.join(axis_trig)} is triggered. Attempting to move away.")
            if axis == 'x' or axis == 'x2':
                gcode_handler.send_gcode("G0 X30")
                gcode_handler.wait()
            elif axis == 'y' or axis == 'y2':
                gcode_handler.send_gcode("G0 Y30")
                gcode_handler.wait()
            else:
                raise ValueError(f"Unknown axis {axis} in end stop status.")
            t = gcode_handler.send_gcode("M119")
            count += 1
                # if "TRIGGERED" in t:
                #     raise RuntimeError(f"End stop for axis {axis} is still triggered after moving.")
    except:
        print("Error checking end stops")
        sys.exit()
    
    gcode_handler.auto_home()
    gcode_handler.wait()
    print("Gantry homed!")
def connectGantry():
    """
    Connects to the gantry by selecting an available port and initializing the GCodeHandler.
    This function lists all available ports, prompts the user to select one, and attempts to 
    establish a connection to the gantry using the selected port. If the connection is successful, 
    it returns an instance of GCodeHandler. If the connection fails, it prints an error message 
    and exits the program.
    Returns:
        gCodeHandler: An instance of the GCodeHandler class if the connection is successful.
    Raises:
        SystemExit: If there is an error connecting to the gantry.
    """

    available_ports = gCodeHandler.get_available_ports()
    print("Available ports:")
    #choose between available ports
    for i in range(len(available_ports)): print("port {}: {}".format(i, available_ports[i]))
    t=input("choose port: (typically shows board as USB serial device)")
    port=available_ports[int(t)].device
    print(port)
    try:
        gcode_handler = gCodeHandler.GCodeHandler(port)
        gcode_handler.connect()
    
    except:
        print("Error connecting to gantry")
        sys.exit()
    return gcode_handler

def scanContinuous(gcode_handler,context,savePath,frameRate,speed=5000):
    """
    Perform a continuous scan of a PV panel using a gantry system and save the acquired images.
    Parameters:
        gcode_handler (object): The handler object for controlling the gantry system.
        context (object): FLI context object for image acquisition.
        savePath (str): path where the scanned images will be saved.
        frameRate (int): frame rate for image acquisition.
        speed (int, optional): speed of the gantry in mm/min. Default is 5000 mm/min.
    Raises:
        ValueError: If the scan is interrupted by the user.
    Notes:
    - The user is prompted to place the PV panel under the light source and remove the camera cover before starting the scan.
    - The function calculates the number of images to be acquired based on the travel distance and frame rate.
    - The function waits for the gantry to complete its movement before finishing.
    - The scanned image is saved with a timestamp in the filename.
    """
    offsetBegin=500 #offset from the first edge of the gantry to end stops. This is the 0-point in real life
    offsetEnd=100 #offset from the last edge of the gantry to max travel of the axes
    dist_travel=2000#(2500-offsetBegin-offsetEnd) #Distance with offset included
    nImages=int(dist_travel/(speed/60)*frameRate)
    bufferSize=nImages+400
    gcode_handler.set_speed([speed,speed]) #set speed for both axes
    print("Ready to scan continous. Place PV panel under light source. turn on light source and remember to remove the camera cover:)")
    t=input("Press key to move to position? Press x to stop")
    if t.lower() == 'x':
            print("Scan interrupted by user.")
            #stopGantry(gcode_handler)
            ValueError("Scan interrupted by user.")
            sys.exit()

    gcode_handler.set_position(200,0)
    gcode_handler.set_position(dist_travel+100,dist_travel)
    currentDT = datetime.datetime.now()
    currentDT=currentDT.strftime("%Y-%m-%d_%H-%M")
    imageAcquisition.acquireImage(context,bufferSize,frameRate,nImages,savePath, fileName="scan_cont_{}".format(currentDT))
    gcode_handler.wait()
    print("Full panel scanned! Image saved as scan_cont_{}.tiff".format(currentDT))
    
def scanEL(gcode_handler,context,savePath,frameRate,speed=5000,nsteps=3):
    """
    Only moves camera axis. Not a full function yet.
    """    
    offsetBegin=500 #offset from the first edge of the gantry to end stops. This is the 0-point in real life
    offsetEnd=100 #offset from the last edge of the gantry to max travel of the axes
    dist_travel=1800#(2500-offsetBegin-offsetEnd) #Distance with offset included
    speed=5000 #mm/min
    nImages=int(dist_travel/(speed/60)*frameRate)
    bufferSize=nImages+400
    gcode_handler.set_speed([speed,speed]) #set speed for both axes
    print("Ready to scan continous. Place PV panel under light source. turn on light source and remember to remove the camera cover:)")
    t=input("Press key to move to position? Press x to stop")
    if t.lower() == 'x':
            print("Scan interrupted by user.")
            #stopGantry(gcode_handler)
            ValueError("Scan interrupted by user.")
            sys.exit()

    # gcode_handler.set_position(200,0)
    gcode_handler.set_position(dist_travel,0)
    currentDT = datetime.datetime.now()
    currentDT=currentDT.strftime("%Y-%m-%d_%H-%M")
    imageAcquisition.acquireImage(context,bufferSize,frameRate,nImages,savePath, fileName="scan_EL_cont_{}".format(currentDT))
    gcode_handler.wait()
    print("Full panel scanned! Image saved as scan_EL_cont_{}.tiff".format(currentDT))
def scan(gcode_handler,context,savePath,frameRate,speed=5000,nsteps=3):
    """
    Perform a stepped photoluminescence scan using a gantry system.
    Parameters:
        gcode_handler (object): The handler object to control the gantry system.
        context (object): The context for image acquisition.
        savePath (str): The path where the captured images will be saved.
        frameRate (int): The frame rate for image acquisition.
        speed (int, optional): The speed of the gantry movement in mm/min. Default is 5000.
        nsteps (int, optional): The number of steps for the scan. Default is 3.
    Raises:
        ValueError: If the scan is interrupted by the user.
    Notes:
    - Ensure the PV panel is placed under the light source and the light source is turned on.
    - Remove the camera cover before starting the scan.
    - The function will prompt the user to move to each position and wait for confirmation.
    Example:
    scan(gcode_handler, context, "path/to/save", 30)
    """
    #camera gantry position array
    offsetBegin=500 #offset from the first edge of the gantry to end stops. This is the 0-point in real life
    offsetEnd=100 #offset from the last edge of the gantry to max travel of the axes

    #3 step scan is default
    
    dist_travel=(2500-offsetBegin-offsetEnd)/nsteps #Distance with offset included
    camArr = [[0,0]]
    #Create camera array
    for i in range(nsteps):
        camArr.append([int(dist_travel*(i+1)),int(dist_travel*(i+1))])

    nImages=int(dist_travel/(speed/60)*frameRate) #number of images to capture for camera is related to framerate, travel distance for each step and speed
    bufferSize=nImages+5 #not sure about this. Might cause errors if buffer is too small
    gcode_handler.set_speed([speed,speed]) #set speed for both axes
    print("Ready to scan. Place PV panel under light source. turn on light source and remember to remove camera cover:)")
    for i in range(1,len(camArr)):
        print("Moving to position {}".format(camArr[i]))
        t=input("Press key to move to position? Press x to stop")
        if t.lower() == 'x':
            print("Scan interrupted by user.")
            #stopGantry(gcode_handler)
            ValueError("Scan interrupted by user.")
            sys.exit()
        
        #Set position of camera
        gcode_handler.set_position(camArr[i][0],camArr[i-1][1])
        gcode_handler.wait()
        gcode_handler.get_position()
        #Move IR bar while capturing images
        gcode_handler.set_position(camArr[i][0],camArr[i][1]) 
        imageAcquisition.acquireImage(context,bufferSize,frameRate,nImages,savePath, fileName="scan_{}".format(i))
        print("position {} scanned".format(i))
        #gcode_handler.send_gcode("M114")
    print("All positions scanned. Scan finished")

def stitch(imagepath,K,P,DIM,scantype,width=640,height=512):
    """
    Stitches images  from stepped scan method. From a given file path using specified camera parameters.
    Parameters:
    -----------
    imagepath : str
        The path to the image file to be processed. Supported formats are .raw and .tiff.
    K : array-like
        Camera matrix.
    P : array-like
        Projection matrix.
    DIM : tuple
        Dimensions of the image.
    scantype : str
        Type of scan to be performed. options are 1. multistitch (3 images) 2. continuous scan
    width : int, optional
        Width of the image (default is 640).
    height : int, optional
        Height of the image (default is 512).
    Returns:
    --------
    None
        The function does not return any value. It processes the images and saves the stitched result.
    Notes:
    ------
    - For .raw files, specific processing is done using `ProcessInGaAs.load_raw_image`.
    - For .tiff files, specific processing is done using `tifffile.imread` and `ProcessInGaAs.int16_2_uint16`.
    - The stitched images are saved with the suffix "_stitched.png".
    - The function uses `stitchImages.roughStitchPL` and `stitchImages.roughStitchGeo` for stitching.
    """

    # for i in os.path.join(cwd,"Images"):
    if imagepath.lower().endswith('.raw'):
        # Add specific processing for .raw files if needed
        print("Processing a .raw file")
        images=ProcessInGaAs.load_raw_image(imagepath, width, height)
    elif imagepath.lower().endswith('.tiff'):
        # Add specific processing for .tiff files if needed
        print("Processing a .tiff file") #TODO: Implement tiff loading
        images = tifffile.imread(os.path.join(cwd, "Images", imagepath))
        #DEBUGGING: display linstretched image [0]  
        # cv2.imshow("Test image",ProcessInGaAs.lin_stretch_img(images[0],40,99.99))
        # cv2.waitKey()
        # cv2.destroyAllWindows()
        
        images=ProcessInGaAs.int16_2_uint16(images)
        # cv2.imshow("Test image after normalization",ProcessInGaAs.lin_stretch_img(images[0],40,99.99))
        # cv2.waitKey()
        # cv2.destroyAllWindows()
        #images=ProcessInGaAs.load_tiff_image(imagepath)
    else:
        print("File type not supported")
        return
    
    print("Images loaded. number of images: ",len(images))
    
    # savename = os.path.splitext(imagepath)[0] + "_stitched"
    savename="_stitched.png"
    stitchImages.roughStitchPL(images, K, P, DIM, imagepath,savename=savename,disp=False,EL=True)
    stitchImages.roughStitchGeo(images, K, P, DIM,imagepath, speed=5500, nsteps=3, FPS=50,savename=savename)
    
    pass

#def scan():
    #Psuedo code
    #1. Move camera to first position
    #2. Capture images while moving light bar
    #3. move camera to next position
    #4. Repeat until all positions are scanned
    #5. Process images
    #6. Stitch images together
    #7. Save stitched image
    #camPosArr=[] #Camera Position Array
    #lightPosArr=[] #Light Position Array

def stopCamera(context):
    """
    Stops camera context using FLI API
    """
    FliSdk_V2.Stop(context)
    FliSdk_V2.Exit(context)
    print("Camera disconnected")
def stopGantry(gcode_handler):
    """
    Stops gantry by disconnecting serial connection.
    """
    gcode_handler.disconnect()
def main():
    ####
    #USER VALUES
    ####
    speed=5000 # Gantry speed (mm/min)
    frameRate = 50  # Camera Framerate
    tintVal = 1  # Exposure
    nsteps=3 #number of steps for scan


    ####
    #Undistortion Load
    ####
    calpath=os.path.join(cwd,"Calibration") #path for calibration files
    t=input("Want to load existing undistortion calibration? (y/n)") 
    
    if t=="y":
        calpath=input("enter calibration path. Leave empty for default calibration") or calpath #path for calibration file
        K,P,DIM=calibrateLoad(calpath)
        print("Undistortion calibration loaded")
    else:
        # t=input("Want to load own checkerboard calibration files? (y/n)")
        # if t=="y":
        #     calpath=input("Please enter path to calibration files")
        #     calfile="Checkerboard_0_3_ms_33hz_09012025_175256.raw" #hardcoded for now
        #     cal=os.path.join(calpath,calfile)
        #     calimgs=ProcessInGaAs.load_raw_image(cal,640,512)
        #     K,P,DIM=ProcessInGaAs.calibrateRaw(calimgs)
        #     np.save(os.path.join(calpath,"K_matrix"),K)
        #     np.save(os.path.join(calpath,"P_matrix"),P)
        #     np.save(os.path.join(calpath,"DIM_matrix"),DIM)
        print("Weird calibration path here. just load existing instead. Functions exist to capture new calibration, recalibrate or choose other path, but deemed unnecessary for now.")
        K,P,DIM=calibrateLoad(calpath)
        print("Undistortion calibration loaded")

 
    ############################
    #calibrate FLI camera
    ############################
    t=input("Prepare for camera calibration")
    context=calibrateCamera(frameRate, tintVal) #output context for acquisition

    ############################
    #Connect and Calibrate Gantry
    ############################
    t=input("Prepare for gantry calibration")
    gCode_handler=connectGantry()
    calibrateGantry(gCode_handler)
    gCode_handler.send_gcode("M400")

    ############################
    #Start scanning
    ############################
    scantype=input("Start scanning? Enter type: 1. multistitch (3 images) or 2. continuous scan")
    
    if scantype=="1":    
        try:
            scan(gCode_handler,context,savePath=os.path.join(cwd,"Images"),frameRate=frameRate,speed=speed,nsteps=nsteps)
        except:
            print("Error scanning")
            stopCamera(context)
            stopGantry(gCode_handler)
            sys.exit()
    elif scantype=="2":
        try:
            scanContinuous(gCode_handler,context,savePath=os.path.join(cwd,"Images"),frameRate=frameRate,speed=speed)
        except:
            print("Error scanning")
            stopCamera(context)
            stopGantry(gCode_handler)
            sys.exit()
    else:
        print("Invalid scan type")
        stopCamera(context)
        stopGantry(gCode_handler)
        sys.exit()    
        
    ############################
    #End of scanning
    ############################
    stopCamera(context)
    stopGantry(gCode_handler)

    ############################
    #Process and Stitch images
    ############################
    t=input("Start processing and stitching")
    if scantype==1:
        #Multi-image stitch:
        print("Multi-image stitch starting...")
        image_files = [f for f in os.listdir(os.path.join(cwd, "Images")) if f.endswith('.raw') or f.endswith('.tiff')]
        for image_file in image_files:
            image_path = os.path.join(cwd, "Images", image_file)
            stitch(image_path, K, P, DIM)
        GeoPLstitched_images = [os.path.join(cwd, "Images", f) for f in os.listdir(os.path.join(cwd, "Images")) if f.endswith('GeoPL_stitched.png')]
        stitchImages.multiStitch(GeoPLstitched_images)
    if scantype==2:
        #Continuous scan stitch:
        image_files = [f for f in os.listdir(os.path.join(cwd, "Images")) if f.endswith('.raw') or f.endswith('.tiff')]
        #Only get scan_cont images
        image_files = [f for f in image_files if 'scan_cont' in f] 
        stitchImages.stitchCont(os.path.join(image_files[-1]),K,P,DIM) #stitch the last of these
        pass
if __name__ == "__main__":
    #GUI() #TODO: Implement GUI
    main()
