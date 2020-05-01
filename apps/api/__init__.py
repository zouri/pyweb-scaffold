# -*- coding:utf-8 -*-
#
# Created Time: 2020/4/19 2:34 下午
# Be From: ZouRi 
# Last Modified: x
# e6b0b8e8bf9ce5b9b4e8bdbbefbc8ce6b0b8e8bf9ce783ade6b3aae79b88e79cb6
#
import re

from flask import current_app as _app
from flask import request, session, abort, g

from apps.service.user import UserService
from .router import ApiManager

UserService = UserService()


# 注册api
def register_apis_blueprints(_app):
    _app.register_blueprint(ApiManager, url_prefix='/apps/api')


def is_in_white_list():
    source_url = request.url_rule.__str__()
    for u in _app.config.get('URL_WHITE_LIST', []):
        rd = re.match(u, source_url)
        if rd and rd.span()[1] == len(source_url):
            return True
    return False


@ApiManager.before_request
def before_request():
    # 校验是不是白名单
    if not is_in_white_list():
        UserService.verify_user_token()




@ApiManager.after_request
def after_request(response):
    return response


# 绑定意外情况
@ApiManager.errorhandler(401)
def unauthorized(e):
    return {'message': 'Unauthorized, please check credential'}, 401


@ApiManager.errorhandler(403)
def permission_denied(e):
    return {'message': 'Permission denied, FUCK 403'}, 403


@ApiManager.errorhandler(404)
def page_not_found(e):
    return {'message': 'Not found, I Love 404'}, 404


@ApiManager.errorhandler(500)
def internal_server_error(e):
    return {'message': "I can not do it, Please try again alfred check"}, 500

