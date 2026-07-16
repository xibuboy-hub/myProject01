# -*- coding: utf-8 -*-
"""
**************************************
*  @Author  ：   Joy_Lo
*  @Time    ：   2025/2/5 上午 08:50
*  @Project :   demo01
*  @FileName:   wrapper.py
**************************************
程式用途:检测用户是否登录
"""

from functools import wraps
from flask import session, redirect, url_for, request


def login_reguired(f):
    @wraps(f)
    def wrapper_func(*args, **kwargs):
        # 确认是否登录
        if 'username' not in session:
            session['next'] = request.url  # 存储当前URL
            return redirect(url_for("admin.login"))
        return f(*args, **kwargs)

    return wrapper_func
