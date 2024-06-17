"""
# Serializer Models
"""
from .serializer import (
    AbstractSerializer,
    Validatable,
    Saveable,
    Updatable,
    Deletable,
    Representable,
    InternalValueConvertible,
    Creatable
)
from typing import Self, Optional


# Serializer Interface
class SerializerInterface(
    AbstractSerializer,
    Validatable,
    Saveable,
    Updatable,
    Deletable,
    Representable,
    InternalValueConvertible,
):
    pass


# Serializer class
class Serializer(SerializerInterface):
    def is_valid(self: Self) -> bool:
        # Implement validation logic here
        pass

    def save(self: Self) -> object:
        # Implement save logic here
        pass

    def update(self: Self) -> object:
        # Implement update logic here
        pass

    def delete(self: Self) -> None:
        # Implement delete logic here
        pass

    def to_representation(self, instance: object) -> dict:
        # Implement representation logic here
        pass

    def to_internal_value(self, data: dict) -> object:
        # Implement conversion logic here
        pass


# =====> Model Serializer
class ModelSerializerInterface(SerializerInterface, Creatable):
    pass

# Form Serializer
class ModelSerializer(ModelSerializerInterface):
    def create(self, validated_data: dict) -> object:
        """
        Create a new instance of the model.

        Args:
            - validated_data (dict): Validated data of the parameters of new instance.

        Returns:
            - Newly created instance of the model.
        """
        # Create the model
        instance = self.model(**validated_data)
        # Create instance
        instance.save()
        # Return the instance
        return instance