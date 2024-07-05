"""
# Validator Model for Shipping Addresses Serializers Package
"""

from playstation.admin.validators import BaseValidator
from playstation.models.users import User
from playstation.models.shipping_address import ShippingAddress
from typing import Optional, NoReturn


# Validate user exists
class UserExists(BaseValidator):
    def validate(self, value: Optional[int]) -> Optional[NoReturn]:
        """
        Validate user exists
        :param value: user id
        :Raises: ValueError: User does not exists
        :return: True if user exists
        """
        if value is None or int(value) < 0:
            raise self.raise_exception(ValueError, "Invalid ID")

        if not User.query.filter_by(id=value).first():
            raise self.raise_exception(ValueError, "User not found")


# Validate if an existing default address exists
class DefaultAddressExists(BaseValidator):

    def get_user(self, user_id) -> User:
        """
        Get user
        """
        return User.query.get(user_id)

    def validate(self, value: Optional[int]) -> Optional[ShippingAddress]:
        """
        Validate if an existing default address exists
        :param value: user id
        :return: Existing default address otherwise None
        """
        # Grab the user
        user: User = self.get_user(value)
        # Check existing default
        # Existing Default
        existing_default: ShippingAddress = next(
            (addr for addr in user.shipping_addresses if addr.default),
            None,  # Default value after interation ends
        )
        # Check if default exists
        if existing_default is not None:
            return existing_default
        # Returns none automatically
        return None


# Shipping Address Exists
class ShippingAddressExists(BaseValidator):
    def validate(self, data: dict) -> Optional[NoReturn]:
        """
        Validate if an existing shipping address exists
        :param data: shipping address data
        :return: Existing shipping address otherwise None
        """
        # Grab the user
        user_id: User = data.get("user_id")
        # address id
        address_id: int = data.get("id")
        # Grab Shipping address
        shipping_address: ShippingAddress = ShippingAddress.query.filter_by(
            id=address_id
        ).first()
        # Check if shipping address exists
        if not shipping_address:
            raise self.raise_exception(ValueError, "Shipping Address not found")
        # Check if the user is the owner of the address
        if shipping_address.user_id != user_id:
            raise self.raise_exception(
                ValueError, "Shipping Address not found among User Addresses"
            )
