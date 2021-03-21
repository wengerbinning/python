# -*-coding:utf-8-*-
# author: Clark
# creationTime: 2019-10-27 17:05
# description:
# package: cv2

from cv2 import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Cannot open camera!")
    exit()
while True:
    ret,frame = cap.read()
    if not ret:
        print("Can't receive frame(stream end?). Exiting ...")
        break
    #cv2.COLOR_BGR2GRAY
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()