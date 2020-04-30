# -*- coding:utf-8 -*-
#
# Created Time: 2020/4/30 3:35 下午
# Be From: ZouRi 
# Last Modified: x
# e6b0b8e8bf9ce5b9b4e8bdbbefbc8ce6b0b8e8bf9ce783ade6b3aae79b88e79cb6
#
from uuid import uuid1
from flask import request, session, abort, g

from apps.dao.user import UserDao

user_dao = UserDao()


class UserService:
    # 登陆
    def login(self, data, ip_addr):
        """
        :param data: request.json
        :return: uwsgi
        """
        # 验证码校验
        if self.verify_captcha(ip_addr, data):
            abort(401)

        # 用户名密码校验
        username, password = data['username'], data['password']
        user_ = user_dao.get_a_user(username)
        if user_ and user_.check_password(password):
            user_token = uuid1().hex
            session[f'token:{user_token}'] = user_.username
            return user_

        return abort(401)

    # 注销
    def logout(self):
        """
        :param data: request.json
        :return: uwsgi
        """
        del session[f'token:{g.token}']
        return {'error_code': 200, 'message': f'token ({g.token}) is die'}

    # 管理员新建用户
    def add_user(self, data):
        return user_dao.add_user(data)

    def get_a_user(self, username):
        if username in ['me', g.user_info.username]:
            res_data = g.user_info
        else:
            res_data = user_dao.get_a_user(username)
            if not res_data:
                return abort(404)
        return res_data

    @staticmethod
    def verify_captcha(ip_addr, data):
        if not session.get(f'client_captcha_ip:{ip_addr}'):
            # 是否需要验证码校验, 缓存 > 没有ip > 不需要检验
            return True

        random_key, v_code = data['random_key'], data['image_verification']
        my_random_key = session.get(f'img_captcha:{random_key}')

        if my_random_key and v_code.lower() == my_random_key.lower():
            del session[f'img_captcha:{random_key}']
            return True
        else:
            return False