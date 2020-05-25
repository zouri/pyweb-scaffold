# -*- coding:utf-8 -*-
#
# Created Time: 2020/5/2 5:15 下午
# Be From: ZouRi 
# Last Modified: x
# e6b0b8e8bf9ce5b9b4e8bdbbefbc8ce6b0b8e8bf9ce783ade6b3aae79b88e79cb6
#


class DocumentVerifyModel:

    # 增加文档
    doc_add = {
        'expected_data': {
            'type': 'dict',
            'empty': False,
            'required': True,
            'schema': {
                'title': {
                    'type': 'string',
                    'empty': False,
                    'required': True
                },
                'content': {
                    'type': 'string',
                    'empty': False,
                    'required': True
                },
                'column_id': {
                    'type': 'string',
                    'empty': False,
                    'required': True
                },
                'cover': {
                    'type': 'string',
                    'empty': True,
                    'required': False,
                },
                'status': {
                    'type': 'integer',
                    'empty': False,
                    'required': True,
                    'default': 2
                }
            }
        }
    }

    # 获取文档列表
    get_doc_list = {
        'expected_data': {
            'type': 'dict',
            'empty': False,
            'required': True,
            'schema': {
                'page_number': {
                    'type': 'integer',
                    'empty': False,
                    'required': True,
                    'coerce': int,
                    'default': 1,
                    'min': 1
                },
                'limit': {
                    'type': 'integer',
                    'empty': False,
                    'required': True,
                    'coerce': int,
                    'default': 15,
                    'max': 100
                },
                'column_id': {
                    'type': 'string',
                    'empty': False,
                    'required': True
                },
                'sort': {
                    'type': 'string',
                    'empty': False,
                    'required': True,
                    'default': 'id'
                },
                'order': {
                    'type': 'string',
                    'empty': False,
                    'required': True,
                    'default': 'desc'
                }
            }
        }
    }

    # 更新文档属性
    update_doc_attr = {
        'expected_data': {
            'type': 'dict',
            'empty': False,
            'required': True,
            'schema': {
                'attr': {
                    'type': 'string',
                    'empty': False,
                    'required': True
                },
                'value': {
                    'anyof_type': ['string', 'integer'],
                    'empty': False,
                    'required': True,
                }
            }
        }
    }
