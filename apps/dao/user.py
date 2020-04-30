# -*- coding:utf-8 -*-
#
# Created Time: 2020/4/30 3:47 下午
# Be From: ZouRi 
# Last Modified: x
# e6b0b8e8bf9ce5b9b4e8bdbbefbc8ce6b0b8e8bf9ce783ade6b3aae79b88e79cb6
#

from apps.main import db
from apps.models import User


class UserDao:
    # 获取用户信息
    def get_a_user(self, username):
        return User.query.filter_by(username=username).first()

    def get_user_id(self, uid):
        return User.query.filter_by(uid=uid).first()

    # 新建用户
    def add_user(self, data):
        new_user = User(
            username=data['username'],
            password=data['password'],
            email=data['email'],
            role=data.get('role', 'user')
        )
        self.save_changes(new_user)
        return self.get_a_user(data['username'])

    @staticmethod
    def save_changes(data=None):
        if data:
            db.session.add(data)
        db.session.commit()
