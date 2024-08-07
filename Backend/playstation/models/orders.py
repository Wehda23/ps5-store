"""
# This file contains the model and methods related to Orders in the database.
"""

from playstation import db, SQLMixin
from sqlalchemy.exc import MultipleResultsFound
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

    def add_product(self, product: object, quantity: int) -> None:
        """
        Adds a product to the order.
        Method must be called right after product has been called.
        """
        # Create an instance of the order_product table to specify the quantity
        order_product_instance = order_product.insert().values(order_id=self.id, product_id=product.id, quantity=quantity)

        # Add the association instance to the session to persist it
        db.session.execute(order_product_instance)

        # Commit the session to save the changes
        self.save()

    def product_quantity(self, product: object) -> int:
        """
        Returns the quantity of a product in the order.
        """
        return db.session.query(order_product.c.quantity).filter(
            order_product.c.order_id == self.id,
            order_product.c.product_id == product.id
        ).scalar()