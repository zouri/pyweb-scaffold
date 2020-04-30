# -*- coding:utf-8 -*-
#
# Created Time: 2020/4/30 4:10 下午
# Be From: ZouRi 
# Last Modified: x
# e6b0b8e8bf9ce5b9b4e8bdbbefbc8ce6b0b8e8bf9ce783ade6b3aae79b88e79cb6
#
from flask_restful import fields

# uid = db.Column(db.String(100), primary_key=True, default=uuid1().hex)
#     username = db.Column(db.String(100), unique=True)
#     email = db.Column(db.String(100), unique=True)
#     password_hash = db.Column(db.String(100))
#     role = db.Column(db.String(100), default='user')
#     registration_time = db.Column(db.DateTime, default=datetime.now())
#     status = db.Column(db.Integer, default=0, nullable=False)

class UserDto:
    # 用户信息
    info = {
        'uid': fields.String,
        'email': fields.String,
        'username': fields.String,
        'role': fields.String,
        'registration_time': fields.String,
        'status': fields.Integer
    }

