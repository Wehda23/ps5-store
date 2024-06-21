"""
# File that contains a model BlackListedTokens.
"""

from playstation import db, SQLMixin
from playstation.admin.authentications.token import RefreshToken
from typing import Self, Optional


# BlackListedTokensMixin
class BlackListedTokensMixin(SQLMixin):
    """
    This class represents a model for BlackListedTokens.
    """

    def check_token_life(self: Self) -> None:
        """
        Method to check if the token is expired on refresh duration then deletes it otherwise no action is taken
        """
        pass


# Class BlackListedTokens
class BlackListedTokens(db.Model, BlackListedTokensMixin):
    # Basic
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    access = db.Column(db.String(1000), nullable=False, unique=True)
    refresh = db.Column(db.String(1000), nullable=False, unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

    # Relationship
    user = db.relationship("User", back_populates="blacklisted_tokens")

    def __repr__(self: Self) -> str:
        """
        Method for representation
        """
        return f"<{self.__class__.__name__} {self.id}>"

    def check_token_life(self: Self) -> None:
        """
        Method to check if the token is expired on refresh duration\
            then deletes it otherwise no action is taken
        """
        # Grab token
        token: Optional[dict] = RefreshToken.decode_token(self.refresh)
        # If token is none delete token
        if token is None:
            self.delete()
