#include <librealsense2/rs.hpp>
#include <librealsense2/rs.hpp>
#include <opencv2/opencv.hpp>
#include <utils.h>

using namespace cv;

int main(int argc, char const *argv[]){
    // Start streaming with the default recommended configuration
    rs2::pipeline pipe;
    // pipe = new rs2::pipeline;

    rs2::config cfg;
    // cfg.enable_stream(RS2_STREAM_COLOR, 1, RS2_FORMAT_Y8, 60);
    cfg.enable_stream(RS2_STREAM_ANY, RS2_FORMAT_Y8);
    pipe.start(cfg); 

    while (true){
        rs2::frameset data = pipe.wait_for_frames(); 
        rs2::frame color = data.get_color_frame();

        // Query frame size (width and height)
        const int w = color.as<rs2::video_frame>().get_width();
        const int h = color.as<rs2::video_frame>().get_height();

        // Create OpenCV matrix of size (w,h) from the colorized depth data
        Mat image(cv::Size(w, h), CV_8UC3, (void*)color.get_data(), Mat::AUTO_STEP);
        imshow("", image);
        waitKey(1);
    }
    
    return 0;
}
