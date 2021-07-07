import cv2

IMG_QR = "pyTool/cvision/media/QR.jpg"

def cv_quitHold(button=27):
    if type(button) == str:
        button = ord(button)
    while True:
        key = cv2.waitKey(10)
        if key == button:
            break

def cv_scale(image, scaler):
    imHeight, imWidth, channels = image.shape
    return cv2.resize(image, (int(imWidth*scaler), int(imHeight*scaler)))

def cv_do(imagePath, function):
    images = function(cv2.imread(imagePath))
    if type(images) == list:
        for idx, image in enumerate(images):
            cv2.imshow("{}_{}".format(function.__name__, idx), 
                        image)
    else:
        cv2.imshow(function.__name__, images)
    cv_quitHold()
