"""
# File that contains serializer for pages application
"""

from playstation import serializers
from playstation.models.products import Product
from typing import Self


class CheckImageSerializer(serializers.Serializer):
    """Serializer for checking image of product"""

    class Meta:
        """Meta class for serializer"""

        model: Product = Product
        fields: list = ["image_url"]

    def validate_image_url(self: Self, value: str) -> str:
        """
        Method for checking image of product
        """
        if not self.model.query.filter_by(image_url=value).first():
            raise ValueError("Image not found")
        return value
