"""
# This file contains the models and methods related to Products and Categories in the database.
"""

from playstation import db, SQLMixin
from playstation.models.junction_models import order_product
from typing import Self
from sqlalchemy import CheckConstraint
from playstation.settings import MEDIA_DIR
import os


class Product(db.Model, SQLMixin):
    """
    Represents a Product in the database.

    Attributes:
        id (int): Primary key.
        name (str): Product name.
        description (str): Product description.
        price (float): Product price.
        discount (float): Discount on the product, between 0 and 100.
        stock (int): Quantity in stock.
        image_url (str): URL to the product image.
        is_sale (bool): Indicates if the product is on sale.
        created_at (datetime): Timestamp when the product was created.
        updated_at (datetime): Timestamp when the product was last updated.
        category_id (int): Foreign key referencing Category.
    """

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(256), nullable=False)
    description = db.Column(db.String(2056), nullable=True)
    price = db.Column(db.Float, nullable=False)
    discount = db.Column(db.Float, CheckConstraint("discount >= 0 AND discount <= 100"), nullable=False, default=0)
    stock = db.Column(db.Integer, nullable=False)
    image_url = db.Column(db.String(2056), default=os.path.join(MEDIA_DIR, "default.png"), nullable=False)
    is_sale = db.Column(db.Boolean, default=False, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    category_id = db.Column(db.Integer, db.ForeignKey("category.id"), nullable=False)
    orders = db.relationship("Orders", secondary=order_product, back_populates="products")
    category = db.relationship("Category", back_populates="products")

    def __repr__(self: Self) -> str:
        """
        String representation of the Product instance.

        Returns:
            str: String representation of the Product instance.
        """
        return f"<{self.__class__.__name__} {self.name}>"

class Category(db.Model, SQLMixin):
    """
    Represents a Category in the database.

    Attributes:
        id (int): Primary key.
        name (str): Category name.
    """

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(256), nullable=False)
    products = db.relationship("Product", back_populates="category")

    def __repr__(self: Self) -> str:
        """
        String representation of the Category instance.

        Returns:
            str: String representation of the Category instance.
        """
        return f"<{self.__class__.__name__} {self.name}>"
