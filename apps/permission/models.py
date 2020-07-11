# -*- coding:utf-8 -*-
#
# Created Time: 2020/4/21 1:24 下午
# Be From: ZouRi 
# Last Modified: x
# e6b0b8e8bf9ce5b9b4e8bdbbefbc8ce6b0b8e8bf9ce783ade6b3aae79b88e79cb6
#
from apps.main import db


class Permission(db.Model):
    """ 用户权限
    """
    __tablename__ = "article"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), unique=True, nullable=False)
    content = db.Column(db.Text, nullable=False)
    column = db.Column(db.String(20), nullable=False, default='news')
    author = db.Column(db.String(50), default='admin')
    article_status = db.Column(db.Integer, nullable=False, default=0)
    article_type = db.Column(db.Integer, nullable=False, default=0)
    create_time = db.Column(db.DateTime, nullable=False)
    pub_time = db.Column(db.DateTime)

    def to_json(self):
        pub_time = self.pub_time.strftime("%Y-%m-%d %H:%S:%M") if self.pub_time else ''
        return {
            'id': self.id,
            'title': self.title,
            'content': self.content,
            'column': self.column,
            'author': self.author,
            'create_time': self.create_time.strftime("%Y-%m-%d %H:%S:%M"),
            'pub_time': pub_time
        }

    def __repr__(self):
        return f"<User '{self.title}'>"
