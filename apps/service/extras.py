# -*- coding:utf-8 -*-
#
# Created Time: 2020/6/11 12:05 上午
# Be From: ZouRi 
# Last Modified: x
# e6b0b8e8bf9ce5b9b4e8bdbbefbc8ce6b0b8e8bf9ce783ade6b3aae79b88e79cb6
#
import os
import imghdr

from flask import current_app as _app
from flask import session, request

from apps.utils.verify import *


class ExtrasService:

    def upload_img(self):
        upload_path = _app.config.get('UPLOAD_PATH', './static/upload')
        file_data = request.files['file']
        file_blob = file_data.stream.read()
        img_type = imghdr.what(file_data.filename, h=file_blob)

        if img_type not in ['jpeg', 'png']:
            return {'error_code': 400, 'message': 'Unable To Determine Picture Type'}

        file_name = f"{uuid1().hex}.{img_type}"
        with open(os.path.join(upload_path, file_name), 'wb') as f:
            f.write(file_blob)

        url = '/static/upload_file/' + file_name
        return {'error_code': 0, 'message': 'success', 'data': {'url': url}}
