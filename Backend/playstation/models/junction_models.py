"""
File Contains Junction model for Orders and Prodcuts
"""

from playstation import db


# Junction Table for many-to-many relationship between Products and Orders
order_product = db.Table(
    "order_product",
    db.Column("order_id", db.Integer, db.ForeignKey("orders.id"), primary_key=True),
    db.Column("product_id", db.Integer, db.ForeignKey("product.id"), primary_key=True),
    db.Column("quantity", db.Integer, nullable=False),  # Example additional column
)

user_coupons = db.Table(
    "user_coupons",
    db.Column("user_id", db.Integer, db.ForeignKey("user.id"), primary_key=True),
    db.Column("coupon_id", db.Integer, db.ForeignKey("coupons.id"), primary_key=True),
)
