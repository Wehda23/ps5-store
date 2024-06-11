"""
# Folder that Contains classes/methods for Payments Model
"""

from playstation import db, SQLMixin
from typing import Self
from playstation.models.orders import Orders


# Payments model
class Payments(db.Model, SQLMixin):
    # Basics
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    amount = db.Column(db.Integer, nullable=False)
    order = db.Column(db.Integer, db.ForeignKey("orders.id"), nullable=False)
    payment_method = db.Column(db.String(50), nullable=False)
    payment_status = db.Column(db.String(50), nullable=False)
    currency = db.Column(db.String(10), nullable=False, default="$")

    # Relationships
    order_obj = db.relationship("Orders", backref=db.backref("payment", lazy=True))

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
