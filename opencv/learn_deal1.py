# -*- coding: utf-8 -*-
# author: Clark
# creationTime: 2019-11-16 13:48
# description: 对图片进行处理
# packages: cv2.cv2

import cv2.cv2 as cv

img = cv.imread("resources/images/dark.jpg")

retval, threshold = cv.threshold(img, 12, 255, cv.THRESH_BINARY)

grayscaled = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

retval2, threshold2 = cv.threshold(grayscaled, 12, 255, cv.THRESH_BINARY)

guas = cv.adaptiveThreshold(grayscaled, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 115, 1)

val2, otsu = cv.threshold(grayscaled, 125, 255, cv.THRESH_BINARY+cv.THRESH_OTSU)




cv.imshow('img', img)
cv.imshow("otsu", otsu)
cv.imshow("guas", guas)
cv.imshow("grayscaled", grayscaled)
cv.imshow("ththreshold",threshold)
cv.imshow("ththreshold2",threshold2)





cv.waitKey(0)
cv.destroyAllWindows()


