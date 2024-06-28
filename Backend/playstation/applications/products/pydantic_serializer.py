"""
# Module contains serializers for product query api
"""

from playstation import serializers
from playstation.models.products import Product, Category
from pydantic import BaseModel, ValidationError
from typing import Self

queries: dict = {
    "category": ("category", None),  # Category Id
    "search": (
        "search",
        None,
    ),  # Word to search for in name of product or in description
    "sort_by": ("sort_by", None),  # Sort by certain attribute
    "start": ("start", 0),  # point of the start of products
    "products": ("products", 10),  # How many products to retrieve from start point
    "low_price": ("low_price", None),  # Lowest price point
    "high_price": ("high_price", None),  # highest price point
    "sale": ("sale", 0),  # Check if the product on sale or not
}


class ProductsQuery(BaseModel):
    """Serializer for product query api"""

    category: int | None = None
    search: str | None = None
    sort_by: str | None = None
    start: int = 0
    products: int = 10
    low_price: int | None = None
    high_price: int | None = None
    sale: int = 0
