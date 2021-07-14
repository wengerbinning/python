# -*- coding:utf-8 -*-
# author: Clark
# creationTime: 2019-11-07 19:03
# Description:颜色空间转换
# packages: cv2.cv2, numpy

from cv2 import cv2 
import numpy

img = cv2.imread("resources/images/picture_1.jpg")
# cv2.cvtColor()    对图片信息进行颜色转换
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower_bule = numpy.array([0, 100, 100])

upper_bule = numpy.array([360, 100, 100])
# cv2.inRange() 对图片信息进行跟踪
mask = cv2.inRange(img, lower_bule, upper_bule)

img_and = cv2.bitwise_and(img,img,None,mask=mask)

cv2.imshow("Demo", img_and)

cv2.waitKey(0)

cv2.destroyAllWindows()

