# GUI Features in OpenCV

```python
__author__ = "Clark Aaron"
__date__ = "2020-03-26"
__time__ = "21:51"
```

## Getting Started with Images

* Using OpenCV read an image: Use the function cv2.imread() to read an image;

the image should be in the working directory or a full path of image should be given. And second argument is a flag which specifies the way image should be read(Note: instead of these flags, you can simply pass imtegers `1,0,-1`).
    1. `cv2.IMREAD_COLOR`: Loads a color image. Any transparency of image will be neglected. It is the default flag;
    2. `cv2.IMREAD_GRAYSCALE`: Loads image in grayscale mode;
    3. `cv2.IMREAD_UNCHANGED`: Loads imageas such including alpha channel;

```python
# Import OpenCV Library
import cv2
# Load an image
image = cv2.imread(<image`s path>,<flags>)
# Even if the image path is wrong, it won't throw any error, but print image will give you None
```

* Display an image: Use the function cv2.imshow() to display an image in a window.The window automatically fits to the image size.

Fist argument is a window name which is a string, second argument is our image. You can create as many windows as you wish, but with different window names;

cv2.waitKay() is a keyboard binding function. Its argumentis the time in milliseconds. The function waits for specified milliseconds for any keyboard event. If you press any key in that time, the program continues. If 0 is pressed, it waits indefinitley for a key stroke. It can also be set to detect specific key strokes like, if key a is pressed etc which we will discuss below(Note: Besides binding keyboard events this function also processes many other GUI events, so you must use it to actually display the image).

cv2.destroyAllWindows() simply destroys all the windows we created. If you want to destroy any specific window, use the function cv2.destroyWindow() where you pass the exact window name as the argument(Note: There is a special case where you can already create a window and load image to it later. In that case, you can specify whether window is resizable or not. It is done with the function cv2.namedWindow(). By deault, the flag is cv2.WINDOW_AUTOSIZE. But if you specify flag to be cv2.WINDOW_NORMAL,you can resize window. It will be helpful when image is too large in dimension and adding track bar to windows)).

```python
# Display an image
cv2.imshow(<window`s name>, <image>)
# Wait some time until any key was pressed
cv2.waitKey(0)
# Destroy all windows
cv2.destroyAllWindows()
```

* Wirte an image: Use the function cv2.imwrite() to save an image;

First argument is the file name, second argument is the image you want to save;

```python
# Save an image
cv2.imwirte(<image`s name>, <img>)
```

Below program loads an image in grayscale, display it, save the image if you press s and exit, or simply exit without saving if you press Esc key;

```python
# Import OpenCV Library
import cv2
# Load an image
image = cv2.imread(<image`s path>, cv2.IMREAD_GRAYSCALE)
# Display an image
cv2.imshow(<window`s name>, image)
# If you are using a 64-bit machine, you will have to modify k = cv2.waitKey(0) line as follows: k = cv2.waitKey(0)&0xFF
key_value = cv2.waitKey(0) & 0xFF
# Wait for s key to save and exit
if key_value == ord('s'):
    print("[INFO] Save image and exit.")
    cv2. imwrite("image.png",image)
# Wait for Esc key to save and exit
elif key_value == 27:
    print("[INFO] Don't save image and exit.")
# Destroy all windows
cv2.destroyAllWindows()
```

### Using Matplotlinb

Matplotlib is a ploting library for Python which gives you wide variety of plotting methods. You will see them incoming articles. Here, you will learn hou to display image with Matplotlib. You can zoom images, save it etc using Matplotlib.

* Display an image using matplotlib

```python
# Import cv2 and pyplot
import cv2
from matplotlib import pyplot
# Load the image
image = cv2.imread(<image_path>, flags)

pyplot.imshow(image, cmap='gray',interpolation='bicubic')

pyplot.xticks([])
pyplot.yticks([])

pyplot.show()
```

## Getting Started with Videos

* Capture Video from Camera

often, we have to capture live stream with camera. OpenCV provides a very simple interface to this. Let's capture a video from the camera(I am using the in-built webcam of my laptop),convert it into grayscale video and display it. Just a simple task tp get started.

To capture a video, you need to create a VideoCapture object.Its argument can be either the device index or the name of a video file. Device index is just the number to specify which camera. Normally one camera will be connected(as in my case). So I simply pass 0(or -1).You can select the second camera by passing 1 and so on. After that, you can capture frame-by-frame. But at the end, don't forget to release the capture.

`cap_video.read()` return a bool. If frame is read correctly, it will be True. So you can check end of the video by checking this return value. Sometimes, cap_video may not have initialized the capture. In that case, this code shows error. You can check whether it is initialized or not by the method `cap_video.isOpened()`. if it is True, OK. Otherwise it using `cap_video.open()`.

You can also access some of the features of this video using `cap.get(propld)` method where propld is a number from 18.Each number denotes a property od the video(if it is applicable to that video) and full details can be seen here: cv::VideoCapture::get(). Some of these values can be modified using `cap_video.set(propld,value)`. value is the new value you want. For example., I can check the frame width and height by `cap_video.get(cv2.CAP_PROP_FRAME_WIDTH)` and `cap_video.get(cv2.CAP_PROP_FRAME_HEIGHT)`. It gives me 640x480 by default. But i want to modify it to 320x240.Just use `ret = cap_video.set(cv2.CAP_PROP_FRAME_WIDTH,320)` and `ret = cap_video.set(cv2.CAP_PROP_FRAME_WEIGHT,240)`(Note: If you are getting error, make sure camera is working fine using any other camera application(like Cheese in Linux)).

```python
# Import OpenCV
import cv2
# Create a videocapture object
cap_video = cv2.VideoCapture(0)
while True:
    # Capture frame-by-frame
    ret, frame = cap_video.read()
    # Our operations on the frame come here
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    # Display the resulting frame
    cv2.imshow('DemoVideo',gray)
    # Wait until any key is pressed
    key_value = cv2.waitKey(0) & 0xFF
    if key_value == 27:
        break
# Release the capture
cap_video.release()
# destroy all window
cv2.destroyAllWindows()
```

* Playing Video from file

It is same as capturing from Camera, just change camera index with video file name. Also while display the frame, use appropriate time for `cv2.waitKey()`. If it is too less, video will be very fast and if it is too high, video will be slow(Well, that is how you can display videos in show motion). 25 milliseconds will be OK in normal cases(Note: Make sure proper versions of ffmpeg or gstreamer is installed. Sometimes, it is a headache to work with Video Capture mostly due to wrong installation of ffmpeg/gstreamer).

```python
# Import OpenCV
import cv2
# Create videocapture object
cap_video - cv2. VideoCapture("vtest.avi")
# Check capture video's status
cap_status = cap_video.isOpened()
while cap_status:
    ret, frame = cap_video.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('DemoVideo',gray)
    key_value = cv2.waitKey(25) & 0xFF
    if key_value == ord('q'):
        break
# release the capture
cap_video.release()
cv2.destroyAllWindows()
```

* saving a Video

So we capture a video, process it frame-by-frame and we want to save that video. For images, it is very simple, just use cv2.imwrite(). Here a little more work is required.

This time we create a VideoWriter object. We should specify the output file name(eg: output.avi). Then we should specify the FourCC code (details in next paragraph). Then number of frames per second(fps) and frame size should be passed. And last one is isColor flag. If it is True. encoder expect color frame, otherwise it works with grayscale frame.

FourCC is a 4-byte code used to specify the video codec. The list of available codes can be found in fourc.org. It is platform dependent. Following codecs works fine for me.
    1. In Windows: DIVX(More th be tested and added);
    2. In Fedora: DIVX, XVID, MJPG, X264, WMV2. (XVID is more preferable. MJPG results in high size video. X264 gives very small size video);
    3. In OS X: MJPG(.mp4), DIVX(.avi), X264(.mkv);

FourCC code is passed as `cv2.VideoWriter_fourcc('M','J','P','G')` or `cv2.VideoWriter_fourcc(*'MJPG')` for MJPG;

Below code capture from a Camera, frame in vertical direction and saves it.

```python
import cv2
cap_video = VideoCapture(0)
# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('out.avi',fourcc,20,0,(640,480))
while(cap_video.isOpened()):
    ret, frame = cap_video.read()
    if ret == True:
        frame = cv2.flip(frame,0)
        # Wirte the fipped frame
        out.write(frame)
        cv2.imshow('DemoVideo', frame)
        key_value = cv2.waitKey(0) & 0xFF
        if key_value == ord('q'):
            break
    else:
        break
# Release everything if job is finished
cap_video.release()
out.release()
cv2.destroyAllWindows()
```

## Drawing Function in OpenCV

In all the above functions, yiu will see some common arguments as give below:
    1. `img`: The image where you want to draw the shapes;
    2. `color`: Color of the shape, for BGR, pass it as a tuple, eg: (255,0,0) for blue. For grayscale, just pass the scalar value.
    3. `thickness`: Thickness of the line or circle etc. If `-1` is passed for cloesed figures like circles, it will fill the shape, default thickness = 1.
    4. `lineType`: Type of line, whether 8-connected, anti-alised line etc. By default, it is 8-connected. `cv2.LINE_AA` gives anti-alised line which looks great for curves.

* Drawing Line: To draw a line, you need to pass starting and ending coordinates of line. We will crate a black image and draw a blue line on it from top-left to bottom-right corners.

```python
import numpy as np, cv2
# Create a black image
img = np.zeros((512,512,3),np.uint8)
# Draw a diagonal blue line with thickness of 5 px
img = cv2.line(img,(0,0),(511,511),(255,0,0),5)
```

* Drawing Rectangle: To draw a rectangle, you need top-left corner and bottom-right corner of rectangle. This time we will draw a green rectangle at the top-right corneer of image.

```python
# Draw a green rectangle with thickness of 3 px
img = cv2.rectangle(img,(384,0),(510,128),(0,255,0),3)
```

* Drawing Circle: TO draw a clrcle, you need its center coordinates and reaius. We will draw a circle inside the rectangle drawn above.

```python
# Draw a red circle with thickness of -1 px
img = cv2.circle(img,(447,630),63,(0,0,255),-1)
```

* Drawing Ellipse: To draw the ellipse, you need to pass several arguments. one argument is the center location(x,y). Next argumnet is axes legths(major axis length, minor axis length). `angle` is the angle of rotation of ellipse in anti-clockwise direction. `startAngle` and `endAngle` denotes the starting and ending of ellipse arc measured in clockwise direction from major axis.i.e.giving values 0 and 360 gives the full ellipse. For more details, check the documentation of `cv2.ellipse()`. Below example draws a half ellipse at the center of the image.

```python
img = cv2,ellipse(img,(256,256),(100,50),0,0,180,255,-1)
```

* Drawing Polygon: To draw a polygon, first you need corrinates of vertices. Make those points into an array of shape `ROWSx1x2` where ROWS are number of vertices and it should be of type `int32`. Here we draw a small polygon of with four vertices in yellow color(Note: if thrid argument is False, you will get a polylines joining all the points, not a closed shape).

Note: `cv2.polylines(0)` can be used to draw multiple lines. Just create a list of all the lines you want to draw and pass it to the function. All lines will be drawn individually. It is more better and faster way to draw a group of lines than calling `cv2.line()` for each line.

```python
pts = np.array([[10,5],[20,30],[70,20],[50,10]],np.int32)
pts = pts.reshape(-1,1,2)
img = cv2.polylines(img,[pts],True,(0,255,255))
```

* Adding Text to Images: To put texts in images, you need specify following things.

  * Text data that you want to write;
  * Position coordinates of where you want put it (i.e.bottom-left corneer where data starts);
  * Font type(Check `cv2.putText()` docs for supported fonts);
  * Font Scale(specifies the size of font);
  * Regular things like color, thickness, lineType etc. For better look `lineType = cv2.LINE_AA` is recommended;

We will write OpenCV on our image in white color.

```python
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'OpenCV',(10,500),font,4,(255,255,255),2,cv2.LINE_AA)
```

## Mouse as a Paint-Brush

* Simple Demo: Here, we create a simple application which draws a circle on an image wherever we double-click on it.

First we create a mouse callback function which is executed when a mouse event take place. Mouse event can be anying related to mouse like left-button down, left-button up, left-button double-click etc. It gives us the coordinates(x,y) for every mouse event. With this event and location we can do whatever we like. To list all avaliable events available, run the following code in Python terminal.

```python
import cv2
events = [i for i in dir(cv2) if 'EVENT' in i]
print(events)
```

Creating mouse callback function has a specific format which is same everywhere. It differs only in what the function does. So our mouse callback function does one thiing, it draws a circle where we double-click. So see the code below. Code is self-explanatory from comments.

```python
import cv2, numpy as np
# mouse_callback function
def draw_circle(evnts,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img,(x,y),100,(255,0,0),-1)
# Create a black image, a window and bind the function to window
img = np.zeros((512,512,3),np.uint8)
cv2.nameWindow('image')
cv2.setMouseCallback('img',draw_circle)
while True:
    cv2.imshow('image',img)
    if cv2.waitKey(20) & 0xFF == 27:
        break
cv2.destroyAllWindows()
```

* More Advanced Demo: Now