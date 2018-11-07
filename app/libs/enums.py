# -*- coding:utf-8 -*-
"""
@author: guoyang
@contact: guoyang_add@163.com
@file: enums.py
@time: 2018/11/6 1:20 PM
@desc:
"""
from enum import Enum

__author__ = 'guoyang'


class ClientTypeEnum(Enum):
    USER_EMAIL = 100
    USER_MOBILE = 101

    USER_MINA = 200
    USER_WX = 201
