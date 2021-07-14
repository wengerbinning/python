#!/usr/local/bin python3
# -*- coding:UTF-8 -*-
__author__ = "Clark Aaron"
__date__ = "2019-10-27"
__time__ = "16:33"

'''
description: Use OpenCV load an image and display it.
packages: cv2
'''

# import OpenCV package
import cv2 as cv
# Load an image
image = cv.imread("resources/images/python_logo.jpg",cv.IMREAD_COLOR)
# display the image
cv.imshow("DemoImage",image)
# waiting 3ms until <Esc> is pressed
while True:
    key = cv.waitKey(3)
    if key == 27:
        break
# destroy all windows
cv.destroyAllWindows() 
