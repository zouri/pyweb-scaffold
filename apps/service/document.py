# -*- coding:utf-8 -*-
#
# Created Time: 2020/4/30 3:35 下午
# Be From: ZouRi 
# Last Modified: x
# e6b0b8e8bf9ce5b9b4e8bdbbefbc8ce6b0b8e8bf9ce783ade6b3aae79b88e79cb6
#
from uuid import uuid1
from flask import request, session, abort, g

from apps.main import ApiException
from apps.models import Document
from apps.dao.document import DocumentDao


Dao = DocumentDao()


class DocumentService:

    def add_doc(self, data):
        if Dao.get_doc_by_title(data['title'], data['column_id']) is not None:
            # 如果已经存在
            raise ApiException(409)
        return Dao.add_doc(data)

    def del_doc_list(self, doc_id_list):
        if Dao.del_doc_list(doc_id_list):
            response_object = {
                'error_code': 0,
                'message': f'id {doc_id_list} is deleted'
            }
            return response_object, 200
        else:
            raise ApiException(500)

    def update_doc(self, doc_id, data):
        doc_ = Dao.get_doc_by_id(doc_id)
        if not doc_:
            raise ApiException(404)
        print(doc_)
        if Dao.update_doc(doc_, data):
            response_object = {
                'error_code': 0,
                'message': 'update doc success',
                'data': doc_.to_json()
            }
            return response_object, 200
        raise ApiException(500)

    def update_doc_attr(self, doc_id, attr, data):
        doc_ = Dao.get_doc_by_id(doc_id)
        if not doc_:
            raise ApiException(404)
        if hasattr(doc_, attr) and attr in ['title', 'content', 'push_time', 'status']:
            Dao.update_doc_attr(doc_, attr, data)
            doc_ = Dao.get_doc_by_id(doc_id)
            return doc_
        else:
            raise ApiException(404)

    def get_a_doc(self, doc_id):
        doc_info = Dao.get_doc_by_id(doc_id)
        if not doc_info:
            raise ApiException(404)
        return doc_info

    def get_doc_list(self, data):
        page_number = data['page_number']
        limit = data['limit']
        offset = page_number * limit - limit
        limit = offset + limit

        # 栏目名称
        if data['column_id'] != 'all':
            param = [Document.column_id == data['column_id']]
        else:
            param = []
        # 排序字段
        sort_field_str = data['sort']
        if sort_field_str not in ['id', 'create_time', 'pub_time']:
            sort_field_str = 'id'
        sort_field_ = getattr(Document, sort_field_str)

        # 排序方式升序倒序
        if data['order'] == 'asc':
            sort_by = getattr(sort_field_, 'asc')
        else:
            sort_by = getattr(sort_field_, 'desc')

        doc_list = Dao.get_doc_list(param=param, sort_by=sort_by, offset=offset, limit=limit)
        doc_total = Dao.get_total_by_param(param)
        return doc_list, doc_total
