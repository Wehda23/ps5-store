"""
# Folder that Contains classes/methods for Users Model
"""

from playstation import db, SQLMixin
from typing import Self, Optional, NoReturn
from werkzeug.security import generate_password_hash, check_password_hash
from .exceptions import ExistingEmail


# Add SQLUserMixin
class UserMixin(SQLMixin):
    """
    Mixin to add modification to user class
    """

    @classmethod
    def hash_password(cls, password: str) -> str:
        """
        Method used to has password
        """
        return generate_password_hash(password)

    def check_password(self, password: str) -> bool:
        """
        Method used to check
        """
        return check_password_hash(self.password, password)

    # Function to create new user
    @classmethod
    def create_user(cls, **kwargs) -> Self:
        """
        Create a new user
        Args:
            - **kwargs: User details

        Returns:
            - New User
        """
        # Check password key existing
        if "password" not in kwargs:
            raise ValueError("Password field is required")

        # Check email field
        if "email" not in kwargs:
            raise ValueError("Email field is required")

        # hash password
        kwargs["password"] = cls.hash_password(kwargs["password"])

        # Check user
        email: str = kwargs.get("email")
        # Use .__safe() function
        cls.__safe(email)

        # Create new instance and return new user
        new_user: object = cls(**kwargs)

        # Create user
        new_user.save()
        return new_user

    @classmethod
    def __safe(cls, value: Optional[str]) -> Optional[NoReturn]:
        """
        Method used to check if there is no duplicate user

        Args:
            - value (Optional[str]): Value at which to check user existance.

        Raises:
            - error in case user exists
        """
        if value is not None and cls.query.filter_by(email=value).first() is not None:
            raise ExistingEmail("User already exists")


# Users model
class User(db.Model, UserMixin):
    # Basics
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    # Permissions and Status
    is_staff = db.Column(db.Boolean, default=False, nullable=False)
    is_admin = db.Column(db.Boolean, default=False, nullable=False)
    active = db.Column(db.Boolean, default=True, nullable=False)

    # Dates
    last_login = db.Column(
        db.DateTime, nullable=False, default=db.func.current_timestamp()
    )
    created_at = db.Column(
        db.DateTime, nullable=False, default=db.func.current_timestamp()
    )
    updated_at = db.Column(
        db.DateTime,
        nullable=False,
        default=db.func.current_timestamp(),
        onupdate=db.func.current_timestamp(),
    )

    # Relationship
    blacklisted_tokens = db.relationship(
        "BlackListedTokens", back_populates="user", cascade="all, delete-orphan"
    )

    def __repr__(self: Self):
        """
        Method for representation
        """
        return f"<{self.__class__.__name__} {self.email}>"

    def update_last_login(self: Self) -> None:
        """
        Method used to update last_login attribute
        """
        self.last_login = db.func.current_timestamp()
