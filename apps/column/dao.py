# -*- coding:utf-8 -*-
#
# Created Time: 2020/4/30 3:47 下午
# Be From: ZouRi 
# Last Modified: x
# e6b0b8e8bf9ce5b9b4e8bdbbefbc8ce6b0b8e8bf9ce783ade6b3aae79b88e79cb6
#
from sqlalchemy import or_, and_

from apps.main import db
from apps.document.models import Document
from .models import Column


class ColumnDao:

    def add_column(self, id_, title, parent_id):
        """
        新增栏目
        :param parent_id: 父目录, 'root'为根目录
        :param id_: 栏目自定义id, 例如<title>的拼音
        :param title: 栏目名称
        :return: 返回新建的栏目对象
        """
        new_col = Column(
            id=id_,
            title=title,
            parent_id=parent_id,
        )
        self.save_changes(new_col)
        return self.get_a_column(id_)

    def del_column(self, column_id_list):
        column_list = Column.query.filter(Column.id.in_(column_id_list)).all()
        [db.session.delete(c) for c in column_list]
        self.save_changes()
        return True

    def get_a_column(self, column_id):
        """
        获取指定栏目信息
        :param column_id: 栏目自定义ID
        :return: column Obj or None
        """
        return Column.query.filter_by(id=column_id).first()

    def get_child_column(self, parent_id=None):
        """
        获取子栏目列表
        :param parent_id: 父栏目ID
        :return: 返回子栏目对象列表
        """
        if parent_id is None:
            return Column.query.all()
        else:
            return Column.query.filter_by(parent_id=parent_id).all()

    @staticmethod
    def save_changes(data=None):
        """
        保存数据库更改
        :param data:
        :return:
        """
        if data:
            db.session.add(data)
        db.session.commit()

    def is_column_existe(self, id_, title, parent_id):
        """
        判断栏目是否已经存在
        :param id_: 栏目id
        :param title: 栏目标题, 在同一个父栏目下 title不能重复
        :param parent_id: 父栏目
        :return:
        """
        # print(id_, title, parent_id)
        col = Column.query.filter(
            or_(
                Column.id == id_,
                and_(
                    Column.parent_id == parent_id,
                    Column.title == title
                )
            )
        ).all()
        print(col, 'abcddffdfdfdf')
        if col:
            return True
        else:
            return False

    def get_column_doc(self, column_id_list):
        """
        判断栏目是否为空
        :param column_id:
        :return:
        """
        return Document.query.filter(Document.column_id.in_(column_id_list)).all()
