"""
# File that contains permissions required for this application
"""

from playstation.admin.permissions import BasePermission
from playstation.models.users import User
from playstation.models.shipping_address import ShippingAddress
from typing import Self, Optional
from flask import Request


# Create Permission Class
class IsAddressOwner(BasePermission):
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
        user: Optional[User] = getattr(request, "user", None)
        # Check if user exists
        if user is None:
            return False
        # Grab address_id
        address_id = kwargs.get("address_id", None)
        # Check if address_id exists
        if address_id is None:
            return False

        shipping_address: ShippingAddress = ShippingAddress.query.get(address_id)

        if shipping_address is None:
            return False

        # Check if user pk id is same as request.user id
        return shipping_address.user_id == user.id
