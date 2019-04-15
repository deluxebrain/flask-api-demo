import os
from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from apispec_webframeworks.flask import FlaskPlugin
from flask_marshmallow import Marshmallow
from config import config_map

ma = Marshmallow()

spec_v1 = APISpec(
   title='Flask Api One-Pager Demo',
   version='1.0.0',
   openapi_version='3.0.2',
   plugins=[
      FlaskPlugin(),
      MarshmallowPlugin(),
   ]
)

spec_v2 = APISpec(
   title='Flask Api One-Pager Demo',
   version='2.0.0',
   openapi_version='3.0.2',
   plugins=[
      FlaskPlugin(),
      MarshmallowPlugin(),
   ]
)

def init_app(app):

    # Marshmallow
    ma.init_app(app)

    # Configuration
    config = config_map[os.getenv('FLASK_CONFIG') or 'default']
    app.config.from_object(config)
    config.init_app(app)
