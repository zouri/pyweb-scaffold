# -*- coding:utf-8 -*-
#
# Created Time: 2020/4/17 10:22 下午
# Be From: ZouRi 
# Last Modified: x
# e6b0b8e8bf9ce5b9b4e8bdbbefbc8ce6b0b8e8bf9ce783ade6b3aae79b88e79cb6
#
from flask import request, g
from flask_restful import Resource, marshal_with, reqparse, abort

from apps.validators import param_validator, UserVerifyModel
from apps.service.user import UserService
from apps.serializers.user import UserSerialization


Service = UserService()
# Serialize = UserSerialization()
VerifyModel = UserVerifyModel()


class UserLogin(Resource):

    @param_validator(VerifyModel.user_login)
    # @marshal_with(Serialize.login)
    def post(self):
        # data = request.json
        data = g.norm_data
        ip_addr = request.remote_addr
        return Service.login(data, ip_addr)


class UserLogout(Resource):

    def post(self):
        return Service.logout()


class UserRegister(Resource):
    def get(self):
        return '注册'


# 管理用户
class UserManager(Resource):

    @param_validator(VerifyModel.user_add)
    # @marshal_with(Serialize.info)
    def post(self):
        norm_data = g.norm_data
        return Service.add_user(norm_data)


# 用户信息
class UserInfo(Resource):

    # @marshal_with(Serialize.info)
    def get(self, username):
        user_ = Service.get_a_user(username)

        return user_.to_json()
