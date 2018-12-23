# -*- coding: utf-8 -*-

import os
import logging


basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:1234@localhost/creditstu'
    # 上面的配置 url 要根据自己的mysql 情况而定
    SECRET_KEY = 'kiso@$*333^2si89%)$'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    LOGGING_FORMAT = '%(asctime)s %(levelname)s:%(message)s [in %(pathname)s:%(lineno)d]'
    LOGGING_LOCATION = os.path.dirname(basedir) + '.log'
    LOGGING_LEVEL = logging.DEBUG
