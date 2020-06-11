# -*- coding:utf-8 -*-
#
# Created Time: 2020/6/9 10:04 下午
# Be From: ZouRi 
# Last Modified: x
# e6b0b8e8bf9ce5b9b4e8bdbbefbc8ce6b0b8e8bf9ce783ade6b3aae79b88e79cb6
#
from flask_restful import Resource

from apps.service.public_info import PublicInfoService


Service = PublicInfoService()


class BannerService(Resource):
    def get(self):
        return Service.get_banner()

    def post(self):
        return Service.set_banner()