cmake_minimum_required(VERSION 3.0)

project(Arithmetic)

set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_EXTENSIONS OFF)

add_library(arithmetic src/add.cpp)

target_include_directories(arithmetic
  PUBLIC
  $<BUILD_INTERFACE:${PROJECT_SOURCE_DIR}/include>
  $<INSTALL_INTERFACE:include>
)

target_link_libraries(arithmetic)

enable_testing()
add_subdirectory(test)

install(TARGETS arithmetic
        RUNTIME DESTINATION bin
        LIBRARY DESTINATION lib
        ARCHIVE DESTINATION lib)

install(DIRECTORY include DESTINATION .)
