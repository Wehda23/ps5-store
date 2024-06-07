"""
# Application that handles the Users API
"""
from flask import Blueprint

# Declare route prefix
url_prefix: str = "/api/users"

# Blueprint
users_api: Blueprint = Blueprint("users", __name__, url_prefix=url_prefix)

# Home page
@users_api.route("/")
def users_test() -> str:
    """
    Checks Users API
    """
    return "Users API"