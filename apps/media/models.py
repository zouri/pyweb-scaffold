# -*- coding:utf-8 -*-
#
# Created Time: 2020/6/21 2:43 下午
# Be From: ZouRi 
# Last Modified: x
# e6b0b8e8bf9ce5b9b4e8bdbbefbc8ce6b0b8e8bf9ce783ade6b3aae79b88e79cb6
#
from datetime import datetime

from apps.main import db


class MediaInfo(db.Model):
    """
    图片视频实际存储位置
    """
    __tablename__ = "media"

    id = db.Column(db.String(35), primary_key=True)
    type_ = db.Column(db.Integer, nullable=False)
    suffix = db.Column(db.String(10), nullable=False)
    title = db.Column(db.Text, nullable=True)
    file_dir = db.Column(db.String(200), nullable=False)
    hash = db.Column(db.String(50), nullable=False)
    reference = db.Column(db.Integer, nullable=False, default=1)
    create_time = db.Column(db.DateTime, nullable=False, default=datetime.now())

    @property
    def url(self):
        return f"{self.file_dir}/{self.id}.{self.suffix}"

    @property
    def tb_url(self):
        return f"{self.file_dir}/tb_{self.id}.png"

    @property
    def file_name(self):
        return f"{self.id}.{self.suffix}"

    @property
    def incr_reference(self):
        return f"<MediaInfo '{self.reference}'>"

    @incr_reference.setter
    def incr_reference(self, value=1):
        self.reference += value

    def to_json(self):
        return {
            'id': self.id,
            'type': self.type_,
            'url': self.url,
            'tb_url': self.tb_url,
            'title': self.title,
            'create_time': self.create_time.strftime("%Y-%m-%d %H:%S:%M")
        }


class BannerInfo(db.Model):
    """ Banner存储
    """
    __tablename__ = "banner"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    order_id = db.Column(db.Integer, nullable=False, default=100)
    img_id = db.Column(db.String(35), db.ForeignKey('media.id'))
    type_ = db.Column(db.String(50), nullable=False, default='index')
    title = db.Column(db.String(200), nullable=True)
    link_url = db.Column(db.String(200), nullable=True)
    create_time = db.Column(db.DateTime, nullable=False, default=datetime.now())
    status = db.Column(db.String(100), nullable=False)
    media_info = db.relationship('MediaInfo', backref=db.backref('banner'))

    def to_json(self):
        return {
            'id': self.id,
            'order_id': self.order_id,
            'file_id': self.img_id,
            'title': self.title,
            'type_': self.type_,
            'url': self.media_info.url,
            'link_url': self.link_url,
            'create_time': self.create_time.strftime("%Y-%m-%d %H:%S:%M"),
            'status': self.status
        }

    def __repr__(self):
        return f"<BannerInfo '{self.id}'>"
