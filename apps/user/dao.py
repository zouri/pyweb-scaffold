# -*- coding:utf-8 -*-
#
# Created Time: 2020/4/30 3:47 下午
# Be From: ZouRi 
# Last Modified: x
# e6b0b8e8bf9ce5b9b4e8bdbbefbc8ce6b0b8e8bf9ce783ade6b3aae79b88e79cb6
#
from flask import session
from apps.main import db
from apps.models import User


class UserDao:

    def add_user(self, data):
        """
        新建用户
        :param data: 用户信息字典
        :return: user obj
        """
        new_user = User(
            username=data['username'],
            password=data['password'],
            email=data['email'],
            role=data.get('role', 'user')
        )
        self.save_changes(new_user)
        return True

    @staticmethod
    def get_user(username):
        """
        获取用户信息
        :param username:
        :return: user obj
        """
        user_info = session.get(f'user_cache:{username}')
        if not user_info:
            user_info = User.query.filter_by(username=username).first()
        return user_info

    @staticmethod
    def get_user_by_uid(uid):
        """
        根据 uid 获取用户对象
        :param uid:
        :return:  user obj
        """
        return User.query.filter_by(uid=uid).first()

    @staticmethod
    def save_changes(data=None):
        """
        保存数据库更改
        :param data:
        :return:
        """
        if data:
            db.session.add(data)
        db.session.commit()
