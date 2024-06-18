"""
# Application that handles the Products API

- This is the application that handles all user related actions such as new account creation, profile updates, registeration, login etc..

## Api routes

##### Protected Routes
- /Products/me: Get the current user's profile
- /Products/me/update: Update the current user's profile
- /Products/me/delete: Delete the current user's account

#### Public Routes
- /Products/register: Register a new user
- /Products/login: Login a user
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
