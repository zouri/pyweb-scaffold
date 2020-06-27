# -*- coding:utf-8 -*-
#
# Created Time: 2020/6/9 10:04 下午
# Be From: ZouRi 
# Last Modified: x
# e6b0b8e8bf9ce5b9b4e8bdbbefbc8ce6b0b8e8bf9ce783ade6b3aae79b88e79cb6
#
from flask import request, g
from flask_restful import Resource

from apps.validators import param_validator, PublicInfoVerifyModel, Valid_IdList_Del
from apps.service.media import MediaService


Service = MediaService()


class MediaManager(Resource):
    # def get(self):
    #     return Service.get_banner()

    def post(self):
        img_data = request.files['file']
        return Service.upload_file(img_data)


class BannersManager(Resource):
    def get(self):
        return Service.get_banner()

    @param_validator(PublicInfoVerifyModel.add_banner)
    def post(self):
        data = g.norm_data
        return Service.add_banner(data)

    @param_validator(Valid_IdList_Del)
    def delete(self):
        data = request.json
        return Service.del_banner(data)


class BannerManager(Resource):
    def get(self, banner_id):
        res_data = Service.get_a_banner(banner_id)
        return res_data.to_json()

    @param_validator(PublicInfoVerifyModel.add_banner)
    def put(self, banner_id):
        data = g.norm_data
        res_data = Service.update_banner(banner_id, data)
        return {
            'error_code': 0,
            'message': 'update doc success',
            'data': res_data.to_json()
        }