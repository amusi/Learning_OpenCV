import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while cap.open(0):
    _, frame = cap.read()
    # convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # set the range of red
    lower_red = np.array([10, 0 , 0])
    upper_red = np.array([255, 255, 255])

    # filter red
    mask = cv2.inRange(hsv, lower_red, upper_red)
    res = cv2.bitwise_and(frame, frame, mask = mask)

    cv2.imshow('frame', frame)
    cv2.imshow('hsv', hsv)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)
    k = cv2.waitKey(5) & 0xFF

    
    if k == 27:
        break
    
cv2.destroyAllWindows()
cap.release()
