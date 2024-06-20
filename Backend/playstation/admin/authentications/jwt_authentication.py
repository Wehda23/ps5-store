"""
# File that contains classes related to JWT Authentication.
"""

from typing import Optional, Self
from flask import request
from . import Authentication
from playstation.models.users import User
from playstation.models.blacklisted_tokens import BlackListedTokens
from .token import RefreshToken


class JWTAuthentication(Authentication):
    """
    Class for JWT Authentication.
    """
    def check_blacklisted(self: Self, token: str, user: User, field: str = 'access') -> bool:
        """
        Check if the token is blacklisted.

        Args:
            - token (str): String token.
            - user (User): The user whose tokens are being checked.
            - field (str): The token field to check (default is 'access').

        Returns:
            - bool: True if the token is blacklisted, otherwise False.
        """
        # Grab the blacklisted tokens
        blacklisted_tokens: list[BlackListedTokens] = user.blacklisted_tokens
        # variable for blacklisted token
        is_blacklisted: bool = False
        # Loop over the tokens
        for blacklisted_token in blacklisted_tokens:
            # Check if access token is blacklisted
            if getattr(blacklisted_token, field) == token:
                is_blacklisted: bool = True
            # Check token lift to delete expired tokens from database
            blacklisted_token.check_token_life()
        return is_blacklisted

    def decode(self: Self, token: str) -> Optional[dict[str, str]]:
        """
        Decodes the JWT token and checks if it's valid.

        Args:
            token (str): The JWT token to decode.

        Returns:
            Optional[dict[str, str]]: The decoded token if valid, otherwise None.
        """
        return RefreshToken.decode_token(token)

    def token_type(self: Self, data: dict[str, str]) -> bool:
        """
        Method used to check if the token type is access token.

        Args:
            data (dict): Dictionary that contains token details.

        Returns:
            bool: True if the token type is access, otherwise False.
        """
        return data.get("type", None) == "access"

    def authenticate(self: Self, token: str) -> bool:
        """
        Authenticate the user using JWT token.

        Args:
            token (str): The JWT token to authenticate.

        Returns:
            bool: True if authentication is successful, False otherwise.
        """
        # Decode the token
        valid_token = self.decode(token)

        # Check if token is valid
        if valid_token is None:
            return False

        # Check token type
        if not self.token_type(valid_token):
            return False

        # Get user ID from token
        user_id: int = valid_token.get("User")

        # Query the user from the database
        user: Optional[User] = User.query.get(user_id)

        # Check if user exists
        if user is None:
            return False

        # check if user is an active user
        if not user.active:
            return False

        # Check if the token is blacklisted
        if self.check_blacklisted(token, user):
            return False

        # Attach user to the request object
        setattr(request, "user", user)

        return True


# Refresh Token Authenticator
class RefreshTokenAuthentication(JWTAuthentication):
    """
    Class for JWT Refresh Token Authentication.
    """

    def check_blacklisted(self: Self, token: str, user: User, field: str = 'refresh') -> bool:
        return super().check_blacklisted(token, user, field)

    def token_type(self: Self, data: dict[str, str]) -> bool:
        """
        Method used to check if the token type is refresh token.

        Args:
            data (dict): Dictionary that contains token details.

        Returns:
            bool: True if the token type is refresh, otherwise False.
        """
        return data.get("type", None) == "refresh"
