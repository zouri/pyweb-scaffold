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


def get_child(parent_id=0, data=None):
    if data is None:
        data = []
    columns = Column.query.filter_by(parent_id=parent_id).all()
    for col in columns:
        col_data = col.to_json()
        col_data['children'] = []
        data.append(col_data)
        child_col = Column.query.filter_by(parent_id=col.id).all()
        if len(child_col) > 0:
            get_child(col.id, col_data['children'])
    return data


class ColumnsManager(Resource):

    # @login_required
    def get(self):
        data = get_child()
        return {'error_code': 0, 'message': 'success', 'data': data}

    # @login_required
    def post(self):
        """创建一个栏目"""
        data = request.json
        print(data, 'data')
        try:
            parent_id = data.get('parent_id', 0)
            if parent_id != 0:
                ColumnManager().get_a_col(parent_id)
            new_col = Column(
                name=data['name'],
                title=data['title'],
                parent_id=parent_id
            )
            db.session.add(new_col)
            db.session.commit()
            colInfo = Column.query.filter_by(column_name=data['column_name']).first()
        except KeyError as e:
            return abort(400)
        except Exception as e:
            return abort(500)

        return {'error_code': 0, 'message': 'column is created', 'data': colInfo.to_json()}



class ColumnManager(Resource):
    # @login_required
    def get(self, column_id):
        col_ = self.get_a_col(column_id)
        # colTree = {}
        return {'error_code': 0, 'message': 'success', 'data': col_.to_json()}

    # @login_required
    def delete(self, column_id):
        data = request.json
        if not data:
            return {'error_code': 0, 'message': 'not change'}
        col_ = self.get_a_col(column_id)

        # 判断是否还有子栏目
        childColList = Column.query.filter_by(parent_id=col_.id).all()
        if len(childColList) > 0:
            del_type = request.args.get('type', 'safety')
            if del_type == 'force':
                db.session.delete(col_)
                [db.session.delete(c) for c in childColList]
            else:
                return {'error_code': 400, 'message': f'column is not null'}
        else:
            db.session.delete(col_)
        db.session.commit()
        return {'error_code': 0, 'message': f'column {col_.column_name} is deleted'}

    @staticmethod
    def get_a_col(column_id):
        col_ = Column.query.filter_by(id=column_id).first()
        if not col_:
            return abort(404)
        return col_

    def get_details_col(self, column_, depth=1):
        child_col = Column.query.filter_by(parent_id=column_.id).all()
        for c in child_col:
            return self.get_details_col(c)

