'''
Author: D-Jy
Date: 2023-07-12 09:42:36
LastEditTime: 2023-07-19 15:03:44
LastEditors: D-Jy
Description: DepthCamera
FilePath: .\DepthCamera.py
'''
import pyrealsense2 as rs
import numpy as np
import cv2

class RGBD:
    def __init__(self, color_image, depth_image):
        """
        初始化RGBD对象
        """
        self.color_image = color_image
        self.depth_image = depth_image

    def getImage(self):
        """
        返回彩色图像numpy数组
        """
        return self.color_image

    def getDepth(self):
        """
        返回深度信息numpy数组
        """
        return self.depth_image

    def saveImage(self, path):
        """
        将彩色图像保存成图片文件
        """
        cv2.imwrite(path, self.color_image)


class DepthCamera:
    def __init__(self):
        """
        初始化深度摄像头
        """
        self.pipeline = rs.pipeline()
        self.config = rs.config()
        self.pipeline.start(self.config)

    def getImage(self):
        """
        获取当前彩色图像并返回一个numpy数组
        """
        frames = self.pipeline.wait_for_frames()
        color_frame = frames.get_color_frame()
        color_image = np.asanyarray(color_frame.get_data())
        return color_image

    def saveImage(self, path):
        """
        获取当前彩色图像并根据传入路径保存图片文件
        """
        color_image = self.getImage()
        cv2.imwrite(path, color_image)

    def getDepthPoint(self, height, width):
        """
        获取当前深度信息（摄像头到某个像素点位置的距离）
        """
        frames = self.pipeline.wait_for_frames()
        depth_frame = frames.get_depth_frame()
        distance = depth_frame.get_distance(width, height)
        return distance

    def getDepth(self):
        """
        获取当前深度信息，直接返回一个numpy数组
        """
        frames = self.pipeline.wait_for_frames()
        depth_frame = frames.get_depth_frame()
        depth_image = np.asanyarray(depth_frame.get_data())
        return depth_image

    def getRGBD(self):
        """
        获取当前彩色图像和图像深度信息
        """
        frames = self.pipeline.wait_for_frames()
        color_frame = frames.get_color_frame()
        depth_frame = frames.get_depth_frame()
        color_image = np.asanyarray(color_frame.get_data())
        depth_image = np.asanyarray(depth_frame.get_data())
        return RGBD(color_image, depth_image)

    def close(self):
        """
        关闭深度摄像头
        """
        self.pipeline.stop()
