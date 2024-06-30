"""
# File that contains validators for this application
"""

import re
from playstation.admin.validators import BaseValidator
from playstation.models.users import User
from typing import Self, Optional, NoReturn


# Email Validator class
class EmailValidator(BaseValidator):
    """
    This class validates email addresses
    """

    # Regex format for emails
    regex: str = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"

    def validate(self: Self, email: str) -> Optional[NoReturn]:
        """
        Method used to validate email address

        Args:
            - email (str): Email address to go through validation process

        Raises:
            - Error in case email validation failed.

        Returns:
            - None
        """
        # Check Regex Email
        if not re.fullmatch(self.regex, email):
            raise self.raise_exception(ValueError, "Invalid email address.")


# Name Validating
class NameValidator(BaseValidator):
    """
    This class validates names
    """

    def validate(self: Self, name: str) -> Optional[NoReturn]:
        """
        Method used to validate name

        Args:
            - name (str): Name to go through validation process

        Raises:
            - Error incase name validation failed.

        Returns:
            - Nothing.
        """
        # Check if name contains only alphabets
        if not name.isalpha():
            raise self.raise_exception(ValueError, "Your first name can only contain characters.")


# Password Validating
class PasswordValidator(BaseValidator):
    """
    This class validates passwords
    """

    def length(self: Self, password: str) -> bool:
        """
        Method used to check the length of the input password.

        Args:
            - password (str): Password input to pass by the length validations.

        Raises:
            - self.error (object): In case password is shorter than 8 characters|numbers|special characters \
                or Incase password is longer than 128 characters|numbers|special characters.

        Returns:
            - True incase password is valid in terms of lengths
        """
        if len(password) < 8:
            raise self.raise_exception(
                ValueError,
                "Password should be longer than 8 characters|numbers|special characters."
            )
        elif len(password) > 128:
            raise self.raise_exception(
                ValueError,
                "Password should be less than 128 characters|numbers|special characters."
            )
        else:
            return True

    def character_format(self: Self, password: str):
        """
        Method used to validate password format

        Raises:
            - self.raise_exception (object): In case password does not contain at least one character A-Z a-z.\
                or Password does not contain at least one number 0-9..

        Args:
            - password (str): Password input to pass by the format validations.
        """
        # Validate password for at least containing Alphabetical characters A-Z a-z.
        if not any(char.isalpha() for char in password):
            raise self.raise_exception(
                ValueError,
                "Password should contain at least one character A-Z a-z."
            )
        # Validate password for at least containing  Numeric characters 0-9.
        if not any(number.isnumeric() for number in password):
            raise self.raise_exception(
                ValueError,
                "Password should contain at least one number 0-9."
            )
        # Return Valid Password
        return True

    def validate(self: Self, password: str) -> Optional[NoReturn]:
        """
        Method used to validate password

        Args:
            - password (str): password to go through validation process

        Raises:
            - Error incase password validation failed.

        Returns:
            - Nothing.
        """
        # Validate password by format.
        format_valid: bool = self.character_format(password)
        # Validate password by length.
        length_valid: bool = self.length(password)
        # Return validation results.
        return format_valid and length_valid


class IDValidator(BaseValidator):
    """
    Class used to validate ID input
    """

    def validate(self, id: Optional[int]) -> Optional[NoReturn]:
        """
        Method used to validate ID input

        Args:
            - id (int): Id of the user

        Returns:
            - Nothing
        """
        if id is None or id < 0:
            raise self.raise_exception(ValueError, "Invalid ID")

        if not User.query.filter_by(id=id).first():
            raise self.raise_exception(ValueError, "User not found")
