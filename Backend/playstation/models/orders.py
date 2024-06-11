"""
# File Contains Orders Model & Methods
"""

from playstation import db, SQLMixin
from playstation.models.users import User
from playstation.models.shipping_address import ShippingAddress
from playstation.models.coupons import Coupons


# Orders Model
class Orders(db.Model, SQLMixin):
    # Basic
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    shipping_address = db.Column(
        db.Integer, db.ForeignKey("shipping_address.id"), nullable=False
    )
    coupon = db.Column(db.Integer, db.ForeignKey("coupons.id"))
    order_date = db.Column(db.DateTime, default=db.func.current_timestamp())
    total_amount = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(50), nullable=False)

    # Relationships
    user_obj = db.relationship("User", backref=db.backref("orders", lazy=True))

    def __repr__(self) -> str:
        """
        Method for representation
        """
        return f"<{self.__class__.__name__} {self.id}>"
