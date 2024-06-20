"""
# File that contains permissions required for this application
"""

from playstation.admin.permissions import BasePermission
from playstation.models.users import User
from typing import Self, Optional
from flask import Request


# Create Permission Class
class IsAccountOwner(BasePermission):
    """
    Class Created to demonstrated permission classes
    """

    def has_permission(self: Self, request: Request, *args, **kwargs) -> bool:
        """
        Main method to handle permissions

        Args:
            - request (Request): Flask Request Class Handler.

        Returns:
            - bool: True in case satisfies all permissions otherwise False
        """
        # grab request user
        user: Optional[User] = getattr(request, 'user', None)
        # Check if user exists
        if user is None:
            return False
        # Check if user pk id is same as request.user id
        return kwargs.get("pk", None) == user.id
