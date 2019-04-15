from marshmallow import fields

from flask_api_demo.extensions import ma

class UserSchema(ma.Schema):
    name = fields.Str(required=True)
    created_at = fields.Date(required=True)
    _links = ma.Hyperlinks({
        'self': ma.URLFor('api_v1_user.user_detail', user_id='<id>'),
        'collection': ma.URLFor('api_v1_user.user_listing')
    })

user_schema = UserSchema()
users_schema = UserSchema(many=True)
