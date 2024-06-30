"""
Serializers for managing product and category data within the application.

This module provides serializers for handling CRUD operations and validation
of product and category data using SQLAlchemy ORM and Pydantic for query
validation.

Usage:
- Import the serializers as needed for creating, updating, retrieving, and
  deleting products and categories.
- Each serializer provides methods for validating input data and converting
  database objects into JSON-compatible representations.

Note:
- Ensure that SQLAlchemy models (`Product` and `Category`) are properly defined
  in the application and imported correctly for these serializers to work.
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
    ProductValidatorByImageURL,
)
from .pydantic_serializer import ProductsQuery, SortByChoices
from sqlalchemy import or_
from sqlalchemy.orm import Query
import os
from typing import Any, Optional, Union


# Category Serializer
class CategorySerializer(serializers.ModelSerializer):
    """
    Serializer for Category model.

    Provides methods for serializing Category objects to dictionaries.
    """

    class Meta:
        model: Category = Category
        fields: list[str] = ["id", "name"]

    @staticmethod
    def get_all_categories(*args: Any, **kwargs: Any) -> list[dict]:
        """
        Retrieve all categories.

        Returns:
            list[dict]: Serialized list of category objects.
        """
        categories: list[Category] = Category.query.all()
        serializer = CategorySerializer(categories, many=True)
        return serializer.data


# Create Category Serializer
class CreateCategorySerializer(serializers.Serializer):
    """
    Serializer for creating a new category.

    Provides methods for validating and serializing input data for creating
    a new category.
    """

    class Meta:
        model: Category = Category
        fields: list[str] = ["name"]

    def validate_name(self, value: str) -> Optional[str]:
        """
        Validate category name.

        Args:
            value (str): Name of the new category.

        Raises:
            ValueError: If category name already exists.

        Returns:
            str: Validated category name.
        """
        CategoryValidatorByName(serializers.SerializerError).validate(value)
        return value


# Delete Category Serializer
class DeleteCategorySerializer(serializers.Serializer):
    """
    Serializer for deleting a category.

    Provides methods for validating and serializing input data for deleting
    a category by its ID.
    """

    class Meta:
        model: Category = Category
        fields: list[str] = ["id"]

    def validate_id(self, value: int) -> int:
        """
        Validate category ID.

        Args:
            value (int): ID of the category to delete.

        Raises:
            ValueError: If category ID does not exist.

        Returns:
            int: Validated category ID.
        """
        if not CategoryValidatorByID().validate(value):
            raise serializers.SerializerError(ValueError, "Category does not exist")
        self.instance = self.to_instance()
        return value


# Product Serializer
class ProductSerializer(serializers.ModelSerializer):
    """
    Serializer for Product model.

    Provides methods for customizing the serialization of Product objects,
    including retrieving associated category data.
    """

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

    def to_representation(self, instance: Product) -> dict:
        """
        Custom representation of a product.

        Retrieves associated category data and adds it to the serialized product
        representation.

        Args:
            instance (Product): Product instance to serialize.

        Returns:
            dict: Serialized representation of the product.
        """
        data: dict = super().to_representation(instance)
        category: Category = Category.query.get(data.pop("category_id"))
        data["category"] = CategorySerializer(instance=category).data
        return data


# Get Product Serializer
class GetProductSerializer(serializers.Serializer):
    """
    Serializer for retrieving a product.

    Provides methods for validating product IDs and converting Product objects
    into JSON-compatible representations.
    """

    class Meta:
        model: Product = Product
        fields: list[str] = ["id"]

    def validate_id(self, value: int) -> int:
        """
        Validate product ID.

        Args:
            value (int): ID of the product to retrieve.

        Raises:
            ValueError: If product ID does not exist.

        Returns:
            int: Validated product ID.
        """
        if not ProductValidatorByID().validate(value):
            raise ValueError("Product does not exist")
        self.instance: Product = self.to_instance()
        return value

    def to_representation(self, instance: object) -> dict:
        """
        Convert Product instance to representation.

        Args:
            instance (object): Product instance to serialize.

        Returns:
            dict: Serialized representation of the product.
        """
        product: Product = self.instance
        serializer = ProductSerializer(instance=product)
        return serializer.data

    def delete(self) -> None:
        """
        Delete the product instance.
        """
        self.instance: Product = self.to_instance()
        super().delete()

    @classmethod
    def get_products(cls, queries: dict[str, str]) -> Optional[list[dict]]:
        """
        Retrieve products based on specified queries.

        Args:
            queries (dict[str, str]): Queries to filter products.

        Returns:
            Optional[list[dict]]: List of products matching the queries.
        """
        # Verify Queries
        pydantic_model: ProductsQuery = ProductsQuery(**queries)
        # Grab validated queries
        validated_queries: dict[str, str] = pydantic_model.model_dump()
        # Retrieve products
        # products: list[Product] = cls.get_products_query(validated_queries)
        # Serialize products
        # serializer: ProductSerializer = ProductSerializer(instance=products, many=True)
        # Return Serialized Data
        return validated_queries

    @classmethod
    def get_products_query(cls, validated_queries: dict) -> list[Product]:
        """
        Retrieve products based on validated queries.

        Args:
            validated_queries (dict): Validated queries to filter products.

        Returns:
            list[Product]: List of products matching the queries.
        """
        # Build Up Query
        query: Query = Product.query
        query: Query = cls.filter_sale(query, validated_queries)
        query: Query = cls.filter_category(query, validated_queries)
        query: Query = cls.filter_price(query, validated_queries)
        query: Query = cls.filter_search(query, validated_queries)
        query: Query = cls.sort_by(query, validated_queries)
        query: Query = cls.paginate(query, validated_queries)
        # Execute Query
        return query.all()

    @classmethod
    def filter_sale(cls, query: Query, validated_queries: dict):
        """
        Filter products by sale status.

        Args:
            query: SQLAlchemy query object.
            validated_queries (dict): Validated queries to filter products.

        Returns:
            Query: Filtered SQLAlchemy query object.
        """
        if validated_queries.get("sale"):
            query = query.filter(Product.is_sale == True)
        return query

    @classmethod
    def filter_category(cls, query: Query, validated_queries: dict):
        """
        Filter products by category.

        Args:
            query: SQLAlchemy query object.
            validated_queries (dict): Validated queries to filter products.

        Returns:
            Query: Filtered SQLAlchemy query object.
        """
        category = validated_queries.get("category")
        if category and category != "all":
            category_ids = cls.parse_category_ids(category)
            valid_category_ids = cls.validate_category_ids(category_ids)
            if valid_category_ids:
                query = query.filter(Product.category_id.in_(valid_category_ids))
        return query

    @staticmethod
    def parse_category_ids(category: Union[str, int]) -> list[int]:
        """
        Parse category IDs from string format.

        Args:
            category (Union[str, int]): Category ID(s) as string or integer.

        Returns:
            list[int]: List of parsed category IDs.
        """
        if isinstance(category, int):
            return [category]
        return [int(cat_id) for cat_id in category.split("-")]

    @staticmethod
    def validate_category_ids(category_ids: list[int]) -> list[int]:
        """
        Validate category IDs against existing categories.

        Args:
            category_ids (list[int]): List of category IDs to validate.

        Returns:
            list[int]: List of valid category IDs.
        """
        valid_category_ids = []
        for cat_id in category_ids:
            exists = Category.query.filter_by(id=cat_id).first()
            if exists:
                valid_category_ids.append(cat_id)
        return valid_category_ids

    @classmethod
    def filter_price(cls, query: Query, validated_queries: dict):
        """
        Filter products by price range.

        Args:
            query: SQLAlchemy query object.
            validated_queries (dict): Validated queries to filter products.

        Returns:
            Query: Filtered SQLAlchemy query object.
        """
        low_price = validated_queries.get("low_price")
        if low_price is not None:
            query = query.filter(Product.price >= low_price)

        high_price = validated_queries.get("high_price")
        if high_price is not None:
            query = query.filter(Product.price <= high_price)
        return query

    @classmethod
    def filter_search(cls, query: Query, validated_queries: dict):
        """
        Filter products by search keyword.

        Args:
            query: SQLAlchemy query object.
            validated_queries (dict): Validated queries to filter products.

        Returns:
            Query: Filtered SQLAlchemy query object.
        """
        search = validated_queries.get("search")
        if search:
            query = query.filter(
                or_(
                    Product.name.ilike(f"%{search}%"),
                    Product.description.ilike(f"%{search}%"),
                )
            )
        return query

    @classmethod
    def sort_by(cls, query: Query, validated_queries: dict):
        """
        Sort products based on specified criteria.

        Args:
            query: SQLAlchemy query object.
            validated_queries (dict): Validated queries to sort products.

        Returns:
            Query: Sorted SQLAlchemy query object.
        """
        sort_by = validated_queries.get("sort_by")
        if sort_by:
            if sort_by == SortByChoices.price:
                query = query.order_by(Product.price)
            elif sort_by == SortByChoices.price_desc:
                query = query.order_by(Product.price.desc())
            elif sort_by == SortByChoices.name:
                query = query.order_by(Product.name)
            elif sort_by == SortByChoices.name_desc:
                query = query.order_by(Product.name.desc())
            elif sort_by == SortByChoices.date:
                query = query.order_by(Product.created_at)
            elif sort_by == SortByChoices.date_desc:
                query = query.order_by(Product.created_at.desc())
        return query

    @classmethod
    def paginate(cls, query: Query, validated_queries: dict):
        """
        Paginate the products query.

        Args:
            query: SQLAlchemy query object.
            validated_queries (dict): Validated queries for pagination.

        Returns:
            Query: Paginated SQLAlchemy query object.
        """
        start = validated_queries.get("start", 0)
        products = validated_queries.get("products", 10)
        query = query.offset(start).limit(products)
        return query


# Create Product Serializer
class CreateProductSerializer(serializers.Serializer):
    """
    Serializer for creating a new product.

    Provides methods for validating and serializing input data for creating
    a new product.
    """

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

    def validate_name(self, value: str) -> str:
        """
        Validate product name.

        Args:
            value (str): Name of the product.

        Raises:
            ValueError: If name length is invalid or product with the same name
                        already exists.

        Returns:
            str: Validated product name.
        """
        if not ProductNameByLength().validate(value):
            raise ValueError("Name should be between 3 and 255 characters")

        if ProductValidatorByName().validate(value):
            raise ValueError("Product with the same name already exists")

        return value

    def validate_price(self, value: float) -> float:
        """
        Validate product price.

        Args:
            value (float): Price of the product.

        Raises:
            ValueError: If price is negative.

        Returns:
            float: Validated product price.
        """
        if value < 0:
            raise ValueError("Price cannot be negative")
        return value

    def validate_description(self, value: str) -> str:
        """
        Validate product description.

        Args:
            value (str): Description of the product.

        Returns:
            str: Validated product description.
        """
        return value

    def validate_stock(self, value: int) -> int:
        """
        Validate product stock.

        Args:
            value (int): Stock of the product.

        Raises:
            ValueError: If stock is less than or equal to 0.

        Returns:
            int: Validated product stock.
        """
        if value <= 0:
            raise ValueError("Stock must be more than 0")
        return value

    def validate_category_id(self, value: int) -> int:
        """
        Validate product category ID.

        Args:
            value (int): Category ID of the product.

        Raises:
            ValueError: If category ID does not exist.

        Returns:
            int: Validated product category ID.
        """
        if not CategoryValidatorByID().validate(value):
            raise ValueError("Category does not exist")

        return value

    def validate_image_url(self, value: Optional[str]) -> str:
        """
        Validate product image URL.

        Args:
            value (str): Image URL of the product.

        Raises:
            ValueError: If URL is invalid.

        Returns:
            str: Validated image URL of the product.
        """
        if isinstance(value, FileStorage):
            value = image_handler.save_image(
                value,
                upload_dir=os.path.join(MEDIA_DIR, self._data.get("name", "random")),
                safe=True,
            )
        elif value is None:
            value = os.path.join(MEDIA_DIR, "default.png")

        if not ImageUrlValidator().validate(value):
            raise ValueError("URL is not valid")

        return value


# Update Product Serializer
class UpdateProductSerializer(serializers.Serializer):
    """
    Serializer for updating a product.

    Provides methods for validating and serializing input data for updating
    an existing product.
    """

    class Meta:
        model: Product = Product
        fields: list[str] = [
            "id",
            "name",
            "description",
            "price",
            "stock",
            "category_id",
            "image_url",
        ]

    def validate_id(self, value: int) -> int:
        """
        Validate product ID.

        Args:
            value (int): ID of the product to update.

        Raises:
            ValueError: If product ID does not exist.

        Returns:
            int: Validated product ID.
        """
        if not ProductValidatorByID().validate(value):
            raise ValueError("Product does not exist")
        return value

    def validate_name(self, value: str) -> str:
        """
        Validate product name.

        Args:
            value (str): Name of the product.

        Raises:
            ValueError: If name length is invalid or product with the same name
                        does not exist.

        Returns:
            str: Validated product name.
        """
        if not ProductNameByLength().validate(value):
            raise ValueError("Name should be between 3 and 255 characters")

        if not ProductValidatorByName().validate(value):
            raise ValueError("Product with that name does not exist")

        return value

    def validate_price(self, value: int) -> int:
        """
        Validate product price.

        Args:
            value (int): Price of the product.

        Raises:
            ValueError: If price is negative.

        Returns:
            int: Validated product price.
        """
        if value < 0:
            raise ValueError("Price cannot be negative")
        return value

    def validate_description(self, value: str) -> str:
        """
        Validate product description.

        Args:
            value (str): Description of the product.

        Returns:
            str: Validated product description.
        """
        return value

    def validate_stock(self, value: int) -> int:
        """
        Validate product stock.

        Args:
            value (int): Stock of the product.

        Raises:
            ValueError: If stock is less than or equal to 0.

        Returns:
            int: Validated product stock.
        """
        if value <= 0:
            raise ValueError("Stock must be more than 0")
        return value

    def validate_category_id(self, value: int) -> int:
        """
        Validate product category ID.

        Args:
            value (int): Category ID of the product.

        Raises:
            ValueError: If category ID does not exist.

        Returns:
            int: Validated product category ID.
        """
        if not CategoryValidatorByID().validate(value):
            raise ValueError("Category does not exist")

        return value

    def validate_image_url(self, value: Optional[str]) -> str:
        """
        Validate product image URL.

        Args:
            value (str): Image URL of the product.

        Raises:
            ValueError: If URL is invalid.

        Returns:
            str: Validated image URL of the product.
        """
        if ProductValidatorByImageURL().validate(value):
            pass
        elif isinstance(value, FileStorage):
            value = image_handler.save_image(
                value,
                upload_dir=os.path.join(MEDIA_DIR, self._data.get("name", "random")),
            )
        elif value is None:
            value = os.path.join(MEDIA_DIR, "default.png")

        if not ImageUrlValidator().validate(value):
            raise ValueError("URL is not valid")

        return value
