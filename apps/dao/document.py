# -*- coding:utf-8 -*-
#
# Created Time: 2020/4/30 3:47 下午
# Be From: ZouRi 
# Last Modified: x
# e6b0b8e8bf9ce5b9b4e8bdbbefbc8ce6b0b8e8bf9ce783ade6b3aae79b88e79cb6
#
from datetime import datetime

from flask import session, g

from apps.main import db
from apps.models import Document


class DocumentDao:
    def add_doc(self, data):
        new_doc = Document(
            title=data['title'],
            content=data['content'],
            content_html=data['content'],
            column_id=data['column_id'],
            author_id=g.user_info.uid,
            create_time=datetime.now(),
            status=data['status']
        )
        self.save_change(new_doc)
        return self.get_doc_by_title(data['title'], data['column_id'])

    def del_doc_list(self, data):
        docs = Document.query.filter(Document.id.in_(data))
        [db.session.delete(a) for a in docs]
        self.save_change()
        return True

    def update_doc(self, doc_, data):
        doc_.update(data)
        doc_.content = data['content']
        if data['status'] == 2:
            doc_.update({'pub_time': datetime.now()})
        self.save_change()
        return True

    def update_doc_attr(self, doc, attr_name, value):
        setattr(doc, attr_name, value)
        self.save_change()
        return True

    def get_doc_list(self, param=None, sort_by=None, offset=0, limit=15):
        if param is None:
            param = []
        if sort_by is None:
            # 如未传入条件使用asc
            sort_by = Document.id.asc
        return Document.query.filter(*param).order_by(sort_by()).slice(offset, limit).all()

    def get_doc_by_title(self, title, column_id):
        return Document.query.filter_by(title=title, column_id=column_id).first()

    def get_doc_by_id(self, id):
        return Document.query.filter_by(id=id).first()

    def get_total_by_param(self, param=None):
        if param is None:
            param = []
        return Document.query.filter(*param).count()

    @staticmethod
    def save_change(data=None):
        if data:
            db.session.add(data)
        db.session.commit()