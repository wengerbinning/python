# -*- coding:utf-8 -*-
# author: Clark
# creationTime: 2019-11-14 21:54
# desciption: 写入视频文件
# packages: cv2.cv2

from cv2 import cv2

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('resources/videos/video1.avi', fourcc, 20.0, (640, 480) )
while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    out.write(frame)

    cv2.imshow('frame', frame)
    cv2.imshow('gray', gray)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()

