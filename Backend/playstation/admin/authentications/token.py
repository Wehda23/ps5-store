"""
# Module contains all classes and functions related to tokens
"""

import jwt
from datetime import datetime, timezone
from typing import Self, Optional, Union
from playstation.settings import JWT_AUTHENTICATIONS
from playstation.models.users import User


# Token class
class Token:
    """
    class to store a token
    """

    def __init__(self, access_token: str = None, refresh_token: str = None) -> None:
        """
        Method used when a new instance is initialized
        """
        self.access_token: str = access_token
        self.refresh_token: str = refresh_token


class TokenUtility:
    """
    Utility class for handling token operations.
    """

    @staticmethod
    def has_id_attribute(model: object, id: str = "id") -> bool:
        """
        Check if the model has an id attribute.

        Args:
            - model (object): Model instance
            - id (str): Attribute name to check

        Returns:
            - bool: True if model has id attribute, False otherwise
        """
        return hasattr(model, id)


# Refresh Token Class
class RefreshToken:
    """
    Class used to generate both access token and refresh token
    """

    # Create method to generate access token
    @staticmethod
    def create_access_token(model: object, id: str = "id") -> str:
        """
        Generate an access token.

        Args:
            - model (object): Model instance to use as payload for the token
            - id (str): Attribute name for the id

        Returns:
            - str: Generated access token
        """
        # Check id
        if not TokenUtility.has_id_attribute(model, id):
            raise ValueError("Model instance must have an id attribute")
        # Payload
        payload: dict[str, str] = {
            f"{model.__class__.__name__}": getattr(model, id),
            "type": "access",
            "exp": datetime.now(timezone.utc)
            + JWT_AUTHENTICATIONS["ACCESS_TOKEN_LIFETIME"],
        }
        # Generate token
        access_token: str = jwt.encode(
            payload,
            key=JWT_AUTHENTICATIONS["SECRET_KEY"],
            algorithm=JWT_AUTHENTICATIONS["ALGORITHM"],
        )
        # Return access_token
        return access_token

    # Create method to generate refresh token.
    @staticmethod
    def create_refresh_token(model: object, id: str = "id") -> str:
        """
        Generate a refresh token.

        Args:
            - model (object): Model instance to use as payload for the token
            - id (str): Attribute name for the id

        Returns:
            - str: Generated refresh token
        """
        # Check id
        if not TokenUtility.has_id_attribute(model, id):
            raise ValueError("Model instance must have an id attribute")
        # Payload
        payload: dict[str, str] = {
            f"{model.__class__.__name__}": getattr(model, id),
            "type": "refresh",
            "exp": datetime.now(timezone.utc)
            + JWT_AUTHENTICATIONS["REFRESH_TOKEN_LIFETIME"],
        }
        # Generate token
        refresh_token: str = jwt.encode(
            payload,
            key=JWT_AUTHENTICATIONS["SECRET_KEY"],
            algorithm=JWT_AUTHENTICATIONS["ALGORITHM"],
        )
        # Return refresh_token
        return refresh_token

    # Create method to genereate both tokens
    @staticmethod
    def for_user(user: User, id: str = "id") -> Token:
        """
        Generate tokens for a user.

        Args:
            - user (User): User model instance
            - id (str): Attribute name for the id

        Returns:
            - Token: Token instance containing the access & refresh tokens
        """
        # Check id
        if not TokenUtility.has_id_attribute(user, id):
            raise ValueError("User instance must have an id attribute")
        # Initialize an instance
        token: Token = Token()
        # Create access_token
        token.access_token = RefreshToken.create_access_token(user)
        # Create refresh_token
        token.refresh_token = RefreshToken.create_refresh_token(user)
        # Return the token
        return token

    # Create method to decode the token
    @staticmethod
    def decode_token(token: str) -> Optional[dict[str, Union[str, int]]]:
        """
        Decode a JWT token.

        Args:
            - token (str): The JWT token to decode

        Returns:
            - dict: The decoded token payload or None if invalid
        """
        try:
            return jwt.decode(
                token,
                key=JWT_AUTHENTICATIONS["SECRET_KEY"],
                algorithms=[JWT_AUTHENTICATIONS["ALGORITHM"]],
            )
        except (jwt.ExpiredSignatureError, jwt.InvalidTokenError):
            return None


# Function to create JWT access & refresh tokens
def get_tokens_for_user(user: User) -> dict[str, str]:
    """
    Create access & refresh tokens for a User.

    Args:
        - user (User): User model

    Returns:
        - dict: Access token and Refresh token
    """
    # Create token
    refresh: Token = RefreshToken.for_user(user)
    # Return tokens
    return {
        "access": refresh.access_token,
        "refresh": refresh.refresh_token,
    }
