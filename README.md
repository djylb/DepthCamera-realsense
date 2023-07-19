# DepthCamera 使用说明 By D-Jy

`DepthCamera.py` 是一个 Python 类文件，用于操作和获取 Intel RealSense 深度摄像头的图像和深度信息。这个类文件中提供了多个方法，可以方便地获取并保存深度摄像头的彩色图像和深度信息。

## 安装依赖

在使用 DepthCamera 类之前，需要确保已安装以下 Python 库：

- `pyrealsense2`: Intel RealSense 深度摄像头的 Python API
- `opencv-python`: OpenCV 库的 Python 版本
- `numpy`: Python 的科学计算库

可以使用以下命令进行安装：

```bash
pip install pyrealsense2 opencv-python numpy
```

## 导入 DepthCamera 类

首先，需要从 DepthCamera.py 文件中导入 DepthCamera 类：

```python
from DepthCamera import DepthCamera
```

然后，可以创建一个 DepthCamera 对象，以使用深度摄像头：

```python
dc = DepthCamera()
```

## 方法说明

`DepthCamera` 类包含以下方法：

### getImage

此方法用于获取当前实时彩色图像，返回值为一个 numpy 数组，形状为 `(height, width, 3)`，其中 `height` 和 `width` 是图像的高和宽，3 代表 RGB 三个通道。

示例：

```python
image = dc.getImage()
```

### saveImage

此方法用于获取当前实时彩色图像，并根据传入路径保存图片文件。参数 `path` 是保存图片的路径，可以是绝对路径或相对路径，支持 png、jpg、jpeg 等格式。

示例：

```python
dc.saveImage('path/to/save/image.jpg')
```

### getDepthPoint

此方法用于获取当前实时深度信息，即摄像头到某个像素点位置的距离。参数 `height` 和 `width` 是像素点的坐标。返回一个浮点数，表示深度值。

示例：

```python
depth_point = dc.getDepthPoint(120, 240)
```

### getDepth

此方法用于获取当前实时深度信息，直接返回一个 numpy 数组。数组的形状为 `(height, width)`，其中 `height` 和 `width` 是图像的高和宽。

示例：

```python
depth = dc.getDepth()
```

### getRGBD

此方法用于获取当前彩色图像和图像深度信息，返回一个 RGBD 对象。这个对象包含以下方法：

- `getImage`: 返回彩色图像 numpy 数组
- `getDepth`: 返回深度信息 numpy 数组
- `saveImage`: 将彩色图像保存成图片文件
- `getDepthPoint`: 获取某个像素点的深度信息

示例：

```python
rgbd = dc.getRGBD()
rgbd_image = rgbd.getImage()
rgbd_depth = rgbd.getDepth()
rgbd.saveImage('path/to/save/rgbd_image.jpg')
rgbd_depth_point = rgbd.getDepthPoint(120, 240)
```

### close

此方法用于关闭深度摄像头，结束使用时务必调用此方法。

示例：

```python
dc.close()
```

## 注意事项

在使用 `DepthCamera` 类时，需要确保 Intel RealSense 深度摄像头已经正确连接并可以正常工作。请按照官方用户手册进行操作，确保深度摄像头的驱动程序已经正确安装，并且摄像头已经被系统识别。

## 示例代码

下面是一个简单的示例，展示了如何使用这个类文件：

```python
from DepthCamera import DepthCamera
import cv2

# 创建 DepthCamera 对象
dc = DepthCamera()

# 获取彩色图像
image = dc.getImage()
print("获取到的彩色图像为 numpy 数组，形状为：", image.shape)

# 保存彩色图像
dc.saveImage('image.jpg')
print("已将彩色图像保存到 'image.jpg'")

# 获取某个像素点的深度信息
depth_point = dc.getDepthPoint(120, 240)
print("摄像头到像素点 (120, 240) 的距离为：", depth_point)

# 获取深度图像
depth = dc.getDepth()
print("获取到的深度图像为 numpy 数组，形状为：", depth.shape)

# 获取 RGBD 对象
rgbd = dc.getRGBD()

# 使用 RGBD 对象的方法
rgbd_image = rgbd.getImage()
print("RGBD 对象的彩色图像为 numpy 数组，形状为：", rgbd_image.shape)

rgbd_depth = rgbd.getDepth()
print("RGBD 对象的深度图像为 numpy 数组，形状为：", rgbd_depth.shape)

rgbd.saveImage('rgbd_image.jpg')
print("已将 RGBD 对象的彩色图像保存到 'rgbd_image.jpg'")

rgbd_depth_point = rgbd.getDepthPoint(120, 240)
print("RGBD 对象中像素点 (120, 240) 的深度为：", rgbd_depth_point)

# 关闭深度摄像头
dc.close()
```