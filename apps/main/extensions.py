# -*- coding:utf-8 -*-
#
# Created Time: 2020/3/10 6:46 下午
# Be From: ZouRi 
# Last Modified: x
# e6b0b8e8bf9ce5b9b4e8bdbbefbc8ce6b0b8e8bf9ce783ade6b3aae79b88e79cb6
#
from flask import request, g, session


def before_process():
    pass
    # print(session.keys(), 'kkkkeeeeesssss')
    # print(session.get('token:b14ef9b4832311eaa0eaacde48001122a'), 'a')
    # print(session.get('token:b14ef9b4832311eaa0eaacde48001122'), 'b')


def after_process(response):
    # 此处可写
    return response


# APi 异常
class ApiException(Exception):
    code = 400

    def __init__(self, code=None, message=None, payload=None, http_code=200):
        Exception.__init__(self)
        self.http_code = http_code
        self.message = message
        if code is not None:
            self.code = code
        self.payload = payload
        if self.message is None:
            if self.code == 400:
                self.message = 'please check parameter'
            elif self.code == 401:
                self.message = 'unauthorized, please check credential'
            elif self.code == 403:
                self.message = 'permission denied, FUCK 403'
            elif self.code == 404:
                self.message = 'there is no resources, I Love 404'
            elif self.code == 409:
                self.message = 'existing resources'
            elif self.code == 500:
                self.message = 'i can not do it, please try again alfred check'
            else:
                self.message = 'I can not do it, Please try again alfred check'

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        rv['http_code'] = self.http_code
        return rv
