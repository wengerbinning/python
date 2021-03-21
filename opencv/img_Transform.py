# -*-coding:utf-8-*-
# author: Clark
# creationTime: 2019-11-09 09:23
# description: 图像的几何变换
# packages: cv2.cv2, numpy

from cv2 import cv2
import numpy
from matplotlib import pyplot

img = cv2.imread("resources/images/picture_1.jpg")
rows,cols= img.shape[:2]
# cv2.warpAffine(接收参数,2X3的变换矩阵), cv2.warpPerspective(接受参数,3X3的变换矩阵); 平移
distance = numpy.float32([[1,0,100],[0,1,50]])
img_shift = cv2.warpAffine(img, distance, (cols,rows))
#cv2.imshow("Shift",img_shift)

# rotate cv2.getRotationMatrix2D() 旋转图片
rotate = cv2.getRotationMatrix2D((cols/2,rows/2),90,0.6)
img_rotate = cv2.warpAffine(img, rotate, (2*cols,2*rows))
cv2.imshow("Shift",img_rotate)

#cv2.resize()缩放,方法一:
img_resize = cv2.resize(img, None, fx=4, fy=4, interpolation=cv2.INTER_CUBIC)
#cv2.imshow("Demo", img_resize)

#cv2.resize()缩放,方法二:
height, width = img.shape[:2]
img_resize2 = cv2.resize(img, (200,200), interpolation=cv2.INTER_CUBIC)
#cv2.imshow("Demo2", img_resize2)

# 仿射变换 cv2.getAffineTransform()
#pst1 = numpy.float32( [[50,50], [200,50], [50, 200]] )
#pst2 = numpy.float32( [[10,100], [200, 50], [100, 250]] )

#m2 = cv2.getAffineTransform(pst1, pst2)

#dst = cv2.warpAffine(img, m2, (cols, rows) )

#matplotlib.subplot(121)
#matplotlib.imshow(img)
#matplotlib.title('Input')

#matplotlib.subplot(122)
#matplotlib.imshow(dst)
#matplotlib.title('Output')

#matplotlib.show()

# 透视变换:cv2.getPerspectiveTransform() , cv2.warpPerspective()
# m3 = cv2.getPerspectiveTransform(pst1, pst2)
# dst2 = cv2.warpPerspective(img, m3, (300, 300)) 
# 
#matplotlib.subplot(121)
#matplotlib.imshow(img)
#matplotlib.title('Input')

#matplotlib.subplot(122)
#matplotlib.imshow(dst2)
#matplotlib.title('Output')
#matplotlib.show()

# 图像阈值,cv2.threshhold()
#Ostu`s二值化



cv2.waitKey(0)
cv2.destroyAllWindows()

