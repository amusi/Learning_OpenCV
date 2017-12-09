import cv2
import numpy as np

img = cv2.imread('watch.jpg', cv2.IMREAD_COLOR)
# get pixel value
px = img[250, 250]
print(px)

# modify pixel value
img[250, 250] = [255, 255, 255]
px = img[250, 250]
print(px)

# ROI(Region of Image)
roi = img[200:400, 200:400]


watch_face = img[300:600, 300:600]
img[200:300, 400:650] = [255, 255, 255]

cv2.imshow('watch_face', watch_face)
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

