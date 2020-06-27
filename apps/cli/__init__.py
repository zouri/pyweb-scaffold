# -*- coding:utf-8 -*-
#
# Created Time: 2020/6/27 7:30 下午
# Be From: ZouRi 
# Last Modified: x
# e6b0b8e8bf9ce5b9b4e8bdbbefbc8ce6b0b8e8bf9ce783ade6b3aae79b88e79cb6
#
from .user import *


# 注册命令行
def register_cli(_app):
    _app.cli.add_command(user_cli)
