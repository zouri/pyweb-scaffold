# -*- coding:utf-8 -*-
#
# Created Time: 2020/6/10 10:38 下午
# Be From: ZouRi 
# Last Modified: x
# e6b0b8e8bf9ce5b9b4e8bdbbefbc8ce6b0b8e8bf9ce783ade6b3aae79b88e79cb6
#
import os
import imghdr
import shutil
import filetype
from uuid import uuid1
from datetime import datetime
from io import BytesIO as Bytes2Data

import cv2
from PIL import Image
from flask import request
from flask import current_app as _app

from apps.main import ApiException
from apps.utils import get_file_md5
from .dao import MediaDao, MediaInfo


Dao = MediaDao()


class MediaService:

    def upload_file_chunk(self, save_path, file_data):
        """
        分段上传接口,依赖save_path判断文件是否存在或者追加,暂未使用
        :param save_path:
        :param file_data:
        :return:
        """
        current_chunk = int(request.form['dzchunkindex'])

        if os.path.exists(save_path) and current_chunk == 0:
            # 400 and 500s will tell dropzone that an error occurred and show an error
            return {
                'error_code': 500,
                'message': 'update doc success'
            }

        try:
            with open(save_path, 'ab') as f:
                f.seek(int(request.form['dzchunkbyteoffset']))
                f.write(file_data.stream.read())
        except OSError:
            # log.exception will include the traceback so we can see what's wrong
            # log.exception('Could not write to file')
            return {
                'error_code': 500,
                'message': 'Not sure why, but we could ont write the file to disk'
            }

        total_chunks = int(request.form['dztotalchunkcount'])
        if current_chunk + 1 == total_chunks:
            # This was the last chunk, the file should be complete and the size we expect
            if os.path.getsize(save_path) != int(request.form['dztotalfilesize']):
                # log.error(f"File {file_data.filename} was completed, "
                #           f"but has a size mismatch."
                #           f"Was {os.path.getsize(save_path)} but we"
                #           f" expected {request.form['dztotalfilesize']} ")
                return {
                    'error_code': 500,
                    'message': 'Size mismatch'
                }
        #     else:
        #         log.info(f'File {file_data.filename} has been uploaded successfully')
        # else:
        #     log.debug(f'Chunk {current_chunk + 1} of {total_chunks}'
        #               f'for file {file_data.filename} complete')
        return {
            'error_code': 200,
            'message': 'Chunk upload successful'
        }

    def upload_file(self, file_data):
        """
        上传文件
        :param file_data:
        :return:
        """
        file_id = uuid1().hex

        # 创建文件保存目录,按天分割
        dir_datetime_name = datetime.now().strftime('%Y-%m-%d')
        storage_dir = f"{_app.config.get('UPLOAD_PATH')}/{dir_datetime_name}"
        if not os.path.isdir(storage_dir):
            os.makedirs(storage_dir)

        old_file_path = storage_dir + file_id
        # 保存到本地路径
        file_data.save(old_file_path)
        
        file_type, file_type_code = self.check_file_type(old_file_path)

        # 生成缩略图
        img_thumb = os.path.join(storage_dir, f"tb_{file_id}.png")
        if file_type_code == 1:
            # 如果文件是图片的话, 生成缩略图
            self.image_thumbnail(old_file_path, 300, 300, img_thumb)
        elif file_type_code == 2:
            # 视频生成缩略图
            self.video_thumbnail(old_file_path, 300, 300, img_thumb)
        else:
            pass

        # 移动到新的地方
        file_name = file_id + '.' + file_type
        file_path = os.path.join(storage_dir, file_name)
        shutil.move(old_file_path, file_path)

        # md5
        with open(file_path, 'rb') as f:
            file_md5 = get_file_md5(f)

        # 数据库存储
        Dao.add_media_file({
            'id': file_id,
            'type_': file_type_code,
            'suffix': file_type,
            'title': file_data.filename.split(".")[0],
            'file_dir': dir_datetime_name,
            'hash': file_md5,
            'create_time': datetime.now()
        })

        return {
            'file_id': file_id,
            'suffix': file_type,
            'type': file_type_code,
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

    def check_file_type(self, file_path):
        """
        文件类型检测
        :param file_path:
        :return:
            file_type 文件类型,
            file_code 1图片 2视频
        """
        f = filetype.guess(file_path)
        if f is None:
            raise ApiException(code=400, message='Unknown Type', http_code=400)

        if f.extension in _app.config.get("ALLOW_FILE_TYPE_P"):
            # 图片类型检测
            return f.extension, 1

        elif f.extension in _app.config.get("ALLOW_FILE_TYPE_V"):
            # 视频检测 暂时没有任何检测
            return f.extension, 2

        else:
            raise ApiException(code=400, message='Unknown Type', http_code=400)

    @staticmethod
    def is_img(img_path, img_stream=None):
        """
        判断图片类型
        :param img_path: 文件路径名
        :param img_stream: 文件流,如果文件流不为空的话则 img_path 失效否则尝试读取img_path指定的文件
        :return:
        """
        img_type = imghdr.what(img_path, h=img_stream)
        # if img_type not in _app:
        #     return None
        return img_type

    @staticmethod
    def is_video():
        pass

    @staticmethod
    def image_thumbnail(file_data, dst_width, dst_height, save_path):
        """
        将原始图片的宽高比例调整到跟目标图的宽高比例一致，所以需要：
        1. 切图，缩小原始图片的宽度或者高度
        2. 将切图后的新图片生成缩略图
        :param file_data: 原始图片的数据
        :param dst_width: 目标图片的宽度
        :param dst_height: 目标图片的高度
        """
        if isinstance(file_data, str):
            src_image = Image.open(file_data)
        else:
            src_image = Image.open(Bytes2Data(file_data))

        # 原始图片的宽度和高度
        src_width, src_height = src_image.size
        # 原始图片的宽高比例，保留2位小数
        src_ratio = float('%.2f' % (src_width / src_height))
        dst_ratio = float('%.2f' % (dst_width / dst_height))

        # 如果原始图片的宽高比例大，则将原始图片的宽度缩小
        if src_ratio >= dst_ratio:
            # 切图后的新高度和宽度
            new_src_height = src_height
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

        # 切图&保存
        new_src_image = src_image.crop(box)
        new_src_image.thumbnail((dst_width, dst_height))
        new_src_image.save(save_path)

        return None

    @staticmethod
    def video_thumbnail(video_path, dst_width, dst_height, save_path):
        """视频截封面图片 方法有问题"""
        v_cap = cv2.VideoCapture(video_path)
        res, im_ar = v_cap.read()
        while im_ar.mean() < 1 and res:
            res, im_ar = v_cap.read()

        # 切图&保存
        im_ar = cv2.resize(im_ar, (dst_width, dst_height), 0, 0, cv2.INTER_LINEAR)
        cv2.imwrite(save_path, im_ar)

        return None


MediaService = MediaService()
