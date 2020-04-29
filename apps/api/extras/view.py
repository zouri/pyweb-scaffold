# -*- coding:utf-8 -*-
#
# Created Time: 2020/4/22 2:27 下午
# Be From: ZouRi 
# Last Modified: x
# e6b0b8e8bf9ce5b9b4e8bdbbefbc8ce6b0b8e8bf9ce783ade6b3aae79b88e79cb6
#
import os
from uuid import uuid1

from werkzeug.utils import secure_filename
from flask import current_app as _app
from flask import session, request
from flask_restful import Resource, reqparse

from apps.utils.verification_code import *


class ImageUpload(Resource):
    def post(self):
        upload_path = _app.config.get('UPLOAD_PATH', './static/upload')
        img = request.files['file']
        file_name = uuid1().hex + '.' + secure_filename(img.filename).split('.')[-1]
        img.save(os.path.join(upload_path, file_name))
        url = '/static/upload_file/' + file_name
        return {'error_code': 0, 'message': 'success', 'data': {'url': url}}


class ImageCode(Resource):

    def get(self):
        v, img_data = generate_img_captcha()
        img_data.__str__()
        random_key = uuid1().hex
        session[f'img_captcha:{random_key}'] = v
        res_data = {'img': img_data, 'random_key': random_key}
        return {'error_code': 0, 'message': 'success', 'data': res_data}


