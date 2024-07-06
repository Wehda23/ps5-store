"""
# File that contains a model Coupons and it's methods
"""

from playstation import db, SQLMixin
from .junction_models import user_coupons
from typing import Self


class Coupons(db.Model, SQLMixin):
    # Basic
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    code = db.Column(db.String(100), nullable=False, unique=True)
    discount = db.Column(db.Float, nullable=False)
    expiration_date = db.Column(db.DateTime, nullable=False)
    # Relationships
    orders = db.relationship("Orders", back_populates="coupon")
    users = db.relationship("User", secondary=user_coupons, back_populates="coupons")

    def __repr__(self: Self) -> str:
        """
        Method for representation
        """
        return f"<{self.__class__.__name__} {self.id}>"
