"""
# File contains all permission classes required for products application
"""

from playstation.admin.permissions import BasePermission
from playstation.models.users import User
from typing import Self, Optional, Any
from flask import Request


# Class IsAdmin
class IsAdmin(BasePermission):
    """
    Permission class to check if the user is an admin
    """

    def has_permission(self: Self, request: Request, *args: Any, **kwargs: Any) -> bool:
        """
        Method to check if the user is an admin
        Args:
            request (Request): The request object
            *args (Any): Additional arguments
            **kwargs (Any): Additional keyword arguments
        Returns:
            bool: True if the user is an admin, False otherwise
        """
        # Grab user
        user: Optional[User] = request.user
        # Validate that the user is an admin
        return user is not None and user.is_admin and user.active
