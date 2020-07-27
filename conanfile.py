from conans import ConanFile, CMake
import os

class ArithmeticConan(ConanFile):
   name = "arithmetic";
   version = "0.1";
   settings = "os", "arch", "build_type", "compiler"
   #s compiler.libcxx=libstdc++11
    
   def source(self):
      print("\n\n\nCalling SOURCE");
      url = "https://github.com/nemezisSherokee/FOSDEM2018-arithmetic";
      #self.run("git clone %s arithmetic" % url)
    
   def build(self):
      print("\n\n\nCalling BUILD");
      #cmake = CMake(self, make_program="C:\\compiler\\GnuWin32\\bin\\make.exe")
      cmake.configure(source_dir="arithmetic")
      cmake.build()
      #cmake.install()
   
   def package_info(self):
      self.cpp_info.libs=["arithmetic"]
      
   def package(self):
      #cmake = CMake(self, make_program="C:\\compiler\\GnuWin32\\bin\\make.exe")
      cmake.install()

##########FINAL NOTES################
#
#1- write a recipe like this current document
#2- build your library and create a conan ready deployment
#   conan create  <PATH WHERE TO RECIPE conanfile.py RESIDES> hermann/stable 
#   this line can be used if no profile file is defined. a path to the compiler must me set in default profile file or as env variable
#   conan create ../.. -s compiler.version=9 -s compiler=gcc -s compiler.libcxx=libstdc++11 -s compiler.version=4.9
#3- Upload your library to the remote repository
#      conan upload --remote nemezis 'arithmetic/0.1@hermann/stable' --all
#
#Now other users or project can use this library in theier project. To do this, they must:
#4 - write a conanfile and a CMakeLists.txt 
#5 - install the Libraries by using the following command : conan install <PATH WHERE TO RECIPE conanfile.txt RESIDES>
#6 - Cmake the project with this command : cmake <PATH WHERE TO RECIPE CMakeLists.txt RESIDES> -G Ninja
#7 - make the projet. We will use the command 'Ninja'.
##########END FINAL NOTES#############



#https://www.youtube.com/watch?v=RDsn0TKcdPQ
#https://bintray.com/nemezis/nemezis
    
# conan install .. -s compiler.version=9 -s compiler=clang -s compiler.libcxx=libstdc++11 -s compiler.version=9
# yes|conan remove "Ari*"
# conan create .. hermann/stable
# conan create .. -s compiler=clang -s compiler.libcxx=libstdc++11 -s compiler.version=9
#conan create . -s compiler=clang -s compiler.libcxx=libstdc++11 -s compiler.version=9 -s build_type=Debug

# conan remote add nemezis https://api.bintray.com/conan/nemezis/nemezis 
# 0c9bdf0edc67734b2c9adcc3e4f50509826c4466
# nemezis
# conan user -p <APIKEY> -r <REMOTE> <USERNAME>
# conan upload --remote nemezis 'arithmetic/0.1@hermann/stable' --all
# conan search "Arith"
# conan search "arith*" --remote nemezis

# C/C++ Compiler installation : http://win-builds.org/doku.php/download_and_installation_from_windows
#conan create . hermann/stable -e CXX=C:\compiler\bin\c++.exe -e CC=C:\compiler\bin\cc.exe
#  conan upload --remote nemezis 'arithmetic/0.1@hermann/stable' --all
#conan install .. -s compiler.version=9 -s compiler=clang -s compiler.libcxx=libstdc++11 -s compiler.version=9 --build arithmetic
# ninja
# cmake .. -G Ninja