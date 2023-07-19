# DepthCamera User Guide

`DepthCamera.py` is a Python class file for operating and obtaining image and depth information from the Intel RealSense depth camera. This class file provides multiple methods for easily obtaining and saving color images and depth information from the depth camera.

## Installation Dependencies

Before using the DepthCamera class, make sure the following Python libraries are installed:

- `pyrealsense2`: Python API for Intel RealSense depth camera
- `opencv-python`: Python version of OpenCV library
- `numpy`: Python's scientific computing library

You can install them with the following command:

```bash
pip install pyrealsense2 opencv-python numpy
```

## Importing the DepthCamera Class

First, import the DepthCamera class from the `DepthCamera.py` file:

```python
from DepthCamera import DepthCamera
```

Then, create a DepthCamera object to use the depth camera:

```python
dc = DepthCamera()
```

## Method Description

The `DepthCamera` class contains the following methods:

### getImage

This method is used to obtain the current real-time color image. The return value is a numpy array of shape `(height, width, 3)`, where `height` and `width` are the height and width of the image, and 3 represents the three RGB channels.

Example:

```python
image = dc.getImage()
```

### saveImage

This method is used to obtain the current real-time color image and save the image file according to the input path. The parameter `path` is the path to save the image, which can be an absolute or relative path, and supports formats such as png, jpg, jpeg.

Example:

```python
dc.saveImage('path/to/save/image.jpg')
```

### getDepthPoint

This method is used to obtain the current real-time depth information, that is, the distance from the camera to a certain pixel position. The parameters `height` and `width` are the coordinates of the pixel. It returns a floating point number, representing the depth value.

Example:

```python
depth_point = dc.getDepthPoint(120, 240)
```

### getDepth

This method is used to obtain the current real-time depth information, and directly returns a numpy array. The shape of the array is `(height, width)`, where `height` and `width` are the height and width of the image.

Example:

```python
depth = dc.getDepth()
```

### getRGBD

This method is used to obtain the current color image and image depth information, and returns an RGBD object. This object contains the following methods:

- `getImage`: Returns a color image numpy array
- `getDepth`: Returns a depth information numpy array
- `saveImage`: Saves the color image as an image file
- `getDepthPoint`: Gets the depth information of a certain pixel point

Example:

```python
rgbd = dc.getRGBD()
rgbd_image = rgbd.getImage()
rgbd_depth = rgbd.getDepth()
rgbd.saveImage('path/to/save/rgbd_image.jpg')
rgbd_depth_point = rgbd.getDepthPoint(120, 240)
```

### close

This method is used to close the depth camera. Be sure to call this method when you finish using it.

Example:

```python
dc.close()
```

## Precautions

When using the `DepthCamera` class, make sure the Intel RealSense depth camera is properly connected and can work normally. Please follow the official user manual to operate, ensure that the driver of the depth camera is correctly installed, and the camera has been recognized by the system.

## Sample Code

Here is a simple example showing how to use this class file:

```python
from DepthCamera import DepthCamera
import cv2

# Create DepthCamera object
dc = DepthCamera()

# Get color image
image = dc.getImage()
print("The obtained color image is a numpy array with a shape of:", image.shape)

# Save color image
dc.saveImage('image.jpg')
print("The color image has been saved to 'image.jpg'")

# Get depth information of a certain pixel point
depth_point = dc.getDepthPoint(120, 240)
print("The distance from the camera to the pixel point (120, 240) is:", depth_point)

# Get depth image
depth = dc.getDepth()
print("The obtained depth image is a numpy array with a shape of:", depth.shape)

# Get RGBD object
rgbd = dc.getRGBD()

# Use methods of RGBD object
rgbd_image = rgbd.getImage()
print("The color image of the RGBD object is a numpy array with a shape of:", rgbd_image.shape)

rgbd_depth = rgbd.getDepth()
print("The depth image of the RGBD object is a numpy array with a shape of:", rgbd_depth.shape)

rgbd.saveImage('rgbd_image.jpg')
print("The color image of the RGBD object has been saved to 'rgbd_image.jpg'")

rgbd_depth_point = rgbd.getDepthPoint(120, 240)
print("The depth of the pixel point (120, 240) in the RGBD object is:", rgbd_depth_point)

# Close the depth camera
dc.close()
```