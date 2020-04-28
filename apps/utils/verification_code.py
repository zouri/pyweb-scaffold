# -*- coding:utf-8 -*-
#
# Created Time: 2020/4/22 2:10 下午
# Be From: ZouRi 
# Last Modified: x
# e6b0b8e8bf9ce5b9b4e8bdbbefbc8ce6b0b8e8bf9ce783ade6b3aae79b88e79cb6
#
import random
import base64
import string
from uuid import uuid1
from io import BytesIO
from captcha.image import ImageCaptcha


def generate_img_captcha(char_num=4):
    image = ImageCaptcha(160, 60)  # 图片宽 160 高 60
    characters = string.digits + string.ascii_uppercase + string.ascii_lowercase  # 验证码组成，数字+大写字母+小写字母
    captcha_str = ''.join(random.sample(characters, char_num))
    img = image.generate_image(captcha_str)

    buffer = BytesIO()
    img.save(buffer, format='PNG')
    data = buffer.getvalue()

    img_base64 = 'data:image/png;base64,' + base64.b64encode(data).decode()
    return captcha_str, img_base64.__str__()


# def generate_captcha(char_num=4):
#     captcha_str = ''.join(random.choice( '1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ') for i in range(4))
#     image = ImageCaptcha().generate_image(captcha_str)
#     buffer = BytesIO()
#     image.save(buffer, format='PNG')
#     data = buffer.getvalue()
#     return 'data:image/png;base64,' + base64.b64encode(data).decode()


def sms_code():
    pass


def email_code():
    pass
