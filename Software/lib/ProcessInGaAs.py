"""
Created on Dec 12 2024
@author: Carl Emil Elling

Image calibration and processing library for DTU InGaAs cameras
"""
import numpy as np
import cv2
from matplotlib import pyplot as plt
import os
import sys
from lib import ProcessInGaAs


def load_raw_image(file_path, width, height):
    """Load a .RAW multi-image file."""
    image = np.fromfile(file_path, dtype=np.int16, sep="")
    num_images = image.size // (width * height)
    if image.size != num_images * width * height:
        raise ValueError(f"File size does not match expected dimensions: {num_images} images of {width}x{height}")
    image = image.reshape((num_images, height, width))
    image= int16_2_uint16(image)
    return image
def crop_image(image):
    """Crop the image to only the columns with data."""
    # Find the first and last column with non-zero pixel values
    col_sums = np.sum(image, axis=0)
    first_col = np.nonzero(col_sums)[0][0]
    print("first_col",first_col)
    last_col = np.nonzero(col_sums[::-1])[0][0]
    last_col = image.shape[1] - last_col - 1
    print("last_col",last_col)
    # Crop the image to the region with data
    cropped_image = image[:, first_col:last_col]
    return cropped_image
def lin_stretch_img(img, low_prc, high_prc):
    """
    Perform histogram linear stretch on an image.
    This function enhances the contrast of an image by stretching the pixel values
    linearly between the specified low and high percentiles.
    Parameters:
    img (numpy.ndarray): The input image to be stretched.
    low_prc (float): The low percentile for the stretch (e.g., 1 for 1%).
    high_prc (float): The high percentile for the stretch (e.g., 99 for 99%).
    Returns:
    numpy.ndarray: The contrast-enhanced image with pixel values stretched between 0 and 255.
    Notes:
    - If the low and high percentiles are equal, the function returns a gray image.
    - The input image is expected to be a NumPy array.
    - The output image is of type uint8.
    Example:
    >>> import numpy as np
    >>> img = np.random.rand(100, 100) * 255  # Example image
    >>> enhanced_img = lin_stretch_img(img, 1, 99)
  https://stackoverflow.com/questions/75624273/how-to-read-and-enhance-contrast-of-32bit-tiff-image-using-opencv2-in-python-co  """
    # from 
    lo, hi = np.percentile(img, (low_prc, high_prc))  # Example: 1% - Low percentile, 99% - High percentile
    if lo == hi:
        return np.full(img.shape, 128, np.uint8)  # Protection: return gray image if lo = hi. converts to uint8

    stretch_img = (img.astype(np.float32) - lo) * (255/(hi-lo))  # Linear stretch: lo goes to 0, hi to 255.
    stretch_img = stretch_img.clip(0, 255).astype(np.uint8)  # Clip range to [0, 255] and convert to uint8
    return stretch_im

def CLAHE_STRETCH(img):
    """Apply CLAHE (Contrast Limited Adaptive Histogram Equalization) to the image."""
    #Image must be uint16
    clahe = cv2.createCLAHE(clipLimit=20, tileGridSize=(8, 8))
    cl1 = clahe.apply(img)  # CLAHE in OpenCV does not support float32. apply CLAHE to the uint16 image.
    cl1 = cv2.convertScaleAbs(cl1, alpha=255/65535)  # Convert from uint16 to uint8
    return cl1

def find_peak_intensity(image,disp=False):
    """Find the average intensity along one axis. Then, find the index of the peak value."""
    imsum=np.sum(image,axis=0)/np.shape(image)[0] #averaged sum
    idx=round(imsum.argmax()) #index of peak
    if disp:
        xax=np.arange(0, len(imsum), 1)
        plt.plot(xax,imsum,"r-")
        plt.axvline(x=idx) #plot the peak line!
        plt.axis((0, len(imsum), 0, max(imsum)))
        plt.xlabel("Column Index [px]")
        plt.ylabel("Average Intensity[arb. u]")
        plt.ylim(0, 255)
        plt.title("Average emmision intensity along x-axis")
        plt.show()
    return idx

def create_bounding_box(image, idx,BB_width=15,ELoffset=30,LEDoffset=40,disp=True):
    """
    Create a vertical bounding box in the image based on an index.

    Parameters:
    image (numpy.ndarray): The input image in which the bounding box will be created.
    idx (int): The index around which the bounding box will be centered.
    BB_width (int, optional): The width of the bounding box. Default is 15.
    disp (bool, optional): If True, the image with the bounding box will be displayed. Default is True.

    Returns:
    tuple: A tuple containing two lists:
        - BB_PL (list): The primary bounding box coordinates as [(minx, miny), (maxx, maxy)].
        - BB_EL (list): The EL bounding box coordinates as [(minx, miny), (maxx, maxy)].
        - BB_LED (list): The LED bounding box coordinates as [(minx, miny), (maxx, maxy)].
    """
   
    # _, binary = cv2.threshold(image, threshold, 255, cv2.THRESH_BINARY)
    rectColor=(255, 0, 0)
    rectColorEL=(255, 0, 255)
    thickness=1
    BB_PL=[((idx-round(BB_width/2)),0),((idx+round(BB_width/2)),np.shape(image)[0])] #kernel bounding box [(minx,miny)(maxx)(maxy)] (that is, [upper left, lower right])
    BB_EL=[((idx-round(BB_width/2))+ELoffset,0),((idx+round(BB_width/2))+ELoffset,np.shape(image)[0])] #For EL. 
    BB_LED=[((idx-round(BB_width/3))-LEDoffset,0),((idx+round(BB_width/3))-LEDoffset,np.shape(image)[0])] #For LEDS. 
    #Either this, or threshold, segment, find contours and subtract PL box?
    if disp:
        imageRGB=ProcessInGaAs.lin_stretch_img(image,1,99.99)
        imageRGB = cv2.cvtColor(imageRGB, cv2.COLOR_GRAY2BGR)
        cv2.rectangle(imageRGB,BB_PL[0],BB_PL[1],rectColor,thickness)
        cv2.rectangle(imageRGB,BB_EL[0],BB_EL[1],rectColorEL,thickness)
        cv2.imshow("LoadedImageEnhanced1_kernel",imageRGB)
        cv2.waitKey(1)
    return BB_PL,BB_EL,BB_LED

def display_and_save_video(image, bounding_box, output_file):
    """Display and save video in .mp4 format of linear stretching and bounding box."""
    height, width = image.shape
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_file, fourcc, 20.0, (width, height))

    for _ in range(100):  # Display the same frame 100 times for demonstration
        frame = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
        if bounding_box:
            x, y, w, h = bounding_box
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        out.write(frame)
        cv2.imshow('Frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    out.release()
    cv2.destroyAllWindows()

#def acquireCalSequence(context):
def int16_2_uint16(img):
    """
    Normalize a 16-bit signed integer image to a 16-bit unsigned integer image.
    Parameters:
    img (numpy.ndarray): Input image with 16-bit signed integer pixel values.
    Returns:
    numpy.ndarray: Normalized image with 16-bit unsigned integer pixel values.
    """
    norm_img = cv2.normalize(img, dst=None, alpha=0, beta=65535,norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_16U)
    return norm_img
def int16_2_uint8(img):
    """
    Convert a 16-bit integer image to an 8-bit unsigned integer image.

    This function normalizes the input 16-bit integer image to the range [0, 255]
    and converts it to an 8-bit unsigned integer image.

    Parameters:
    img (numpy.ndarray): Input image with 16-bit integer pixel values.

    Returns:
    numpy.ndarray: Output image with 8-bit unsigned integer pixel values.
    """
    norm_img = cv2.normalize(img, dst=None, alpha=0, beta=255,norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)
    return norm_img


def shitty_lens_dist(img, k1 = -7.0e-6, f = 6.):
    """
    Basic image undistortion when all else fails. 
    From Rodrigo.
    """
    # grid: image to distort

    # k1: lens curvature param

    # f: lens focal length
    s = img.shape
    distCoeff = np.zeros((4,1))#,np.float32)
    distCoeff[0,0] = k1
    # set focal length
    #f = 8.
    # assume unit matrix for camera
    cam = np.eye(3)#,dtype=np.float32)
    cam[0,2] = s[1]/2.  # define center x
    cam[1,2] = s[0]/2. # define center y
    cam[0,0] = f        # define focal length x
    cam[1,1] = f        # define focal length y
    #return cv2.undistort(img.astype(np.float32), cam, distCoeff)
    return cv2.undistort(img, cam, distCoeff)

def calibrateRaw(rawImgs, checkerboard=(6,8),disp=False):
    
    """
    Calibrate a fisheye camera using a series of raw images of a checkerboard pattern.
    This function performs fisheye camera calibration using OpenCV. It converts the calibration image set to uint8 format,
    detects checkerboard corners in the images, and computes the camera matrix and distortion coefficients.

    Parameters:
    rawImgs (list of ndarray): .raw multi-image opened as array (n-images) to be used for calibration.
    checkerboard (tuple of int, optional): Number of inner corners per a chessboard row and column (default is (6, 8)).
    disp (bool, optional): If True, displays the images with detected corners (default is False).
    Returns:
    tuple: A tuple containing:
        - K (ndarray): Camera matrix.
        - P (ndarray): Distortion coefficients.
    Raises:
    AssertionError: If all images are not the same size.
    Notes:
    - The function uses subpixel corner detection and fisheye calibration methods from OpenCV.
    - The function assumes that the input images are grayscale.
    - subpixel fisheye calibration code with inspiration from https://medium.com/@kennethjiang/calibrate-fisheye-lens-using-opencv-333b05afa0b0
    Example:
    >>> K, P, DIMS = calibrateRaw(rawImgs, checkerboard=(6, 8), disp=True)
    """
    print("Calibrating Camera")
    images=int16_2_uint8(rawImgs) # Convert int16 to uint8 (for findChessboardCorners function)
    subpix_criteria = (cv2.TERM_CRITERIA_EPS+cv2.TERM_CRITERIA_MAX_ITER, 30, 0.1)
    calibration_flags = cv2.fisheye.CALIB_RECOMPUTE_EXTRINSIC+cv2.fisheye.CALIB_CHECK_COND+cv2.fisheye.CALIB_FIX_SKEW
    #Make object points like (0,0,0), (1,0,0), (2,0,0) ...., (6,5,0)
    objp = np.zeros((1, checkerboard[0]*checkerboard[1], 3), np.float32)
    objp[0,:,:2] = np.mgrid[0:checkerboard[0], 0:checkerboard[1]].T.reshape(-1, 2)
    objpoints = [] # 3d point in real world space
    imgpoints = [] # 2d points in image plane.
    _img_shape = None   

    path=os.getcwd()
    for i in range(len(images)):
        ret, corners = cv2.findChessboardCorners(images[i], checkerboard, cv2.CALIB_USE_INTRINSIC_GUESS)
        if _img_shape == None:
            _img_shape = images[i].shape[:2]
        else:
            assert _img_shape == images[i].shape[:2], "All images must share the same size."
        if ret:
            if disp:
                fimg = cv2.drawChessboardCorners(images[i], checkerboard, corners, ret)
                cv2.imshow('img', fimg)
                cv2.waitKey(1)
                print("Found all corners")
            objpoints.append(objp)
            cv2.cornerSubPix(images[i],corners,(3,3),(-1,-1),subpix_criteria)
            imgpoints.append(corners)
    cv2.destroyAllWindows()
    N_OK = len(objpoints)
    K = np.zeros((3, 3))
    D = np.zeros((4, 1))
    rvecs = [np.zeros((1, 1, 3), dtype=np.float64) for i in range(N_OK)]
    tvecs = [np.zeros((1, 1, 3), dtype=np.float64) for i in range(N_OK)]
    rms, _, _, _, _ = \
        cv2.fisheye.calibrate(
            objpoints,
            imgpoints,
            images[i].shape[::-1],
            K,
            D,
            rvecs,
            tvecs,
            calibration_flags,
            (cv2.TERM_CRITERIA_EPS+cv2.TERM_CRITERIA_MAX_ITER, 30, 1e-6)
        )
    print("Found " + str(N_OK) + " valid images for calibration with RMS val:", rms)
    DIM=np.asarray(_img_shape[::-1])
    print("DIM=" + str(DIM))
    print("K=np.array(" + str(K.tolist()) + ")")
    print("D=np.array(" + str(D.tolist()) + ")")
    return K,D,DIM
def loadCal(calpath,width,height):
    """
    Loads calibration matrices from the specified path. If the calibration files are not found,
    prompts the user to perform calibration using a pre-set calibration video.
    Parameters:
    calpath (str): The path to the directory containing the calibration files.
    width (int): The width of the image used for calibration.
    height (int): The height of the image used for calibration.
    Returns:
    tuple: A tuple containing the calibration matrices K, P, and DIM.
    Raises:
    SystemExit: If the user chooses not to perform calibration when prompted.
    Notes:
    - The function expects the calibration files to be named 'K_matrix.npy', 'P_matrix.npy', and 'DIM_matrix.npy'.
    - If calibration is performed, the function saves the new calibration matrices to the specified path.
    - The calibration process currently supports a hardcoded checkerboard calibration file.
    """
    try:
        K=np.load(os.path.join(calpath,"K_matrix.npy"))#,allow_pickle=True)
        P=np.load(os.path.join(calpath,"P_matrix.npy"))#,allow_pickle=True)
        DIM=np.load(os.path.join(calpath,"DIM_matrix.npy"))#,allow_pickle=True)
        print("Calibration Files Loaded!")
    except: 
        print("Calibration Files not found! Please calibrate the camera first!")
        t=input("calibrate using pre-set calibration video (in calibration folder)? (y/n)")
        if t=="y":
            t=input("calibration type: 1. Checkerboard 2. Dots")
            if t=="1":
                #os.listdir(calpath)
                calfile="Checkerboard_0_3_ms_33hz_09012025_175256.raw" #hardcoded for now
                cal=os.path.join(calpath,calfile)
                #Checkerboard calibration
                width, height = 640, 512  # Example dimensions, adjust as necessary
                imgCal = load_raw_image(cal, width, height)
                K,P,DIM= calibrateRaw(imgCal, checkerboard=(6,8), disp=False)
                np.save(os.path.join(calpath,"K_matrix"),K)
                np.save(os.path.join(calpath,"P_matrix"),P)
                np.save(os.path.join(calpath,"DIM_matrix"),DIM)
                print("Calibration performed and Files Saved!")
        else:
            sys.exit(0)
        
    return K,P,DIM
def undistort(imageArr,K,D,dim=(640,512)):
    """
    Undistorts a given image using the provided camera matrix and distortion coefficients.
    Parameters:
    image (numpy array): The distorted input image array.
    K (numpy array): Camera matrix (intrinsic parameters).
    D (numpy array): Distortion coefficients.
    dim (tuple): The dimensions (width, height) of the image used in calibration. Default is (640, 512).
    Returns:
    undistorted_img (numpy array): The undistorted image.
    Raises:
    AssertionError: If the aspect ratio of the input image does not match the aspect ratio of the calibration dimensions.
    """
    undistorted_img=[]
    dim1 = imageArr[0].shape[:2][::-1]
    assert dim1[0]/dim1[1] == dim[0]/dim[1], "Image to undistort needs to have same aspect ratio as the ones used in calibration"
    map1, map2 = cv2.fisheye.initUndistortRectifyMap(K, D, np.eye(3), K, dim, cv2.CV_16SC2)
    for image in imageArr:
       undistorted_img.append(cv2.remap(image, map1, map2, interpolation=cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT))
    return undistorted_img

