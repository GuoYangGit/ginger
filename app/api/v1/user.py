# -*- coding:utf-8 -*-
"""
@author: guoyang
@contact: guoyang_add@163.com
@file: user.py
@time: 2018/11/6 1:20 PM
@desc:
"""
from flask import jsonify, g

from app.libs.error_code import DeleteSuccess
from app.models.base import db
from app.models.user import User
from app.libs.redprint import Redprint
from app.libs.token_auth import auth

__author__ = 'guoyang'

api = Redprint('user')


@api.route('/<int:uid>', methods=['GET'])
@auth.login_required
def super_get_user(uid):
    user = User.query.get_or_404(uid)
    return jsonify(user)


@api.route('', methods=['GET'])
@auth.login_required
def get_user():
    uid = g.user.uid
    user = User.query.filter_by(id=uid).first_or_404()
    return jsonify(user)


# 管理员
@api.route('/<int:uid>', methods=['DELETE'])
def super_delete_user(uid):
    pass


@api.route('', methods=['DELETE'])
@auth.login_required
def delete_user():
    uid = g.user.uid
    with db.auto_commit():
        user = User.query.filter_by(id=uid).first_or_404()
        user.delete()
    return DeleteSuccess()
