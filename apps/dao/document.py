# -*- coding:utf-8 -*-
#
# Created Time: 2020/4/30 3:47 下午
# Be From: ZouRi 
# Last Modified: x
# e6b0b8e8bf9ce5b9b4e8bdbbefbc8ce6b0b8e8bf9ce783ade6b3aae79b88e79cb6
#
from flask import session
from apps.main import db
from apps.models import Document


class DocumentDao:

    def get_doc_list(self, param=None, sort_by=None):
        """
        获取
        :param param:
        :return:
        """
        if param is None:
            param = []
        if sort_by is None:
            # 如未传入条件使用asc
            sort_by = Document.id.asc

        docs = Document.query.filter(*param).order_by(sort_by()).slice(offset, limit).all()
        total_number = Document.query.filter(*param).count()
        if docs:
            res_data = [x.to_json() for x in docs]
        else:
            res_data = []
