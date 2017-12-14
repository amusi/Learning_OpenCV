import cv2
import numpy as np


# open video from computer's camera
cap = cv2.VideoCapture(0)
# open video from disk
# cap = cv2.VideoCapture('input.avi')

# save video
# frame value: 25.0
# linux: XVID, X264;  Windows: DIVX
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter("output.avi", fourcc, 25.0, (640, 480))

while(cap.isOpened()):
    ret, frame = cap.read()
    # convert BGR to gray
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # display video
    cv2.imshow('frame', frame)
    cv2.imshow('gray', gray)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
