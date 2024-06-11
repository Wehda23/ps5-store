"""
# Application that handles the Orders API
"""

from flask import Blueprint


# Declare route prefix
url_prefix: str = "/api/orders"

# Blueprint
orders_api: Blueprint = Blueprint("orders_api", __name__, url_prefix=url_prefix)


# Test API
@orders_api.route("", methods=["GET"])
def orders_test() -> str:
    """
    Check orders API
    """
    return "Orders API is working!"
