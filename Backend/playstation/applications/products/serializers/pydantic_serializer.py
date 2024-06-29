"""
# Module contains serializers for product query api
"""

from playstation import serializers
from playstation.models.products import Product, Category
from pydantic import (
    BaseModel,
    StrictInt,
    StrictStr,
    field_validator,
    ConfigDict,
    Field
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
    # Configuration Pydantic V2
    model_config = ConfigDict(
        extra = 'forbid',
        validate_default = True, # Ensure default values are validated
        use_enum_values = True  # Serialize enum fields using their values
    )

    # Fields
    category: Union[StrictInt, StrictStr] = 'all'  # Field that can be an int (ID) or the string "all"
    search: Optional[StrictStr] = None  # Optional Field
    sort_by: SortByChoices = SortByChoices.date  # Optional Field
    start: int = Field(0, ge=0)  # Optional Field, int
    products: int = Field(10, ge=10, le=40)  # Optional Field, int
    low_price: Optional[int] = Field(None, ge=0)  # Optional Field, int or None
    high_price: Optional[int] = Field(None, ge=0)  # Optional Field, int or None
    sale: bool = False  # Optional Field, StrictBool

    @field_validator('category')
    @classmethod
    def check_category(cls, v: str):
        """Check if category is valid"""
        if isinstance(v, str) and v != 'all' and v.isalpha():
            # By default return all
            return "all"
        return v