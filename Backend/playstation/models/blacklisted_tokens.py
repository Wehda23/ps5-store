"""
# This file contains the model and methods related to BlackListedTokens in the database.
"""

from playstation import db, SQLMixin
from playstation.admin.authentications.token import RefreshToken
from playstation.settings import JWT_AUTHENTICATIONS
from typing import Self, Optional


class BlackListedTokensMixin(SQLMixin):
    """
    Mixin class providing functionalities for BlackListedTokens.
    """

    def check_token_life(self: Self) -> None:
        """
        Checks if the token is expired based on the refresh duration and deletes it if expired.
        """
        pass


class BlackListedTokens(db.Model, BlackListedTokensMixin):
    """
    Represents a BlackListedToken in the database.

    Attributes:
        id (int): Primary key.
        access (str): Access token.
        refresh (str): Refresh token.
        user_id (int): Foreign key referencing User.
        user (User): The user associated with this token.
    """

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    access = db.Column(db.String(1000), nullable=False, unique=True)
    refresh = db.Column(db.String(1000), nullable=False, unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    user = db.relationship("User", back_populates="blacklisted_tokens")

    def __repr__(self: Self) -> str:
        """
        String representation of the BlackListedTokens instance.

        Returns:
            str: String representation of the BlackListedTokens instance.
        """
        return f"<{self.__class__.__name__} {self.id}>"

    def check_token_life(
        self: Self,
        key: str = JWT_AUTHENTICATIONS["SECRET_KEY"],
        algorithm: str = JWT_AUTHENTICATIONS["ALGORITHM"],
    ) -> None:
        """
        Checks if the token is expired based on the refresh duration and deletes it if expired.

        Args:
            key (str): Secret key for decoding the token.
            algorithm (str): Algorithm used for decoding the token.
        """
        token: Optional[dict] = RefreshToken.decode_token(self.refresh, key, algorithm)
        if token is None:
            self.delete()
