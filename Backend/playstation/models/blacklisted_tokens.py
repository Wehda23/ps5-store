"""
# File that contains a model Coupons and it's methods
"""

from playstation import db, SQLMixin
from typing import Self


class BlackListedTokens(db.Model, SQLMixin):
    # Basic
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    access = db.Column(db.String(1000), nullable=False, unique=True)
    refresh = db.Column(db.String(1000), nullable=False, unique=True)
    access_expiration_date = db.Column(db.DateTime, nullable=False)
    refresh_expiration_date = db.Column(db.DateTime, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    # Relationship
    user = db.relationship('User', back_populates='blacklisted_tokens')

    def __repr__(self: Self) -> str:
        """
        Method for representation
        """
        return f"<{self.__class__.__name__} {self.id}>"
