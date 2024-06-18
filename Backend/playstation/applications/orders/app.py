"""
# Application that handles the Orders API

- This is the application that handles all user related actions such as new account creation, profile updates, registeration, login etc..

## Api routes

##### Protected Routes
- /Orders/me: Get the current user's profile
- /Orders/me/update: Update the current user's profile
- /Orders/me/delete: Delete the current user's account

#### Public Routes
- /Orders/register: Register a new user
- /Orders/login: Login a user
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
