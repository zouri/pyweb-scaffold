# -*- coding:utf-8 -*-
#
# Created Time: 2020/4/17 10:22 下午
# Be From: ZouRi 
# Last Modified: x
# e6b0b8e8bf9ce5b9b4e8bdbbefbc8ce6b0b8e8bf9ce783ade6b3aae79b88e79cb6
#
from uuid import uuid1
from flask import request, abort, session, g
from flask_restful import Resource, marshal_with

from apps.main import db
from apps.models.user import User
from .service import login_required


class UserLogin(Resource):

    def post(self):
        data = request.json
        try:
            random_key = data['random_key']
            verification_code = data['image_verification']
            username = data['username']
            password = data['password']
        except KeyError as e:
            return abort(400)

        # 验证码校验
        my_random_key = session.get(f'img_captcha:{random_key}')
        if my_random_key and verification_code.lower() == my_random_key.lower():
            del session[f'img_captcha:{random_key}']
        else:
            return {'error_code': 401, 'message': 'verification code is error'}, 401

        # 用户名密码校验
        user_ = User.query.filter_by(username=username).first()
        if user_ and user_.check_password(password):
            user_token = uuid1().hex
            session[f'token:{user_token}'] = user_.username
            return {'error_code': 0, 'message': 'success', 'data': {'token': user_token}}

        return {'error_code': 401, 'message': 'username or password error'}, 401


class UserLogout(Resource):
    @login_required
    def post(self):
        del session[f'token:{g.token}']
        return {'error_code': 200, 'message': f'token ({g.token}) is die'}


class UserRegister(Resource):
    def get(self):
        return '注册'


class UserManager(Resource):

    # @login_required
    def post(self):
        data = request.json
        try:
            username = data['username']
            password = data['password']
        except KeyError as e:
            print('错误')
            return abort(400)
        new_user = User(
            username=username,
            password=password,
        )
        try:
            db.session.add(new_user)
            db.session.commit()
            return {'error_code': 0, 'message': 'success'}

        except Exception as e:
            return {'error_code': 500, 'message': 'user already exists'}, 500


class UserInfo(Resource):

    @login_required
    def get(self, username):
        print(username)
        if username in ['me', g.user_info.username]:
            res_data = g.user_info.to_json()
        else:
            user_ = User.query.filter_by(username=username).first()
            if user_:
                res_data = user_.to_json()
            else:
                abort(404)
        return {'error_code': 0, 'message': 'success', 'data': res_data}
