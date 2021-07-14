# -*- coding: utf-8 -*-
# author: Clark
# creationTime: 2019-11-16 13:03
# description: 对图片进行融合
# packages: cv2.cv2

import cv2.cv2 as cv

expension = 65

img1 = cv.imread("resources/images/hand.jpg")
img2 = cv.imread("resources/images/python_logo.jpg")

high, width, channels = img2.shape
img2 = img2[expension:(high-expension), expension+10:(width-expension-10)]
high, width, channels = img2.shape
img3 = img1[0:high, 0:width]

img2_gray = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)
#提取黑白色在(100~255)之间的像素并返回到mask图像中
ret, mask = cv.threshold(img2_gray, 100, 255, cv.THRESH_BINARY_INV)
#对mask图片进行取反
mask_inv = cv.bitwise_not(mask)

img1_bg = cv.bitwise_and(img3, img3, mask=mask_inv)
img2_fg = cv.bitwise_and(img2, img2, mask=mask)

img4 = cv.add(img1_bg, img2_fg,)

img1[0:high, 0:width] = img4

cv.imshow("img4", img4)
cv.imshow("img2", img2_gray)
cv.imshow("img1", img1)
cv.imshow("mask_inv", mask_inv)





cv.waitKey(0)
cv.destroyAllWindows()

