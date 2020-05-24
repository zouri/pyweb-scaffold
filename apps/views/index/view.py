# -*- coding:utf-8 -*-
#
# Created Time: 2020/4/16 6:17 下午
# Be From: ZouRi 
# Last Modified: x
# e6b0b8e8bf9ce5b9b4e8bdbbefbc8ce6b0b8e8bf9ce783ade6b3aae79b88e79cb6
#
from flask import Blueprint, render_template

from apps.dao.document import DocumentDao

IndexBp = Blueprint('Index', __name__)


DAO = DocumentDao()


# 首页
@IndexBp.route('/')
def index():
    last_new = DAO.get_doc_list(offset=0, limit=5)
    print(last_new)
    return render_template('index.html')


# 关于
@IndexBp.route('/about')
def web_about():
    # 做些处理
    return render_template('about.html')


# 活动
@IndexBp.route('/activity')
def activity():
    return render_template('activity.html')


# 产品
@IndexBp.route('/product')
def product():
    return render_template('product.html')


# 公益
@IndexBp.route('/charity')
def charity():
    return render_template('charity.html')


# 招聘
@IndexBp.route('/join_us.html')
def join_us():
    return render_template('join_us.html')

