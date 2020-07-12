# -*- coding:utf-8 -*-
#
# Created Time: 2020/4/19 4:34 下午
# Be From: ZouRi 
# Last Modified: x
# e6b0b8e8bf9ce5b9b4e8bdbbefbc8ce6b0b8e8bf9ce783ade6b3aae79b88e79cb6
#
from flask import request, g
from flask_restful import Resource

from .validators import param_validator
from .validators import DocumentVerifyModel as VerifyModel
from .service import DocumentService as Service


class DocumentsManager(Resource):

    @param_validator(VerifyModel.get_doc_list)
    def get(self):
        """
        获取文档列表
        :return:
        """
        data = g.norm_data
        doc_list, doc_total = Service.get_doc_list(data)
        response_object = {
            'total': doc_total,
            'resources': [d.to_json() for d in doc_list]
        }
        return response_object

    @param_validator(VerifyModel.doc_add)
    def post(self):
        """创建一片文章"""
        data = g.norm_data
        doc_ = Service.add_doc(data)
        print(doc_)
        return doc_.to_json()

    def delete(self):
        data = request.json
        return Service.del_doc_list(data)


# 单篇文章管理
class DocumentManager(Resource):

    def get(self, doc_id):
        """获取一片文章"""
        doc_ = Service.get_a_doc(doc_id)
        return doc_.to_json()

    def put(self, doc_id):
        """更新一片文章"""
        data = request.json
        return Service.update_doc(doc_id, data)

    @param_validator(VerifyModel.update_doc_attr)
    def patch(self, doc_id):
        data = request.json
        doc_ = Service.update_doc_attr(doc_id, data['attr'], data['value'])
        return doc_.to_json()

