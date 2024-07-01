"""
# Application to handle Payments
"""

from flask import current_app, make_response, request, Response
from playstation.admin.permissions import permission_required
from playstation.admin.authentications import authentication_classess
from . import payments_api


# Test API
@payments_api.route("/", methods=["GET"])
def base(*args, **kwargs) -> Response:
    """ """
    return "Payments API"
