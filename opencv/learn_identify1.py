# -*- coding:utf-8 -*-
# author: Clark
# creationTime: 2019-11-20 12:17
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

    kernel = np.ones( (15, 15), np.float32)/255
    smoothed = cv.filter2D(res, -1, kernel)

    blur = cv.GaussianBlur(res, (15, 15), 0)
    median = cv.medianBlur(res, 15)
    bilateral = cv.bilateralFilter(res, 15, 75, 75)

    



    cv.imshow('frame', frame)
    cv.imshow('mask', mask)
    cv.imshow('res', res)
    cv.imshow('hsv', hsv)
    cv.imshow('smoothed', smoothed)
    cv.imshow('blur',blur )
    cv.imshow('median', median)
    cv.imshow('bilateral', bilateral)

    

    k = cv.waitKey(5) & 0xFF
    if k == 27 :
        break
cv.destroyAllWindows()
cap.release()