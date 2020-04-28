# -*- coding:utf-8 -*-
#
# Created Time: 2020/3/12 4:08 下午
# Be From: ZouRi 
# Last Modified: x
# e6b0b8e8bf9ce5b9b4e8bdbbefbc8ce6b0b8e8bf9ce783ade6b3aae79b88e79cb6
#
import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

from .config import config


db = SQLAlchemy()
flask_bcrypt = Bcrypt()


current_path = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.path.sep + ".")
root_path = '/'.join(current_path.split('/')[:-2])


def create_app(config_name):
    app = Flask(__name__, root_path=root_path)
    app.config.from_object(config[config_name])
    db.init_app(app)
    flask_bcrypt.init_app(app)
    # login_manager.init_app(app)
    return app