# -*- coding:utf-8 -*-
#
# Created Time: 2020/4/19 8:59 下午
# Be From: ZouRi 
# Last Modified: x
# e6b0b8e8bf9ce5b9b4e8bdbbefbc8ce6b0b8e8bf9ce783ade6b3aae79b88e79cb6
#
from flask import Blueprint
from flask_restful import Api

from apps.user.api import *
from apps.document.api import *
from apps.column.api import *
from apps.media.api import *
from apps.extras.api import *


ApiManager = Blueprint('ApiManager', __name__, url_prefix='/apps/api')


_api = Api(ApiManager)


# 验证码
_api.add_resource(ImageCode, '/verify/img')

# 用户管理,登陆,注销注册
_api.add_resource(UserManager, '/user')
_api.add_resource(UserLogin, '/user/login')
_api.add_resource(UserLogout, '/user/logout')
_api.add_resource(UserRegister, '/user/register')
_api.add_resource(UserInfo, '/user/<string:username>')

# 获取菜单
_api.add_resource(UserNavColumns, '/user/column/nav')


# 文章相关
_api.add_resource(DocumentsManager, '/document')
_api.add_resource(DocumentManager, '/document/<string:doc_id>')
# _api.add_resource(ArticleUpdate, '/article/<int:article_id>/<string:attr>')


# 媒体管理
_api.add_resource(MediaManager, '/media')
_api.add_resource(MediaUpload, '/media/upload')
_api.add_resource(BannersManager, '/media/banners')
_api.add_resource(BannerManager, '/media/banner/<int:banner_id>')


# 栏目相关
_api.add_resource(ColumnsManager, '/column')
_api.add_resource(ColumnManager, '/column/<string:column_name>')
