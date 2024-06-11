"""
# Package for Authentication related classes and functions
"""

from typing import Self, Callable, Union, Any
from flask import make_response, Response, request
from functools import wraps
from playstation.settings import JWT_AUTHENTICATIONS
from abc import ABC, abstractmethod


# Invalid Token Error
class InvalidTokenError(Exception):
    pass


# Abstract Class
class Authentication(ABC):
    """
    Abstract Class for Authentication
    """

    @abstractmethod
    def authenticate(self: Self, token: str) -> bool:
        """
        Method used to authenticate request.
        """
        pass


# Authentication Decorator.
def authentication_classess(
    auth_classes: list[Authentication],
) -> Union[Callable, Response]:
    """
    A decoratorr that checks if the request meets all specified authentications

    Args:
        auth_classess (list[Authentication]): A list of authentication classes

    Returns:
        Callable: The decorated route function in case of success.
        Response: A 401 Unauthorized response in case of failure.
    """

    def decorator(view: Callable) -> Union[Callable, Response]:
        @wraps(view)
        def decorated_function(*args, **kwargs) -> Union[Response, Any]:
            # Token
            token: str = request.headers.get("Authorization")
            # Token Prefix
            prefix: str = JWT_AUTHENTICATIONS.get("AUTH_HEADER_TYPES", None)
            # Check Token first
            if token is None or not token.startswith(prefix):
                return make_response({"error": "Unauthorized access"}, 401)
            # Grab the token
            token: str = token.split(" ")[1]
            # Run authorization classes
            for authentication in auth_classes:
                if not authentication.authenticate(token):
                    return make_response({"error": "Unauthorized access"}, 401)
            return view(*args, **kwargs)

        return decorated_function

    return decorator



