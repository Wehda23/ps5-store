"""
# This file contains every configeration related to flask application database
"""

from flask import Flask
from playstation import db
from playstation.models.users import User
from playstation.models.blacklisted_tokens import BlackListedTokens
from playstation.models.coupons import Coupons
from playstation.models.orders import Orders
from playstation.models.payments import Payments
from playstation.models.products import Product, Category
from playstation.models.shipping_address import ShippingAddress
from playstation.settings import DATABASE

# Create function
def database(app: Flask) -> None:
    """
    This function is used to configure database for flask application

    Args:
        - app (Flask): Flask application

    Returns:
        - Nothing
    """
    # Database Configurations
    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # Initialize the app with the extension
    db.init_app(app)

    # Create Database Tables
    with app.app_context():
        db.create_all()

    # Clear Session
    @app.teardown_appcontext
    def shutdown_session(exception=None):
        """
        Closes session after each request or application context shutdown to avoid leaks
        """
        db.session.remove()
