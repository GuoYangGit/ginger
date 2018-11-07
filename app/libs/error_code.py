# -*- coding:utf-8 -*-
"""
@author: guoyang
@contact: guoyang_add@163.com
@file: error_code.py
@time: 2018/11/6 1:20 PM
@desc:
"""
from app.libs.error import ApiException

__author__ = 'guoyang'


class Success(ApiException):
    code = 201
    msg = 'ok'
    error_code = 0


class DeleteSuccess(Success):
    code = 202
    error_code = 1


class ServerError(ApiException):
    code = 500
    msg = 'sorry,we made a mistake~'
    error_code = 999


class ClientTypeError(ApiException):
    # 400 参数错误 401 未授权 403 禁止访问 404 没有找到资源
    # 500 未知错误
    # 200 请求成功
    # 301 302 重定向
    code = 400
    msg = 'client is invalid'
    error_code = 1006


class ParameterException(ApiException):
    code = 400
    msg = 'invalid parameter'
    error_code = 1000


class NotFound(ApiException):
    code = 404
    msg = 'the resource are not_found 0_0...'
    error_code = 1001


class AuthFailed(ApiException):
    code = 401
    error_code = 1005
    msg = 'authorzation failed'


class Forbidden(ApiException):
    code = 403
    error_code = 1004
    msg = 'forbidden,not in scope'
