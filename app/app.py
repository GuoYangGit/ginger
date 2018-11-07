# -*- coding:utf-8 -*-
"""
@author: guoyang
@contact: guoyang_add@163.com
@file: app.py
@time: 2018/11/6 1:20 PM
@desc:
"""
from datetime import date
from flask import Flask as _Flask
from flask.json import JSONEncoder as _JSONEncoder

from app.libs.error_code import ServerError

__author__ = 'guoyang'


class JSONEncoder(_JSONEncoder):
    def default(self, o):
        if hasattr(o, 'keys') and hasattr(o, '__getitem__'):
            return dict(o)
        if isinstance(o, date):
            return o.strftime('%Y-%m-%d')
        else:
            raise ServerError()


class Flask(_Flask):
    json_encoder = JSONEncoder
