# -*- coding:utf-8 -*-
#
# Created Time: 2020/6/9 10:05 下午
# Be From: ZouRi 
# Last Modified: x
# e6b0b8e8bf9ce5b9b4e8bdbbefbc8ce6b0b8e8bf9ce783ade6b3aae79b88e79cb6
#
import json

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
