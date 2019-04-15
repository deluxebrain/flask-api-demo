import datetime as dt
from flask_api_demo.api.common.users.models import User

class User2(User):
    def __init__(self, name, email):
        User.__init__(self, name)
        self.email = email

    def __repr__(self):
        return '<User(name={self.name!r})>'.format(self=self)
