from flask import Blueprint

api = Blueprint('api_v2', __name__, url_prefix="/api/v2")

from . import resources
from . import users
