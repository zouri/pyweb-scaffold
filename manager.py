# -*- coding:utf-8 -*-

from flask_migrate import Migrate

from apps import app
from apps.main import db
from cli import register_cli


migrate = Migrate(app, db)

# 注册自定义命令行
register_cli(app)


if __name__ == "__main__":
    app.run()

