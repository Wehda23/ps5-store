"""
# File Contains Orders Model & Methods
"""

from playstation import db, SQLMixin
from playstation.models.junction_models import order_product


# Orders Model
class Orders(db.Model, SQLMixin):
    # Basic
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    order_date = db.Column(db.DateTime, default=db.func.current_timestamp())
    total_amount = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(50), nullable=False)

    # Foreign Keys
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=True)
    shipping_address_id = db.Column(
        db.Integer, db.ForeignKey("shipping_address.id"), nullable=True
    )
    payment_id = db.Column(db.Integer, db.ForeignKey("payments.id"), nullable=True)
    coupon_id = db.Column(db.Integer, db.ForeignKey("coupons.id"), nullable=True)

    # Relationships
    user = db.relationship("User", back_populates="orders")  # One User to Many Orders
    shipping_address = db.relationship(
        "ShippingAddress", back_populates="orders"
    )  # One Address to Many Orders
    products = db.relationship(
        "Product", secondary=order_product, back_populates="orders"
    )  # Many Products to Many Orders
    payment = db.relationship("Payments", back_populates="order")

    def __repr__(self) -> str:
        """
        Method for representation
        """
        return f"<{self.__class__.__name__} {self.id}>"
