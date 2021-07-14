# -*-coding:utf-8-*-
# author: Clark
# creationTime: 2019-11-10 14:43
# description: 对图像进行平滑处理,OpenCV提供四种模糊技术
# packages: cv2.cv2, numpy, matplotlib.pyplot

from cv2 import cv2
import numpy
from matplotlib import pyplot


img = cv2.imread("resources\\images\\picture_1.jpg")

kernel = numpy.ones((5, 5), numpy.float32)/25
#归一化卷积cv2.blur() 和 cv2.boxFilter()
#高斯模糊 cv2.GaussianBlur()
#中值模糊 cv2.MedianBlur()
#双边滤波 cv2.bilateralFilter(0)

blur = cv2.blur(img, (5, 5))

dst = cv2.filter2D(img, -1, kernel)

pyplot.subplot(221)
pyplot.imshow(img)
pyplot.title('Orignal')

pyplot.xticks([])
pyplot.yticks([])

pyplot.subplot(222)
pyplot.imshow(dst)
pyplot.title('Averaging')

pyplot.xticks()
pyplot.yticks()

pyplot.subplot(223)
pyplot.imshow(blur)
pyplot.title('Blur')

pyplot.xticks([])
pyplot.yticks([])

pyplot.show()
# 形态学转化
# 腐蚀cv2.ercode(), 膨胀cv2.dilate(), 闭运算cv2.morphologyEx()
#图像梯度
# cv2.Sobel(), cv2.Schar(), cv2.Laplacian()
