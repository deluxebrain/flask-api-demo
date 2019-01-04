import logging

from flask import Blueprint

log = logging.getLogger(__name__)

blueprint = Blueprint('api_v1', __name__, url_prefix="/api/v1")

from . import users
