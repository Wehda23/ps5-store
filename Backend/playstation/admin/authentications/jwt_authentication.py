"""
# File That contains classes related to JWTAuthentication.
"""

from typing import Self
from . import Authentication


# JWT Authentication class
class JWTAuthentication(Authentication):
    """
    Class for JWT Authentication
    """

    def authenticate(self: Self, token: str) -> bool:
        """
        Authenticate the user using JWT token
        """
        pass
