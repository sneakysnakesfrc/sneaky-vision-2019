# Debug or not
DEBUG = 1
# Trackbar or not
CREATE_TRACKBARS = 0
# Display or not
DISPLAY = 1
# Image or Video, if "Video" is given as argument, program will use cv2.VideoCapture
# If "Image" argument is given the program will use cv2.imread
imageType = "Video" # Image
# Image/Video source 0 or 1 for webcam or the file path of the video source such as 
# "images/rocket/RocketPanelStraightDark72in.jpg" or "images/rocket/testvideo.mp4"
imageSource = 1
# Ip address
ipAddress = "10.99.99.2"
# The script to make camera arrangements
osScript = "v4l2-ctl -d /dev/video1 -c exposure_auto=1 -c exposure_auto_priority=0 -c exposure_absolute=50"
# Call OS script or not, close this in WINDOWS
callOS = 1
# NetworkTable Name
networkTableName = "visiontable"
# Camera Properties
camera = { 'HFOV'        : 80.0,  # Horizontal FOV of the camera, see camera datsheet
           'VFOV'        : 64.0,  # Vertical FOV of the camera, see camera datasheet
           'Brightness'  : 1,     # Brightness of the image
           'Contrast'    : 1000,  # Contrast of the image
           'HeightDiff'  : 15,    # Height difference between camera and target
           'MountAngle'  : -5,    # Mounting angle of the camera need minus sign if pointing downwards
           'Size'        : 300,   # Resized image size in pixels (image becomes square)
           'DoCrop'      : 1,     # Crop the image or don't
           'CropXLow'    : 0,     # Lowest Point in X axis to be cropped
           'CropXHigh'   : 300,   # Highest Point in X axis to be cropped
           'CropYLow'    : 125,   # Lowest Point in Y axis to be cropped
           'CropYHigh'   : 300,   # Highest Point in Y axis to be cropped
           'ColorSpace'  : 'HSV', # Which color space to use default is BGR if not HSV is defined
           'H_low'       : 13,    # Lower Hue value to be filtered, 55
           'H_high'      : 255,   # Higher Hue to be filtered
           'S_low'       : 25,    # Lower Saturation to be filtered, 97
           'S_high'      : 255,   # Higher Saturation to be filtered
           'V_low'       : 24,   # Lower Value to be filtered, 177
           'V_high'      : 255,   # Higher Value to be filtered
           'B_low'       : 5,     # Lower Blue value to be filtered
           'B_high'      : 95,    # Higher Blue value to be filtered
           'G_low'       : 135,   # Lower Green value to be filtered
           'G_high'      : 255,   # Higher Green value to be filtered   
           'R_low'       : 121,   # Lower Red value to be filtered
           'R_high'      : 181    # Higher Red value to be filtered
        }

filter = {  'MinArea' : 20, # Minimum value of area filter in pixels
            'MaxArea'  : 900 # Maximum value of area filter in pixels
        }