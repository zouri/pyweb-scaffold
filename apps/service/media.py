# -*- coding:utf-8 -*-
#
# Created Time: 2020/6/10 10:38 下午
# Be From: ZouRi 
# Last Modified: x
# e6b0b8e8bf9ce5b9b4e8bdbbefbc8ce6b0b8e8bf9ce783ade6b3aae79b88e79cb6
#
import os
import imghdr
from datetime import datetime
from uuid import uuid1

from flask import current_app as _app

from apps.main import ApiException
from apps.dao.media import MediaDao


Dao = MediaDao()


class MediaService:

    def upload_file(self, file_data):
        """
        上传文件
        :param file_data:
        :return:
        """
        f_name, f_stream = file_data.filename, file_data.stream.read()

        # 图片检测
        is_img, img_type = self.is_img(f_name, f_stream)
        if is_img is False:
            return {'error_code': 400, 'message': 'Unable To Determine Picture Type'}

        # 刚才一响
        time_now = datetime.now()

        # 创建图片保存目录,按天分割
        dir_datetime_name = time_now.strftime('%Y-%m-%d')
        storage_dir = f"{_app.config.get('UPLOAD_PATH')}/{dir_datetime_name}"
        if not os.path.isdir(storage_dir):
            os.makedirs(storage_dir)

        file_id = uuid1().hex
        file_name = f"{file_id}.{img_type}"

        with open(os.path.join(storage_dir, file_name), 'wb') as f:
            f.write(f_stream)

        # 数据库存储
        Dao.add_media_file({
            'id': file_id,
            'type_': img_type,
            'file_name': f"{file_id}.{img_type}",
            'file_path': dir_datetime_name,
            'create_time': datetime.now()
        })

        return {
            'file_id': file_id,
            'file_type': img_type,
            'abs_path': f"{dir_datetime_name}/{file_name}",
            'url': f"/static/upload_file/{dir_datetime_name}/{file_name}",
        }

    def add_banner(self, data):
        """
        添加banner图片
        :return:
        """
        img = Dao.add_banner(data)
        return img.to_json()

    def del_banner(self, doc_id_list):
        """
        删除banner图片
        :return:
        """
        if Dao.del_banner_list(doc_id_list):
            response_object = {
                'error_code': 0,
                'message': f'id {doc_id_list} is deleted'
            }
            return response_object, 200
        else:
            raise ApiException(500)

    def update_banner(self, banner_id, data):
        banner = Dao.get_banner_by_id(banner_id)
        if not banner:
            raise ApiException(404)
        if Dao.update_banner(banner, data):
            return banner
        raise ApiException(500)

    def get_banner(self):
        """
        获取banner图片
        :return:
        """
        data = Dao.get_banner()
        if data is None:
            return []
        return [i.to_json() for i in data]

    def get_a_banner(self, banner_id):
        """
        获取banner图片
        :return:
        """
        data = Dao.get_banner_by_id(banner_id)
        if data is None:
            raise ApiException(404)
        return data

    @staticmethod
    def is_img(img_name, img_stream):
        """
        判断图片类型
        :param img_data:
        :return:
        """
        img_type = imghdr.what(img_name, h=img_stream)
        if img_type not in ['jpeg', 'png', 'jpg']:
            return False, None
        return True, img_type