from cvision.src.utils import cv_autoShow
import pyrealsense2 as rs
import numpy as np
import torch

# # Model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')  # or yolov5m, yolov5x, custom

@cv_autoShow()
def showCam():
    frames = pipe.wait_for_frames()
    image = np.array(frames.get_color_frame().get_data()) 
    results = model(image)
    return results.render()[0][...,::-1] # convert BGR to RGB


if __name__ == "__main__":
    pipe = rs.pipeline()
    profile = pipe.start()
    try:
        showCam()
    except Exception as reason:
        print(reason)
    finally:
        pipe.stop()
