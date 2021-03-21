# -*- coding:utf-8 -*-
# author: Clark
# creationTime: 2019-11-14 21:15
# description: 读取一张图片并显示
# packages: cv2.cv2

from cv2 import cv2

img = cv2.imread("resources/images/picture_1.jpg", cv2.IMREAD_COLOR)

cv2.imshow("Demo", img)

cv2.waitKey(0)
cv2.destroyAllWindows()