"""
File Contains Junction model for Orders and Prodcuts
"""

from playstation import db


# Junction Table for many-to-many relationship between Products and Orders
order_product = db.Table(
    "order_product",
    db.Column("order_id", db.Integer, db.ForeignKey("orders.id"), primary_key=True),
    db.Column("product_id", db.Integer, db.ForeignKey("product.id"), primary_key=True),
)
