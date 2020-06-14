# -*- coding:utf-8 -*-
#
# Created Time: 2020/4/22 2:27 下午
# Be From: ZouRi 
# Last Modified: x
# e6b0b8e8bf9ce5b9b4e8bdbbefbc8ce6b0b8e8bf9ce783ade6b3aae79b88e79cb6
#
import os
import imghdr

from werkzeug.utils import secure_filename
from flask import current_app as _app
from flask import session, request
from flask_restful import Resource, reqparse

from apps.service.extras import ExtrasService
from apps.utils.verify import *


Service = ExtrasService()


class ImageUpload(Resource):
    def post(self):
        img_data = request.files['file']
        data = Service.upload_img(img_data)
        return {'error_code': 0, 'message': 'success', 'data': data}
        # return ES.upload_img(file_data)
        # upload_path = _app.config.get('UPLOAD_PATH', './static/upload')
        # file_data = request.files['file']
        # file_blob = file_data.stream.read()
        # img_type = imghdr.what(file_data.filename, h=file_blob)
        #
        # if img_type not in ['jpeg', 'png']:
        #     return {'error_code': 400, 'message': 'Unable To Determine Picture Type'}
        #
        # file_name = f"{uuid1().hex}.{img_type}"
        # with open(os.path.join(upload_path, file_name), 'wb') as f:
        #     f.write(file_blob)
        #
        # url = '/static/upload_file/' + file_name
        # return {'error_code': 0, 'message': 'success', 'data': {'url': url}}


class ImageCode(Resource):

    def get(self):
        v, img_data = generate_img_captcha()
        img_data.__str__()
        random_key = uuid1().hex
        session[f'img_captcha:{random_key}'] = v
        res_data = {'img': img_data, 'random_key': random_key}
        return {'error_code': 0, 'message': 'success', 'data': res_data}


