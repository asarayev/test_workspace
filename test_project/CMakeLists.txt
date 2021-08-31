cmake_minimum_required(VERSION 3.17)

project(test_project)

set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)
set(CMAKE_BUILD_WITH_INSTALL_NAME_DIR TRUE)

include(${CMAKE_CURRENT_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(TARGETS)

add_library(${PROJECT_NAME}
  include/test.h
  src/test.cpp
)

target_include_directories(${PROJECT_NAME}
  PUBLIC
    include/
  PRIVATE
    src/
)

install(TARGETS ${PROJECT_NAME} DESTINATION lib)
install(DIRECTORY include DESTINATION .)