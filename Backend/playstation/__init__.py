from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from typing import Self

# Base Model Class
class Base(DeclarativeBase):
    pass

# Declare Database
db: SQLAlchemy = SQLAlchemy(model_class=Base)


# Create modification class
class SQLMixin:
    """
    This is a class to add modifications for Model classes
    Mixin Design Pattern
    """

    # Create a Save Method
    def save(self: Self, *args, **kwargs) -> None:
        """
        Method used to save SQL Session
        """
        # Check if instance exists
        instance: object = db.session.query(self.__class__).filter_by(id=self.id).first()
        # Create new instance if instance does not exists
        if instance is None:
            db.session.add(self)
        # Commit Changes
        db.session.commit()

    # Create a Delete Method
    def delete(self: Self, *args, **kwargs) -> None:
        """
        Method used to delete an instance from SQL
        """
        db.session.delete(self)
        # Commit Changes
        db.session.commit()