"""
# Application to handle Shipping Addresses
"""

from flask import current_app, make_response, request, Response
from playstation.admin.permissions import permission_required
from playstation.admin.authentications import authentication_classess
from . import shipping_addresses_api




# Test API
@shipping_addresses_api.route("/", methods=["GET"])
def base(*args, **kwargs) -> Response:
    """ """
    return "Shipping addresses API"
