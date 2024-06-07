"""
# Application that handles the products API
"""
from flask import Blueprint


# Declare route prefix
url_prefix: str = "/api/products"

# Blueprint
products_api: Blueprint = Blueprint("products_api", __name__, url_prefix=url_prefix)


# Test API
@products_api.route("", methods=["GET"])
def products_test() -> str:
    """
    Check products API
    """
    return "Products API is working!"