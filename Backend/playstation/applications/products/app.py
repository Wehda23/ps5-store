"""
Application that handles the Products API

This application manages all product-related actions, including category creation, product creation, updates, and deletion. It defines API routes to facilitate these actions, ensuring secure and efficient product management.

## API Routes

### Protected Routes
These routes require authentication and appropriate permissions to access:

- **/api/products/category: Create a new product category.
  - Method: POST
  - Description: Allows admins to create a new product category.
  - Authentication: JWT required
  - Permissions: Admin permissions required

- **/api/products/category/<int:category_id>: Update a product category.
  - Method: PUT
  - Description: Allows admins to update a product category by its ID.
  - Authentication: JWT required
  - Permissions: Admin permissions required

- **/api/products/category/<int:category_id>: Delete a product category.
  - Method: DELETE
  - Description: Allows admins to delete a product category by its ID.
  - Authentication: JWT required
  - Permissions: Admin permissions required

- **/api/products: Create a new product.
  - Method: POST
  - Description: Allows admins to create a new product.
  - Authentication: JWT required
  - Permissions: Admin permissions required

- **/api/products/<int:product_id>: Update a product.
  - Method: PUT
  - Description: Allows admins to update a product by its ID.
  - Authentication: JWT required
  - Permissions: Admin permissions required

- **/api/products/<int:product_id>: Delete a product.
  - Method: DELETE
  - Description: Allows admins to delete a product by its ID.
  - Authentication: JWT required
  - Permissions: Admin permissions required

### Public Routes
These routes are accessible without authentication:

- **/api/products/categories: Get all product categories.
  - Method: GET
  - Description: Retrieves all product categories.

- **/api/products/<int:product_id>: Get product.
  - Method: GET
  - Description: Retrieves product information.

- **/api/products: Get all products.
  - Method: GET
  - Description: Retrieves all products.
  - Query Parameters:
    - **category** (str, optional): Filter products by category.
    - **search** (str, optional): Search products by name or description.
    - **sort_by** (str, optional): Sort products by specified field (e.g., price, name).
    - **start** (int, optional): Specify the page number for pagination.
    - **products** (int, optional): Specify the number of products per page for pagination.
    - **low_price** (int, optional): Specify the lowest price for product.
    - **high_price** (int, optional): Specify the highest price for the product.
    - **sale** (bool, optional): Specify if the product is on sale.
"""

from flask import Blueprint, Response, make_response, request
from typing import Optional
from playstation.admin.authentications import authentication_classess
from playstation.admin.authentications.jwt_authentication import JWTAuthentication
from playstation.admin.permissions import permission_required
from werkzeug.datastructures import FileStorage
from .permissions import IsAdmin
from .serializers import (
    CategorySerializer,
    CreateCategorySerializer,
    DeleteCategorySerializer,
    CreateProductSerializer,
    GetProductSerializer,
    UpdateProductSerializer,
)
from .serializers.exceptions import InvalidCategoriesDelimiter, InvalidCategoriesOption
from sqlalchemy.exc import SQLAlchemyError
from pydantic import ValidationError
from . import logger


# Declare route prefix
url_prefix: str = "/api/products"

# Blueprint
products_api: Blueprint = Blueprint("products_api", __name__, url_prefix=url_prefix)


# API to Create product category
@products_api.route("/category", methods=["POST"])
@authentication_classess([JWTAuthentication])
@permission_required([IsAdmin])
def create_category(*args, **kwargs) -> Response:
    """
    Create a new product category

    Returns:
        Response: A success message with status 200.

    Error Codes:
        - 400: Bad Request - If the input data is invalid.
        - 401: Unauthorized - If the user is not authenticated.
        - 403: Forbidden - If the user does not have the required permissions.
    """
    try:
        # Get the request data
        data = request.get_json()
        # Here should be the logic to create a category
        # Create serializer
        serializer: CreateCategorySerializer = CreateCategorySerializer(data=data)
        # Validate the serializer
        if serializer.is_valid():
            # Save the category
            serializer.save()
            # Return success message
            return make_response("Category created successfully", 200)
        # Error
        error: list[str] = serializer.errors
        return make_response(error, 400)
    except Exception as e:
        error: str = str(e)
        logger.error(error)
        return make_response("Failed to create product category", 400)


# API to Grab all product categories
@products_api.route("/categories", methods=["GET"])
def get_categories(*args, **kwargs) -> Response:
    """
    Get all product categories

    Returns:
        Response: A list of all product categories with status 200.

    Error Codes:
        - 404: Not Found - If no categories are found.
    """
    try:
        # Get all categories
        categories = CategorySerializer.get_all_categories()
        return make_response(categories, 200)
    except Exception as e:
        error: str = str(e)
        logger.error(error)
        return make_response("Failed to grab product categories", 404)


# API to Update a product category
@products_api.route("/category/<int:category_id>", methods=["PUT"])
@authentication_classess([JWTAuthentication])
@permission_required([IsAdmin])
def update_category(category_id: int, *args, **kwargs) -> Response:
    """
    Update a product category

    Args:
        category_id (int): Category ID

    Returns:
        Response: A success message with status 200.

    Error Codes:
        - 400: Bad Request - If the input data is invalid.
        - 401: Unauthorized - If the user is not authenticated.
        - 403: Forbidden - If the user does not have the required permissions.
        - 404: Not Found - If the category is not found.
    """
    try:
        # Get data
        data = request.get_json()
        # Check id exists within the body or not.
        if "id" not in data:
            data["id"] = category_id
        # Serializer
        serializer: CategorySerializer = CategorySerializer(data=data)
        if serializer.is_valid():
            # Update category
            serializer.save()
            return make_response(serializer.data, 200)
        # error
        error: list[str] = serializer.errors
        return make_response(serializer.errors, 404)
    except Exception as e:
        error: str = str(e)
        logger.error(error)
        return make_response("Failed to update product category", 400)


# API to Delete a product category
@products_api.route("/category/<int:category_id>", methods=["DELETE"])
@authentication_classess([JWTAuthentication])
@permission_required([IsAdmin])
def delete_category(category_id: int, *args, **kwargs) -> Response:
    """
    Delete a product category

    Args:
        category_id (int): Category ID

    Returns:
        Response: A success message with status 200.

    Error Codes:
        - 401: Unauthorized - If the user is not authenticated.
        - 403: Forbidden - If the user does not have the required permissions.
        - 404: Not Found - If the category is not found.
    """
    try:
        # Get category
        data: dict = {"id": category_id}
        # Serializer
        serializer: DeleteCategorySerializer = DeleteCategorySerializer(data=data)
        # Validate serializer
        if serializer.is_valid():
            # Delete category
            serializer.delete()
            return make_response("Category deleted successfully", 200)
        # Error
        error: list[str] = serializer.errors
        return make_response(error, 404)
    except Exception as e:
        error: str = str(e)
        logger.error(error)
        return make_response("Failed to delete product category", 404)


# API to create new product
@products_api.route("", methods=["POST"])
@authentication_classess([JWTAuthentication])
@permission_required([IsAdmin])
def create_product(*args, **kwargs) -> Response:
    """
    Create a new product

    Returns:
        Response: A success message with status 201.

    Error Codes:
        - 400: Bad Request - If the input data is invalid.
        - 401: Unauthorized - If the user is not authenticated.
        - 403: Forbidden - If the user does not have the required permissions.
        - 415: Unsupported Media Type - Allowed media types 'application/json' or 'multipart/form-data'
    """
    try:
        # Check content Type
        if request.content_type.startswith("application/json"):
            # Get data from request
            data: dict = request.get_data()
        elif request.content_type.startswith("multipart/form-data"):
            # Get data from request
            data: dict = request.form.to_dict()
            image_file: Optional[FileStorage] = request.files.get("image", None)
            data["image_url"] = image_file
        else:
            # Invalid content type.
            return make_response("Invalid content type", 415)
        # Serializer
        serializer: CreateProductSerializer = CreateProductSerializer(data=data)
        # Validate serializer
        if serializer.is_valid():
            # Create product
            serializer.save()
            return make_response("Product created successfully", 201)
        # Error
        error: list[str] = serializer.errors
        return make_response(error, 400)
    except SQLAlchemyError as e:
        error: str = str(e)
        logger.error(error)
        return make_response("Database error while creating product", 500)
    except Exception as e:
        error: str = str(e)
        logger.error(error)
        return make_response("Failed to create product", 400)


# Create API to grab product by id
@products_api.route("/<int:product_id>", methods=["GET"])
def get_product_by_id(product_id: int) -> Response:
    """
    Get a product by id

    Args:
        product_id (int): The id of the product to retrieve.

    Returns:
        Response: The product with the specified id and status 200.

    Error Codes:
        - 404: Not Found - If the product is not found.
    """
    # Logic to get product by id
    data: dict = {
        "id": product_id,
    }
    # Serializer
    serializer: GetProductSerializer = GetProductSerializer(data=data)
    try:
        # Validate serializer
        if serializer.is_valid():
            # Return product details
            return make_response(serializer.data, 200)
        # Error
        error: list[str] = serializer.errors
        return make_response(error, 400)
    except Exception as e:
        error: str = str(e)
        logger.error(error)
        return make_response("Failed to grab product information", 404)


# API to update a product
@products_api.route("/<int:product_id>", methods=["PUT"])
@authentication_classess([JWTAuthentication])
@permission_required([IsAdmin])
def update_product(product_id: int, *args, **kwargs) -> Response:
    """
    Update a product

    Args:
        product_id (int): Product ID

    Returns:
        Response: A success message with status 200.

    Error Codes:
        - 400: Bad Request - If the input data is invalid.
        - 401: Unauthorized - If the user is not authenticated.
        - 403: Forbidden - If the user does not have the required permissions.
        - 404: Not Found - If the product is not found.
    """
    try:
        # Check content Type
        if request.content_type.startswith("application/json"):
            # Get data from request
            data: dict = request.get_json()
        elif request.content_type.startswith("multipart/form-data"):
            # Get data from request
            data: dict = request.form.to_dict()
            image_file: Optional[FileStorage] = request.files.get("image", None)
            data["image_url"] = image_file
        else:
            # Invalid content type.
            return make_response("Invalid content type", 415)
        # Check product id exists within the data
        if "id" not in data:
            # if does not exists embed the product_id as data['id']
            data["id"] = product_id
        # Serializer
        serializer: UpdateProductSerializer = UpdateProductSerializer(data=data)
        # Validate serializer
        if serializer.is_valid():
            # Update product
            serializer.save()
            return make_response("Product updated successfully", 200)
        # Logic to update product
        error: list[str] = serializer.errors
        return make_response(error, 400)
    except SQLAlchemyError as e:
        error: str = str(e)
        logger.error(error)
        return make_response("Database error while updating product", 500)
    except Exception as e:
        error: str = str(e)
        logger.error(error)
        return make_response("Failed to update product", 400)


# API to delete a product
@products_api.route("/<int:product_id>", methods=["DELETE"])
@authentication_classess([JWTAuthentication])
@permission_required([IsAdmin])
def delete_product(product_id: int, *args, **kwargs) -> Response:
    """
    Delete a product

    Args:
        product_id (int): Product ID

    Returns:
        Response: A success message with status 200.

    Error Codes:
        - 401: Unauthorized - If the user is not authenticated.
        - 403: Forbidden - If the user does not have the required permissions.
        - 404: Not Found - If the product is not found.
    """
    # Create data
    data: dict = {
        "id": product_id,
    }
    # Serializer
    serializer: GetProductSerializer = GetProductSerializer(data=data)
    try:
        # Validate data
        if serializer.is_valid():
            # Logic to delete product
            serializer.delete()
            return make_response("Product deleted successfully", 200)
        # error
        error: list[str] = serializer.errors
        return make_response(error, 400)
    except SQLAlchemyError as e:
        error: str = str(e)
        logger.error(error)
        return make_response("Database error while deleting product", 500)
    except Exception as e:
        error: str = str(e)
        logger.error(error)
        return make_response("Failed to delete product", 404)


# API to grab all products
@products_api.route("", methods=["GET"])
def get_all_products(*args, **kwargs) -> Response:
    """
    Get all products

    Returns:
        Response: A list of all products with status 200.

    Query Parameters:
        - category (str, optional): Filter products by category.
        - search (str, optional): Search products by name or description.
        - sort_by (str, optional): Sort products by specified field (e.g., price, name).
        - start (int, optional): Specify the page number for pagination.
        - products (int, optional): Specify the number of products per page for pagination.
        - low_price (int, optional): Specify the lowest price for product.
        - high_price (int, optional): Specify the highest price for the product.
        - sale (bool, optional): Specify the sale for the product.

    Error Codes:
        - 404: Not Found - If no products are found.
    """
    queries: dict = request.args.to_dict()
    try:
        serialized_products: list[dict] = GetProductSerializer.get_products(queries)
        # Logic to get all products
        return make_response(serialized_products, 200)
    except ValidationError as e:
        # Grab error to logs
        errors: list = e.errors()
        return make_response(errors, 404)
    except (InvalidCategoriesOption, InvalidCategoriesDelimiter) as e:
        # Grab error to logs
        error: str = str(e)
        logger.error(error)
        return make_response("Forbidden Request", 403)
    except SQLAlchemyError as e:
        # Grab error to logs
        error: str = str(e)
        logger.error(error)
        return make_response("Failed to retrieve products", 500)
    except Exception as e:
        error: str = str(e)
        logger.error(error)
        return make_response("Failed to retrieve products", 500)
