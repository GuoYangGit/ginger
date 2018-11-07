# -*- coding:utf-8 -*-
"""
@author: guoyang
@contact: guoyang_add@163.com
@file: fake.py
@time: 2018/11/6 4:32 PM
@desc:
"""
from app import create_app
from app.models.base import db
from app.models.user import User

__author__ = 'guoyang'

app = create_app()
with app.app_context():
    with db.auto_commit():
        # 创建一个超级管理员
        user = User()
        user.nickname = 'Super'
        user.password = '123456'
        user.email = '999@qq.com'
        user.auth = 2
        db.session.add(user)
