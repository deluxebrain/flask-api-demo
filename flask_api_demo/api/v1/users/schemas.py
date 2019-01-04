import logging

from flask_api_demo.extensions import ma

log = logging.getLogger(__name__)

class UserSchema(ma.Schema):
    class Meta:
        fields = ('name', 'email', 'created_at', '_links')
    _links = ma.Hyperlinks({
        'self': ma.URLFor('api_v1.user_api', id='<id>'),
        'collection': ma.URLFor('api_v1.user_api')
    })

user_schema = UserSchema()
users_schema = UserSchema(many=True)
