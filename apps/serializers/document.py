# -*- coding:utf-8 -*-
#
# Created Time: 2020/4/30 4:10 下午
# Be From: ZouRi 
# Last Modified: x
# e6b0b8e8bf9ce5b9b4e8bdbbefbc8ce6b0b8e8bf9ce783ade6b3aae79b88e79cb6
#
from flask_restful import fields


class DocumentSerialization:
    # 文档信息
    info = {
        'id': fields.Integer,
        'title': fields.String,
        'content': fields.String,
        'content_html': fields.String,
        'column': fields.String,
        'column_id': fields.String,
        'create_time': fields.String,
        'pub_time': fields.String,
        'status': fields.Integer
    }
    # 用户登录后序列化信息
    # login = info.copy()['token'] = fields.String

