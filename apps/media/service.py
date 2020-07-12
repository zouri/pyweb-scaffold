# -*- coding:utf-8 -*-
#
# Created Time: 2020/6/10 10:38 下午
# Be From: ZouRi 
# Last Modified: x
# e6b0b8e8bf9ce5b9b4e8bdbbefbc8ce6b0b8e8bf9ce783ade6b3aae79b88e79cb6
#
import os
import imghdr
from uuid import uuid1
from datetime import datetime
from io import BytesIO as Bytes2Data

from flask import current_app as _app
from PIL import Image


from apps.main import ApiException
from apps.utils import get_file_md5
from .dao import MediaDao, MediaInfo


Dao = MediaDao()


class MediaService:

    def upload_video(self, file_data):
        pass

    def upload_images(self, file_data):
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

        # 创建图片保存目录,按天分割
        dir_datetime_name = datetime.now().strftime('%Y-%m-%d')
        storage_dir = f"{_app.config.get('UPLOAD_PATH')}/{dir_datetime_name}"
        if not os.path.isdir(storage_dir):
            os.makedirs(storage_dir)

        file_id = uuid1().hex

        # 生成文件缩略图
        img_t = self.image_thumbnail(f_stream, 300, 300)

        # 保存源文件和缩略图
        file_name = f"{file_id}.{img_type}"
        img_t.save(os.path.join(storage_dir, f"tb_{file_name}"))
        with open(os.path.join(storage_dir, file_name), 'wb') as f:
            f.write(f_stream)

        # 数据库存储
        Dao.add_media_file({
            'id': file_id,
            'type_': 1,
            'suffix': img_type,
            'title': f_name,
            'file_dir': dir_datetime_name,
            'hash': get_file_md5(file_data),
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

    def update_banner(self, banner_id, data):
        banner = Dao.get_banner_by_id(banner_id)
        if not banner:
            raise ApiException(404)
        if Dao.update_banner(banner, data):
            return banner
        raise ApiException(500)

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

    def get_media(self, data):
        """
        获取banner图片
        :return:
        """
        page_number = data['page_number']
        limit = data['limit']
        offset = page_number * limit - limit
        limit = offset + limit

        # 排序字段
        sort_field_str = data['sort']
        if sort_field_str not in ['id', 'create_time', 'pub_time']:
            sort_field_str = 'id'
        sort_field_ = getattr(MediaInfo, sort_field_str)

        # 排序方式升序倒序
        if data['order'] == 'asc':
            sort_by = getattr(sort_field_, 'asc')
        else:
            sort_by = getattr(sort_field_, 'desc')

        media_list = Dao.get_media_list(sort_by=sort_by, offset=offset, limit=limit)
        media_total = Dao.get_total_by_param()
        return media_list, media_total

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

    @staticmethod
    def image_thumbnail(file_data, dst_width, dst_height):
        """
        将原始图片的宽高比例调整到跟目标图的宽高比例一致，所以需要：
        1. 切图，缩小原始图片的宽度或者高度
        2. 将切图后的新图片生成缩略图
        :param file_data: 原始图片的名字
        :param dst_width: 目标图片的宽度
        :param dst_height: 目标图片的高度
        """
        src_image = Image.open(Bytes2Data(file_data))

        # 原始图片的宽度和高度
        src_width, src_height = src_image.size
        # 原始图片的宽高比例，保留2位小数
        src_ratio = float('%.2f' % (src_width / src_height))
        # 目标图片的宽高比例，保留2位小数
        dst_ratio = float('%.2f' % (dst_width / dst_height))

        # 如果原始图片的宽高比例大，则将原始图片的宽度缩小
        if src_ratio >= dst_ratio:
            # 切图后的新高度
            new_src_height = src_height
            # 切图后的新宽度
            new_src_width = int(new_src_height * dst_ratio)  # 向下取整
            if new_src_width > src_width:
                # 比如原始图片(1280*480)和目标图片(800*300)的比例完全一致时，
                # 此时new_src_width=1281，可能四周会有一条黑线
                new_src_width = src_width
            blank = int((src_width - new_src_width) / 2)  # 左右两边的空白。向下取整
            # 左右两边留出同样的宽度，计算出新的 box: The crop rectangle, as a (left, upper, right, lower)-tuple
            box = (blank, 0, blank + new_src_width, new_src_height)
        # 如果原始图片的宽高比例小，则将原始图片的高度缩小
        else:
            # 切图后的新宽度
            new_src_width = src_width
            # 切图后的新高度
            new_src_height = int(new_src_width / dst_ratio)  # 向下取整
            if new_src_height > src_height:
                new_src_height = src_height
            blank = int((src_height - new_src_height) / 2)  # 上下两边的空白。向下取整
            # 上下两边留出同样的高度，计算出新的 box: The crop rectangle, as a (left, upper, right, lower)-tuple
            box = (0, blank, new_src_width, blank + new_src_height)

        # 切图
        new_src_image = src_image.crop(box)
        new_src_image.thumbnail((dst_width, dst_height))
        return new_src_image


MediaService = MediaService()
