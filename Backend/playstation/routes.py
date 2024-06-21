"""
# File that contains flask application routes

Usage Example:

```py
from playstation.routes import routes
from flask import Flask

# Initiate your flask application
app: Flask = Flask(__name__)


# Setup routes
routes(app)
```
"""

from flask import Flask
from playstation.applications.pages.app import pages
from playstation.applications.users.app import users_api
from playstation.applications.orders.app import orders_api
from playstation.applications.products.app import products_api
from playstation.applications.shipping_addresses.app import shipping_addresses_api
from playstation.applications.payments.app import payments_api
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
    # Register Shipping Addresses application blueprint
    app.register_blueprint(shipping_addresses_api)
    # Register Payments application blueprint
    app.register_blueprint(payments_api)

    # Check if debug
    if debug:
        # Register Swagger
        app.register_blueprint(swaggerui_blueprint)
