# -*- coding:utf-8 -*-
#
# Created Time: 2020/5/2 5:23 下午
# Be From: ZouRi 
# Last Modified: x
# e6b0b8e8bf9ce5b9b4e8bdbbefbc8ce6b0b8e8bf9ce783ade6b3aae79b88e79cb6
#
from functools import wraps

from flask import request, g
from cerberus import Validator

from apps.main import ApiException


# 通用模型
Valid_IdList_Del = {
    'expected_data': {
        'type': 'list',
        'empty': True,
        'required': True,
        'schema': {
            'type': 'integer',
            'empty': True,
            'required': True
        }
    }
}


# 参数校验器
def param_validator(schema_data):
    def _valid(fun_api):
        @wraps(fun_api)
        def wrapper(*args, **kwargs):
            try:
                if request.method.lower() == 'get':
                    document = {'expected_data': dict(request.args)}
                else:
                    if 'application/json' not in request.content_type:
                        raise ApiException(400, http_code=400)
                    document = {'expected_data': request.json}
                vd = Validator(allow_unknown=True)
                vd.schema = schema_data
                status = vd.validate(document)
                # 数据标准化处理
                # document = vd.normalized(document)
                # g.norm_data = document['expected_data']
            except Exception as e:
                print(e, '数据校验有问题')
                raise ApiException(500, http_code=500)

            if status:
                # 数据标准化处理
                document = vd.normalized(document)
                g.norm_data = document['expected_data']
            else:
                print(vd.errors, '验证状态,验证失败')
                raise ApiException(400, vd.errors.__str__())

            return fun_api(*args, **kwargs)
        return wrapper
    return _valid
