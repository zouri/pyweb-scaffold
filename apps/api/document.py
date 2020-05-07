# -*- coding:utf-8 -*-
#
# Created Time: 2020/4/19 4:34 下午
# Be From: ZouRi 
# Last Modified: x
# e6b0b8e8bf9ce5b9b4e8bdbbefbc8ce6b0b8e8bf9ce783ade6b3aae79b88e79cb6
#
from datetime import datetime

from flask import request, abort, g
from flask_restful import Resource, marshal_with

from apps.validators import param_validator, DocumentVerifyModel
from apps.service.document import DocumentService
from apps.serializers.document import DocumentSerialization


Service = DocumentService()
Serialize = DocumentSerialization()
VerifyModel = DocumentVerifyModel()


class DocumentsManager(Resource):

    @param_validator(VerifyModel.get_doc_list)
    @marshal_with(Serialize.info, envelope='resource')
    def get(self):
        """
        获取文档列表
        :return:
        """
        data = g.norm_data
        return Service.get_doc_list(data)

    @param_validator(VerifyModel.doc_add)
    @marshal_with(Serialize.info)
    def post(self):
        """创建一片文章"""
        data = g.norm_data
        return Service.add_doc(data)

    def delete(self):
        data = request.json
        return Service.del_doc_list(data)


# 单篇文章管理
class DocumentManager(Resource):

    def get(self, doc_id):
        """获取一片文章"""
        return Service.get_a_doc(doc_id)

    def put(self, doc_id):
        """更新一片文章"""
        data = request.json
        return Service.update_doc(doc_id, data)

    def patch(self, doc_id):
        data = request.json
        attr = data['attr']
        value = data['value']
        return Service.update_doc_attr(doc_id, attr, value)

