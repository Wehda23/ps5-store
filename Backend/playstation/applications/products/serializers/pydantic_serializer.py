"""
# Module: products_query_serializer
# This module contains serializers for the product query API.
# It includes the definition of query parameters and validation logic using Pydantic.
"""

from pydantic import BaseModel, StrictInt, StrictStr, field_validator, ConfigDict, Field
from typing import Union, Optional
from enum import Enum
from .exceptions import InvalidCategoriesDelimiter, InvalidCategoriesOption


# Enum for sorting choices
class SortByChoices(str, Enum):
    """
    Enum class for sorting options.
    """

    price = "price"
    price_desc = "price_desc"
    name = "name"
    name_desc = "name_desc"
    date = "date"
    date_desc = "date_desc"


class ProductsQuery(BaseModel):
    """
    Serializer for product query API.
    Defines the query parameters and their validation logic using Pydantic.
    """

    # Configuration for Pydantic V2
    model_config = ConfigDict(
        extra="forbid",  # Forbid extra fields not defined in the model
        validate_default=True,  # Ensure default values are validated
        use_enum_values=True,  # Serialize enum fields using their values
    )

    # Fields
    category: Union[StrictInt, StrictStr] = (
        "all"  # Field that can be an int (ID) or the string "all"
    )
    search: Optional[StrictStr] = None  # Optional search field
    sort_by: SortByChoices = (
        SortByChoices.date
    )  # Optional sort by field, default is 'date'
    start: int = Field(0, ge=0)  # Optional start field, must be >= 0
    products: int = Field(
        10, ge=10, le=40
    )  # Optional products field, must be between 10 and 40
    low_price: Optional[int] = Field(
        None, ge=0
    )  # Optional low price field, must be >= 0
    high_price: Optional[int] = Field(
        None, ge=0
    )  # Optional high price field, must be >= 0
    sale: bool = False  # Optional sale field, default is False

    @field_validator("category")
    @classmethod
    def check_category(cls, v: str):
        """
        Validator method for the 'category' field.
        Ensures the category is either 'all', an integer, or a valid delimited string of integers.
        """
        if isinstance(v, str) and v != "all":
            if v.isalpha():
                raise InvalidCategoriesOption(
                    f"Only allowed string option is 'all', you entered: {v}"
                )
            # Check if the value is not entirely numeric and not a valid delimited string of numbers
            if not v.isdigit() and not v.replace("-", "").isdigit():
                raise InvalidCategoriesDelimiter(
                    f"Only allowed category delimiter is '-', you entered: {v}"
                )
        return v
