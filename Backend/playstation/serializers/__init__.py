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
    ToInstance,
)
from typing import Self, NoReturn, Optional, Iterable


# Serializer Interface
class SerializerInterface(
    AbstractSerializer,
    Validatable,
    Saveable,
    Updatable,
    Deletable,
    Representable,
    Creatable,
    ToInstance,
):
    pass


# Serializer class
class Serializer(SerializerInterface):
    @property
    def data(self: Self) -> dict:
        """
        Property to get data
        """
        # Check instance
        if self.instance:
            return self.to_representation(self.instance)
        # Return self._data
        return self.validated_data

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
        if self.validate(data):
            # Create validated_data
            self._validated_data: dict = data
            return True
        # Data not valid
        return False

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
        # Check data keys if match the fields of the model or mismatch
        self.__validate_data_fields(data)
        # Get all validate methods
        validate_methods: list[str] = self.__validate_methods()

        # Check Validation methods
        if validate_methods:
            for method in validate_methods:
                try:
                    # Grab the field
                    field: Optional[str] = data.get(method.replace("validate_", ""))
                    # Call each validation method
                    self._data[field] = getattr(self, method)(field)
                except Exception as e:
                    self.errors.append(str(e))

        return not bool(self.errors)

    def __validate_data_fields(self: Self, data: dict) -> Optional[NoReturn]:
        """
        Method used to validate data fields
        """
        # Grab fields
        fields: set = {
            key for key in self.model.__dict__.keys() if not key.startswith("_")
        }
        # Check if data keys match with fields
        for key in data.keys():
            if key not in fields:
                raise ValueError(f"Invalid field: {key}")

    def __validate_methods(self: Self) -> list[str]:
        """
        Method to retrieve a list of validation callable methods.

        Returns:
            - list of (callable) methods
        """
        return [
            method
            for method in dir(self)
            if method.startswith("validate_")
            if callable(getattr(self, method))
        ]

    def save(self: Self) -> object:
        """
        Method to create new instance of an object or update an existing object

        Returns:
            - Instance of the model.
        """
        # Grab the data
        data: Optional[dict] = getattr(self, "validated_data", None)
        # Check data
        if data is None:
            raise ValueError("No validated data found")
        # Check if save method exists
        self.__check_save()
        # Check if object instance exists or not
        # Grab object id
        object_id: Optional[int] = data.get("id", None)
        instance: Optional[None] = None
        # Check if id exists
        if object_id:
            # Check if object instance exists or not
            instance: object = self.model.query.get(object_id)
            if instance:
                # Update instance
                self.instance = self.update(data, instance)
                return self.instance
        # Else perform create new instance method
        self.instance = self.create(data)
        # Return the instance
        return self.instance

    def __check_save(self: Self) -> Optional[NoReturn]:
        """
        Checker function to check if model object has a method .save()

        Raises:
            - Error in case the model does not have a method .save()
        """
        if not hasattr(self.model, "save"):
            raise AttributeError("Model object must have a method .save()")

    def update(self: Self, validated_data: dict, instance: object) -> object:
        """
        Method to update an existing object
        """
        # Implement update logic here
        for key, value in validated_data.items():
            # Check if model has the key and key is not in read_only fields
            if hasattr(self.model, key) and key not in self.read_only:
                setattr(instance, key, value)
        # Save
        instance.save()
        # Return instance
        return instance

    def delete(self: Self) -> None:
        """
        Method to delete an existing object
        """
        # Implement delete logic here
        instance: object = self.instance
        # Check instance
        if not instance:
            raise ValueError("Instance does not exist")
        # Perform delete function
        if not hasattr(instance, "delete"):
            raise AttributeError("Model object must have a method .delete()")
        # Initiate delete instance
        instance.delete()

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
        """
        Convert the model instance into a dictionary representation.
        """
        # Implement representation logic here
        fields: list[str] = self.fields
        # Serialize
        serialized_data: dict = {
            field: getattr(instance, field)
            for field in fields
            if field not in self.write_only
        }
        # Return Serialized data
        return serialized_data

    def to_instance(self, find_by: str = "id") -> Optional[object]:
        """
        Convert the dictionary representation into a model instance.
        """
        # Implement instance creation logic here
        if self._data:
            instance: object = self.model.query.get(self._data[find_by])
            return instance
        return None


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

        # Treat instance as many instances
        if self.many:
            if not isinstance(self.instance, list):
                raise TypeError("Expected a list of instances with many set to True")
            return [self.to_representation(instance) for instance in self.instance]
        # Call to_representation method
        return self.to_representation(model)
