import logging.config
from flask import Flask

app = Flask(__name__.split('.')[0])

from flask_api_demo.extensions import init_app
import flask_api_demo.api.v1
import flask_api_demo.api.v2

def create_app():

    init_app(app)
    return app
