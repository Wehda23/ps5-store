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
    Creatable,
)
from typing import Self, NoReturn, Optional


# Serializer Interface
class SerializerInterface(
    AbstractSerializer,
    Validatable,
    Saveable,
    Updatable,
    Deletable,
    Representable,
    Creatable
):
    pass


# Serializer class
class Serializer(SerializerInterface):
    @property
    def data(self: Self) -> dict:
        """
        Property to get data
        """
        # Return self._data
        return self._data

    @property
    def validated_data(self: Self) -> dict:
        """
        Property to get validated data

        Returns:
            - Python Dictionary of the validated data
        """
        # Check validated data
        if not hasattr(self, "_validated_data"):
            raise Exception("You Should run .is_valid() method first to validate data.")
        # Return validated_data
        return self._validated_data

    def is_valid(self: Self) -> bool:
        """
        Method to validate data

        Returns:
            - True incase data validation passes otherwise False
        """
        # Implement validation logic here
        # Grab the data
        data: Optional[dict] = self._data

        # Check data
        self.__data_checker()

        # validate data
        self.validate(data)

        # Create validated_data
        self._validated_data: dict = data

    def __data_checker(self: Self) -> Optional[NoReturn]:
        """
        Method used to check private attribute _data
        """
        # Grab data
        data: Optional[dict] = self._data
        # Check if it is not None
        if data is None:
            raise ValueError("data: parameter should not be None")
        # Check datatype for self._data
        if not isinstance(data, dict):
            raise TypeError("data: parameter should be of type dictionary")

    def validate(self: Self, data: dict) -> bool:
        """
        Method used to validate data.

        Returns:
            - bool True in case of validated otherwise False
        """
        # Implement your validation logic here
        return super().validate()

    def save(self: Self) -> object:
        # Implement save logic here
        pass

    def update(self: Self) -> object:
        # Implement update logic here
        pass

    def delete(self: Self) -> None:
        # Implement delete logic here
        pass

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

    def to_representation(self, instance: object) -> dict:
        # Implement representation logic here
        pass


# Model Serializer
class ModelSerializer(Serializer):
    @property
    def data(self: Self) -> dict:
        """
        Property to get serialized model
        """
        # Get the model
        model: object = self.instance
        # Check model
        if model is None:
            raise ValueError("Model instance is not provided")
        # Call to_representation method
        return self.to_representation(model)