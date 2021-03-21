# -*- coding:utf-8 -*-
# author: Clark
# creationTime: 2019-11-21 22:11
# description:滤波器的处理
# packages: cv2.cv2, numpy

import cv2.cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)

while True:
    _, frame = cap.read()
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    # hsv hue sat value
    lower_red = np.array([80, 0, 0])
    upper_red = np.array([225, 255, 255])

    mask = cv.inRange(hsv, lower_red, upper_red)
    res = cv.bitwise_and(frame, frame, mask=mask)

    kernel = np.ones( (5, 5), np.uint8)
    erosion = cv.erode(mask, kernel, iterations = 1)
    dilation = cv.dilate(mask, kernel, iterations = 1)

    opening = cv.morphologyEx(mask, cv.MORPH_OPEN, kernel)
    closing = cv.morphologyEx(mask, cv.MORPH_CLOSE, kernel)




    cv.imshow('frame', frame)
    cv.imshow('mask', mask)
    cv.imshow('res', res)
    cv.imshow('hsv', hsv)
    cv.imshow('erosion', erosion)
    cv.imshow('dilation',dilation)
    cv.imshow('opening', opening)
    cv.imshow('closing', closing)
    

    k = cv.waitKey(5) & 0xFF
    if k == 27 :
        break
cv.destroyAllWindows()
cap.release()