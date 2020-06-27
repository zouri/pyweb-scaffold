# -*- coding:utf-8 -*-
#
# Created Time: 2020/6/10 9:38 下午
# Be From: ZouRi 
# Last Modified: x
# e6b0b8e8bf9ce5b9b4e8bdbbefbc8ce6b0b8e8bf9ce783ade6b3aae79b88e79cb6
#

from apps.main import db
from apps.models import PublicInfo, BannerInfo


class PublicInfoDao:

    def get_data(self, key_name):
        return PublicInfo.query.filter(PublicInfo.name == key_name).first()

    def get_banner(self, type_='index'):
        sort_by = BannerInfo.order_id.asc
        return BannerInfo.query.filter(BannerInfo.type_ == type_).order_by(sort_by()).all()

    def get_a_banner(self, img_name):
        return BannerInfo.query.filter(BannerInfo.img_name == img_name).first()

    def add_banner(self, data):
        new_banner = BannerInfo(
            order_id=data['order_id'],
            title=data['title'],
            img_name=data['img_name'],
            link_url=data['link_url'],
            status=data['status']
        )
        self.save_change(new_banner)
        return self.get_a_banner(data['img_name'])

    @staticmethod
    def save_change(data=None):
        if data:
            db.session.add(data)
        db.session.commit()