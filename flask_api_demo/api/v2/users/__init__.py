from flask import Blueprint

user_api = Blueprint('api_v2_user', __name__, url_prefix="/api/v2/users")

from . import resources

