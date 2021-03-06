import logging
from flask import jsonify

log = logging.getLogger(__name__)

from flask_api_demo import app
from flask_api_demo.api.v1.users import user_api
from flask_api_demo.api.common.users.models import User
from flask_api_demo.api.common.users.schemas import UserParameter
from flask_api_demo.api.v1.users.schemas import users_schema, user_schema
from flask_api_demo.extensions import spec_v1 as spec

@user_api.route('/')
def user_listing():
    """User listing view.
    ---
    get:
        description: Get user listing
        responses:
            200:
                description: User listing
                schema: UserSchema
    """
    users = [ User(name="Bob") ]
    return users_schema.jsonify(users)

@user_api.route('/<user_id>')
def user_detail(user_id):
    """User detail view.
    ---
    get:
        description: Get user by id
        parameters:
            - in: user_id
              schema: UserParameter
        responses:
            200:
                description: The specified user
                schema: UserSchema
    """
    the_user = User(name="Bob")
    return user_schema.jsonify(the_user)

app.register_blueprint(user_api)

with app.test_request_context():
    spec.path(view=user_listing)
    spec.path(view=user_detail)