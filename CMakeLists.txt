cmake_minimum_required(VERSION 3.1)

project(test_workspace)

# set(CONAN_EXPORTED ON)
set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/lib)
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/lib)
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin)
set(CMAKE_INSTALL_PREFIX ${CMAKE_BINARY_DIR}/usr/local)

include(${CMAKE_CURRENT_BINARY_DIR}/conanworkspace.cmake)

function(add_library NAME)
  _add_library(${NAME} ${ARGN})
endfunction()

conan_workspace_subdirectories()

enable_testing()
