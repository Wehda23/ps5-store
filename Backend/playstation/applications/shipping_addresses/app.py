"""
# Application to handle Shipping Addresses
"""

from flask import Blueprint, make_response, request, Response
from playstation.admin.permissions import permission_required
from playstation.admin.authentications import authentication_classess


# Declare route prefix
url_prefix: str = "/api/shipping_addresses"

# Blueprint
shipping_addresses_api: Blueprint = Blueprint("shipping_addresses", __name__, url_prefix=url_prefix)

# Test API
@shipping_addresses_api.route("/", methods=["GET"])
def base(*args, **kwargs) -> Response:
    """
    """
    return "Shipping addresses API"
