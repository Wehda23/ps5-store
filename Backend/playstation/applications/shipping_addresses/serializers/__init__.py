"""
# Serializer package for Shipping Addressses Application
"""

from playstation import serializers
from playstation.models.shipping_address import ShippingAddress
from playstation.models.users import User
from playstation.applications.users.serializers import UserSerializer
from playstation.models.exceptions import UserShippingAddressRelation
from .pydantic_serializer import CreateShippingAddress, UpdateShippingAddress
from .validators import UserExists, DefaultAddressExists, ShippingAddressExists
from typing import Self, Optional


# Create Serializer to grab all shipping_addresses
class ShippingAddressSerializer(serializers.ModelSerializer):
    user: UserSerializer = UserSerializer() # Must initiate serializer

    class Meta:
        model: ShippingAddress = ShippingAddress
        fields: str = "__all__"  # Grab all fields

    @classmethod
    def get_shipping_addresses(
        cls: "ShippingAddressSerializer", user: User, *args, **kwargs
    ) -> list[dict]:
        """Get a shipping address by id"""
        # Shipping Addresses
        addresses: list[ShippingAddress] = getattr(user, "shipping_addresses", None)
        # Empty Addresses
        if addresses is None:
            raise UserShippingAddressRelation(
                "No Shipping Addresses RelationShip Established/Wrong Attribute Call"
            )
        # Return serialized shipping addresses
        return ShippingAddressSerializer(instance=addresses, many=True).data


# Serializer to create Shipping Address
class ShippingAddressCreateSerializer(serializers.Serializer):
    """Serializer to create Shipping Address"""

    pydantic_model: CreateShippingAddress = CreateShippingAddress

    class Meta:
        model: ShippingAddress = ShippingAddress
        fields: list[str] = [
            "user_id",
            "address",
            "city",
            "state",
            "country",
            "default",
        ]

    def validate_user_id(self: Self, value: int) -> int:
        """Validate user_id is a valid user_id"""
        # Validate user_id is a valid user_id
        UserExists(serializers.SerializerError).validate(value)
        return value

    # Create functionality for create method
    def create(self, validated_data: dict) -> object:
        """Create a shipping address for a user"""
        # Grab the default field
        default: bool = validated_data.get("default", False)
        # Grab the user id
        user_id: int = validated_data.get("user_id")
        # Check if default is set to true
        if default == True:
            # Call existing default to check if default address exists and set it to false
            self._existing_default(user_id)
        # Create the object
        return super().create(validated_data)

    def _existing_default(self, user_id: int) -> None:
        """Check if user has a shipping_addresses with default == True"""
        # Grab default address
        existing_default: Optional[ShippingAddress] = DefaultAddressExists.validate(
            user_id
        )
        # Check if it exists update it's default field
        if existing_default is not None:
            # Update it
            existing_default.default = False
            existing_default.save()


# Update Shipping Address Serializer
class ShippingAddressUpdateSerializer(serializers.Serializer):
    """Serializer to update Shipping Address"""

    pydantic_model: UpdateShippingAddress = UpdateShippingAddress

    class Meta:
        model: ShippingAddress = ShippingAddress
        fields: list[str] = [
            "address",
            "city",
            "state",
            "country",
            "user_id",
            "id",
            "default",
        ]

    def validate_user_id(self, value: int) -> int:
        """Validate user_id is a valid user_id"""
        # Validate user_id is a valid user_id
        UserExists(serializers.SerializerError).validate(value)
        return value

    def validate_id(self, value: int) -> int:
        """Validate id is a valid id"""
        data: dict = {"user_id": self._data["user_id"], "id": value}
        # Validate id is a valid id and if the user owns this address instance
        ShippingAddressExists(serializers.SerializerError).validate(data)
        return value

    def update(self, validated_data: dict) -> ShippingAddress:
        """Update a shipping address for a user"""
        # Grab the default field
        default: bool = validated_data.get("default", False)
        # Grab the user id
        user_id: int = validated_data.get("user_id")
        # Check if default is set to true
        if default == True:
            # Call existing default to check if default address exists and set it to false
            self._existing_default(user_id)
        # Update the object
        return super().update(validated_data)

    def _existing_default(self, user_id: int) -> None:
        """Check if user has a shipping_addresses with default == True"""
        # Grab default address
        existing_default: Optional[ShippingAddress] = DefaultAddressExists.validate(
            user_id
        )
        # Check if it exists update it's default field
        if existing_default is not None:
            # Update it
            existing_default.default = False
            existing_default.save()

    # Override Create method
    def create(self, validated_data: dict) -> None:
        pass


# Delete Serializer
class DeleteShippingAddressSerializer(serializers.Serializer):
    """Delete a shipping address for a user"""

    class Meta:
        model: ShippingAddress = ShippingAddress
        fields: list[str] = ["user_id", "id"]

    def validate_id(self, value: int) -> int:
        """Validate id is a valid id"""
        data: dict = {"user_id": self._data["user_id"], "id": value}
        # Validate id is a valid id and if the user owns this address instance
        ShippingAddressExists(serializers.SerializerError).validate(data)
        # Assign an instance
        self.instance: ShippingAddress = ShippingAddress.query.get(value)
        # Return Id
        return value
