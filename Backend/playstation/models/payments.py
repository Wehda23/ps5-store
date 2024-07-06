"""
# Folder that Contains classes/methods for Payments Model
"""

from playstation import db, SQLMixin
from typing import Self


# Payments model
class Payments(db.Model, SQLMixin):
    # Basics
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    amount = db.Column(db.Integer, nullable=False)
    order_id = db.Column(db.Integer, db.ForeignKey("orders.id"), nullable=False, unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    payment_method = db.Column(db.String(50), nullable=False)
    payment_status = db.Column(db.String(50), nullable=False)
    currency = db.Column(db.String(10), nullable=False, default="$")

    # Relationships
    order = db.relationship("Orders", back_populates='payment', uselist=False)
    user = db.relationship("User", back_populates='payments')

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

    def __repr__(self: Self):
        """
        Method for representation
        """
        return f"<{self.__class__.__name__} {self.id}>"
