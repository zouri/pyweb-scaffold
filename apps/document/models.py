# -*- coding:utf-8 -*-
#
# Created Time: 2020/4/16 5:49 下午
# Be From: ZouRi 
# Last Modified: x
# e6b0b8e8bf9ce5b9b4e8bdbbefbc8ce6b0b8e8bf9ce783ade6b3aae79b88e79cb6
#
from bs4 import BeautifulSoup
from sqlalchemy import UniqueConstraint

from apps.main import db


class Document(db.Model):
    """ 企业动态
    """
    __tablename__ = "document"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    cover = db.Column(db.String(200))
    content_text = db.Column(db.Text, nullable=False)
    content_html = db.Column(db.Text, nullable=False)
    column_id = db.Column(db.String(100), db.ForeignKey('column.id'))
    author_id = db.Column(db.String(100), db.ForeignKey('user.uid'))
    status = db.Column(db.Integer, nullable=False, default=0)
    type = db.Column(db.Integer, nullable=False, default=0)
    create_time = db.Column(db.DateTime, nullable=False)
    pub_time = db.Column(db.DateTime)
    column = db.relationship('Column', backref=db.backref('document'))
    author = db.relationship('User', backref=db.backref('document'))

    __table_args__ = (
        UniqueConstraint('title', 'column_id'),  # 同一栏目下文档标题唯一
    )

    @property
    def content(self):
        return self.content_text

    @content.setter
    def content(self, content_html):
        soup = BeautifulSoup(content_html, 'html.parser')
        self.content_text = soup.text

    def to_json(self):
        pub_time = self.pub_time.strftime("%Y-%m-%d %H:%S:%M") if self.pub_time else ''
        return {
            'id': self.id,
            'title': self.title,
            'cover': self.cover,
            'content': self.content_text,
            'content_html': self.content_html,
            'column': self.column.title,
            'column_id': self.column_id,
            'author': self.author.username,
            'create_time': self.create_time.strftime("%Y-%m-%d %H:%S:%M"),
            'pub_time': pub_time,
            'status': self.status
        }

    def __repr__(self):
        return f"<Document '{self.title}'>"