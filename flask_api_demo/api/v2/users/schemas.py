from marshmallow import fields

from flask_api_demo.extensions import ma
from flask_api_demo.api.v1.users.schemas import UserSchema

class UserSchema2(UserSchema):
    email = fields.Email(required=True)

user_schema = UserSchema2()
users_schema = UserSchema2(many=True)
