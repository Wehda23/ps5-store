"""
# File contains validators for serializer class
"""

from abc import ABC, abstractmethod
from typing import Self


# Abstract Validation
class AbstractValidation:
    """
    Abstract class for validators
    """

    @abstractmethod
    def validate(self, data: dict) -> bool:
        pass
