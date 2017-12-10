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

    kernel = np.ones((15, 15), np.float32)/225
    smoothed = cv2.filter2D(res, -1, kernel)

    # gaussian blur
    blur = cv2.GaussianBlur(res, (15, 15), 0)
    # median blur
    median_blur = cv2.medianBlur(res, 15)
    # bilateral blur
    bilateral_blur = cv2.bilateralFilter(res, 15, 75, 75)
    
    cv2.imshow('frame', frame)
    cv2.imshow('hsv', hsv)
    #cv2.imshow('mask', mask)
    cv2.imshow('res', res)
    cv2.imshow('smoothed', smoothed)
    cv2.imshow('blur', blur)
    cv2.imshow('median_blur', median_blur)
    cv2.imshow('bilateral_blur', bilateral_blur)
    
    k = cv2.waitKey(5) & 0xFF
    # press key 'q' to break
    if k == ord('q'):
        break
    
cv2.destroyAllWindows()
cap.release()
