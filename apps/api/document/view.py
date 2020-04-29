# -*- coding:utf-8 -*-
#
# Created Time: 2020/4/19 4:34 下午
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


class DocumentsManager(Resource):

    @login_required
    def get(self):
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
            order_by_ = getattr(sort_field_, 'asc')
        else:
            # print('降序')
            order_by_ = getattr(sort_field_, 'desc')

        docs = Document.query.filter(*param).order_by(order_by_()).slice(offset, limit).all()
        total_number = Document.query.filter(*param).count()
        if docs:
            res_data = [x.to_json() for x in docs]
        else:
            res_data = []
        return {'error_code': 0, 'message': 'success', 'data': {'total': total_number, 'resources': res_data}}

    @login_required
    def post(self):
        """创建一片文章"""
        data = request.json
        try:
            new_doc = Document(
                title=data['title'],
                content=data['content'],
                content_html=data['content'],
                column_id=data['column_id'],
                author=g.user_info.username,
                create_time=datetime.now(),
                status=data['status']
            )
            db.session.add(new_doc)
            db.session.commit()
            docInfo = Document.query.filter_by(title=data['title']).first()
        except KeyError as e:
            print(e, "ssssssss")
            return abort(400)
        except Exception as e:
            print(e, "susnusnusnsunsusn")
            return abort(500)

        return {'error_code': 0, 'message': 'document is created', 'data': docInfo.to_json()}

    @login_required
    def delete(self):
        data = request.json
        if not data:
            return {'error_code': 304, 'message': 'not change'}, 304
        docs = Document.query.filter(Document.id.in_(data))
        [db.session.delete(a) for a in docs]
        db.session.commit()
        return {'error_code': 0, 'message': f'document {data} is deleted'}


# 单篇文章管理
class DocumentManager(Resource):

    @login_required
    def get(self, doc_id):
        """获取一片文章"""
        doc_info = Document.query.filter_by(id=doc_id).first()
        if not doc_info:
            return abort(404)
        return {'error_code': 0, 'message': 'success', 'data': doc_info.to_json()}

    @login_required
    def put(self, doc_id):
        """更新一片文章"""
        data = request.json
        print(data, '更新的数据')
        try:
            doc_ = Document.query.filter_by(id=doc_id)
            if not doc_:
                return abort(404)

            doc_.update({
                'title': data['title'],
                'content_html': data['content'],
                # 'column_id': data['column_id'],
                'author': g.user_info.username,
                'status': data['status']
            })
            if data['status'] == 2:
                doc_.update({'pub_time': datetime.now()})
            # 更新纯文本
            doc_.first().content = data['content']
            db.session.commit()
            doc_info = Document.query.filter_by(id=doc_id).first()
            return {'error_code': 0, 'message': 'update doc success', 'data': doc_info.to_json()}
        except KeyError as e:
            return abort(400)
        except Exception as e:
            return abort(500)

    @login_required
    def patch(self, doc_id):
        attr = request.args.get('attr')
        if not attr:
            return abort(406)

        doc_info = Document.query.filter_by(id=doc_id).first()
        if not doc_info:
            return abort(404)
        data = request.json
        if hasattr(doc_info, attr) and attr in ['title', 'content', 'push_time', 'status']:
            setattr(doc_info, attr, data['value'])
            db.session.commit()
            return {'error_code': 0, 'message': f'update {attr} success', 'data': doc_info.to_json()}
        else:
            return abort(404)


# 文章属性更新更新
# class DocumentUpdate(Resource):
#     @login_required
#     def put(self, doc_id, attr):
#         doc_info = Document.query.filter_by(id=doc_id).first()
#         if not doc_info:
#             return abort(404)
#         data = request.json
#         if hasattr(doc_info, attr) and attr in ['title', 'content', 'push_time', 'status']:
#             setattr(doc_info, attr, data['value'])
#             db.session.commit()
#             return {'error_code': 0, 'message': f'update {attr} success'}
#         else:
#             return abort(404)

