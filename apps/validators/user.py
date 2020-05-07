# -*- coding:utf-8 -*-
#
# Created Time: 2020/5/2 5:15 下午
# Be From: ZouRi 
# Last Modified: x
# e6b0b8e8bf9ce5b9b4e8bdbbefbc8ce6b0b8e8bf9ce783ade6b3aae79b88e79cb6
#


class UserVerifyModel:

    # 增加用户
    user_add = {
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
                'email': {
                    'type': 'string',
                    'empty': False,
                    'required': False,
                    'default': 'abcdef'
                },
                'role': {
                    'type': 'string',
                    'empty': False,
                    'required': True,
                    'default': 'user'
                },
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