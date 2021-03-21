# -*- coding:UTF-8 -*-
# author: Clark
# creationTime: 2019-10-27 15:43
# description: 测试openCV的python环境是否正常
# packages: cv2

from cv2 import cv2
#加载图片到grayscale
img = cv2.imread('resources\\images\\picture_1.jpg',0)
#设置窗口自动大小
#cv2.namedWindow('Demo',cv2.WINDOW_AUTOSIZE)
#在窗口显示一张图片
cv2.imshow("Demo", img)
#检测按键
cv2.waitKey(0)
#关闭所有窗口
cv2.destroyAllWindows()