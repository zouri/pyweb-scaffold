# -*- coding:utf-8 -*-
#
# Created Time: 2020/4/19 2:34 下午
# Be From: ZouRi 
# Last Modified: x
# e6b0b8e8bf9ce5b9b4e8bdbbefbc8ce6b0b8e8bf9ce783ade6b3aae79b88e79cb6
#
from .router import ApiManager


# 注册api
def register_apis_blueprints(_app):
    _app.register_blueprint(ApiManager, url_prefix='/apps/api')
