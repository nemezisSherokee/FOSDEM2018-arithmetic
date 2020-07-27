echo "1 - REMOVE ALL Arithmetic Lib..."
yes|conan remove "Ari*"

echo 
echo 

echo "2 - BUILD YOUR LIBRARY AND CREATE A CONAN READY DEPLOYMENT..."
conan create  ../.. hermann/stable 


echo 
echo 

echo "3 - UPLOAD YOUR LIBRARY TO THE REMOTE REPOSITORY..."
conan upload --remote nemezis 'arithmetic/0.1@hermann/stable' --all

echo 
echo 

echo "4 - INSTALL THE LIBRARIES BY USING THE FOLLOWING COMMAND..."
conan install ..

echo 
echo 

echo "5- CMAKE THE PROJECT WITH THIS COMMAND..."
cmake .. -G Ninja

echo "6- make the projet. We will use the command -Ninja-..."

echo 
echo 
ninja



