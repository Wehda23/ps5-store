"""
# Application to handle Payments
"""

from flask import Blueprint, make_response, request, Response
from playstation.admin.permissions import permission_required
from playstation.admin.authentications import authentication_classess


# Declare route prefix
url_prefix: str = "/api/payments"

# Blueprint
payments_api: Blueprint = Blueprint("payments", __name__, url_prefix=url_prefix)


# Test API
@payments_api.route("/", methods=["GET"])
def base(*args, **kwargs) -> Response:
    """ """
    return "Payments API"
