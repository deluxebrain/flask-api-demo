from flask import Blueprint

user_api = Blueprint('api_v1_user', __name__, url_prefix="/api/v1/users")

from . import resources

