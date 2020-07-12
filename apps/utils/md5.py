# -*- coding:utf-8 -*-
#
# Created Time: 2020/7/19 12:48 上午
# Be From: ZouRi 
# Last Modified: x
# e6b0b8e8bf9ce5b9b4e8bdbbefbc8ce6b0b8e8bf9ce783ade6b3aae79b88e79cb6
#
import hashlib


def get_file_md5(file_data):
    """
    计算文件的md5
    :param file_data: 打开的文件
    :return:
    """
    m = hashlib.md5()   #创建md5对象
    while True:
        data = file_data.read(4096)
        if not data:
            break
        m.update(data)  # 更新md5对象

    # 返回md5对象
    return m.hexdigest()


def get_str_md5(content):
    """
    计算字符串md5
    :param content:
    :return:
    """
    m = hashlib.md5(content) #创建md5对象
    return m.hexdigest()