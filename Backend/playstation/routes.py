"""
# File that contains flask application routes
"""

from flask import Flask
from playstation.applications.pages.app import pages
from playstation.applications.users.app import users_api
from playstation.applications.orders.app import orders_api
from playstation.applications.products.app import products_api
from playstation.applications.swagger import swaggerui_blueprint
from playstation.settings import DEBUG


# Define function for routes
def routes(app: Flask, debug: bool = DEBUG) -> None:
    """
    Function used to register Flask BluePrints to the Main Flask application

    Args:
        - app (Flask): Flask application
        - debug (bool): Check if the application is in debug mode or not

    Returns:
        - Nothing
    """
    # Register pages application blueprint
    app.register_blueprint(pages)
    # Register user application blueprint
    app.register_blueprint(users_api)
    # Register orders application blueprint
    app.register_blueprint(orders_api)
    # Register products application blueprint
    app.register_blueprint(products_api)

    # Check if debug
    if debug:
        # Register Swagger
        app.register_blueprint(swaggerui_blueprint)
