# -*- coding:utf-8 -*-
#
# Created Time: 2020/6/10 9:38 下午
# Be From: ZouRi 
# Last Modified: x
# e6b0b8e8bf9ce5b9b4e8bdbbefbc8ce6b0b8e8bf9ce783ade6b3aae79b88e79cb6
#
from flask import current_app as _app

from apps.main import db
from apps.models import PublicInfo, BannerInfo, MediaInfo


class MediaDao:

    def add_media_file(self, data):
        """
        媒体文件信息保存到库中
        :param data:
        :return:
        """
        new_file = MediaInfo(
            id=data['id'],
            type_=1,
            file_name=data['file_name'],
            file_path=data['file_path'],
            create_time=data['create_time'],
        )
        self.save_change(new_file)
        return self.get_media_by_id(data['id'])

    def add_banner(self, data):
        new_banner = BannerInfo(
            img_id=data['img_id'],
            order_id=data['order_id'],
            type_=data['type_'],
            title=data['title'],
            status=data['status'],
            link_url=data['link_url']
        )
        self.save_change(new_banner)
        return self.get_banner_by_media(data['img_id'])

    def del_banner_list(self, data):
        docs = BannerInfo.query.filter(BannerInfo.id.in_(data))
        [db.session.delete(a) for a in docs]
        self.save_change()
        return True

    def update_banner(self, Img_, data):
        Img_.order_id = data['order_id']
        Img_.type_ = data['type_']
        Img_.title = data['title']
        Img_.img_id = data['img_id']
        Img_.status = data['status']
        Img_.link_url = data['link_url']
        self.save_change()
        return True

    def get_banner(self, type_='index'):
        sort_by = BannerInfo.order_id.asc
        return BannerInfo.query.filter(BannerInfo.type_ == type_).order_by(sort_by()).all()

    def get_media_by_id(self, file_id):
        return MediaInfo.query.filter(MediaInfo.id == file_id).first()

    def get_banner_by_id(self, banner_id):
        return BannerInfo.query.filter(BannerInfo.id == banner_id).first()

    def get_banner_by_media(self, file_id):
        return BannerInfo.query.filter(BannerInfo.img_id == file_id).first()

    @staticmethod
    def save_change(data=None):
        if data:
            db.session.add(data)
        db.session.commit()