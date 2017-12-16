# Summary: Python for Image Analysis using custom training data
# Author:      Amusi
# Date:         2017-12-16

import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
watch_cascade = cv.CascadeClassifier('watch-cascade-12stages.xml')

cap = cv2.VideoCapture(0)

while True:
    # load frame
    ret , img = cap.read()
    # grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # using face harr cascade 
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    # using watch harr cascade
    watches = watch_cascade.detectMultiScale(gray., 30, 30)

    # draw watches
    for (x, y, wj, h) in watches:
        # put text in object
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv.putText(img, 'watch', (x-w, x-h), font, 0.5, (255, 255, 0), 2, cv2.LINE_AA)
        cv2.rectangle(img, (x,y), (x+w, y+h), (0, 255, 0), 2)

    # draw faces and eyes
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)
        # eyes in face
        roi_color = img[y:y+h, x:x+w]
        roi_gray = gray[y:y+h, x:x+w]
        # using eye  harr cascade
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (eye_x, eye_y, eye_w, eye_h) in eyes:
            cv2.rectangle(roi_color, (eye_x, eye_y), (eye_w, eye_h), (0,255,255), 2)

    cv2.imshow('img', img)
    k = cv2.waitKey(27) & 0xff
    if  k == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
            
        


