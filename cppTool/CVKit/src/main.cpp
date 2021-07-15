#include "utils.h"

using namespace cv;
using namespace cvk;
float f = 0.1;
bool increase = true;
Mat scaleImage(Mat img){
    Mat temp = img;
    if (increase)f+=0.01;
    else f-=0.01;

    if (f>=1.0)increase=false;
    else if (f<=0.2)increase=true;
    return scale(temp, f);
}

int main(int argc, char const *argv[]){
    MMFuncList funcs;
    funcs.push_back(scaleImage);
    perform_auto(imread("../media/cvTest.jpg"), scaleImage);
    return 0;
}

