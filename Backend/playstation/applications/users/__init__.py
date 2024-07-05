"""
Initiate logger for Flask Blueprint application
"""

from flask import Blueprint
from playstation.settings import LOGGING_COFIGURATION

# Declare route prefix
url_prefix: str = "/api/users"

# Blueprint
users_api: Blueprint = Blueprint("users", __name__, url_prefix=url_prefix)

from . import views
