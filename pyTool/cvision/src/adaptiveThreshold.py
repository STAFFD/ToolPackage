from cv2 import *
from cvision.src.utils import *
import numpy as np

def func(img):
    ret, thresh1 = threshold(img, 127, 255, THRESH_BINARY)
    ret,thresh2 = threshold(img,127,255,THRESH_BINARY_INV)
    ret,thresh3 = threshold(img,127,255,THRESH_TRUNC)
    ret,thresh4 = threshold(img,127,255,THRESH_TOZERO)
    ret,thresh5 = threshold(img,127,255,THRESH_TOZERO_INV)
    imHeight, imWidth = img.shape
    print("imHeight:{}".format(imHeight))
    print("imWidth:{}".format(imWidth))

    for col in range(0, imWidth, 4):
        for row in range(0, imHeight, 4):
            m = img[row:row+4, col:col+4].mean()
            a = img[row:row+4, col:col+4]
            a = np.where(a>m, a, 255)
            a = np.where(a==255, a, 0)
            img[row:row+4, col:col+4] = a
    return img

def scale_grey(image):
    return cvtColor(cv_scale(image, 0.5), COLOR_BGR2GRAY)

def adapTh(image):
    return adaptiveThreshold(image, 200, ADAPTIVE_THRESH_GAUSSIAN_C, THRESH_BINARY, 3, 2)

def boundarySegmentation(image):
    print(image)
    return image

if __name__ == "__main__":
    # image = np.random.randint(255, size=(800,800,3),dtype=np.uint8)
    # cv_do(image, func)

    cv_do(IMG_QR, [ 
                    scale_grey,
                    adapTh, 
                    boundarySegmentation
                    ])