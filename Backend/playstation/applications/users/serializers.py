"""
# File the contains Serializers for User Application
"""

from playstation import serializers
from playstation.models.users import User
from typing import Self


# User Registeration serializer
class UserRegisterSerializer(serializers.Serializer):
    class Meta:
        model: object = User
        fields: list[str] = ["first_name", "email", "last_name", "password"]

    def validate_first_name(self: Self, value: str) -> str:
        """
        Method used to validate the first_name field

        Args:
            - value (str): first_name of the model instance.

        Returns:
            - Validated first_name
        """
        return value
