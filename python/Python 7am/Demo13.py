
# Example to Open an Image and resize and show

from PIL import Image

#Image.open("man.png").resize((100,100)).show()


# Example to Open an Image and resize and save

Image.open("man.png").resize((50,50)).save("man50.png")

print("Image Saved")

