"""
# File that contains permission concerned Classes & Functions for the application
"""

from abc import ABC, abstractmethod
from typing import Self, Callable, Any, Union
from flask import request, jsonify, Request, Response
from functools import wraps


# BaseClass
class BasePermission(ABC):
    """
    Abstract class to represent permission classes
    """

    @abstractmethod
    def has_permission(self: Self, request: Request, *args, **kwargs) -> bool:
        """
        Method used to check permissions
        """
        pass


# Permission decorator function
def permission_required(permissions: list[BasePermission]) -> Union[Callable, Response]:
    """
    A decorator that checks if the request meets all specified permissions.

    Args:
        permissions (list[BasePermission]): A list of permission classes to check.

    Returns:
        Callable: The decorated route function in case of success.
        Response: A 403 Permission Denied in case of failure.
    """

    def decorator(view: Callable) -> Callable:
        @wraps(view)
        def decorated_function(*args: Any, **kwargs: Any) -> Any:
            for permission in permissions:
                if not permission().has_permission(request, *args, **kwargs):
                    return jsonify({"message": "Permission denied"}), 403
            return view(*args, **kwargs)

        return decorated_function

    return decorator
