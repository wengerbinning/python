# -*-coding:utf-8-*-
# author: Clark
# creationTime: 2019-11-10 15:17
# description: Canny边缘检测
# packages: cv2.cv2, numpy, matplotlib.pyplot

from cv2 import cv2
import numpy
from matplotlib import pyplot

img = cv2.imread("resources\\images\\picture_1.jpg")

edges = cv2.Canny(img, 100, 200)

lower_reso = cv2.pyrDown(higher_reso)
higher_reso = cv2.pyrUp(lower_reso)



pyplot.subplot(121)
pyplot.imshow(img, cmap='gray')
pyplot.title("Original Image")
pyplot.xticks([])
pyplot.yticks([])

pyplot.subplot(122)
pyplot.imshow(edges, cmap='gray')
pyplot.title("Edge Image")
pyplot.xticks([])
pyplot.yticks([])

pyplot.show()


