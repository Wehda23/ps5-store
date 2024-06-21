"""
# Application that handles the Products API

- This is the application that handles all user related actions such as new account creation, profile updates, registeration, login etc..

## Api routes

##### Protected Routes
- /Products/me: Get the current user's profile
- /Products/me/update: Update the current user's profile
- /Products/me/delete: Delete the current user's account

#### Public Routes
- /Products/register: Register a new user
- /Products/login: Login a user
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
    """
    return "Products API is working!"


# API to Create product category
@products_api.route("/category", methods=["POST"])
@authentication_classess([JWTAuthentication])
@permission_required([IsAdmin])
def create_category(*args, **kwargs) -> Response:
    """
    Create a new product category

    Returns:
        - Response: ...
    """
    # Get the request data
    data = request.get_json()
    return make_response("Product Categories", 200)


# API to Grab all product categories
@products_api.route("/categories", methods=["GET"])
@authentication_classess([JWTAuthentication])
def get_categories(*args, **kwargs) -> Response:
    """
    Get all product categories

    Returns:
        Response: ...
    """
    return make_response("Product Categories", 200)


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
        Response: ...
    """
    return make_response("Product Categories", 200)


# API to Delete a product category
@products_api.route("/category/<int:category_id>", methods=["DELETE"])
@authentication_classess([JWTAuthentication])
@permission_required([IsAdmin])
def update_category(category_id: int, *args, **kwargs) -> Response:
    """
    Delete a product category

    Args:
        category_id (int): Category ID

    Returns:
        Response: ...
    """
    return make_response("Product Categories", 200)


# API to create new product
@products_api.route("", methods=["POST"])
@authentication_classess([JWTAuthentication])
@permission_required([IsAdmin])
def create_product(*args, **kwargs) -> Response:
    """
    Create a new product

    Returns
        Response: ...
    """
    return make_response("Product Created", 201)


# API to grab all products
@products_api.route("", methods=["GET"])
def get_all_products(*args, **kwargs) -> Response:
    """
    Get all products

    Returns
        Response: ...
    """
    return make_response("Products", 200)


# API to update a product
@products_api.route("/<int:product_id>", methods=["PUT"])
@authentication_classess([JWTAuthentication])
@permission_required([IsAdmin])
def update_product(product_id: int, *args, **kwargs) -> Response:
    """
    Update a product

    Args:
        product_id (int): Product ID

    Returns
        Response: ...
    """
    return make_response("Product Updated", 200)


# API to delete a product
@products_api.route("/<int:product_id>", methods=["DELETE"])
@authentication_classess([JWTAuthentication])
@permission_required([IsAdmin])
def delete_product(product_id: int, *args, **kwargs) -> Response:
    """
    Delete a product

    Args:
        product_id (int): Product ID

    Returns
        Response: ...
    """
    return make_response("Product Deleted", 200)
