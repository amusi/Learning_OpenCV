# Summary:  Background Reduction
# Author:      Amusi
# Date:          2017-12-14
# Reference: http://www.jianshu.com/p/12533816eddf
import cv2
import numpy as np

def background_detect(video):
    cap = cv2.VideoCapture(video)
    # training frame number
    history = 20

    # using MOG subtractor
    #fgbg= cv2.bgsegm.createBackgroundSubtractorMOG()

    # using MOG2 subtractor
    #fgbg = cv2.createBackgroundSubtractorMOG2()

    # using KNN subtractor
    fgbg = cv2.createBackgroundSubtractorKNN(detectShadows=True)
    fgbg.setHistory(history)
    
    # using GMG subtractor
    #fgbg = cv2.bgsegm.createBackgroundSubtractorGMG()

    frames = 0
    
    while True:
        res, frame = cap.read()

        if not res:
            break

        # get foreground mask
        fgmask = fgbg.apply(frame)

        if frames < history:
            frames += 1
            continue

        # binary
        th = cv2.threshold(fgmask.copy(), 244, 255, cv2.THRESH_BINARY)[1]
        # erode and dialte
        th = cv2.erode(th, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3)), iterations = 2)
        dilated = cv2.dilate(th, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (8,3)), iterations = 2)

        # [findContours]get all contours
        image, contours, hier = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # remove small areas and get all bounding box
        for c in contours:
            # get rectangle data
            x, y, w, h = cv2.boundingRect(c)
            # calculate the area of rectangle
            area = cv2.contourArea(c)
            if  500 < area < 3000:
                cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 0), 2)

        cv2.imshow('detection', frame)
        cv2.imshow('fg', dilated)

        k = cv2.waitKey(30) & 0xFF
        if k == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


video = 'people-walking.avi'
background_detect(video)
