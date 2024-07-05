"""
# Initiate Shipping Address Application
"""

from flask import Blueprint

# Declare route prefix
url_prefix: str = "/api/shipping_addresses"

# Blueprint
shipping_addresses_api: Blueprint = Blueprint(
    "shipping_addresses", __name__, url_prefix=url_prefix
)

from . import views
