"""
Application that handles the Shipping Addresses API

This application manages all shipping address-related actions, including creation, updates, and deletion. It defines API routes to facilitate these actions, ensuring secure and efficient management of shipping addresses.

## API Routes

### Protected Routes
These routes require authentication and appropriate permissions to access:

- **/api/shipping_addresses: Retrieve a user's shipping addresses.
  - Method: GET
  - Description: Fetches all shipping addresses associated with the authenticated user.
  - Authentication: JWT required

- **/api/shipping_addresses: Create a new shipping address.
  - Method: POST
  - Description: Allows users to create a new shipping address.
  - Authentication: JWT required

- **/api/shipping_addresses/<int:address_id>: Update a shipping address.
  - Method: PUT
  - Description: Allows users to update an existing shipping address by its ID.
  - Authentication: JWT required
  - Permissions: Account owner required

- **/api/shipping_addresses/<int:address_id>: Delete a shipping address.
  - Method: DELETE
  - Description: Allows users to delete an existing shipping address by its ID.
  - Authentication: JWT required
  - Permissions: Account owner required
"""

from flask import current_app, make_response, request, Response
from playstation.admin.permissions import permission_required
from playstation.admin.authentications import authentication_classess
from playstation.admin.authentications.jwt_authentication import JWTAuthentication
from playstation.admin.authentications.exceptions import UserNotAssignedError
from playstation.models.users import User
from playstation.models.exceptions import UserShippingAddressRelation
from sqlalchemy.exc import SQLAlchemyError
from pydantic import ValidationError
from .permissions import IsAccountOwner
from .serializers import (
    ShippingAddressSerializer,
    ShippingAddressCreateSerializer,
    ShippingAddressUpdateSerializer,
    DeleteShippingAddressSerializer,
)
from . import shipping_addresses_api

# "/api/shipping_addresses"


@shipping_addresses_api.route("/", methods=["GET"])
@authentication_classess(auth_classes=[JWTAuthentication])
def get_addresses(*args, **kwargs) -> Response:
    """
    Retrieve a user's shipping addresses

    Returns:
        Response: A list of the user's shipping addresses with status 200.

    Error Codes:
        - 401: Unauthorized - If the user is not authenticated.
        - 500: Internal Server Error - If an error occurs while retrieving addresses.
    """
    try:
        # Grab user
        user: User = getattr(request, "user", None)
        # Check if user is assigned
        if user is None:
            raise UserNotAssignedError("User not assigned")
        # Get shipping addresses
        shipping_addresses: list[dict] = (
            ShippingAddressSerializer.get_shipping_addresses(user)
        )
        # Return response
        return make_response(shipping_addresses, 200)
    except UserShippingAddressRelation as e:
        current_app.logger.error(str(e))
        return make_response("Something went wrong", 500)
    except UserNotAssignedError as e:
        current_app.logger.error(str(e))
        return make_response("User not assigned", 401)
    except Exception as e:
        current_app.logger.error(e)
        return make_response("Something went wrong", 500)


@shipping_addresses_api.route("/", methods=["POST"])
@authentication_classess(auth_classes=[JWTAuthentication])
def create_address(*args, **kwargs) -> Response:
    """
    Create a new shipping address

    Returns:
        Response: A success message with status 201.

    Error Codes:
        - 400: Bad Request - If the input data is invalid.
        - 401: Unauthorized - If the user is not authenticated.
        - 500: Internal Server Error - If an error occurs while creating the address.
    """
    try:
        # Get the request data
        data = request.get_json()
        # Grab user
        user: User = getattr(request, "user", None)
        # Check if user is assigned
        if user is None:
            raise UserNotAssignedError("User not assigned")
        if "user_id" not in data:
            data["user_id"] = user.id
        # Create serializer
        serializer = ShippingAddressCreateSerializer(data=data)
        # Validate the serializer
        if serializer.is_valid():
            # Save the address
            serializer.save()
            # Return success message
            return make_response("Shipping address created successfully", 201)
        # Error
        error = serializer.errors
        return make_response(error, 400)
    except ValidationError as e:
        error: list[dict] = e.errors()
        return make_response(error, 400)
    except SQLAlchemyError as e:
        current_app.logger.error(e)
        return make_response("Something went wrong", 500)
    except Exception as e:
        current_app.logger.error(str(e))
        print(e)
        return make_response("Failed to create shipping address", 500)


@shipping_addresses_api.route("/<int:address_id>", methods=["PUT"])
@authentication_classess(auth_classes=[JWTAuthentication])
@permission_required(permissions=[IsAccountOwner])
def update_address(address_id: int, *args, **kwargs) -> Response:
    """
    Update a shipping address

    Args:
        address_id (int): The ID of the address to update.

    Returns:
        Response: A success message with status 200.

    Error Codes:
        - 400: Bad Request - If the input data is invalid.
        - 401: Unauthorized - If the user is not authenticated.
        - 403: Forbidden - If the user does not have the required permissions.
        - 404: Not Found - If the address is not found.
        - 500: Internal Server Error - If an error occurs while updating the address.
    """
    try:
        # Get the request data
        data = request.get_json()
        # Check if address_id is in the data
        if "id" not in data:
            data["id"] = address_id
        # Create serializer
        serializer = ShippingAddressUpdateSerializer(data=data)
        # Validate the serializer
        if serializer.is_valid():
            # Update the address
            serializer.save()
            # Return success message
            return make_response("Shipping address updated successfully", 200)
        # Error
        error = serializer.errors
        return make_response(error, 400)
    except ValidationError as e:
        error: list[dict] = e.errors()
        return make_response(error, 400)
    except SQLAlchemyError as e:
        current_app.logger.error(e)
        return make_response("Something went wrong", 500)
    except Exception as e:
        current_app.logger.error(str(e))
        return make_response("Failed to update shipping address", 500)


@shipping_addresses_api.route("/<int:address_id>", methods=["DELETE"])
@authentication_classess(auth_classes=[JWTAuthentication])
@permission_required(permissions=[IsAccountOwner])
def delete_address(address_id: int, *args, **kwargs) -> Response:
    """
    Delete a shipping address

    Args:
        address_id (int): The ID of the address to delete.

    Returns:
        Response: A success message with status 200.

    Error Codes:
        - 401: Unauthorized - If the user is not authenticated.
        - 403: Forbidden - If the user does not have the required permissions.
        - 500: Internal Server Error - If an error occurs while deleting the address.
    """
    try:
        # Create data dictionary
        data = {"id": address_id}
        # Create serializer
        serializer = DeleteShippingAddressSerializer(data=data)
        # Validate the serializer
        if serializer.is_valid():
            # Delete the address
            serializer.delete()
            # Return success message
            return make_response("Shipping address deleted successfully", 200)
        # Error
        error = serializer.errors
        return make_response(error, 400)
    except SQLAlchemyError as e:
        current_app.logger.error(e)
        return make_response("Something went wrong", 500)
    except Exception as e:
        current_app.logger.error(str(e))
        return make_response("Failed to delete shipping address", 500)
