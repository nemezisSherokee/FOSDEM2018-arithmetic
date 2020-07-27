cmake_minimum_required (VERSION 3.8)

project(Calculator)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

add_executable(${PROJECT_NAME} src/main.cpp)
#add_library(${PROJECT_NAME}_LIB SHARED src/main.cpp)
message("Libs Connan = " +${CONAN_LIBS})

target_link_libraries(${PROJECT_NAME} ${CONAN_LIBS})
