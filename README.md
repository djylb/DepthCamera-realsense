# DepthCamera 使用说明 By D-Jy

`DepthCamera.py` 是一个 Python 类文件，用于操作和获取 Intel RealSense 深度摄像头的图像和深度信息。这个类文件中提供了多个方法，可以方便地获取并保存深度摄像头的彩色图像和深度信息。

## 如何使用

1. 首先，您需要安装 `pyrealsense2` 、 `opencv-python` 和 `numpy` Python 库。您可以使用以下命令来安装：

```
pip install pyrealsense2 opencv-python numpy
```

2. 导入 `DepthCamera` 类：

```python
from DepthCamera import DepthCamera
```

3. 创建一个 `DepthCamera` 对象：

```python
dc = DepthCamera()
```

## 方法说明

`DepthCamera` 类中提供了以下方法：

- `getImage()`: 获取当前实时彩色图像并返回一个 numpy 数组。数组的形状为 `(height, width, 3)`，其中 `height` 和 `width` 是图像的高和宽，3 代表 RGB 三个通道。

- `saveImage(path)`: 获取当前实时彩色图像并根据传入路径保存图片文件。`path` 是保存图片的路径，可以是绝对路径或相对路径，支持 png、jpg、jpeg 等格式。

- `getDepthPoint(height, width)`: 获取当前实时深度信息（摄像头到某个像素点位置的距离）。`height` 和 `width` 是像素点的坐标。返回一个浮点数，表示深度值。

- `getDepth()`: 获取当前实时深度信息，直接返回一个 numpy 数组。数组的形状为 `(height, width)`，其中 `height` 和 `width` 是图像的高和宽。

- `getRGBD()`: 获取当前彩色图像和图像深度信息，返回一个 RGBD 对象。这个对象包含以下方法：

  - `getImage()`: 返回彩色图像 numpy 数组。
  - `getDepth()`: 返回深度信息 numpy 数组。
  - `saveImage(path)`: 将彩色图像保存成图片文件。
  - `getDepthPoint(height, width)`: 获取某个像素点的深度信息。

- `close()`: 关闭深度摄像头。

## 返回内容及其结构

1. `getImage` 方法：返回一个 numpy 数组，数组的形状是 (480, 640, 3)，即 (高度, 宽度, RGB通道)。
2. `saveImage` 方法：无返回值，但会在指定路径保存一张图片文件。
3. `getDepthPoint` 方法：返回一个浮点数，表示摄像头到指定像素点的距离（单位：米）。
4. `getDepth` 方法：返回一个 numpy 数组，数组的形状是 (480, 640)，即 (高度, 宽度)。
5. `getRGBD` 方法：返回一个包含彩色图像和深度信息的对象。

## 示例代码

下面是一个简单的示例，展示了如何使用这个类文件：

```python
from DepthCamera import DepthCamera

# 创建一个 DepthCamera 对象
dc = DepthCamera()

# 获取并保存彩色图像
dc.saveImage('color_image.jpg')

# 获取深度信息
depth = dc.getDepth()
print(depth)

# 获取深度信息（指定像素点）
depth_point = dc.getDepthPoint(100, 100)
print(depth_point)

# 获取彩色图像和深度信息
rgbd = dc.getRGBD()
rgbd.saveImage('rgbd_image.jpg')
depth = rgbd.getDepth()
print(depth)

# 关闭深度摄像头
dc.close()
```

在使用 `DepthCamera` 类时，请确保您的 Intel RealSense 深度摄像头已经正确连接并可以正常工作。
