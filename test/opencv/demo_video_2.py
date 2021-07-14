#!/usr/local//bin python3
# -*-coding:utf-8-*-
__author__ = "Clark Aaron"
__date__ = "2019-11-10"
__time__ = "15:59"

'''
# description: play video from file
# packages: cv2
'''

import cv2 as cv

cap_video = cv.VideoCapture("resources/videos/demo1.avi")

while cap_video.isOpened():
    ret,frame = cap_video.read()
    if ret == True:
        cv.imshow("DemoVideo",frame)
        key_value = cv.waitKey(15) & 0xFF
        if key_value == 27:
            break
    else:
        break
cap_video.release()
cv.destroyAllWindows()