import logging
from flask import jsonify

log = logging.getLogger(__name__)

from flask_api_demo.api.v2 import api
from flask_api_demo import app
from flask_api_demo.extensions import spec_v2 as spec

@api.route('/swagger')
def get_swagger():
    return jsonify(spec.to_dict())

app.register_blueprint(api)
