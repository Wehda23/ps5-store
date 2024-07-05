"""
# Initiate Orders Application
"""

from flask import Blueprint

# Declare route prefix
url_prefix: str = "/api/orders"

# Blueprint
orders_api: Blueprint = Blueprint("orders_api", __name__, url_prefix=url_prefix)

from . import views
