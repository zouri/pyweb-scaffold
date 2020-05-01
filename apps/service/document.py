# -*- coding:utf-8 -*-
#
# Created Time: 2020/4/30 3:35 下午
# Be From: ZouRi 
# Last Modified: x
# e6b0b8e8bf9ce5b9b4e8bdbbefbc8ce6b0b8e8bf9ce783ade6b3aae79b88e79cb6
#
from uuid import uuid1
from flask import request, session, abort, g

from apps.models import Document
from apps.dao.document import DocumentDao


Dao = DocumentDao()


class DocumentService:

    def get_doc_list(self):
        args = request.args
        if not args:
            args = {}
        page_number = int(args.get('page_number', 1))
        limit = int(args.get('limit', 15))
        if page_number < 1:
            page_number = 1
        offset = page_number * limit - limit
        limit = offset + limit
        # print(offset, limit, '开始实施')
        # 栏目名称
        column_id = int(args.get('column', 0))
        if column_id != 0:
            param = [Document.column_id == column_id]
        else:
            param = []
        # 排序字段
        sort_field_str = args.get('sort', 'id')
        if sort_field_str not in ['id', 'create_time', 'pub_time']:
            sort_field_str = 'id'
        sort_field_ = getattr(Document, sort_field_str)
        # 排序方式升序倒序
        if args.get('order', 'asc') == '':
            sort_by = getattr(sort_field_, 'asc')
        else:
            # print('降序')
            sort_by = getattr(sort_field_, 'desc')

        return Dao.get_doc_list(param=param, sort_by=sort_by)