
# Example Program to Open an Image and rotate and show

from PIL import Image

# Image.open("man.png").rotate(90).show()

# Example to rotate and save

# Image.open("man.png").rotate(90).save("man90.png")

Image.open("man.png").rotate(180).save("C:\\Users\\android\\Desktop\\banner\\man180.png")

print("Image saved")
