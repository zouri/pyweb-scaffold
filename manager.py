# -*- coding:utf-8 -*-

import click
from flask_migrate import Migrate

from apps import app
from apps.main import db
from apps.cli import register_cli


migrate = Migrate(app, db)

# 注册自定义命令行
register_cli(app)




