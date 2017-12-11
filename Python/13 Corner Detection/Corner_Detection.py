# Summary:  Corner Detection
# Author:      Amusi
# Date:          2017-12-11
import cv2
import numpy as np

img = cv2.imread('corner-detection.jpg')
#img = cv2.imread('corner-detection2.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)

# calculate all corners
corners = cv2.goodFeaturesToTrack(gray, 200, 0.01, 10)
corners = np.int0(corners)

# draw corner
for corner in corners:
    # ravel
    x, y = corner.ravel()
    cv2.circle(img, (x,y), 8, (0, 0, 255), -1)

cv2.imshow('corner', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
