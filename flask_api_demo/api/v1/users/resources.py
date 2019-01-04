import logging

from flask import jsonify
from flask.views import MethodView

from flask_api_demo.api.v1 import blueprint as v1_endpoints
from flask_api_demo.api.v1.users.models import User
from flask_api_demo.api.v1.users.schemas import user_schema, users_schema

log = logging.getLogger(__name__)

class UserAPI(MethodView):

    def get(self, id):
        if id is None:
            all_users = [
                User(name="Bob", email="bob@example.com"),
                User(name="Pat", email="pat@example.com")
            ]
            return users_schema.jsonify(all_users)
        else:
            the_user = User(name="Bob", email="bob@example.com")
            return user_schema.jsonify(the_user)

user_view = UserAPI.as_view('user_api')
v1_endpoints.add_url_rule('/users/',
    defaults={'id': None},
    view_func=user_view, methods=['GET'])
v1_endpoints.add_url_rule('/users/<int:id>',
    view_func=user_view, methods=['GET'])
