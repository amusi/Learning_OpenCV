import cv2
import numpy as np

img = cv2.imread('bookpage.png')
# threshold
retval, threshold = cv2.threshold(img, 50, 255, cv2.THRESH_BINARY)

# grayscale
grayscaled= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# binary
retval2, threshold2 = cv2.threshold(grayscaled, 50, 255, cv2.THRESH_BINARY)

# gaussian
gaus = cv2.adaptiveThreshold(grayscaled, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)

# OTSU
retval_OTSU, otsu = cv2.threshold(grayscaled, 125, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

cv2.imshow('original', img)
cv2.imshow('thresholds', threshold)
cv2.imshow('threshold2', threshold2)
cv2.imshow('gaus', gaus)
cv2.imshow('otsu', otsu)
cv2.waitKey(0)
cv2.destroyAllWindows()
