import cv2
import numpy as np
import matplotlib.pyplot as plt

# load image
#img = cv2.imread("lena.png", cv2.IMREAD_COLOR)
img = cv2.imread("lena.png", cv2.IMREAD_GRAYSCALE)
# IMREAD_GRAYSCALE = 0
# IMREAD_COLOR = 1
# IMAGED_UNCHANGED = -1

# display image
cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('watchgray.png', img)

# using matplotlib
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.plot([50,250], [80,100], 'c', linewidth=5)
plt.show()
