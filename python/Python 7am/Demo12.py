# Example to Open an Image convert it into B/W and save.

from PIL import Image

Image.open("man.png").convert("L").save("manbw.png")

print("Image is Saved")
