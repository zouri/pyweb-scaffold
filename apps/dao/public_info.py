# -*- coding:utf-8 -*-
#
# Created Time: 2020/6/10 9:38 下午
# Be From: ZouRi 
# Last Modified: x
# e6b0b8e8bf9ce5b9b4e8bdbbefbc8ce6b0b8e8bf9ce783ade6b3aae79b88e79cb6
#

from apps.models import PublicInfo


class PublicInfoDao:

    def get_data(self, key_name):
        return PublicInfo.query.filter(PublicInfo.name == key_name).first()


