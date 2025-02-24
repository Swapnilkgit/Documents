# WAS to read image path from user and open the IMAGE

from PIL import Image
path = input("Enter the Image Path :")
Image.open(path).show()
