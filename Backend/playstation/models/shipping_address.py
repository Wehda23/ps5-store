"""
# File contains ShippingAddres Model and it's methods
"""
from playstation import db
from playstation.models.users import User
from typing import Self


# Shipping Address
class ShippingAddress(db.Model):
    # Basic
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    address = db.Column(db.String(256), nullable=False)
    city = db.Column(db.String(128), nullable=False)
    state = db.Column(db.String(128), nullable=False)
    country = db.Column(db.String(128), nullable=False)
    default = db.Column(db.Boolean, default=False, nullable=False)

    # Relationships
    user_obj = db.relationship('User', backref=db.backref('shipping_addresses', lazy=True))

    def __repr__(self: Self):
        """
        Method for representation
        """
        return f"<{self.__class__.__name__} {self.id}>"