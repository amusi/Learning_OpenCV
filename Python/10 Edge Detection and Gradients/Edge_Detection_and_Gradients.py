# Summary: Edge Detection and Gradients
# Author:     Amusi
# Date:         2017-12-10

import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while cap.isOpened():
    _, frame = cap.read()

    # laplacian
    laplacian   = cv2.Laplacian(frame, cv2.CV_64F)
    # sobel: x--horizontal,  y--vertical
    sobelx = cv2.Sobel(frame, cv2.CV_64F, 1, 0, ksize = 3)
    sobely = cv2.Sobel(frame, cv2.CV_64F, 0, 1, ksize =3)
    # using Canny algorithm to detect edges
    edges = cv2.Canny(frame, 100, 200)
    
    cv2.imshow('original', frame)
    cv2.imshow('laplacian', laplacian)
    cv2.imshow('sobelx', sobelx)
    cv2.imshow('sobely', sobely)
    cv2.imshow('edges', edges)
    
    k = cv2.waitKey(5) & 0xFF
    # press key 'q' to break
    if k == ord('q'):
        break
    
cv2.destroyAllWindows()
cap.release()
