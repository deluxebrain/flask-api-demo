import datetime as dt

class User(object):
    def __init__(self, name):
        self.id = 1
        self.name = name
        self.created_at = dt.datetime.now()

    def __repr__(self):
        return '<User(name={self.name!r})>'.format(self=self)
