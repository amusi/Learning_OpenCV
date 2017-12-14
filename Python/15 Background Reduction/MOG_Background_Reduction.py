# Summary:  Background Reduction
# Author:      Amusi
# Date:          2017-12-14
import cv2
import numpy as np
import matplotlib.pyplot as plt

#
cap = cv2.VideoCapture('people-walking.avi')


# using MOG subtractor
fgbg= cv2.bgsegm.createBackgroundSubtractorMOG()

# using MOG2 subtractor
#fgbg = cv2.createBackgroundSubtractorMOG2()

# using KNN subtractor
#fgbg = cv2.createBackgroundSubtractorKNN(detectShadows=True)

# using GMG subtractor
#fgbg = cv2.bgsegm.createBackgroundSubtractorGMG()

while True:
    ret, frame = cap.read()
    fgmask = fgbg.apply(frame)

    cv2.imshow('original', frame)
    cv2.imshow('fg', fgmask)

    k = cv2.waitKey(30) & 0xFF
    if k == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

