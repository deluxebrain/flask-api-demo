import os

from flask_marshmallow import Marshmallow
from config import config_map

ma = Marshmallow()

def init_app(app):

    # Marshmallow
    ma.init_app(app)

    # Configuration
    config = config_map[os.getenv('FLASK_CONFIG') or 'default']
    app.config.from_object(config)
    config.init_app(app)
