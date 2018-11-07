# -*- coding:utf-8 -*-
"""
@author: guoyang
@contact: guoyang_add@163.com
@file: ginger.py
@time: 2018/11/6 1:20 PM
@desc:
"""
__author__ = 'guoyang'

from werkzeug.exceptions import HTTPException

from app import create_app
from app.libs.error import ApiException
from app.libs.error_code import ServerError

app = create_app()


@app.errorhandler(Exception)
def framework_error(e):
    if isinstance(e, ApiException):
        return e
    if isinstance(e, HTTPException):
        code = e.code
        msg = e.description
        error_code = 1007
        return ApiException(msg, code, error_code)
    else:
        # 调试模式
        # log
        if not app.config['DEBUG']:
            return ServerError()
        else:
            raise e


if __name__ == '__main__':
    app.run(debug=True)
