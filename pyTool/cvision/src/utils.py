from pyUtils.decorator import parametrized
import numpy as np
import cv2

IMG_QR = "pyTool/cvision/media/QR.jpg"

@parametrized
def cv_autoShow(func, 
                name=None, 
                button=27, 
                holdTime=1):
    """
        This function should be use as a decorator.
        argument func should return a numpy array image
    """
    if type(button) == str:
        button = ord(button)
    def wait():
        while True:
            cv2.imshow(name if name is not None else func.__name__, func())
            key = cv2.waitKey(holdTime)
            if key == button:
                break
    return wait


def cv_quitHold(button=27):
    """
        Hold the image which is shown with cv2.imshow()
        Exit with specific button. 
        Button can be pass in using ascii code or char
    """
    if type(button) == str:
        button = ord(button)
    while True:
        key = cv2.waitKey(10)
        if key == button:
            break


def cv_scale(image, 
            scaler):
    """
        Scale the image with a factor scaler.
    """
    imHeight, imWidth, channels = image.shape
    return cv2.resize(image, (int(imWidth*scaler), int(imHeight*scaler)))


def cv_do(img, 
        function=None, 
        show=True):
    """
        img: the input image. 
            Can be the path to the image (str) or image data (np.ndarray)
        function: the operation to the image. 
                Function must take and return an image. 
                Can be one function or list of function.
        show: should show the image.
    """
    if type(img) == str:
        img = cv2.imread(img)
    if function is not None:
        if type(function) == list:
            images = img
            for func in function:
                images = func(images)
            name = function[-1].__name__
        else:
            images = function(img)
            name = function.__name__
    else:
        images = img
        name = ""
    if not show:
        return images
    if type(images) == list or type(images) == tuple:
        for idx, image in enumerate(images):
            cv2.imshow("{}_{}".format(name, idx), 
                        image)

    elif type(images) == np.ndarray:
        cv2.imshow(name, images)
    else:
        return
    cv_quitHold()
