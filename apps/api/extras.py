# -*- coding:utf-8 -*-
#
# Created Time: 2020/4/22 2:27 下午
# Be From: ZouRi 
# Last Modified: x
# e6b0b8e8bf9ce5b9b4e8bdbbefbc8ce6b0b8e8bf9ce783ade6b3aae79b88e79cb6
#
from flask import session
from flask_restful import Resource

from apps.service.extras import ExtrasService
from apps.utils.verify import *


Service = ExtrasService()


class ImageCode(Resource):

    def get(self):
        v, img_data = generate_img_captcha()
        img_data.__str__()
        random_key = uuid1().hex
        session[f'img_captcha:{random_key}'] = v
        res_data = {'img': img_data, 'random_key': random_key}
        return {'error_code': 0, 'message': 'success', 'data': res_data}


