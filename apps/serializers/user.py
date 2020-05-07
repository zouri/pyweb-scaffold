# -*- coding:utf-8 -*-
#
# Created Time: 2020/4/30 4:10 下午
# Be From: ZouRi 
# Last Modified: x
# e6b0b8e8bf9ce5b9b4e8bdbbefbc8ce6b0b8e8bf9ce783ade6b3aae79b88e79cb6
#
from flask_restful import fields


class UserSerialization:
    # 用户信息
    info = {
        'uid': fields.String,
        'email': fields.String,
        'username': fields.String,
        'role': fields.String,
        'registration_time': fields.String,
        'status': fields.Integer
    }

    # 用户登录后序列化信息
    login = info.copy()
    login['token'] = fields.String

