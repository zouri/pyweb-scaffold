# -*- coding:utf-8 -*-
#
# Created Time: 2020/4/30 3:35 下午
# Be From: ZouRi 
# Last Modified: x
# e6b0b8e8bf9ce5b9b4e8bdbbefbc8ce6b0b8e8bf9ce783ade6b3aae79b88e79cb6
#
from flask import request, session, abort, g

from apps.main import ApiException
from apps.dao.column import ColumnDao


Dao = ColumnDao()


class ColumnService:

    def add_column(self, data):
        """
        增加栏目
        :param data:
        :return:
        """
        id, title, parent_id = data['id'], data['title'], data['parent_id']
        print(id, title, parent_id, '数据数据')
        if Dao.is_column_existe(id, title, parent_id):
            raise ApiException(409, 'column is existing')
        col_info = Dao.add_column(id, title, parent_id)
        print(col_info)
        return col_info.to_json()

    def del_column(self, column_id_list, force=False):
        """
        删除栏目
        :param column_id_list: 传入栏目id列表
        :param force: 强制删除, 如果目录里有文章也删除
        :return:
        """
        column_doc = Dao.get_column_doc(column_id_list)
        if column_doc and not force:
            response_object = {
                'error_code': 'fail',
                'message': f'column {column_doc.title} is not null'
            }
            return response_object, 200

        if Dao.del_column(column_id_list):
            response_object = {
                'error_code': 0,
                'message': f'id {column_id_list} is deleted'
            }
            return response_object, 200
        else:
            response_object = {
                'error_code': 'fail',
                'message': 'Some error occurred. Please try again.'
            }
            return response_object, 500

    def get_a_column(self, column_id):
        column_info = Dao.get_a_column(column_id)
        if column_info:
            return column_info.to_json()
        else:
            response_object = {
                'error_code': 'fail',
                'message': 'Some error occurred. Please try again.'
            }
            return response_object, 404

    def get_column_list(self):
        # column_tree_data = Dao.get_child_column('root')
        # column_tree_data = self.get_tree_column()
        columns = Dao.get_child_column('root')
        data = [c.to_json() for c in columns]
        return data

    def get_tree_column(self, parent_id='root', depth=1, data=None):
        """
        :param parent_id: 父栏目ID默认从根节点(root)目录开始
        :param depth: 递归深度, 1只代表显示根节点目录, 2代表根节点和根节点的子栏目, 依次递归, 默认1层
        :param data: 返回的数据, 一个列表
        :return: 返回传入的data
        """
        if depth == 0:
            return data
        else:
            depth -= 1
        if data is None:
            data = []
        columns = Dao.get_child_column(parent_id)
        for col in columns:
            col_data = col.to_json()
            col_data['children'] = []
            data.append(col_data)
            child_col = Dao.get_child_column(parent_id)
            if len(child_col) > 0:
                self.get_tree_column(col.id, depth, col_data['children'])
        return data

    # def is_column_null(self, column_id_list):
    #     column_doc = Dao.get_column_doc(column_id_list)
    #     if column_doc:
    #         return
    #     return True