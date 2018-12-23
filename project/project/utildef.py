# -*- coding: utf-8 -*-

from flask import current_app, request, jsonify, abort, g
from decimal import Decimal
from datetime import datetime


def wrap_jsonify(f):
    """
    对传入的 request.data 做 json 处理 ，
    对传出的 return 值 如果是字典
    做 json 处理

    ---update---
    原来 Flask 有这个 method了，
    使用 request.get_json()
    就好了，还自带检验机制
    所以剩下的就是 对 response wrap 一下
    """
    def decorator(*args, **kwargs):
        rv = f(*args, **kwargs)
        if isinstance(rv, (list, dict)):
            return(jsonify(rv))
        return rv

    decorator.__name__ = f.__name__
    return decorator


def to_dict(inst):
    converter = dict()

    for c in inst.__table__.columns:
        value = getattr(inst, c.name)

        if isinstance(value, datetime):
            value = value.strftime('%Y-%m-%d %H:%M:%S')

        if isinstance(value, Decimal):
            value = str(value)

        converter[c.name] = value

    return converter
