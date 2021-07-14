# -*- coding: utf-8 -*-
# author: Clark
# creationTime: 2019-11-16 12:38
# description: 对图片进行合并
# packages: cv2.cv2

import cv2.cv2 as cv

img1 = cv.imread("resources/images/hand.jpg")
img2 = cv.imread("resources/images/python_logo.jpg")

heigh, width, channel = img2.shape
#print(heigh, width, channel)

img3 = img1[0:heigh, 0:width]
img4 = cv.copyMakeBorder(img1,0, 0, 0, 0, 1)
img4[0:heigh, 0:width] = img2
img_plus = img2 + img3
img_add = cv.add(img2, img3)


cv.imshow("img1", img1)
cv.imshow("img2", img2)
cv.imshow("img3", img3)
cv.imshow("img4", img4)
cv.imshow("Plus",img_plus)
cv.imshow("Add", img_add)





cv.waitKey(0)
cv.destroyAllWindows()