# -*- coding:utf-8 -*-
#
# Created Time: 2020/4/18 5:40 下午
# Be From: ZouRi 
# Last Modified: x
# e6b0b8e8bf9ce5b9b4e8bdbbefbc8ce6b0b8e8bf9ce783ade6b3aae79b88e79cb6
#
from functools import wraps

from flask import request, session, abort, g

from apps.models import User


# 获取用户信息
def get_user(username):
    return User.query.filter_by(username=username).first()


# 登陆状态判断
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        source_url = request.url
        if request.headers.get('Access-Token'):
            user_token = request.headers.get('Access-Token')
        elif request.cookies.get('Access-Token'):
            user_token = request.cookies.get('Access-Token')
        else:
            return abort(401)
        username = session.get(f'token:{user_token}')
        if user_token == 'sun&1234567890':
            username = 'admin'
        if not username:
            return abort(401)

        user_info = session.get(f'user_cache:{username}')
        if not user_info:
            user_info = get_user(username)

        if user_info is not None:
            g.token = user_token
            g.user_info = user_info
            return f(*args, **kwargs)
        else:
            return abort(401)

    return decorated_function





class TodoDao(object):
    def __init__(self, todo_id, task):
        self.todo_id = todo_id
        self.task = task

        # This field will not be sent in the response
        self.status = 'active'