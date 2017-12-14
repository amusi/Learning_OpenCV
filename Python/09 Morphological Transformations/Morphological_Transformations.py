import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while cap.isOpened():
    _, frame = cap.read()
    # convert BGR to HSV
    # HSV: hue, sat, value
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # set the range of red
    lower_red = np.array([150, 150 , 50])
    upper_red = np.array([180, 255, 255])

    # filter red
    mask = cv2.inRange(hsv, lower_red, upper_red)
    res = cv2.bitwise_and(frame, frame, mask = mask)

    # morphological transformations
    kernel = np.ones((5,5), np.uint8)
    # erode
    erosion = cv2.erode(mask, kernel, iterations = 1)
    dilation = cv2.dilate(mask, kernel, iterations = 1)

    # opening operation: erode, then dilate 
    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    # closing operation: dilate the erode
    closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    
    # Top Hat: it is the difference between input image and Opening of the image
    top_hat = cv2.morphologyEx(mask, cv2.MORPH_TOPHAT, kernel)
    # Black Hat: it is the difference between closing of the input image and input image
    black_hat = cv2.morphologyEx(mask, cv2.MORPH_BLACKHAT, kernel)
    
    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)
    cv2.imshow('erosion', erosion)
    cv2.imshow('dilation', dilation)
    cv2.imshow('opening', opening)
    cv2.imshow('closing', closing)
    cv2.imshow('Top hat', top_hat)
    cv2.imshow('Black hat', black_hat)
    
    k = cv2.waitKey(5) & 0xFF
    # press key 'q' to break
    if k == ord('q'):
        break
    
cv2.destroyAllWindows()
cap.release()
