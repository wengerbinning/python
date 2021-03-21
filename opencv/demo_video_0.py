#!/usr/local/bin python3
# -*-coding:UTF-8-*-
__author__ = "Clark Aaron"
__date__ = "2019-10-27"
__time__ = "17:21"

'''
description: Capture video from camera and display it.
packages: cv2
'''

import cv2 as cv
# Create a videocapture object
cap_video = cv.VideoCapture(0)
# set size
cap_video.set(cv.CAP_PROP_FRAME_WIDTH,1920)
cap_video.set(cv.CAP_PROP_FRAME_HEIGHT,1080)
# get capture's size
width = cap_video.get(cv.CAP_PROP_FRAME_WIDTH)
height = cap_video.get(cv.CAP_PROP_FRAME_HEIGHT)
print("%dx%d px"%(width,height))

while cap_video.isOpened():
    ret,frame = cap_video.read()
    if not ret:
        print("[INFO] Cannot receive frame (stream end?). Exiting ...")
        break
    frame = cv.flip(frame,2)
    # Our operations on the frame come here
    gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    # Display the resulting frame
    cv.imshow('DemoVideo',gray)
    key_value = cv.waitKey(25)& 0xFF

    if key_value == ord('q'):
        break
# Release the capture
cap_video.release()
# Destroy all windows
cv.destroyAllWindows()