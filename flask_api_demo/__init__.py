import logging.config

from flask import Flask, Blueprint
from flask_api_demo.extensions import init_app
from flask_api_demo.api.v1 import blueprint as v1_endpoints
# from flask_api_demo.api.v2 import blueprint as v2_endpoints

def create_app():

    # as we are using a package the application object should be given a hardcoded name
    # the following will pull the application name assuming myapp/__init__.py
    app = Flask(__name__.split('.')[0])
    app.register_blueprint(v1_endpoints)
    # app.register_blueprint(v2_endpoints)

    init_app(app)

    return app

