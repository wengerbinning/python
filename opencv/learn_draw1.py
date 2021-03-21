# -*- coding:utf-8 -*-
# author: Clark
# creationTime: 2019-11-14 21:23
# description: 在图片上画图形
# packages: cv2.cv2, numpy

from cv2 import cv2
import numpy

img = cv2.imread("resources/images/picture_1.jpg", cv2.IMREAD_COLOR)
#画一条从(10, 10)到(30, 30)的颜色为BGR(0, 255, 0)的线段,线宽为2
cv2.line(img, (10, 10), (30, 30), (0, 255, 0), 2)
#画一个以(30, 30)为圆心,半径为20;颜色为GBR(255, 0, 0);线宽为(-1),表示实心圆
cv2.circle(img, (30, 30), 20, (255, 0, 0), -1)
#画一个矩形(30, 30)~(50, 50),颜色为(0, 0, 255);线宽(-1)
cv2.rectangle(img, (30, 30), (50, 50), (0, 0, 255), -1)
#使用numpy画出一个多边形
pts = numpy.array([ [10, 10], [10, 300], [200, 400]], numpy.int32 )
cv2.polylines(img, [pts], True, (127, 127, 127), 1)


cv2.imshow("Demo", img)

cv2.waitKey(0)
cv2.destroyAllWindows()