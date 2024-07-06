"""
# Folder that Contains classes/methods for Products & Categories Models
"""

from playstation import db, SQLMixin
from playstation.models.junction_models import order_product
from typing import Self
from sqlalchemy import CheckConstraint
from playstation.settings import MEDIA_DIR
import os


# Products model
class Product(db.Model, SQLMixin):
    # Basics
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(256), nullable=False)
    description = db.Column(db.String(2056), nullable=True)
    price = db.Column(db.Float, nullable=False)
    discount = db.Column(
        db.Float,
        CheckConstraint("discount >= 0 AND discount <= 100"),
        nullable=False,
        default=0,
    )
    stock = db.Column(db.Integer, nullable=False)
    image_url = db.Column(
        db.String(2056), default=os.path.join(MEDIA_DIR, "default.png"), nullable=False
    )

    # Permissions and Status
    is_sale = db.Column(db.Boolean, default=False, nullable=False)

    # Dates
    created_at = db.Column(
        db.DateTime, nullable=False, default=db.func.current_timestamp()
    )
    updated_at = db.Column(
        db.DateTime,
        nullable=False,
        default=db.func.current_timestamp(),
        onupdate=db.func.current_timestamp(),
    )

    # Relationship
    category_id = db.Column(db.Integer, db.ForeignKey("category.id"), nullable=False)
    orders = db.relationship(
        "Order", secondary=order_product, back_populates="products"
    )

    def __repr__(self: Self):
        """
        Method for representation
        """
        return f"<{self.__class__.__name__} {self.name}>"


class Category(db.Model, SQLMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(256), nullable=False)

    def __repr__(self: Self):
        """
        Method for representation
        """
        return f"<{self.__class__.__name__} {self.name}>"
