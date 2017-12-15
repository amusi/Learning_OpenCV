# Summary: Harr Cascade Detection Face & Eye
# Author:      Amusi
# Date:         2017-12-16
# Reference: http://blog.topspeedsnail.com/archives/10511

import cv2
import numpy as np

# face classifier
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# eye classifier
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

cap = cv2.VideoCapture(0)

while True:
    # load frame
    ret , img = cap.read()
    # grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # using face harr cascade 
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    
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
            
        


