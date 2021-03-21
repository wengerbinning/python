# -*- coding:UTF-8 -*-
# author: Clark
# creationTime: 2019-10-27 16:24
# description: 使用cv2显示与写入图片
# packages: cv2

import cv2
#加载图片到grayscale
img = cv2.imread('resources\\images\\picture_1.jpg',0)
#设置窗口自动大小
#cv2.namedWindow('Demo',cv2.WINDOW_AUTOSIZE)
#在窗口显示一张图片
cv2.imshow("Demo", img)
#检测按键,使用64为计算机时使用以下格式
k = cv2.waitKey(0) & 0xff
#k = cv2.waitKey(0)
if( k == 27 ):
    #关闭所有窗口
    cv2.destroyAllWindows()
elif( k == ord('s') ):
    cv2.imwrite('resources\\images\\picture_1.png',img)
    cv2.destroyAllWindows()