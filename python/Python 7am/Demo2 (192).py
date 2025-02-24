
# Read captcha text from user and create captcha Image and Open & show

from captcha.image import ImageCaptcha
from PIL import Image

text = input("Enter Captcha Text :")

ic = ImageCaptcha()
ic.write(text,"two.png")

Image.open("two.png").show()


