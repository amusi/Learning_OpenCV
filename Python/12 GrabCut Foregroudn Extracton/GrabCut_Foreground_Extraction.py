# Summary: GrabCut Foreground Extraction
# Author:      Amusi
# Date:          2017-12-11
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('foreground-extraction.jpg')
#simg = cv2.imread('foreground-extraction2.jpeg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
mask = np.zeros(img.shape[:2], np.uint8)

bgdmodel = np.zeros((1, 65), np.float64)
fgdmodel = np.zeros((1, 65), np.float64)

# rect: import parameter
rect = (150, 0, 330, 354)     # for foreground-extraction.jpg
#rect =  (300,20, 600,800) # for foreground-extraction2.jpeg

# grabCut
cv2.grabCut(img, mask, rect, bgdmodel, fgdmodel, 5, cv2.GC_INIT_WITH_RECT)
mask2 = np.where((mask==2)|(mask==0), 0, 1).astype('uint8')
img = img*mask2[:, :, np.newaxis]

plt.imshow(img)
plt.colorbar()
plt.show()
