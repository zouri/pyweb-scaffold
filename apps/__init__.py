# -*- coding:utf-8 -*-
#
# Created Time: 2019/12/31 2:31 下午
# Be From: ZouRi
# Last Modified: x
# e6b0b8e8bf9ce5b9b4e8bdbbefbc8ce6b0b8e8bf9ce783ade6b3aae79b88e79cb6
#
import os

from flask import request, jsonify

from apps.main import create_app, before_process, after_process, ApiException
from apps.start_inspection.check_db import check_super_admin
from apps.views import register_front_blueprints
from apps.api import register_apis_blueprints


app = create_app(os.getenv('RUN_ENV') or 'default')
# 蓝图注册
register_front_blueprints(app)
register_apis_blueprints(app)


# @app.before_request
# def before_request():
#     before_process()
#


# Api 异常绑定
@app.errorhandler(ApiException)
def handle_invalid_usage(e):
    return jsonify({'error_code': e.code, 'message': e.message}), e.code
    # return jsonify({'error_code': e.code, 'message': e.message}), e.code
