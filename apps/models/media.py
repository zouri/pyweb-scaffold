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
    file_name = db.Column(db.String(200), nullable=False)
    file_path = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=True)
    create_time = db.Column(db.DateTime, nullable=False, default=datetime.now())

    @property
    def url(self):
        return f"/static/upload_file/{self.file_path}/{self.file_name}"

    @url.setter
    def url(self, content_html):
        raise AttributeError('url: read-only field')


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
