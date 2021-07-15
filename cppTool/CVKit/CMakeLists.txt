cmake_minimum_required(VERSION 3.0.2)
project(CVKit)

find_package(OpenCV REQUIRED)

include_directories(include 
                    ${OpenCV_INCLUDE_DIRS})

file(GLOB SRC_FILES src/*.cpp)

add_executable(main 
                ${SRC_FILES})
target_link_libraries(main 
                        ${OpenCV_LIBRARIES})