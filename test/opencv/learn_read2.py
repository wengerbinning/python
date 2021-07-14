# -*- coding:utf-8 -*-
# author: Clark
# creationTime: 2019-11-14 21:40
# description: 读取摄像头视频
# packages: cv2.cv2

from cv2 import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    cv2.imshow('Demo', frame)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()