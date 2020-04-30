# -*- coding:utf-8 -*-
#
# Created Time: 2020/4/27 3:33 下午
# Be From: ZouRi 
# Last Modified: x
# e6b0b8e8bf9ce5b9b4e8bdbbefbc8ce6b0b8e8bf9ce783ade6b3aae79b88e79cb6
#
from sqlalchemy import UniqueConstraint

from apps.main import db



class Column(db.Model):
    """ 企业动态
    """
    __tablename__ = "column"

    id = db.Column(db.String(100), primary_key=True, nullable=False)
    title = db.Column(db.String(100), nullable=False)
    parent_id = db.Column(db.String(100), nullable=False, default='root')
    type = db.Column(db.String(20))

    __table_args__ = (
        UniqueConstraint('title', 'parent_id'),  # 同一栏目下目录标题唯一
    )

    def to_json(self):
        return {
            'id': self.id,
            'title': self.title,
            'parent_id': self.parent_id,
            'type': self.type,
        }

    def __repr__(self):
        return f"<Column '{self.id}'>"
