"""
# Pydantic Models for Shipping Addresses Application
"""

from pydantic import BaseModel, ConfigDict


# Pydantic Serializer for the shipping address
class CreateShippingAddress(BaseModel):
    # Configuration for Pydantic V2
    model_config = ConfigDict(
        extra="forbid",  # Forbid extra fields not defined in the model
    )
    user_id: int
    address: str
    city: str
    state: str = "N/A"
    country: str
    default: bool = False


class UpdateShippingAddress(BaseModel):
    # Configuration for Pydantic V2
    model_config = ConfigDict(
        extra="forbid",  # Forbid extra fields not defined in the model
    )
    id: int
    user_id: int
    address: str
    city: str
    state: str
    country: str
    default: bool
