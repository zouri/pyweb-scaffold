# -*- coding:utf-8 -*-
#
# Created Time: 2020/6/9 10:05 下午
# Be From: ZouRi 
# Last Modified: x
# e6b0b8e8bf9ce5b9b4e8bdbbefbc8ce6b0b8e8bf9ce783ade6b3aae79b88e79cb6
#
import json
from datetime import datetime

from apps.main import db


class PublicInfo(db.Model):
    """ 公共信息,首页,联系我们等等
    """
    __tablename__ = "public_info"

    name = db.Column(db.String(100), primary_key=True)
    data = db.Column(db.Text, nullable=False)

    def to_json(self):
        return {
            'key': self.key,
            'value': json.loads(self.value)
        }

    def __repr__(self):
        return f"<PublicInfo '{self.key}'>"


class BannerInfo(db.Model):
    """ Banner存储
    """
    __tablename__ = "banner"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    orders_id = db.Column(db.Integer, nullable=False, default=0)
    type_ = db.Column(db.Integer, nullable=False, default=0)
    title = db.Column(db.String(100), nullable=True)
    img_name = db.Column(db.String(50), nullable=False, unique=True)
    link_url = db.Column(db.String(100), nullable=False, default="/")
    description = db.Column(db.Text, nullable=True)
    create_time = db.Column(db.DateTime, nullable=False, default=datetime.now())
    status = db.Column(db.String(100), nullable=False)

    def to_json(self):
        return {
            'id': self.id,
            'orders': self.id,
            'title': self.title,
            'description': self.description,
            'img_path': self.img_path,
            'create_time': self.create_time.strftime("%Y-%m-%d %H:%S:%M"),
            'connect_url': self.connect_url,
            'status': self.status
        }

    def __repr__(self):
        return f"<BannerInfo '{self.title}'>"


# class MediaInfo(db.Model):
#     """ Banner存储
#     """
#     __tablename__ = "banner"
#
#     id = db.Column(db.Integer, autoincrement=True, primary_key=True)
#     orders = db.Column(db.Integer, nullable=False, default=0)
#     title = db.Column(db.String(100), nullable=True)
#     description = db.Column(db.Text, nullable=True)
#     img_path = db.Column(db.String(50), nullable=False, unique=True)
#     create_time = db.Column(db.DateTime, nullable=False, default=datetime.now())
#     connect_url = db.Column(db.String(100), nullable=False, default="/")
#     status = db.Column(db.String(100), nullable=False)
#
#     def to_json(self):
#         return {
#             'id': self.id,
#             'orders': self.id,
#             'title': self.title,
#             'description': self.description,
#             'img_path': self.img_path,
#             'create_time': self.create_time.strftime("%Y-%m-%d %H:%S:%M"),
#             'connect_url': self.connect_url,
#             'status': self.status
#         }
#
#     def __repr__(self):
#         return f"<BannerInfo '{self.title}'>"
