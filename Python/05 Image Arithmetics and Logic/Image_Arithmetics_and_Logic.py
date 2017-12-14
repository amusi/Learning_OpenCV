import cv2
import numpy as np


img1 = cv2.imread('3D-Matplotlib.png')
img2 = cv2.imread('mainsvmimage.png')
img3 = cv2.imread('Python_Logo.jpg')

# resize two images to normalized size for add
# cv2.resize: (400, 300)--width = 400, height = 300
resize_img1 = cv2.resize(img1, (400, 300), interpolation = cv2.INTER_CUBIC)
cv2.imwrite('resize_1.png', resize_img1)
resize_img2 = cv2.resize(img2, (400, 300), interpolation = cv2.INTER_CUBIC)
cv2.imwrite('resize_2.png', resize_img2)
resize_img3 = cv2.resize(img3, (150, 150), interpolation = cv2.INTER_CUBIC)
cv2.imwrite('resize_3.png', resize_img3)

# add two images into one image
# need two images in same size
add1 = resize_img1 + resize_img2

# using cv2.add
# (155, 22, 79) + (50, 170, 200) = (205, 381, 279) is translated to (205, 255, 255)
add2 = cv2.add(resize_img1, resize_img2)

# assign different weight to two images 
weighted = cv2.addWeighted(resize_img1, 0.6, resize_img2, 0.4, 0)

rows, cols, channels = resize_img3.shape
roi = resize_img1[0:rows, 0:cols]

# grayscale
img2gray = cv2.cvtColor(resize_img3, cv2.COLOR_BGR2GRAY)
# binary -- if pixel value > 220, then pixel value = 255, else pixel value = 0
ret, mask = cv2.threshold(img2gray, 220, 255, cv2.THRESH_BINARY)
# bit operation: AND, OR, NOT, XOR   prefix: cv2.bitwise
mask_bit_inv = cv2.bitwise_not(mask)
# binary_inv -- if pixel value > 220, then pixel value = 0, else pixel value = 255
ret_inv, mask_inv = cv2.threshold(img2gray, 220, 255, cv2.THRESH_BINARY_INV)
mask_inv_bit_inv = cv2.bitwise_not(mask_inv)

# foreground and background
# bit operation: bitwise_and
img1_bg = cv2.bitwise_and(roi, roi, mask = mask_inv_bit_inv)
img3_fg = cv2.bitwise_and(resize_img3, resize_img3, mask = mask_inv)
dst = cv2.add(img1_bg, img3_fg)
resize_img1[0:rows, 0:cols] = dst

cv2.imshow('add1', add1)
cv2.imshow('add2', add2)
cv2.imshow("weighted", weighted)
cv2.imshow('mask', mask)
cv2.imshow('mask_bit_inv', mask_bit_inv)
cv2.imshow('mask_inv', mask_inv)
cv2.imshow('img1_bg', img1_bg)
cv2.imshow('img3_fg', img3_fg)
cv2.imshow('res', resize_img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
