
# Example Script to Create CAPTCHA Image with diff color

from captcha.image import ImageCaptcha
from captcha.image import random_color

ic = ImageCaptcha()
#ic.create_captcha_image("naveen",random_color(1,999),random_color(1,10)).show()

ic.create_captcha_image("naveen",(112,240,17),(9,9,230)).show()


# 0 to 255


from captcha.audio import AudioCaptcha