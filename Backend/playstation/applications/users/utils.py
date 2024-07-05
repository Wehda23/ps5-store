"""
# Module contains function for extra utilies concerning User
"""
from playstation.admin.authentications.exceptions import UserNotAssignedError
from playstation.models.users import User
from flask import Request


def get_request_user(request: Request) -> User:
    """Get user from request"""
    user: User = getattr(request, "user", None)
    if user is None:
        raise UserNotAssignedError("User not assigned to request")
    return user