# -*- coding:utf-8 -*-
#
# Created Time: 2020/5/2 5:15 下午
# Be From: ZouRi 
# Last Modified: x
# e6b0b8e8bf9ce5b9b4e8bdbbefbc8ce6b0b8e8bf9ce783ade6b3aae79b88e79cb6
#
from apps.utils.validators import param_validator, Valid_IdList_Del


class MediaVerifyModel:
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

    # 获取文档列表
    get_media = {
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
