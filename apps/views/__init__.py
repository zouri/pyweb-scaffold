# -*- coding:utf-8 -*-
#
# Created Time: 2020/4/18 11:38 上午
# Be From: ZouRi
# Last Modified: x
# e6b0b8e8bf9ce5b9b4e8bdbbefbc8ce6b0b8e8bf9ce783ade6b3aae79b88e79cb6
#
from .admin.view import *
from .index.view import *


# 注册蓝图
def register_front_blueprints(_app):
    _app.register_blueprint(IndexBp, url_prefix='/')

    # 后台管理
    # _app.register_blueprint(LoginManager, url_prefix='/web_manager/login')
    # _app.register_blueprint(AdminBp, url_prefix='/web_manager/dashboard')
