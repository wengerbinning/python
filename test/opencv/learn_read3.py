# -*- coding:utf-8 -*-
# author: Clark
# creationTime: 2019-11-14 22:04
# description: 读取视频文件
# packages: cv2.cv2

from cv2 import cv2

cap = cv2.VideoCapture("resources/videos/video1.avi")

while True:
    ret, frame = cap.read()
    
    if not ret:
        print("Can't receive frame(stream end?). Exiting ...")
        break
    
    cv2.imshow('Demo', frame)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()