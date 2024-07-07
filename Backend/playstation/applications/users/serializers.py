"""
# File that contains Serializers for User Application

This module defines serializers used in the user application for various user-related operations such as registration, login, updating user details, and managing blacklisted tokens. These serializers are responsible for validating input data, ensuring data integrity, and facilitating data serialization and deserialization processes.

Classes:
    - UserRegisterSerializer: Serializer for registering a new user.
    - UserSerializer: Serializer for basic user details.
    - LoginSerializer: Serializer for user login.
    - UpdateUserSerializer: Serializer for updating user details.
    - BlackListedTokenSerializer: Serializer for blacklisted tokens.

Modules:
    - serializers: Imported from playstation, used for creating custom and model serializers.
    - models.users: Contains the User model.
    - models.blacklisted_tokens: Contains the BlackListedTokens model.
    - validators: Custom validators for email, name, password, and ID fields.
    - admin.authentications.token: Contains the function to generate authentication tokens for a user.
"""
from playstation import serializers
from playstation.models.users import User
from playstation.models.blacklisted_tokens import BlackListedTokens
from .validators import EmailValidator, NameValidator, PasswordValidator, IDValidator
from typing import Self
from playstation.admin.authentications.token import get_tokens_for_user
from playstation.applications.shipping_addresses.serializers import (
    ShippingAddressSerializer,
)


# User Registeration serializer
class UserRegisterSerializer(serializers.Serializer):
    """
    Serializer for registering a new user. Validates user input and creates a new User instance.

    Meta:
        model: User model to be serialized.
        fields: List of fields to be serialized.
        write_only: List of fields to be used for write operations only.

    Methods:
        validate_first_name(value): Validates the first name using NameValidator.
        validate_last_name(value): Validates the last name using NameValidator.
        validate_password(value): Validates the password using PasswordValidator.
        validate_email(value): Validates the email using EmailValidator.
        create(validated_data): Creates a new User instance with the validated data.
    """

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
        NameValidator(serializers.SerializerError).validate(value)
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
        NameValidator(serializers.SerializerError).validate(value)
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
        PasswordValidator(serializers.SerializerError).validate(value)
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
        EmailValidator(serializers.SerializerError).validate(value)
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
    Serializer for basic user details.

    Meta:
        model: User model to be serialized.
        fields: List of fields to be serialized.
    """

    # shipping_addresses: ShippingAddressSerializer = ShippingAddressSerializer(many=True) # Nested Serializer Example to get user's all addresses
    class Meta:
        model: User = User
        fields: list[str] = [
            "id",
            "first_name",
            "last_name",
            "email",
            "shipping_addresses",
        ]


# User Login Serializer
class LoginSerializer(serializers.Serializer):
    """
    Serializer for user login. Validates user credentials and returns user details with authentication token.

    Meta:
        model: User model to be serialized.
        fields: List of fields to be serialized.

    Methods:
        validate_password(value): Validates the password by checking if it matches the user's password.
        validate_email(value): Validates the email and checks if the user exists.
        to_representation(instance): Serializes user details and adds authentication token to the data.
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
        self.validate_email(email)

        # Check if password is correct
        if not self.instance.check_password(value):
            raise serializers.SerializerError(ValueError, "Incorrect password")

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
            raise serializers.SerializerError(ValueError, "User does not exist")

        # Assign self.instance
        self.instance: User = user

        return value

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

    def save(self, *args, **kwargs) -> None:
        """
        We need to override parent .save() method to avoid any error
        As this serializer was only meant to validated login infromation
        """
        pass


# UserUpdateSerializer
class UpdateUserSerializer(serializers.Serializer):
    """
    Serializer for updating user details. Validates and updates user information.

    Meta:
        model: User model to be serialized.
        fields: List of fields to be serialized.

    Methods:
        validate_first_name(value): Validates the first name using NameValidator.
        validate_last_name(value): Validates the last name using NameValidator.
        validate_email(value): Validates the email using EmailValidator.
        validate_id(value): Validates the user ID using IDValidator.
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
        NameValidator(serializers.SerializerError).validate(value)
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
        NameValidator(serializers.SerializerError).validate(value)
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
        EmailValidator(serializers.SerializerError).validate(value)
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
        IDValidator(serializers.SerializerError).validate(value)
        # Return the id
        return value


class BlackListedTokenSerializer(serializers.ModelSerializer):
    """
    Serializer for BlackListedTokens model. Manages the serialization and deserialization of blacklisted tokens.

    Meta:
        model: BlackListedTokens model to be serialized.
        fields: List of fields to be serialized.
    """

    class Meta:
        model: BlackListedTokens = BlackListedTokens
        fields: list[str] = ["access", "refresh", "user_id"]
