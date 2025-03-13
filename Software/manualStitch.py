import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
import sys
import time
sys.path.append('FLI_API')
sys.path.append('Stitching')
sys.path.append('Acquisition')
sys.path.append('lib')
from lib import ProcessInGaAs
from lib import imageAcquisition
from lib import gCodeHandler
from lib import stitchImages
import cv2
import tifffile
from scipy.ndimage import rotate
import glob

def manualstitch(source,calpath,rotation=0,speed=5000,drift=0.0466,nsteps=100,FPS=50):
    """
    Manually stitches a sequence of images from a .tiff file using calibration data.
    Parameters:
    source (str): Path to the source .tiff file containing the images to be stitched.
    calpath (str): Path to the calibration files.
    rotation (int, optional): Angle to rotate images for stitching. Default is 0.
                                Supported values are 0, 90, and any other angle for custom rotation
                                (but is a slow affine transformation, be careful!).
    speed (int, optional): Speed parameter for the stitching process. Default is 5000.
    drift (float, optional): Drift correction factor. Default is 0.0466 (experimentally found).
    nsteps (int, optional): NOT USED. TODO:REMOVE IT. Number of steps for the stitching process. Default is 100.
    FPS (int, optional): Frames per second for the stitching process. Default is 50.
    Returns:
    None
    Notes:
    - The function loads calibration files, reads images from the source .tiff file, undistorts the images,
        optionally rotates them, and then stitches them together.
    - The stitched image is saved as "stitched_image_cont.png".
    - The function prints progress and debug information to the console.
    """
    #Load calibration files
    width, height = 640, 512  # Example dimensions, adjust as necessary
    K,P,DIM=ProcessInGaAs.loadCal(calpath,width,height)
    
    # Read images
    print("Processing a .tiff file") #TODO: Implement tiff loading
    images = tifffile.imread(source)
    images=ProcessInGaAs.int16_2_uint16(images)
    print("Images loaded. Number of images: ",len(images))
    print("shape original: ",np.shape(images))

    #Undistort images
    print("Undistorting images")
    imgUndistorted=ProcessInGaAs.undistort(images,K,P,DIM)
    print("Images undistorted")
    #rotate images for stitching
    print("rotating images")
    if rotation==0:
        imagerot=imgUndistorted
    elif rotation==90:
        #fast and easy counter clockwise rotation
        imagerot = [np.rot90(image, k=3) for image in imgUndistorted]
    else:
        DIM=(DIM[1],DIM[0])
        imagerot=rotate(imgUndistorted[0],rotation)
        print("shape before: ",np.shape(imagerot)) #DEBUG
        imagerot=imagerot[np.newaxis,...] #reshaope to 3D array
        for i in range(1, len(imgUndistorted)):
            #rotating images (very slow method... different one somewhere?)
            imagerot = np.append(imagerot, rotate(imgUndistorted[i], rotation)[np.newaxis, ...], axis=0)
            if i%100==0:
                #Progress indicator... so slow
                print("rotating image #",i)
        print("shape after: ",np.shape(imagerot))
    print("Images rotated")
    #Image stitching
    stitchImages.roughStitchCont(imagerot,K,P,DIM,source,speed,nsteps,FPS,savename="stitched_image_cont.png",drift=drift,manualStitch=True)
    print("stitch done!")
def subtract(source1,source2,calpath,rotation=0,speed=4000,drift=0.0466,nsteps=100,FPS=50):
    """
    EXPERIMENTAL:
    Subtracting two images and displaying the result - for modulation!
    """

    #Load calibration files
    width, height = 640, 512  # Example dimensions, adjust as necessary
    K,P,DIM=ProcessInGaAs.loadCal(calpath,width,height)
    
    # Read images
    print("Processing a .tiff file") #TODO: Implement tiff loading
    imageshigh = tifffile.imread(source1)
    imageshigh=ProcessInGaAs.int16_2_uint16(imageshigh)
    imageslow = tifffile.imread(source2)
    imageslow=ProcessInGaAs.int16_2_uint16(imageslow)
    print("Images loaded. Number of images: ",len(imageshigh))
    print("shape original: ",np.shape(imageshigh))

    #Undistort images
    print("Undistorting images")
    imgUndistortedHigh=ProcessInGaAs.undistort(imageshigh,K,P,DIM)
    imgUndistortedLow=ProcessInGaAs.undistort(imageslow,K,P,DIM)
    print("Images undistorted")
    # Concatenate images side by side
    concatenated_image = np.concatenate([ProcessInGaAs.lin_stretch_img(imgUndistortedHigh[168], 40, 99.99), ProcessInGaAs.lin_stretch_img(imgUndistortedLow[168], 40, 99.99)], axis=1)

    # Display concatenated image
    cv2.imshow("Concatenated Image", concatenated_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    #Subtract images
    print("Subtracting images")
    #Print test values from both images at same pixel
    print("High efficiency panel: ",imgUndistortedHigh[168,300,300])
    print("Low efficiency panel: ",imgUndistortedLow[168,300,300])
    imgdiff = imgUndistortedHigh[168]- imgUndistortedLow[168]
    print("Images subtracted")
    #Print test values from subtracted image
    print("Subtracted image: ",imgdiff[300,300])
    # Linstretch the subtracted image
    imgdiff_stretched = ProcessInGaAs.lin_stretch_img(imgdiff, 40, 99.99)
    cv2.imshow("Subtracted image", imgdiff_stretched)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
def savevideo(source,calpath,rotation=0,speed=4000,drift=0.0466,nsteps=100,FPS=50):
     # Load image file to be stitched:
    
    #Load calibration files
    width, height = 640, 512  # Example dimensions, adjust as necessary
    K,P,DIM=ProcessInGaAs.loadCal(calpath,width,height)

    # Read images
    print("Processing a .tiff file") #TODO: Implement tiff loading
    images = tifffile.imread(source)
    images=ProcessInGaAs.int16_2_uint16(images)
    print("Images loaded. Number of images: ",len(images))
    print("shape original: ",np.shape(images))

    #Undistort images
    print("Undistorting images")
    imgUndistorted=ProcessInGaAs.undistort(images,K,P,DIM)

    print("Images undistorted")
    #rotate images for stitching
    print("rotating images")
    if rotation==0:
        #No rotation
        imagerot=imgUndistorted
    elif rotation==90:
        #fast and easy counter clockwise rotation
        imagerot = [np.rot90(image, k=3) for image in imgUndistorted]
    else:
        #Affine transformation of exact degrees. Slow...
        DIM=(DIM[1],DIM[0])
        imagerot=rotate(imgUndistorted[0],rotation) #Rotate first image for holding array
        imagerot=imagerot[np.newaxis,...] #reshaope to 3D array
        for i in range(1, len(imgUndistorted)):
            #rotating images (very slow method... different one somewhere?)
            imagerot = np.append(imagerot, rotate(imgUndistorted[i], rotation)[np.newaxis, ...], axis=0)
            if i%100==0:
                #Progress indicator... so slow
                print("rotating image #",i)
    print("Images rotated, shape: ",np.shape(imagerot))

    #Now save as a video
    print("Saving video")
    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('Scan_video.avi', fourcc, FPS, (np.shape(imagerot)[2], np.shape(imagerot)[1]))

    for i in range(len(imagerot)):
        #Linstretch image and save as .avi
        #Linstretch: High efficiency 1,99.99. Low efficiency panel 40,99.99
        frame = ProcessInGaAs.lin_stretch_img(imagerot[i], 40, 99.99).astype(np.uint8)
        out.write(cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR))  # Convert grayscale to BGR

    out.release()
    print("Video saved as output.avi")

def main():
    """
    Function for manually stitching a continuous PL scan captured as a .tiff file.
    User variables can be set:
    Path:
      Path to the .tiff file to be processed. In the "Images" folder.
    Rotation: 
      Rotation of the images in degrees. 0 for no rotation, 90 for 90 degrees counter clockwise rotation.
      Otherwise uses a slow affine transformation for exact degrees.
    Speed:
      Speed of the scan in mm/s. Nominally 5000 mm/s, but can be varied for better imaging.
    drift:
        Drift of the scan in mm/s. Measured from first and last image in continuous scan, seeing lateral displacement and averaging.
    nsteps:
        Number of steps in the scan. Used for calculating the time of the scan, but here mostly a dummy variable.
        TODO: remove it
    FPS:
        Frames per second of the video. Used for calculating where to stitch subsequent images 
    """

    #setup path
    cwd=os.getcwd()
    impath=os.path.join(cwd,"Images")#Read tiff or raw file with ProcessInGaAs
    calpath=os.path.join(cwd,"Calibration")

    #User variables:
    #path=os.path.join(impath,"scan_cont_2025-02-24_15-53.tiff")
    path=os.path.join(impath,"scan_cont_2025-03-13_20-52.tiff")
    
    rotation=180+88 #In degrees
    rotation=90
    speed=4000
    drift=0.02448
    FPS=50
    nsteps=3
    path1=os.path.join(impath,"scan_cont_2025-02-28_15-48_10ms_low_w_IR.tiff")
    path2=os.path.join(impath,"scan_cont_2025-02-28_15-51_10ms_1_3A_low_noIR_outdoor.tiff")

    #Run either manualstitch or savevideo
    manualstitch(path,calpath,rotation,speed,drift,nsteps,FPS)
    # savevideo(path,calpath,rotation)
    #subtract(path1,path2,calpath)
def loadSnapshot():
    """
    Function for loading a .raw snapshot captured with FLI software and undistorting it. Showing the result in a window.
    """
    cwd=os.getcwd()
    impath=os.path.join(cwd,"Images/Results")#Read tiff or raw file with ProcessInGaAs
    path1=os.path.join(impath,"snapshot_07032025_172117_higheff_dist_2ms_18A.raw")
    width, height = 640, 512
    im=ProcessInGaAs.load_raw_image(path1,width,height)
    calpath=os.path.join(cwd,"Calibration")
    K,P,DIM=ProcessInGaAs.loadCal(calpath,width,height)
    imgUndistorted=ProcessInGaAs.undistort(im,K,P,DIM)
    cv2.imshow("Image", ProcessInGaAs.lin_stretch_img(imgUndistorted[0],1,99.99))
    cv2.waitKey(0)
    cv2.destroyAllWindows()
def histogramPlot():
    """
    Function for plotting histogram of scan before and after linstretch
    """
    cwd=os.getcwd()
    impath=os.path.join(cwd,"Images")#Read tiff or raw file with ProcessInGaAs
    source=os.path.join(impath,"scan_cont_2025-02-24_15-53.tiff")
    width, height = 640, 512
    images = tifffile.imread(source)
    images=ProcessInGaAs.int16_2_uint16(images)
    counts, bins = np.histogram(images[400].ravel(), bins=range(0, 65536))
    plt.figure()
    plt.plot(bins[:-1], counts)  # Use plt.plot for histogram
    plt.xlabel('Pixel Value')
    plt.ylabel('Frequency')
    plt.title('Histogram (before linstretch)')
    plt.show()
    print("Linstretching images")
    images_lin = ProcessInGaAs.lin_stretch_img(images[400:450], 0.01, 99)
    print("Histogram")
    counts, bins = np.histogram(images_lin[0].ravel(), bins=range(0, 255))

    print("plotting")
    cv2.imshow("Image", images_lin[0])
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    plt.figure()
    print("Sum of counts: ",np.sum(counts))
    print("total pixels: ",np.shape(images_lin[0])[0]*np.shape(images_lin[0])[1])
    plt.plot(bins[:-1], counts)  # Use plt.plot for histogram
    plt.xlabel('Pixel Value')
    plt.ylabel('Frequency')
    plt.title('Histogram (after linstretch)')
    plt.show()

def cropRaw():
    """
    Function for cropping, linstretching and saving a raw image. For testing purposes
    """
    cwd = os.getcwd()
    # impath = os.path.join(cwd, "Images/Results")  # Read tiff or raw file with ProcessInGaAs
    # path1 = os.path.join(impath, "snapshot_07032025_172117_higheff_dist_2ms_18A.raw")
    path = os.path.join(cwd, "Images","prelim_tests")
    print(path)
    # Get all .raw images in the specified path
    raw_images = glob.glob(os.path.join(path, "*.raw"))
    name=os.path.join(path,"PL_Test1_29102024_152953.raw")
    width, height = 640, 512
    calpath = os.path.join(cwd, "Calibration")
    K, P, DIM = ProcessInGaAs.loadCal(calpath, width, height)
    for raw_image in raw_images:
        im = ProcessInGaAs.load_raw_image(raw_image, width, height)
        imgUndistorted = ProcessInGaAs.undistort(im, K, P, DIM)
        # Define crop region (example: center crop)
        crop_x, crop_y = 230, 0
        crop_width, crop_height = 400, 200
        cropped_img = imgUndistorted[0][crop_y:crop_y + crop_height, crop_x:crop_x + crop_width]
        # Linstretch the cropped image
        cropped_img_stretched = ProcessInGaAs.lin_stretch_img(cropped_img, 1, 99.99)
        #cropped_img_stretched = rotate(cropped_img_stretched, -3)
        # Save the cropped and linstretched image
        save_path = raw_image+"cropped.png"
        print(save_path)
        cv2.imwrite(save_path, cropped_img_stretched)
    
        # # Display the cropped and linstretched image
        # cv2.imshow("Cropped Image", cropped_img_stretched)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
if __name__ == "__main__":
    main()
    #loadSnapshot()
    #histogramPlot()
    # cropRaw()