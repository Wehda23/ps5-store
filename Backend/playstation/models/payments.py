"""
# This file contains the model and methods related to Payments in the database.
"""

from playstation import db, SQLMixin
from typing import Self


class Payments(db.Model, SQLMixin):
    """
    Represents a Payment in the database.

    Attributes:
        id (int): Primary key.
        amount (int): Payment amount.
        order_id (int): Foreign key referencing Orders.
        user_id (int): Foreign key referencing User.
        payment_method (str): Method of payment.
        payment_status (str): Status of the payment.
        currency (str): Currency used for the payment.
        created_at (datetime): Timestamp when the payment was created.
        updated_at (datetime): Timestamp when the payment was last updated.
    """

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    amount = db.Column(db.Integer, nullable=False)
    order_id = db.Column(db.Integer, db.ForeignKey("orders.id"), nullable=False, unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    payment_method = db.Column(db.String(50), nullable=False)
    payment_status = db.Column(db.String(50), nullable=False)
    currency = db.Column(db.String(10), nullable=False, default="USD")
    order = db.relationship("Orders", back_populates='payment', uselist=False)
    user = db.relationship("User", back_populates='payments')
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    def __repr__(self: Self) -> str:
        """
        String representation of the Payments instance.

        Returns:
            str: String representation of the Payments instance.
        """
        return f"<{self.__class__.__name__} {self.id}>"
