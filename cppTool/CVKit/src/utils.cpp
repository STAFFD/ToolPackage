#include "utils.h"

using namespace cv;

void cvk::quitHold(char button){
    while(true){
        int key = waitKey(10);
        if(key == button)break;
    }
}

void cvk::holdImg(string filename, string windowName, char button){
    holdImg(imread(filename), windowName, button);
}

void cvk::holdImg(Mat image, string windowName, char button){
    imshow(windowName, image);
    quitHold();
}

Mat cvk::perform(Mat image, MMFuncList funcs, bool show){

    for (auto func : funcs) {
        image = func(image);
    }
    if(show) holdImg(image);
    return image;
}

Mat cvk::perform(string imagePath, MMFuncList funcs, bool show){
    return perform(imread(imagePath), funcs, show);
}

Mat cvk::scale(Mat image, double f){
    Mat out;
    cv::resize(image, out, cv::Size(), f, f);
    return out;
}

void cvk::perform_auto(Mat image, MMFunc func, string windowName, char button, int pauseTime){
    for(;;){
        imshow(windowName, func(image));
        int key = waitKey(1);
        if(key == button)break;
    }
}

void cvk::perform_auto(MVFunc func, string windowName, char button, int pauseTime){
    for(;;){
        imshow(windowName, func());
        int key = waitKey(1);
        if(key == button)break;
    }
}