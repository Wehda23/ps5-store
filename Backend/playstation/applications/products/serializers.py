"""
# File that contains serializers for products application
"""

from playstation.admin.file_manager import image_handler
from werkzeug.datastructures.file_storage import FileStorage
from playstation import serializers
from playstation.settings import MEDIA_DIR
from playstation.models.products import Product, Category
from .validators import (
    CategoryValidatorByName,
    CategoryValidatorByID,
    ProductValidatorByID,
    ProductValidatorByName,
    ProductNameByLength,
    ImageUrlValidator,
)
import os
from typing import Any, Self, Optional


# Category Serializer
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model: Category = Category
        fields: list[str] = ["id", "name"]

    @staticmethod
    def get_all_categories(*args: Any, **kwargs: Any) -> list[dict]:
        """Grab all product categories"""
        # Get all categories
        categories: list[Category] = Category.query.all()
        # Serialize categories
        serializer = CategorySerializer(categories, many=True)
        # Return list of serialized categories
        return serializer.data


# Create Category Serializer
class CreateCategorySerializer(serializers.Serializer):
    class Meta:
        model: Category = Category
        fields: list[str] = ["name"]

    def validate_name(self: Self, value: str) -> Optional[str]:
        """
        Validation method for name

        Args:
            value (str): name of the new category

        Raises:
            ValueError: Category already exists.

        Returns:
            str: Value of the name of the category
        """
        # Check if there is a duplicate category name
        CategoryValidatorByName().validate(value)
        # Return the name of the new category
        return value


# Delete serializer
class DeleteCategorySerializer(serializers.Serializer):
    class Meta:
        model: Category = Category
        fields: list[str] = ["id"]

    def validate_id(self: Self, value: int) -> int:
        """
        Validation method for id

        Args:
            value (int): ID of the category

        Returns:
            Verified Id of the category
        """
        # Check if the category exists
        if not CategoryValidatorByID().validate(value):
            raise ValueError("Category does not exist")
        # assign instance
        self.instance = self.to_instance()
        # Return id
        return value


# Product serializer
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model: Product = Product
        fields: list[str] = [
            "id",
            "name",
            "price",
            "description",
            "stock",
            "category_id",
            "image_url",
        ]


# Get Product serializer
class GetProductSerializer(serializers.Serializer):
    class Meta:
        model: Product = Product
        fields: list[str] = ["id"]

    def validate_id(self: Self, value: int) -> int:
        """
        Validation method for id

        Args:
            value (int): id of the product

        Raises:
            ValueError: Product does not exist

        Returns:
            Verified id of the product
        """
        # Check if the product exists
        if not ProductValidatorByID().validate(value):
            raise ValueError("Product does not exist")
        return value

    def to_representation(self, instance: object) -> dict:
        """
        Method to convert instance to representation

        Args:
            instance (object): instance of the product

        Returns:
            dict: representation of the product
        """
        # Get the product by id
        product: Product = self.to_instance(self._data["id"])
        # Serializer
        serializer = ProductSerializer(instance=product)
        # Return serialized data
        return serializer.data

    def delete(self) -> None:
        """
        Method to delete a product
        """
        # Make sure the instance is identified
        self.instance: Product = self.to_instance(self._data["id"])
        # Delete instance
        super().delete()


# Create Product serializer
class CreateProductSerializer(serializers.Serializer):
    class Meta:
        model: Product = Product
        fields: list[str] = [
            "name",
            "price",
            "description",
            "stock",
            "category_id",
            "image_url",
        ]

    # validate fields
    def validate_name(self: Self, value: str) -> str:
        """
        Validation method for name

        Args:
            value (str): Name of the product

        Raises:
            ValueError: Name should be between 3 and 255 characters.
                or Product with same name already exists.

        Returns:
            Verified name of the product
        """
        # Check length of the name
        if not ProductNameByLength().validate(value):
            raise ValueError("Name should be between 3 and 255 characters")

        # Cehck if product with same name exists
        if ProductValidatorByName().validate(value):
            raise ValueError("Product with same name already exists")

        # Return Validated name
        return value

    def validate_price(self: Self, value: float) -> float:
        """
        Validation method for price

        Args:
            value (float): price of the product

        Raises:
            ValueError: Price cannot be negative.

        Returns:
            Verified price of the product
        """
        # Value must be more than 0
        if float(value) < 0:
            raise ValueError("Price cannot be negative")
        # Return validated value
        return value

    def validate_description(self: Self, value: str) -> str:
        """
        Validation method for description

        Args:
            value (str): description of the product

        Returns:
            Verified description of the product
        """
        return value

    def validate_stock(self: Self, value: int) -> int:
        """
        Validation method for stock

        Args:
            value (int): stock of the product

        Raises:
            ValueError: Stock must be more than 0

        Returns:
            Verified stock of the product
        """
        # Check if value is more than 0
        if int(value) <= 0:
            raise ValueError("Stock must be more than 0")
        return value

    def validate_category_id(self: Self, value: int) -> int:
        """
        Validation method for category_id

        Args:
            value (int): category_id of the product

        Raises:
            Category already does not exists

        Returns:
            Verified category_id of the product
        """
        # Validate category exists
        if not CategoryValidatorByID().validate(value):
            raise ValueError("Category does not exist")

        # Return Valiaated Id
        return value

    def validate_image_url(self: Self, value: Optional[str]) -> str:
        """
        Validation method for image_url

        Args:
            value (str): image_url of the product

        Raises:
            Url is not valid

        Returns:
            Verified image_url of the product
        """
        if isinstance(value, FileStorage):
            value: str = image_handler.save_image(
                value,
                upload_dir=os.path.join(MEDIA_DIR, self._data.get("name", "random")),
            )
        elif value is None:
            # Use default Image
            value: str = os.path.join(MEDIA_DIR, "default.png")
        # validate url
        elif not ImageUrlValidator().validate(value):
            raise ValueError("Url is not valid")
        # Return the link to the image
        return value


# UpdateProductSerializer
class UpdateProductSerializer(serializers.Serializer):
    """
    Serializer for updating product
    """

    class Meta:
        model: Product = Product
        fields: list = ["id", "name", "description", "price", "stock", "category_id"]

    def validate_id(self: Self, value: int) -> int:
        """
        Validation method for id
        """
        # Validate product exists
        if not ProductValidatorByID().validate(value):
            raise ValueError("Product does not exist")
        # Return Validated Data
        return value

    def validate_name(self: Self, value: str) -> str:
        """
        Validation method for name

        Args:
            value (str): Name of the product

        Raises:
            ValueError: Name should be between 3 and 255 characters.
                or Product with same name already exists.

        Returns:
            Verified name of the product
        """
        # Check length of the name
        if not ProductNameByLength().validate(value):
            raise ValueError("Name should be between 3 and 255 characters")

        # Cehck if product with same name exists
        if ProductValidatorByName().validate(value):
            raise ValueError("Product with same name already exists")

        # Return Validated name
        return value

    def validate_price(self: Self, value: int) -> int:
        """
        Validation method for price

        Args:
            value (int): price of the product

        Raises:
            ValueError: Price cannot be negative.

        Returns:
            Verified price of the product
        """
        # Value must be more than 0
        if value < 0:
            raise ValueError("Price cannot be negative")
        # Return validated value
        return value

    def validate_description(self: Self, value: str) -> str:
        """
        Validation method for description

        Args:
            value (str): description of the product

        Returns:
            Verified description of the product
        """
        return value

    def validate_stock(self: Self, value: int) -> int:
        """
        Validation method for stock

        Args:
            value (int): stock of the product

        Raises:
            ValueError: Stock must be more than 0

        Returns:
            Verified stock of the product
        """
        # Check if value is more than 0
        if value <= 0:
            raise ValueError("Stock must be more than 0")
        return value

    def validate_category_id(self: Self, value: int) -> int:
        """
        Validation method for category_id

        Args:
            value (int): category_id of the product

        Raises:
            Category already does not exists

        Returns:
            Verified category_id of the product
        """
        # Validate category exists
        if not CategoryValidatorByID().validate(value):
            raise ValueError("Category does not exist")

        # Return Valiaated Id
        return value
