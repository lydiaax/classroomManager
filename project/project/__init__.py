# -*- coding: utf-8 -*-

from __future__ import absolute_import
from flask import Flask
from flask_migrate import Migrate
import logging
from .models import db
from .config import Config

def after_request(response): 
    response.headers['Access-Control-Allow-Origin'] = '*'            
    response.headers['Access-Control-Allow-Methods'] = 'PUT,GET,POST,DELETE' 
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type,Authorization' 
    return response 


def create_app():
    app = Flask(__name__)
    app.after_request(after_request)
    app.config.from_object(Config)

    db.init_app(app)
    Migrate(app, db)

    # Configure logging
    handler = logging.FileHandler(app.config['LOGGING_LOCATION'])
    handler.setLevel(app.config['LOGGING_LEVEL'])
    formatter = logging.Formatter(app.config['LOGGING_FORMAT'])
    handler.setFormatter(formatter)
    app.logger.addHandler(handler)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint, url_prefix='/main')

    return app
