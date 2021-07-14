# -*-coding:utf-8-*-
# author: Clark
# creationTime: 2019-11-10 15:36
# description: COpenCV中的轮廓
# packages: cv2.cv2, numpy, matplotlib.pyplot

from cv2 import cv2
import numpy
from matplotlib import pyplot

img = cv2.imread("resources\\images\\picture_1.jpg")

imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(imgray, 127, 255, 0)

image, contours = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

imgs = cv2.drawContours(img, contours, -1, (0, 255, 0), 3)

cv2.imshow("Demo", imgs)

cv2.waitKey(0)

cv2.destroyAllWindows()
