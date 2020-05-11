# -*- coding:utf-8 -*-
#
# Created Time: 2020/4/27 5:22 下午
# Be From: ZouRi 
# Last Modified: x
# e6b0b8e8bf9ce5b9b4e8bdbbefbc8ce6b0b8e8bf9ce783ade6b3aae79b88e79cb6
#

from flask import request, abort, g
from flask_restful import Resource, marshal_with

from apps.validators import param_validator, ColumnsVerifyModel
from apps.serializers.column import ColumnSerialization
from apps.service.column import ColumnService


Service = ColumnService()
VerifyModel = ColumnsVerifyModel()
Serialize = ColumnSerialization()


class ColumnsManager(Resource):

    def get(self):
        return Service.get_column_list()

    @param_validator(VerifyModel.columns_add)
    # @marshal_with(Serialize.info)
    def post(self):
        """创建一个栏目"""
        # data = request.json
        data = g.norm_data
        return Service.add_column(data)

    def delete(self):
        data = request.json
        return Service.del_column(data)


class ColumnManager(Resource):
    def get(self, column_id):
        return Service.get_a_column(column_id)

    def delete(self, column_id):
        data = [column_id]
        return Service.del_column(data)
