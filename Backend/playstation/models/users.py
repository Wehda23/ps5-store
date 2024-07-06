"""
# This file contains the models and methods related to Users in the database.
"""

from playstation import db, SQLMixin
from typing import Self, Optional, NoReturn
from werkzeug.security import generate_password_hash, check_password_hash
from .junction_models import user_coupons
from .exceptions import ExistingEmail


class UserMixin(SQLMixin):
    """
    Mixin class providing user-specific functionalities like password hashing and user creation.
    """

    @classmethod
    def hash_password(cls, password: str) -> str:
        """
        Hashes the given password.

        Args:
            password (str): The plain text password.

        Returns:
            str: The hashed password.
        """
        return generate_password_hash(password)

    def check_password(self, password: str) -> bool:
        """
        Verifies the given password against the stored hash.

        Args:
            password (str): The plain text password.

        Returns:
            bool: True if the password matches, False otherwise.
        """
        return check_password_hash(self.password, password)

    @classmethod
    def create_user(cls, **kwargs) -> Self:
        """
        Creates a new user with the provided details.

        Args:
            **kwargs: User details such as first_name, last_name, email, password.

        Returns:
            Self: The newly created User object.
        
        Raises:
            ValueError: If required fields are missing.
            ExistingEmail: If a user with the given email already exists.
        """
        if "password" not in kwargs:
            raise ValueError("Password field is required")

        if "email" not in kwargs:
            raise ValueError("Email field is required")

        kwargs["password"] = cls.hash_password(kwargs["password"])

        email: str = kwargs.get("email")
        cls.__safe(email)

        new_user: object = cls(**kwargs)
        new_user.save()
        return new_user

    @classmethod
    def __safe(cls, value: Optional[str]) -> Optional[NoReturn]:
        """
        Ensures there are no duplicate users by email.

        Args:
            value (Optional[str]): The email to check.

        Raises:
            ExistingEmail: If a user with the given email already exists.
        """
        if value is not None and cls.query.filter_by(email=value).first() is not None:
            raise ExistingEmail("User already exists")


class User(db.Model, UserMixin):
    """
    Represents a User in the database.

    Attributes:
        id (int): Primary key.
        first_name (str): User's first name.
        last_name (str): User's last name.
        email (str): User's email, unique.
        password (str): User's hashed password.
        is_staff (bool): Indicates if the user is staff.
        is_admin (bool): Indicates if the user is an admin.
        active (bool): Indicates if the user is active.
        last_login (datetime): Timestamp of the last login.
        created_at (datetime): Timestamp when the user was created.
        updated_at (datetime): Timestamp when the user was last updated.
    """

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    is_staff = db.Column(db.Boolean, default=False, nullable=False)
    is_admin = db.Column(db.Boolean, default=False, nullable=False)
    active = db.Column(db.Boolean, default=True, nullable=False)
    last_login = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    blacklisted_tokens = db.relationship("BlackListedTokens", back_populates="user", cascade="all, delete-orphan")
    shipping_addresses = db.relationship("ShippingAddress", back_populates="user")
    orders = db.relationship("Orders", back_populates="user")
    payments = db.relationship("Payments", back_populates="user")
    coupons = db.relationship("Coupons", secondary=user_coupons, back_populates="users")

    def __repr__(self: Self) -> str:
        """
        String representation of the User instance.

        Returns:
            str: String representation of the User instance.
        """
        return f"<{self.__class__.__name__} {self.email}>"

    def update_last_login(self: Self) -> None:
        """
        Updates the last_login attribute to the current timestamp.
        """
        self.last_login = db.func.current_timestamp()
