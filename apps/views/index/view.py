# -*- coding:utf-8 -*-
#
# Created Time: 2020/4/16 6:17 下午
# Be From: ZouRi 
# Last Modified: x
# e6b0b8e8bf9ce5b9b4e8bdbbefbc8ce6b0b8e8bf9ce783ade6b3aae79b88e79cb6
#
from flask import Blueprint, render_template

IndexBp = Blueprint('Index', __name__)


@IndexBp.route('/')
def index():
    # 做些处理
    return render_template('index.html')

