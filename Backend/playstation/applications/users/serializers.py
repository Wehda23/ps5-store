"""
# File the contains Serializers for User Application
"""

from playstation import serializers
from playstation.models.users import User
from playstation.models.blacklisted_tokens import BlackListedTokens
from .validators import EmailValidator, NameValidator, PasswordValidator, IDValidator
from typing import Self
from playstation.admin.authentications.token import get_tokens_for_user


# User Registeration serializer
class UserRegisterSerializer(serializers.Serializer):
    class Meta:
        model: object = User
        fields: list[str] = ["first_name", "email", "last_name", "password"]
        write_only: list[str] = [
            "password",
        ]

    def validate_first_name(self: Self, value: str) -> str:
        """
        Method used to validate the first_name field

        Args:
            - value (str): first_name of the model instance.

        Returns:
            - str: Validated first_name
        """
        # Validate name
        NameValidator().validate(value)
        return value

    def validate_last_name(self: Self, value: str) -> str:
        """
        Method used to validate the last_name field

        Args:
            - value (str): last_name of the model instance.

        Returns:
            - str: Validated last_name
        """
        # Validate name
        NameValidator().validate(value)
        return value

    def validate_password(self: Self, value: str) -> str:
        """
        Method used to validate the password field

        Args:
            - value (str): password address to run password validations through

        Returns:
            - str: Validated password address
        """
        # Validate password
        PasswordValidator().validate(value)
        return value

    def validate_email(self: Self, value: str) -> str:
        """
        Method used to validate the email field

        Args:
            - value (str): email address to run email validations through

        Returns:
            - str: Validated email address
        """
        # Validate Email
        EmailValidator().validate(value)
        # Return Email
        return value

    # Overwrite Create method
    def create(self: Self, validated_data: dict) -> User:
        """
        Method used to create a new User instance
        Args:
            - validated_data (dict): Validated data from the serializer
        Returns:
            - User: New User instance
        """
        return self.model.create_user(**validated_data)


# User Serializer
class UserSerializer(serializers.ModelSerializer):
    """
    User serializer class
    """

    class Meta:
        model: User = User
        fields: list[str] = [
            "id",
            "first_name",
            "last_name",
            "email",
        ]


# User Login Serializer
class LoginSerializer(serializers.Serializer):
    """
    User login serializer class
    """

    class Meta:
        model: User = User
        fields: list[str] = ["email", "password"]

    def validate_password(self: Self, value: str) -> str:
        """
        Method used to validate password
        """
        # Grab email
        email: str = self._data.get("email")
        # Check if user exists
        user: User = self.validate_email(email)

        # Check if password is correct
        if not user.check_password(value):
            raise Exception("Incorrect password")

        # Assign self.instance
        self.instance: User = user

        return value

    def validate_email(self: Self, value: str) -> User:
        """
        Method used to validate email

        Returns:
            - instance of the user
        """
        user: User = self.model.query.filter_by(email=value).first()

        # Check if user exists
        if not user:
            raise Exception("User does not exist")

        return user

    def to_representation(self, instance: User) -> dict:
        """
        Method to get serialized user details
        """
        # Serialize data
        serializer: UserSerializer = UserSerializer(instance)
        # Data
        data: dict = serializer.data
        # Token
        token: dict = get_tokens_for_user(instance)
        # Add token
        data["token"] = token
        # Update last login
        instance.update_last_login()
        # Return data
        return data


# UserUpdateSerializer
class UpdateUserSerializer(serializers.Serializer):
    """
    Serializer for updating user details
    """

    class Meta:
        model: User = User
        fields: list[str] = ["id", "first_name", "last_name", "email"]

    def validate_first_name(self: Self, value: str) -> str:
        """
        Method used to validate the first_name field

        Args:
            - value (str): first_name of the model instance.

        Returns:
            - str: Validated first_name
        """
        # Validate name
        NameValidator().validate(value)
        return value

    def validate_last_name(self: Self, value: str) -> str:
        """
        Method used to validate the last_name field

        Args:
            - value (str): last_name of the model instance.

        Returns:
            - str: Validated last_name
        """
        # Validate name
        NameValidator().validate(value)
        return value

    def validate_email(self: Self, value: str) -> str:
        """
        Method used to validate the email field

        Args:
            - value (str): email address to run email validations through

        Returns:
            - str: Validated email address
        """
        # Validate Email
        EmailValidator().validate(value)
        # Return Email
        return value

    def validate_id(self: Self, value: int) -> int:
        """
        Method used to validate the id field

        Args:
            - value (int): id of the user

        Returns:
            - int: id of the user
        """
        # Validate ID
        IDValidator().validate(value)
        # Return the id
        return value


class BlackListedTokenSerializer(serializers.ModelSerializer):
    """
    Serializer for BlackListedToken model
    """

    class Meta:
        model: BlackListedTokens = BlackListedTokens
        fields: list[str] = ["access", "refresh", "user_id"]


# User Logout Serializer
