cmake_minimum_required(VERSION 3.0)

add_executable(test_add src/test_add.cpp)
target_link_libraries(test_add arithmetic)

add_test(NAME toto COMMAND test_add)
