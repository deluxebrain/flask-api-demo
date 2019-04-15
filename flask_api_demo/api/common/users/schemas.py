from marshmallow import fields

from flask_api_demo.extensions import ma

class UserParameter(ma.Schema):
    user_id = fields.Int(required=True)

