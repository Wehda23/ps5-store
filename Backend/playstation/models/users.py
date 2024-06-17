"""
# Folder that Contains classes/methods for Users Model
"""

from playstation import db, SQLMixin
from typing import Self
from werkzeug.security import generate_password_hash, check_password_hash

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
        if 'password' not in kwargs:
            raise ValueError("Password field is required")

        # hash password
        kwargs['password'] = cls.hash_password(kwargs['password'])

        # Create new instance and return new user
        new_user: object = cls(**kwargs)
        # Create user
        new_user.save()
        return new_user

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

    def __repr__(self: Self):
        """
        Method for representation
        """
        return f"<{self.__class__.__name__} {self.email}>"
