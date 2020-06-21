# -*- coding:utf-8 -*-
#
# Created Time: 2020/6/10 10:38 下午
# Be From: ZouRi 
# Last Modified: x
# e6b0b8e8bf9ce5b9b4e8bdbbefbc8ce6b0b8e8bf9ce783ade6b3aae79b88e79cb6
#
from flask import request

from apps.dao.public_info import PublicInfoDao
from .extras import ExtrasService


Dao = PublicInfoDao()
ES = ExtrasService()


class PublicInfoService:

    def get_banner(self):
        data = Dao.get_banner()
        print(data)
        if data is None:
            return []
        return []

    def set_banner(self, data):
        Dao.add_banner(data)
        print(data, 'hahahahahhahaah')
        return {'error_code': 0, 'message': 'success', 'data': data}
