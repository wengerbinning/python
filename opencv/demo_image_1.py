#!/usr/local/bin python3
# -*- coding:UTF-8 -*-
__author__ = "Clark Aaron"
__date__ = "2019-10-27"
__time__ = "16:52"

'''
description: Below program loads an image in grayscale, display it, 
    save the image if you press s and exit, or simply exit without saving if you press ESC key.
packages: cv2
'''

# Import OpenCV Library
import cv2 as cv
# Save images' path
image_path = "resources/images/"
# Load the image
image = cv.imread(image_path+"Doraemon.jpg",cv.IMREAD_GRAYSCALE)
# Display the image
cv.imshow("DemoImage0",image)
# Wait some key is pressed
key_value = cv.waitKey(0) & 0xFF
# Save image and exit
if key_value == ord('s'):
    cv.imwrite(image_path+"Doraemon.png",image)
# Don't save image and exit
elif key_value == 27:
    pass
cv.destroyAllWindows()
