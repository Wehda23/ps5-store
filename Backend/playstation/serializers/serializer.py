"""
# File that contains abstract classes for how serializer should be implemented.
"""

from abc import ABC, abstractmethod
from typing import Optional, Iterable, Self
from pydantic import BaseModel


# Abstract Serializer
class AbstractSerializer(ABC):
    """
    Abstract class for serializer implementation.
    """

    def __init__(
        self,
        instance: Optional[object] = None,
        data: Optional[dict] = None,
        many: bool = False,
    ) -> None:
        self.instance: Optional[object] = instance
        self._data: Optional[dict] = data
        self.many: bool = many
        self._errors = []
        self._meta = self.get_meta()  # Access Meta Class
        self._fields: Optional[Iterable[str]] = getattr(self._meta, "fields", None)
        self._write_only: Iterable[str] = getattr(self._meta, "write_only", [])
        self._read_only: Iterable[str] = getattr(self._meta, "read_only", {"id"})

        self.fields = self._fields  # Trigger the fields setter
        self.write_only = self._write_only  # Trigger the write_only setter
        self.read_only = self._read_only  # Trigger the read_only setter

    def get_meta(self):
        meta = getattr(self, "Meta", None)
        if meta is None:
            raise AttributeError("Meta class is not defined.")
        return meta

    @property
    def data(self) -> dict:
        """
        Property to get serialized model
        """
        raise NotImplementedError("data property must be implemented by subclasses")

    @property
    def model(self):
        return getattr(self._meta, "model", None)

    @property
    def fields(self) -> Optional[Iterable[str]]:
        return self._fields

    @fields.setter
    def fields(self, serializer_fields: Optional[Iterable[str]]) -> None:
        """
        Setter property method for fields.

        Args:
            - serializer_fields (Iterable Python Object): Fields for serializer.
        """
        if serializer_fields is None:
            raise ValueError("Fields cannot be None.")
        fields = [key for key in self.model.__dict__.keys() if not key.startswith("_")]
        if not self.__check_fields(serializer_fields):
            fields = [
                key for key in serializer_fields if self.__existing_field(key, fields)
            ]
        self._fields = fields

    @property
    def write_only(self) -> Iterable[str]:
        return self._write_only

    @write_only.setter
    def write_only(self, serializer_fields: Optional[Iterable[str]]) -> None:
        """
        Setter property method write_only fields.

        Args:
            - serializer_fields (Iterable Python Object): Fields for serializer.
        """
        if serializer_fields is None:
            return
        fields = [key for key in self.model.__dict__.keys()]
        if not self.__check_fields(serializer_fields):
            fields = [
                key for key in serializer_fields if self.__existing_field(key, fields)
            ]
        self._write_only = fields

    @property
    def read_only(self) -> Iterable[str]:
        return self._read_only

    @read_only.setter
    def read_only(self, serializer_fields: Optional[Iterable[str]]) -> None:
        """
        Setter property method read_only fields.

        Args:
            - serializer_fields (Iterable Python Object): Fields for serializer.
        """
        if serializer_fields is None:
            return
        fields = [key for key in self.model.__dict__.keys()]
        if not self.__check_fields(serializer_fields):
            fields = [
                key for key in serializer_fields if self.__existing_field(key, fields)
            ]
        self._read_only = fields

    def __existing_field(self, field: str, fields: list[str]) -> bool:
        """
        Check if field exists in fields.
        """
        if field not in fields:
            raise ValueError(f"Field '{field}' does not exist in model.")
        return True

    def __check_fields(self, fields: Optional[Iterable[str]]) -> bool:
        """
        Helper function to check fields specified fields against '__all__'

        Args:
            - fields (Optional[Iterable[str]]): Fields

        Returns:
            - True in case all fields otherwise False
        """
        if isinstance(fields, str) and fields == "__all__":
            return True
        if isinstance(fields, list) and len(fields) == 1 and fields[0] == "__all__":
            return True
        return False

    @property
    def errors(self) -> Optional[list]:
        return self._errors


class Validatable(ABC):
    @property
    def validated_data(self) -> dict:
        pass

    @abstractmethod
    def is_valid(self) -> bool:
        pass

    @abstractmethod
    def validate(self) -> bool:
        pass


class Saveable(ABC):
    @abstractmethod
    def save(self) -> object:
        pass


class Updatable(ABC):
    @abstractmethod
    def update(self) -> object:
        pass


class Deletable(ABC):
    @abstractmethod
    def delete(self) -> None:
        pass


class Representable(ABC):
    @abstractmethod
    def to_representation(self, instance: object) -> dict:
        pass


class Creatable(ABC):
    @abstractmethod
    def create(self, validated_data: dict) -> dict:
        pass


class ToInstance(ABC):
    @abstractmethod
    def to_instance(self, data: dict) -> object:
        pass


class ExtendsPydantic(ABC):
    pydantic_model: Optional[BaseModel] = None

    @abstractmethod
    def validate_pydantic(self: Self, data: dict) -> None:
        pass
