# -*- coding:utf-8 -*-
#
# Created Time: 2020/4/19 2:34 下午
# Be From: ZouRi 
# Last Modified: x
# e6b0b8e8bf9ce5b9b4e8bdbbefbc8ce6b0b8e8bf9ce783ade6b3aae79b88e79cb6
#
import re
import json

from flask import current_app as _app
from flask import request, session, abort, jsonify

from apps.service.user import UserService
from .router import ApiManager

UserService = UserService()


# 注册api
def register_apis_blueprints(_app):
    _app.register_blueprint(ApiManager)


def is_in_url_white_list():
    source_url = request.url_rule.__str__()
    for u in _app.config.get('URL_WHITE_LIST', []):
        rd = re.match(u, source_url)
        if rd and rd.span()[1] == len(source_url):
            return True
    return False


@ApiManager.before_request
def before_request():
    # print(session.get('token:b14ef9b4832311eaa0eaacde48001122'))
    # 校验是不是白名单
    if not is_in_url_white_list():
        print('不是白名单')
        UserService.verify_user_token()
    else:
        print('在白名单里面')


@ApiManager.after_request
def after(response):
    data = response.json
    print(data, type(data))
    if isinstance(data, list) or data.get('error_code', -2) == -2:
        data_str = json.dumps({
            'error_code': 0,
            'message': 'success',
            'data': data
        })
        response.data = data_str
    return response


# 绑定意外情况
@ApiManager.errorhandler(400)
def err_400(e):
    print(e, 400)
    return {'message': 'Permission denied, FUCK 403'}, 400


@ApiManager.errorhandler(401)
def unauthorized(e):
    print(e)
    return {'message': 'Unauthorized, please check credential'}, 200


@ApiManager.errorhandler(403)
def permission_denied(e):
    return {'message': 'Permission denied, FUCK 403'}, 403


@ApiManager.errorhandler(404)
def page_not_found(e):
    return {'message': 'Not found, I Love 404'}, 404


@ApiManager.errorhandler(500)
def internal_server_error(e):
    return {'message': "I can not do it, Please try again alfred check"}, 500
