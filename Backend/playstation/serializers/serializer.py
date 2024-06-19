"""
# File that contains abstract classes for how serializer should be implmented.
"""

from abc import ABC, abstractmethod
from typing import Self, Optional, Iterable, NoReturn


# Abstract Serializer
class AbstractSerializer(ABC):
    """
    Abstract class for serializer implementation.
    """

    def __init__(
        self: Self,
        instance: Optional[object] = None,
        data: Optional[dict] = None,
        many: bool = False,
    ) -> None:
        self.instance: object = instance
        self._data: dict = data
        self.many: bool = many
        self._errors = []
        self._meta = self.get_meta()  # Access Meta Class
        self.fields = getattr(self._meta, "fields", None)
        self.write_only: Iterable = getattr(self._meta, "write_only", None)
        self.read_only: Iterable = getattr(self._meta, "read_only", {"id"})

    def get_meta(self: Self):
        meta = getattr(self, "Meta", None)
        if meta is None:
            raise AttributeError("Meta class is not defined.")
        return meta

    @property
    def data(self: Self) -> dict:
        """
        Property to get serialized model
        """
        pass

    @property
    def model(self: Self):
        return getattr(self._meta, "model", None)

    @property
    def fields(self: Self):
        return self._fields

    @fields.setter
    def fields(self: Self, serializer_fields: Optional[Iterable[str]]) -> None:
        """
        Setter propery method for fields.

        Args:
            - serializer_fields (Iterable Python Object): Fields for serializer.
        """
        # Check if fields is a None
        if serializer_fields is None:
            raise ValueError("Fields cannot be None.")

        # Fields
        fields: list[str] = [key for key in self.model.__dict__.keys()]

        # Check if all fields
        if not self.__check_fields(serializer_fields):
            # Implement All fields logic.
            fields: list[str] = [
                key
                for key in fields
                if self.__existing_field(key, fields)
                if key in serializer_fields
            ]

        self._fields: list[str] = fields

    @property
    def write_only(self: Self):
        return self._write_only

    @write_only.setter
    def write_only(self: Self, serializer_fields: Optional[Iterable[str]]) -> None:
        """
        Setter propery method write_only fields.

        Args:
            - serializer_fields (Iterable Python Object): Fields for serializer.
        """
        # Skip if None
        if serializer_fields is None:
            return

        # Fields
        fields: list[str] = [key for key in self.model.__dict__.keys()]

        # Check if all fields
        if not self.__check_fields(serializer_fields):
            # Implement All fields logic.
            fields: list[str] = [
                key
                for key in fields
                if self.__existing_field(key, fields)
                if key in serializer_fields
            ]

        self._write_only: list[str] = fields

    @property
    def right_only(self: Self):
        return self._right_only

    @right_only.setter
    def right_only(self: Self, serializer_fields: Optional[Iterable[str]]) -> None:
        """
        Setter propery method right_only fields.

        Args:
            - serializer_fields (Iterable Python Object): Fields for serializer.
        """
        # Skip if None
        if serializer_fields is None:
            return

        # Fields
        fields: list[str] = [key for key in self.model.__dict__.keys()]

        # Check if all fields
        if not self.__check_fields(serializer_fields):
            # Implement All fields logic.
            fields: list[str] = [
                key
                for key in fields
                if self.__existing_field(key, fields)
                if key in serializer_fields
            ]

        self._right_only: list[str] = fields

    def __existing_field(self: Self, field: str, fields: list[str]) -> NoReturn:
        """
        Check if field exists in fields.
        """
        if not field in fields:
            raise ValueError(f"Field '{field}' does not exist in model.")

    def __check_fields(self: Self, fields: Optional[Iterable[str]]) -> bool:
        """
        Helper function to check fields specified fields against '__all__'

        Args:
            - fields (Optional[Iterable[str]]): Fields

        Returns:
            - True in case all fields otherwise False
        """
        # Check if fields is a str and == "__all__"
        if isinstance(fields, str) and fields == "__all__":
            return True

        # check if a list and contains 1 length
        if len(fields) == 1 and fields[0] == "__all__":
            return True

        return False

    @property
    def errors(self: Self) -> Optional[dict]:
        return self._errors


class Validatable(ABC):
    @property
    def validated_data(self: Self) -> dict:
        pass

    @abstractmethod
    def is_valid(self: Self) -> bool:
        pass

    @abstractmethod
    def validate(self: Self) -> bool:
        pass


class Saveable(ABC):
    @abstractmethod
    def save(self: Self) -> object:
        pass


class Updatable(ABC):
    @abstractmethod
    def update(self: Self) -> object:
        pass


class Deletable(ABC):
    @abstractmethod
    def delete(self: Self) -> None:
        pass


class Representable(ABC):
    @abstractmethod
    def to_representation(self, instance: object) -> dict:
        pass


class Creatable(ABC):
    @abstractmethod
    def create(self, validated_data: dict) -> dict:
        pass
