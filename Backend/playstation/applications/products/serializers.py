"""
# File that contains serializers for products application
"""

from playstation import serializers
from playstation.models.products import Product, Category
from typing import Any


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
