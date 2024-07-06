from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from .config import config
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
        instance: object = (
            db.session.query(self.__class__).filter_by(id=self.id).first()
        )
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



def create_app(config_name='testing'):
    """
    Function to create application for testing
    """
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    db.init_app(app)

    return app