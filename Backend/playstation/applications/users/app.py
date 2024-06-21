"""
Application that handles the Users API

This application manages all user-related actions, including account creation, profile updates, registration, login, and token refresh. It defines API routes to facilitate these actions, ensuring secure and efficient user management.

## API Routes

### Protected Routes
These routes require authentication and appropriate permissions to access:

- **/api/users/update/<id>: Update the current user's profile.
  - Method: PUT
  - Description: Allows authenticated users to update their profile information.
  - Authentication: JWT required
  - Permissions: Specific user permissions required

- **/api/users/refresh: Generate new access/refresh tokens for the user.
  - Method: POST
  - Description: Provides new JWT tokens to authenticated users for session continuity.
  - Authentication: Refresh token required

- **/api/users/logout: Adds the current user's access and refresh tokens to the blacklist to prevent further use.
  - Method: POST
  - Description: Adds authentication tokens of the current user to blacklisted tokens
  - Authentication: JWT required

### Public Routes
These routes are accessible without authentication:

- **/api/users/register: Register a new user.
  - Method: POST
  - Description: Allows new users to create an account by providing necessary details.
  - Request Data: User details (e.g., first_name, last_name, email, password)
  - Response: Success or error message

- **/api/users/login: Login a user.
  - Method: POST
  - Description: Authenticates a user and provides JWT tokens for session management.
  - Request Data: User credentials (email and password)
  - Response: JWT tokens or error message
"""

from flask import Blueprint, make_response, request, Response
from playstation.models.error_handlers import ExistingEmail
from playstation.admin.permissions import permission_required
from playstation.admin.authentications.jwt_authentication import (
    JWTAuthentication,
    RefreshTokenAuthentication,
)
from playstation.admin.authentications.token import get_tokens_for_user
from playstation.admin.authentications import authentication_classess
from .permissions import IsAccountOwner
from .serializers import UserRegisterSerializer, LoginSerializer, UpdateUserSerializer, BlackListedTokenSerializer


# Declare route prefix
url_prefix: str = "/api/users"

# Blueprint
users_api: Blueprint = Blueprint("users", __name__, url_prefix=url_prefix)


# Register User API
@users_api.route("/register", methods=["POST"])
def register(*args, **kwargs) -> Response:
    """
    Register a new user account API

    Handles the registration of new users by validating the provided data and
    creating a new user account.

    Returns:
        Response: A success message with status 201 if registration is successful,
                  otherwise an error message with the appropriate status code.
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

    Authenticates the user using provided credentials and returns JWT tokens
    if the login is successful.

    Returns:
        Response: A response with JWT tokens if authentication is successful,
                  otherwise an error message with status 404.
    """
    # Data
    data: dict = request.get_json()
    # Check if user exists
    serializer: LoginSerializer = LoginSerializer(data=data)
    try:
        if serializer.is_valid():
            # Generate Token
            return make_response(serializer.data, 201)
        # Grab Error
        error: str = serializer.errors
        return make_response(error, 404)
    except Exception as e:
        # record error in a logging class
        error: str = str(e)
        return make_response("Login Failed", 404)


# Update user information API
@users_api.route("/update/<int:pk>", methods=["PUT"])
@authentication_classess([JWTAuthentication])
@permission_required([IsAccountOwner])
def update_user(pk: int) -> Response:
    """
    Update User information API

    Allows authenticated users to update their profile information.

    Args:
        pk (int): User ID.

    Returns:
        Response: A success message if the update is successful,
                  otherwise an error message with status 404.
    """
    # Data
    data: dict = request.get_json()
    # Set the id for the user
    data["id"] = pk
    # serializer
    serializer: UpdateUserSerializer = UpdateUserSerializer(data=data)
    try:
        if serializer.is_valid():
            # Update User
            serializer.save()
            # Returns updated user details with out without any token modifications
            return make_response(serializer.data, 200)
        # Grab Error
        error: str = serializer.errors
        return make_response(error, 404)
    except Exception as e:
        # Add error message to a logger class to track bugs
        error: str = str(e)
        return make_response("Failed to update user", 404)


# Refresh token api
@users_api.route("/refresh", methods=["POST"])
@authentication_classess([RefreshTokenAuthentication])
def refresh_token(*args, **kwargs) -> Response:
    """
    Refresh token API

    Generates new access and refresh tokens for authenticated users.

    Returns:
        Response: New JWT tokens.
    """
    # Get Data
    data: dict = request.get_json()
    # get user id
    data['user_id'] = request.user.id
    # We have to add the current refresh token and access token to blacklisted token
    serializer: BlackListedTokenSerializer = BlackListedTokenSerializer(data=data)
    try:
        if serializer.is_valid():
            # Blacklist the current token
            serializer.save()
            # Generate new tokens
            token: dict[str, str] = get_tokens_for_user(request.user)
            # Return new tokens
            return make_response(token, 201)
        error: list = serializer.errors
        return make_response(error, 404)
    except Exception as e:
        # Add error message to a logger class to track bugs
        error: str = str(e)
        return make_response("Failed to refresh token", 404)


# Logout API
@users_api.route("/logout", methods=["POST"])
@authentication_classess([JWTAuthentication])
def logout(*args, **kwargs) -> Response:
    """
    Logout API

    Generates new access and refresh tokens for authenticated users.

    Returns:
        Response: Message of a success logout process.
    """
    # Get data
    data: dict = request.get_json()
    # get user id
    data['user_id'] = request.user.id
    # Blacklist serializer
    serializer: BlackListedTokenSerializer = BlackListedTokenSerializer(data=data)
    try:
        if serializer.is_valid():
            # Blacklist the current token
            serializer.save()
            return make_response("Logged out successfully", 200)
        error: list = serializer.errors
        return make_response(error, 404)
    except Exception as e:
        # Add error message to a logger class to track bugs
        error: str = str(e)
        print(e)
        return make_response("Failed to logout", 404)


# Reset Password Mechanisim
