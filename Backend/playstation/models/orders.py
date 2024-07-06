"""
# This file contains the model and methods related to Orders in the database.
"""

from playstation import db, SQLMixin
from playstation.models.junction_models import order_product


class Orders(db.Model, SQLMixin):
    """
    Represents an Order in the database.

    Attributes:
        id (int): Primary key.
        order_date (datetime): Date and time when the order was placed.
        total_amount (float): Total amount of the order.
        status (str): Status of the order.
        user_id (int): Foreign key referencing User.
        shipping_address_id (int): Foreign key referencing ShippingAddress.
        coupon_id (int): Foreign key referencing Coupons.
    """

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    order_date = db.Column(db.DateTime, default=db.func.current_timestamp())
    total_amount = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(50), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=True)
    shipping_address_id = db.Column(db.Integer, db.ForeignKey("shipping_address.id"), nullable=True)
    coupon_id = db.Column(db.Integer, db.ForeignKey("coupons.id"), nullable=True)
    user = db.relationship("User", back_populates="orders")
    shipping_address = db.relationship("ShippingAddress", back_populates="orders")
    products = db.relationship("Product", secondary=order_product, back_populates="orders")
    payment = db.relationship("Payments", back_populates="order", uselist=False)
    coupon = db.relationship("Coupons", back_populates="orders")

    def __repr__(self) -> str:
        """
        String representation of the Orders instance.

        Returns:
            str: String representation of the Orders instance.
        """
        return f"<{self.__class__.__name__} {self.id}>"
