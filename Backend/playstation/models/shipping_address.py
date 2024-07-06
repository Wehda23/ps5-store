"""
# This file contains the model and methods related to Shipping Addresses in the database.
"""

from playstation import db, SQLMixin
from typing import Self


class ShippingAddress(db.Model, SQLMixin):
    """
    Represents a shipping address in the database.

    Attributes:
        id (int): Primary key.
        user_id (int): Foreign key referencing User.
        address (str): Street address.
        city (str): City of the address.
        state (str): State of the address.
        country (str): Country of the address.
        default (bool): Whether this is the default shipping address for the user.
    """

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=True)
    address = db.Column(db.String(256), nullable=False)
    city = db.Column(db.String(128), nullable=False)
    state = db.Column(db.String(128), nullable=False)
    country = db.Column(db.String(128), nullable=False)
    default = db.Column(db.Boolean, default=False, nullable=False)

    user = db.relationship("User", back_populates="shipping_addresses")
    orders = db.relationship("Orders", back_populates="shipping_address")

    def __repr__(self: Self) -> str:
        """
        String representation of the ShippingAddress instance.

        Returns:
            str: String representation of the ShippingAddress instance.
        """
        return f"<{self.__class__.__name__} {self.id}>"
