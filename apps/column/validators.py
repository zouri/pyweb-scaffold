# -*- coding:utf-8 -*-
#
# Created Time: 2020/5/2 5:15 下午
# Be From: ZouRi 
# Last Modified: x
# e6b0b8e8bf9ce5b9b4e8bdbbefbc8ce6b0b8e8bf9ce783ade6b3aae79b88e79cb6
#
from apps.utils.validators import param_validator, Valid_IdList_Del


class ColumnVerifyModel:

    # 增加栏目
    columns_add = {
        'expected_data': {
            'type': 'dict',
            'empty': False,
            'required': True,
            'schema': {
                'id': {
                    'type': 'string',
                    'empty': False,
                    'required': True
                },
                'title': {
                    'type': 'string',
                    'empty': False,
                    'required': True
                },
                'parent_id': {
                    'type': 'string',
                    'empty': False,
                    'required': True,
                    'default': 'root'
                },
                'type': {
                    'type': 'integer',
                    'empty': False,
                    'required': True,
                    'default': 1
                }
            }
        }
    }

    user_login = {
        'expected_data': {
            'type': 'dict',
            'empty': False,
            'required': True,
            'schema': {
                'username': {
                    'type': 'string',
                    'empty': False,
                    'required': True
                },
                'password': {
                    'type': 'string',
                    'empty': False,
                    'required': True
                },
                'random_key': {
                    'type': 'string',
                    'empty': False,
                    'required': True,
                    'default': 'no_key'
                },
                'seccode': {
                    'type': 'string',
                    'empty': False,
                    'required': True,
                    'default': 'no_code'
                }
            }
        }
    }
