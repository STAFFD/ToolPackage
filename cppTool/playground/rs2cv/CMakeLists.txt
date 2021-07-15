cmake_minimum_required(VERSION 3.0.2)
project(rs2cv)

find_package(realsense2 REQUIRED)
find_package(OpenCV REQUIRED)

file(GLOB SRC_FILES src/*.cpp)
file(GLOB CVKIT_SRC_FILES ../../CVKit/src/utils.cpp)
set(CVKIT_INCLUDE_DIR ../../CVKit/include)

include_directories(include 
                    ${OpenCV_INCLUDE_DIRS}
                    ${CVKIT_INCLUDE_DIR})
add_executable(main 
                ${CVKIT_SRC_FILES}
                ${SRC_FILES})
target_link_libraries(main 
                        ${OpenCV_LIBRARIES}
                        ${realsense2_LIBRARY})