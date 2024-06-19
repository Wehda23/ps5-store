"""
# File that contains base validator class
"""

from abc import ABC, abstractmethod
from typing import Self


# Abstracted Validator Class
class BaseValidator(ABC):

    def __init__(self: Self, raise_exception: Exception = Exception):
        self.raise_exception: Exception = raise_exception

    @abstractmethod
    def validate(self, data):
        pass
