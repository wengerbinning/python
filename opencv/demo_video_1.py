#!/usr/local/bin python3
# -*- ccoding: utf-8 -*-
__author__ = "Clark Aaron"
__date__ = "2020-03-28"
__time__ = "22:58"

'''
description: Capture the video from camera and save it
packages: cv2
'''

import cv2 as cv
# Create a videocapture object
cap_video = cv.VideoCapture(0)

# GEt video fps
fps = cap_video.get(cv.CAP_PROP_FPS)
# Get video size
size =( int(cap_video.get(cv.CAP_PROP_FRAME_WIDTH)), int(cap_video.get(cv.CAP_PROP_FRAME_HEIGHT)) )

fourcc = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter('resources/videos/demo1.avi',fourcc,fps,size)

while cap_video.isOpened():
    ret, frame = cap_video.read()
    if ret == True:
        frame = cv.flip(frame,2)
        # Wirte the fipped frame
        out.write(frame)
        #gray = cv.cvtColor(frame,cv.COLOR_BAYER_BG2GRAY)
        cv.imshow("DemoVideo",frame)
        key_value = cv.waitKey(15) & 0xFF
        if key_value == 27:
            break
    else:
        break
# Release everything if job is finished
cap_video.release()
out.release()
cv.destroyAllWindows()

