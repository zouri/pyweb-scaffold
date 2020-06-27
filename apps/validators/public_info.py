# -*- coding:utf-8 -*-
#
# Created Time: 2020/6/14 10:26 下午
# Be From: ZouRi 
# Last Modified: x
# e6b0b8e8bf9ce5b9b4e8bdbbefbc8ce6b0b8e8bf9ce783ade6b3aae79b88e79cb6
#


class PublicInfoVerifyModel:
    # 增加Banner图片
    add_banner = {
        'expected_data': {
            'type': 'dict',
            'empty': False,
            'required': True,
            'schema': {
                'order_id': {
                    'type': 'integer',
                    'empty': False,
                    'required': False,
                    'default': 100
                },
                'img_id': {
                    'type': 'string',
                    'empty': False,
                    'required': True
                },
                'type_': {
                    'type': 'string',
                    'empty': False,
                    'required': True,
                    'default': 'index'
                },
                'title': {
                    'type': 'string',
                    'empty': True,
                    'required': False,
                    'default': ''
                },
                'link_url': {
                    'type': 'string',
                    'empty': True,
                    'required': False,
                    'default': ''
                },
                'status': {
                    'type': 'integer',
                    'empty': False,
                    'required': True,
                    'default': 0
                }
            }
        }
    }