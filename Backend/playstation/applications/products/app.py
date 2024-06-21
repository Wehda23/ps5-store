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

- **/api/products: Get all products.
  - Method: GET
  - Description: Retrieves all products.
"""

from flask import Blueprint, Response, make_response, request
from playstation.admin.authentications import authentication_classess
from playstation.admin.authentications.jwt_authentication import JWTAuthentication
from playstation.admin.permissions import permission_required
from .permissions import IsAdmin

# Declare route prefix
url_prefix: str = "/api/products"

# Blueprint
products_api: Blueprint = Blueprint("products_api", __name__, url_prefix=url_prefix)

# Test API
@products_api.route("", methods=["GET"])
def products_test() -> str:
    """
    Check products API

    Returns:
        str: Message indicating the API is working.
    """
    return "Products API is working!"

# API to Create product category
@products_api.route("/category", methods=['POST'])
@authentication_classess([JWTAuthentication])
@permission_required([IsAdmin])
def create_category(*args, **kwargs) -> Response:
    """
    Create a new product category

    Returns:
        Response: A success message with status 200.
    """
    # Get the request data
    data = request.get_json()
    return make_response("Product Categories", 200)

# API to Grab all product categories
@products_api.route("/categories", methods=['GET'])
@authentication_classess([JWTAuthentication])
def get_categories(*args, **kwargs) -> Response:
    """
    Get all product categories

    Returns:
        Response: A list of all product categories with status 200.
    """
    return make_response("Product Categories", 200)

# API to Update a product category
@products_api.route("/category/<int:category_id>", methods=['PUT'])
@authentication_classess([JWTAuthentication])
@permission_required([IsAdmin])
def update_category(category_id: int, *args, **kwargs) -> Response:
    """
    Update a product category

    Args:
        category_id (int): Category ID

    Returns:
        Response: A success message with status 200.
    """
    return make_response("Product Categories", 200)

# API to Delete a product category
@products_api.route("/category/<int:category_id>", methods=['DELETE'])
@authentication_classess([JWTAuthentication])
@permission_required([IsAdmin])
def delete_category(category_id: int, *args, **kwargs) -> Response:
    """
    Delete a product category

    Args:
        category_id (int): Category ID

    Returns:
        Response: A success message with status 200.
    """
    return make_response("Product Categories", 200)

# API to create new product
@products_api.route("", methods=['POST'])
@authentication_classess([JWTAuthentication])
@permission_required([IsAdmin])
def create_product(*args, **kwargs) -> Response:
    """
    Create a new product

    Returns:
        Response: A success message with status 201.
    """
    return make_response("Product Created", 201)

# API to grab all products
@products_api.route("", methods=['GET'])
def get_all_products(*args, **kwargs) -> Response:
    """
    Get all products

    Returns:
        Response: A list of all products with status 200.
    """
    return make_response("Products", 200)

# API to update a product
@products_api.route("/<int:product_id>", methods=['PUT'])
@authentication_classess([JWTAuthentication])
@permission_required([IsAdmin])
def update_product(product_id: int, *args, **kwargs) -> Response:
    """
    Update a product

    Args:
        product_id (int): Product ID

    Returns:
        Response: A success message with status 200.
    """
    return make_response("Product Updated", 200)

# API to delete a product
@products_api.route("/<int:product_id>", methods=['DELETE'])
@authentication_classess([JWTAuthentication])
@permission_required([IsAdmin])
def delete_product(product_id: int, *args, **kwargs) -> Response:
    """
    Delete a product

    Args:
        product_id (int): Product ID

    Returns:
        Response: A success message with status 200.
    """
    return make_response("Product Deleted", 200)
