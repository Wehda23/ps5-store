"""
# Application that handles the Users API
"""
from flask import Blueprint, make_response, request
from playstation.models.users import User
from playstation.permissions import permission_required
from .permissions import Permission

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


# Register User API
@users_api.route("/register", methods=['POST'])
def register(*args, **kwargs) -> str:
    """
    Register a new user account API

    Returns:
        str: Success message or error message 400
    """
    # TO DO: Implement user registration logic
    # Get data from request
    data = request.get_json()
    # New user
    user: User = User(**data)
    # Save user
    user.save()
    return "User registration API"


#! This route should be a protected route.
# Update user information API
@users_api.route("/update/<int:pk>", methods=['PUT'])
@permission_required([Permission])
def update_user(pk: int) -> str:
    """
    Update User information API

    Args:
        - pk (int): User Id.

    Returns:
        str: Success message or error message 404
    """
    # TO DO: Implement user update logic
    # Get user by id
    user: User = User.query.get(pk)
    # Check if user exists
    if not user:
        return make_response("User not found", 404)
    # Get data from request
    data = request.get_json()
    # Update user
    user.first_name = data['first_name']
    # Commit changes
    user.save()
    return "User updated successfully"



