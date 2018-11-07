# -*- coding:utf-8 -*-
"""
@author: guoyang
@contact: guoyang_add@163.com
@file: book.py
@time: 2018/11/6 1:20 PM
@desc:
"""
from app.libs.redprint import Redprint
from app.validators.forms import BookSearchForm

__author__ = 'guoyang'

api = Redprint('book')


@api.route('/search')
def search_book():
    form = BookSearchForm().validate_for_api()
    q = form.q.data
    return q
