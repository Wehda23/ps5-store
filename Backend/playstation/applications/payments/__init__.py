"""
# Initiate Payment Application
"""
from flask import Blueprint

# Declare route prefix
url_prefix: str = "/api/payments"

# Blueprint
payments_api: Blueprint = Blueprint("payments", __name__, url_prefix=url_prefix)

from . import app