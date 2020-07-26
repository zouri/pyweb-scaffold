# -*- coding:utf-8 -*-
#
# Created Time: 2020/6/9 10:04 下午
# Be From: ZouRi 
# Last Modified: x
# e6b0b8e8bf9ce5b9b4e8bdbbefbc8ce6b0b8e8bf9ce783ade6b3aae79b88e79cb6
#
from flask import request, g
from flask_restful import Resource

from .validators import *
from .service import MediaService as Service


class MediaManager(Resource):

    @param_validator(MediaVerifyModel.get_media)
    def get(self):
        data = g.norm_data
        media_list, media_total = Service.get_media(data)
        response_object = {
            'total': media_total,
            'resources': [d.to_json() for d in media_list]
        }
        return response_object


class MediaUpload(Resource):

    def post(self):
        img_data = request.files['file']
        print(img_data.filename)
        return Service.upload_file(img_data)


class BannersManager(Resource):
    def get(self):
        return Service.get_banner()

    @param_validator(MediaVerifyModel.add_banner)
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

    @param_validator(MediaVerifyModel.add_banner)
    def put(self, banner_id):
        data = g.norm_data
        res_data = Service.update_banner(banner_id, data)
        return {
            'error_code': 0,
            'message': 'update doc success',
            'data': res_data.to_json()
        }