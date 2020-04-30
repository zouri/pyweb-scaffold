# -*- coding:utf-8 -*-
#
# Created Time: 2020/4/27 5:22 下午
# Be From: ZouRi 
# Last Modified: x
# e6b0b8e8bf9ce5b9b4e8bdbbefbc8ce6b0b8e8bf9ce783ade6b3aae79b88e79cb6
#
from datetime import datetime
from uuid import uuid1
from flask import request, abort, g
from flask_restful import Resource, marshal_with
from bs4 import BeautifulSoup

from apps.main import db
from apps.api.user.service import login_required
from apps.models.column import Column
from apps.models.document import Document
from apps.service.column import ColumnService

Service = ColumnService()


class ColumnsManager(Resource):

    # @login_required
    def get(self):
        return Service.get_column_list()

    # @login_required
    def post(self):
        """创建一个栏目"""
        data = request.data
        return Service.add_column(data)

    def delete(self):
        data = request.json
        return Service.del_column(data)


class ColumnManager(Resource):
    # @login_required
    def get(self, column_id):
        return Service.get_a_column(column_id)

    # @login_required
    def delete(self, column_id):
        data = [column_id]
        return Service.del_column(data)
