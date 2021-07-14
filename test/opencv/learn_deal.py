# -*- coding:utf-8 -*-
# author: Clark
# creationTime: 2019-11-21 22:22
# description: 图像处理
# packages: cv2.cv2, np

import cv2.cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)

while True:
    _, frame = cap.read()

    laplacian = cv.Laplacian(frame, cv.CV_32F)
    sobelx = cv.Sobel(frame, cv.CV_64F, 1, 0, ksize=5)
    sobely = cv.Sobel(frame, cv.CV_64F, 0, 1, ksize=5)
    edges = cv.Canny(frame, 100, 200)

    cv.imshow('frame',frame)
    cv.imshow('laplacian',laplacian)
    cv.imshow('sobelx',sobelx)
    cv.imshow('sobely',sobely)
    cv.imshow('edges',edges)

    if cv.waitKey(30) & 0xFF == 27 :
        break
cap.release()
cv.destroyAllWindows()

