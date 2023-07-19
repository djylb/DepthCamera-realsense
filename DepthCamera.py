import pyrealsense2 as rs
import numpy as np
import cv2

class RGBD:
    def __init__(self, color_image, depth_image):
        """
        Initialize the RGBD object with color and depth image data.
        """
        self.color_image = color_image
        self.depth_image = depth_image

    def getImage(self):
        """
        Return the stored color image as a numpy array.
        """
        return self.color_image

    def getDepth(self):
        """
        Return the stored depth data as a numpy array.
        """
        return self.depth_image

    def saveImage(self, path):
        """
        Save the stored color image to a file at the given path.
        """
        cv2.imwrite(path, self.color_image)

    def getDepthPoint(self, height, width):
        """
        Get the depth data for a specific point in the depth image.
        """
        return self.depth_image[height, width]


class DepthCamera:
    def __init__(self):
        """
        Initialize the depth camera and start the camera pipeline.
        """
        self.pipeline = rs.pipeline()
        self.config = rs.config()
        self.pipeline.start(self.config)

    def _get_frames(self):
        """
        Capture frames from the camera and return color and depth frames.
        """
        frames = self.pipeline.wait_for_frames()
        color_frame = frames.get_color_frame()
        depth_frame = frames.get_depth_frame()
        return color_frame, depth_frame

    def getImage(self):
        """
        Capture a color image from the camera and return it as a numpy array.
        """
        color_frame, _ = self._get_frames()
        return np.asanyarray(color_frame.get_data())

    def saveImage(self, path):
        """
        Capture a color image from the camera and save it to a file.
        """
        cv2.imwrite(path, self.getImage())

    def getDepthPoint(self, height, width):
        """
        Get the depth data for a specific point in the depth image.
        """
        _, depth_frame = self._get_frames()
        return depth_frame.get_distance(width, height)

    def getDepth(self):
        """
        Capture depth data from the camera and return it as a numpy array.
        """
        _, depth_frame = self._get_frames()
        return np.asanyarray(depth_frame.get_data())

    def getRGBD(self):
        """
        Capture color and depth data from the camera and return as an RGBD object.
        """
        color_frame, depth_frame = self._get_frames()
        color_image = np.asanyarray(color_frame.get_data())
        depth_image = np.asanyarray(depth_frame.get_data())
        return RGBD(color_image, depth_image)

    def close(self):
        """
        Stop the camera pipeline.
        """
        self.pipeline.stop()
