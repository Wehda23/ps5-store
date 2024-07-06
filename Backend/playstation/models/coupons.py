"""
# This file contains the model and methods related to Coupons in the database.
"""

from playstation import db, SQLMixin
from .junction_models import user_coupons
from typing import Self


class Coupons(db.Model, SQLMixin):
    """
    Represents a Coupon in the database.

    Attributes:
        id (int): Primary key.
        code (str): Unique coupon code.
        discount (float): Discount percentage.
        expiration_date (datetime): Expiration date of the coupon.
        orders (list): List of orders that used this coupon.
        users (list): List of users that used this coupon.
    """

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    code = db.Column(db.String(100), nullable=False, unique=True)
    discount = db.Column(db.Float, nullable=False)
    expiration_date = db.Column(db.DateTime, nullable=False)
    orders = db.relationship("Orders", back_populates="coupon")
    users = db.relationship("User", secondary=user_coupons, back_populates="coupons")

    def __repr__(self: Self) -> str:
        """
        String representation of the Coupons instance.

        Returns:
            str: String representation of the Coupons instance.
        """
        return f"<{self.__class__.__name__} {self.id}>"
