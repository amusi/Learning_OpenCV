import cv2
import numpy as np

img = cv2.imread('watch.jpg', cv2.IMREAD_COLOR)

# draw a line in red color
cv2.line(img, (0,0), (150,150), (0, 0, 255), 15)

# draw a rectangle in green color
cv2.rectangle(img, (150, 250), (600, 600), (0, 255, 0), 5)

# draw a circle in blue color
cv2.circle(img, (100, 200), 55, (255, 0, 0), -1)

# draw a ellipse
cv2.ellipse(img, (300,400), (100,50),0,0,180,(255, 255, 0),-1)

# draw a poly 
pts = np.array([[800,700], [650,650], [680,850], [760,860]], np.int32)
#pts = pts.reshape((-1,1,2))
cv2.polylines(img, [pts], True, (0, 255, 255), 3)

# add Text
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'OpenCV_Python', (600,100), font, 1, (255,255,255),2,cv2.LINE_AA)

cv2.imwrite('draw_image.png', img)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
