"""
# File that contains permissions required for this application
"""
from playstation.permissions import BasePermission
from typing import Self
from flask import Request


# Create Permission Class
class Permission(BasePermission):
    """
    Class Created to demonstrated permission classes
    """
    def has_permission(self: Self, request: Request, *args, **kwargs) -> bool:
        """
        Main method to handle permissions

        Args:
            - request (Request): Flask Request Class Handler.

        Returns:
            - True in case satisfies all permissions otherwise False
        """
        print(request.get_json())
        return True

