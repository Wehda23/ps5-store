"""
# Application that handles the Users API

- This is the application that handles all user related actions such as new account creation, profile updates, registeration, login etc..

## Api routes

##### Protected Routes
- /users/me: Get the current user's profile
- /users/me/update: Update the current user's profile
- /users/me/delete: Delete the current user's account

#### Public Routes
- /users/register: Register a new user
- /users/login: Login a user
"""

from flask import Blueprint, make_response, request, Response
from playstation.models.users import User
from playstation.models.error_handlers import ExistingEmail
from playstation.admin.permissions import permission_required
from playstation.admin.authentications.jwt_authentication import (
    JWTAuthentication,
    RefreshTokenAuthentication,
)
from playstation.admin.authentications.token import get_tokens_for_user
from playstation.admin.authentications import authentication_classess
from .permissions import Permission
from .serializers import UserRegisterSerializer, LoginSerializer

# Declare route prefix
url_prefix: str = "/api/users"

# Blueprint
users_api: Blueprint = Blueprint("users", __name__, url_prefix=url_prefix)


# Register User API
@users_api.route("/register", methods=["POST"])
def register(*args, **kwargs) -> Response:
    """
    Register a new user account API

    Returns:
        str: Success message or error message 400
    """
    # Get data from request
    data = request.get_json()
    # Create serializer
    serializer: UserRegisterSerializer = UserRegisterSerializer(data=data)
    try:
        # Validate data
        if serializer.is_valid():
            # Create user
            serializer.save()
            return make_response("Successful Registeration", 201)
        error: list[str] = serializer.errors
        return make_response(error, 403)
    except ExistingEmail as e:
        return make_response("Email is already registered", 409)
    except Exception as e:
        # Write Logic to check registeration failed through logs functionality
        error: str = str(e)
        # Record Error Through logs
        # Return a response `Registeration Failed`
        return make_response("Registeration Failed", 400)


# Login User API
@users_api.route("/login", methods=["POST"])
def login(*args, **kwargs) -> Response:
    """
    Login user API
    """
    # Data
    data: dict = request.get_json()
    # Check if user exists
    serializer: LoginSerializer = LoginSerializer(data=data)
    # if user and user.check_password(data.get("password")):
    if serializer.is_valid():
        # Generate Token
        return make_response(serializer.data, 201)

    error: str = serializer.errors
    return make_response(error, 404)


#! This route should be a protected route.
# Update user information API
@users_api.route("/update/<int:pk>", methods=["PUT"])
@authentication_classess([JWTAuthentication])
@permission_required([Permission])
def update_user(pk: int) -> Response:
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
    user.first_name = data["first_name"]
    # Commit changes
    user.save()
    return "User updated successfully"


# Refresh token api
@users_api.route("/refresh", methods=["POST"])
@authentication_classess([RefreshTokenAuthentication])
def refresh_token(*args, **kwargs) -> Response:
    """
    Refresh token API
    """
    return "Refresh token API"


# Reset Password Mechanisim
