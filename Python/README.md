Learning OpenCV in Python from the video: https://www.bilibili.com/video/av13924091/

# 1.Intro and Loading Images

## Functions

cv2.imread()

cv2.imshow()

cv2.waitKey()

cv2.destroyAllWindows()

cv.imwrite()

# Variables

cv2.IMREAD_COLOR = 1

cv2.IMREAD_GRAYSCALE = 0

cv2.IMREAD_UNCHANGED = -1



# 2.Loading Video Source

## Functions

cv2.VideoCapture()

cv2.VideoWrite_fourcc()

cv2.VideoWrite()

cv2.cvtColor()



## 3.Drawing and Writing on Image

## Functions

cv2.line()

cv2.rectangle()

cv2.circle()

cv2.ellipse()

cv2.polylines()

cv2.putText()

## Variables

cv.LINE_AA



# 4.Image Operations

**Pixel**

img[300, 400]: row=300, col=400

**Rectangle(ROI)**

roi[300:500, 400:700]: 300 =< row <= 500,  400 =<col <= 700



# 5.Image Arithmetics and Logic

## Functions

cv2.resize()

cv2.add()

cv2.addWeighted()

cv2.threshold()

cv2.bitwise_and()

cv2.bitwise_or()

cv2.bitwise_no()

cv2.bitwise_xor()

## Variables

cv2.BGR2GRAY

cv2.GRAY2BGR

cv2.THRESH_BINARY

cv2.THRESH_BINARY_INV

# 6.Thresholding

## Functions

cv.threshold()

cv2.cvtColor()

cv2.adaptiveThreshold()

## Variables

cv2.THRESH_BINARY

cv2.THRESH_BINARY_INV

cv2.ADAPTIVE_THRESH_GAUSSIAN_C

cv2.THRESH_OTSU



# 7.Color Filtering

## Functions

cv2.inRange()

## Variables

cv2.COLOR_BGR2HSV



# 8.Bluring and Smoothing

## Functions

cv2.filter2D()

cv2.GaussianBlur()

cv2.medianBlur()

cv2.bilateralFilter()



# 9.Morphological Transformation

## Functions

cv2.erode()

cv2.dilate()

cv2.morphologyEx()

## Variables

cv2.MORPH_OPEN

cv2.MORPH_CLOSE

cv2.MORPH_TOPHAT

cv2.MORPH_BLACKHAT



## 10.Edge Detection and Gradients

## Functions

cv2.Laplacian()

cv2.Sobel()

cv2.Canny()



## Variables

cv2.CV_64F



# 11.Template Matching

12.GrabCut Foreground Extraction

13.Corner Detection

14.Feature Matching(Homography) Brute Force

15.MOG Background Reduction

16.Haar Cascade Object Detection Face & Eye

17.Making your own Haar Cascade Intro

18.Gathering Images for Haar Cascade

19.Cleaning Images and Creating Descriptors

20.Training Haar Cascade Object Detection

21.Python for Image Video Analysis