# Summary:  Feature matching(ORB)
# Author:      Amusi
# Date:          2017-12-14
import cv2
import numpy as np
import matplotlib.pyplot as plt

# grayscale
img1 = cv2.imread('feature-matching-template.jpg', 0)
#dst = cv2.resize(img1,  (800, 600) )
#imwrite("dst.jpg", dst)
img2 = cv2.imread('feature-matching-image.jpg',  0)

# create ORB
# ORB: Fast detector and BRIEF descriptor
orb = cv2.ORB_create()

# using ORB to detect feature points and describe feature points
kp1, des1 = orb.detectAndCompute(img1, None)
kp2, des2 = orb.detectAndCompute(img2, None)

# create BF(Brute Force) matcher
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck = True)

# BF macth
matches = bf.match(des1, des2)
# sort matching pairs according to the distance of matching pairs
# sorted function and lambda 
matches = sorted(matches, key = lambda x:x.distance)

# draw  10 matching pairs
img3 = cv2.drawMatches(img1, kp1, img2, kp2, matches[:10], None, flags=2)
plt.imshow(img3)
plt.show()
