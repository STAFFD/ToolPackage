from cv2 import *
from cvision.src.utils import *

def func(image):
    image = cv_scale(image, 0.5)
    ret, thresh1 = threshold(image, 127, 255, THRESH_BINARY)
    ret,thresh2 = threshold(image,127,255,THRESH_BINARY_INV)
    ret,thresh3 = threshold(image,127,255,THRESH_TRUNC)
    ret,thresh4 = threshold(image,127,255,THRESH_TOZERO)
    ret,thresh5 = threshold(image,127,255,THRESH_TOZERO_INV)
    return [thresh1, thresh2, thresh3, thresh4, thresh5]

if __name__ == "__main__":
    cv_do(IMG_QR, func)