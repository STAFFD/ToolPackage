#ifndef UTILS_H_
#define UTILS_H_

#include <iostream>
#include <list>
#include <functional>
#include <opencv2/opencv.hpp>

namespace cvk{
    using namespace std;
    using namespace cv;

    typedef std::function<Mat(Mat)> MMFunc;
    typedef list<MMFunc> MMFuncList;
    typedef std::function<Mat(void)> MVFunc;
    
    void quitHold(char button='q');
    void holdImg(string filename, 
                string windowName="holdImg", 
                char button='q');
    void holdImg(Mat image, 
                string windowName="holdImg", 
                char button='q');
    Mat perform(Mat image, 
                MMFuncList, 
                bool show);
    Mat perform(string imagePath,
                MMFuncList funcs, 
                bool show);
    Mat scale(Mat image, 
            double f);
    void perform_auto(Mat image, 
                    MMFunc func, 
                    string windowName="perform_auto", 
                    char button='q', 
                    int pauseTime=1);
    void perform_auto(MVFunc func, 
                    string windowName="perform_auto", 
                    char button='q', 
                    int pauseTime=1);               
}

#endif