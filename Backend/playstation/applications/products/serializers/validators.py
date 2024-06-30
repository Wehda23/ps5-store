"""
# File that contains validators for the products application
"""

from playstation.admin.validators import BaseValidator
from playstation.models.products import Category, Product
from typing import Self, Optional, NoReturn
import re


# class to check if category exists
class CategoryValidatorByName(BaseValidator):
    def validate(self: Self, data: str) -> Optional[NoReturn]:
        """
        Validate if the category exists in the database

        Args:
            data (str): The category name to be validated

        Raises:
            ValueError: Category already exists.

        Returns:
            Optional[NoReturn]: If the category exists, returns None. Otherwise, raises a ValueError
        """
        # Check if there is a duplicate category name
        if Category.query.filter_by(name=data).first():
            raise self.raise_exception(ValueError, "Category already exists")


class CategoryValidatorByID(BaseValidator):
    def validate(self: Self, data: int) -> bool:
        """
        Validate if the category exists in the database

        Args:
            data (int): The category ID to be validated

        Returns:
            bool: True if the category exists, False otherwise
        """
        # Check if there is a duplicate category ID
        if Category.query.filter_by(id=data).first():
            return True
        # Category does not exist return False
        return False


# class to check if exists
class ProductValidatorByName(BaseValidator):
    def validate(self: Self, data: str) -> bool:
        """
        Validate if the Product exists in the database

        Args:
            data (str): The Product name to be validated

        Raises:
            ValueError: Product already exists.

        Returns:
            bool: If the Product exists, returns True. Otherwise, False
        """
        # Check if there is a duplicate Product name
        if Product.query.filter_by(name=data).first():
            return True
        # Product does not exist return False
        return False


class ProductValidatorByID(BaseValidator):
    def validate(self: Self, data: int) -> bool:
        """
        Validate if the product exists in the database

        Args:
            data (int): The product ID to be validated

        Returns:
            bool: True if the product exists, False otherwise
        """
        # Check if there is a duplicate product ID
        if Product.query.filter_by(id=data).first():
            return True
        # product does not exist return False
        return False


class ProductNameByLength(BaseValidator):
    def validate(self: Self, name: str) -> bool:
        """
        Validate if the product name is within the allowed length

        Args:
            name (str): The product name to be validated

        Returns:
            bool: True incase passes the validated length
        """
        if len(name) < 3 or len(name) > 255:
            return False
        return True


class ImageUrlValidator(BaseValidator):
    def validate(self: Self, url: str) -> bool:
        """
        Validate if the image URL is a valid HTTPS URL and points to an image file.

        Args:
            url (str): The image URL to be validated

        Returns:
            bool: True if the URL is valid and points to an image, False otherwise
        """
        regex = re.compile(
            r"^https://"
            r"(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|"
            r"localhost|"
            r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|"  # IPv4
            r"\[?[A-F0-9]*:[A-F0-9:]+\]?)"  # IPv6
            r"(?::\d+)?"  # Port
            r"(?:/?|[/?]\S+)$",
            re.IGNORECASE,
        )

        # Image file extensions
        image_extensions = re.compile(r"\.(jpg|jpeg|png)$", re.IGNORECASE)
        # image_extensions = re.compile(r"\.(jpg|jpeg|png|gif|bmp|webp)$", re.IGNORECASE)
        # Validate the URL
        if not regex.match(url):
            return False

        # Validate the image file extension
        if not image_extensions.search(url):
            return False

        return True


class ProductValidatorByImageURL(BaseValidator):
    """
    Check if a product with the same image link exists
    """

    def _validate_image_url(self: Self, url: str) -> bool:
        """
        Validate if the image URL is a valid HTTPS URL and points to an image file.
        """
        if Product.query.filter_by(image_url=url).first():
            return True
        return False

    def validate(self: Self, url: str) -> bool:
        """
        Validate if the product with the same image link exists

        Args:
            url (str): The image URL to be validated

        Returns:
            bool: True if the product with the same image link exists, False otherwise
        """
        # Validate the image URL
        if not self._validate_image_url(url):
            return False
        return True
