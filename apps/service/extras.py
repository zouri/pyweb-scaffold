# -*- coding:utf-8 -*-
#
# Created Time: 2020/6/11 12:05 上午
# Be From: ZouRi 
# Last Modified: x
# e6b0b8e8bf9ce5b9b4e8bdbbefbc8ce6b0b8e8bf9ce783ade6b3aae79b88e79cb6
#
import os
import imghdr
import time

from flask import current_app as _app
from flask import session, request

from apps.utils.verify import *


class ExtrasService:

    def upload_img(self, img_data):
        # img_data = request.files['file']
        file_stream = img_data.stream.read()
        img_type = imghdr.what(img_data.filename, h=file_stream)

        if img_type not in ['jpeg', 'png']:
            return {'error_code': 400, 'message': 'Unable To Determine Picture Type'}

        # 创建图片保存目录,按天分割
        dir_datetime_name = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        upload_path = f"{_app.config.get('UPLOAD_PATH', './static/upload')}/{dir_datetime_name}"
        if not os.path.isdir(upload_path):
            os.makedirs(upload_path)

        file_name = f"{uuid1().hex}.{img_type}"
        with open(os.path.join(upload_path, file_name), 'wb') as f:
            f.write(file_stream)

        return {
            'url': f"/static/upload_file/{dir_datetime_name}/{file_name}",
            'abs_path': f"{dir_datetime_name}/{file_name}",
            'datetime': dir_datetime_name,
            'file_name': file_name
        }

