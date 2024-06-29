"""
# Module contains serializers for product query api
"""

from playstation import serializers
from playstation.models.products import Product, Category
from pydantic import (
    BaseModel,
    StrictInt,
    StrictStr,
    StrictBool,
    field_validator
)
from typing import Union, Optional
from enum import Enum

# Choices for sort
class SortByChoices(str, Enum):
    price = "price"
    price_desc = "price_desc"
    name = "name"
    name_desc = "name_desc"
    date = "date"
    date_desc = "date_desc"

class ProductsQuery(BaseModel):
    """Serializer for product query api"""

    category: Union[StrictInt, StrictStr] = 'all'  # Field that can be an int (ID) or the string "all"
    search: Optional[StrictStr] = None  # Optional Field
    sort_by: SortByChoices = SortByChoices.date  # Optional Field
    start: StrictInt = 0  # Optional Field, StrictInt
    products: StrictInt = 10  # Optional Field, StrictInt
    low_price: Optional[StrictInt] = None  # Optional Field, StrictInt or None
    high_price: Optional[StrictInt] = None  # Optional Field, StrictInt or None
    sale: StrictBool = False  # Optional Field, StrictBool

    class Config:
        extra = 'forbid'
        validate_default = True # Ensure default values are validated
        use_enum_values = True  # Serialize enum fields using their values

    @field_validator('category')
    @classmethod
    def check_category(cls, v):
        if isinstance(v, str) and v != 'all':
            raise ValueError('Category must be an integer or the string "all"')
        return v