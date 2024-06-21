"""
# File that contains serializers for products application
"""

from playstation import serializers
from playstation.models.products import Product, Category
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
        if Category.query.filter_by(name=value).first():
            raise ValueError("Category already exists")
        # Return the name of the new category
        return value