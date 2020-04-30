# -*- coding:utf-8 -*-
#
# Created Time: 2020/4/17 10:22 下午
# Be From: ZouRi 
# Last Modified: x
# e6b0b8e8bf9ce5b9b4e8bdbbefbc8ce6b0b8e8bf9ce783ade6b3aae79b88e79cb6
#
from uuid import uuid1
from flask import request, abort, session, g
from flask_restful import Resource, marshal_with, reqparse

from .service import login_required
from apps.service.user import UserService
from apps.dto.user import UserDto

Service = UserService()
Dto = UserDto()


# 登陆
class UserLogin(Resource):

    @marshal_with(Dto.info)
    def post(self):
        data = request.json
        ip_addr = request.remote_addr
        return Service.login(data, ip_addr)


# 注销
class UserLogout(Resource):
    @login_required
    def post(self):
        return Service.logout()


# 注册
class UserRegister(Resource):
    def get(self):
        return '注册'


# 管理用户
class UserManager(Resource):

    # @login_required
    def post(self):
        data = request.json
        return Service.add_user(data)


# 用户信息
class UserInfo(Resource):

    @login_required
    def get(self, username):
        return Service.get_a_user(username)
