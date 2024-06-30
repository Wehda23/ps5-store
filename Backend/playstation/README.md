# Playstation Packages for backend project

This package contains the packages/Models & Applications required for Play Station Store application.

1. admin
2. applications
3. models
4. serializers
5. file_manager
6. settings.py
7. logger.py
8. database.py
9. routes.py


# File/Folder Structure

```txt
playstation/
        __init__.py
        app.py
        README.md // Explains the Playstation Package
        routes.py
        database.py
        logger.py
        settings.py
        admin/
            __init__.py
            permissions.py
            authentications/
                __init__.py
                jwt_authentication.py
                token.py
            file_manager/
                __init__.py
                file_handler.py
                image_handler.py
                storage.py
                exceptions.py
        applications/
            README.md // Explains how to interact with APIs and API end points
            __init__.py
            pages/
                __init__.py
                app.py
            users/
                __init__.py
                app.py
            products/
                __init__.py
                app.py
            orders/
                __init__.py
                app.py
            shipping_addresses/
                __init__.py
                app.py
            payments/
                __init__.py
                app.py
            swagger/
                __init__.py
        models/
            __init__.py
            user.py
            products.py
            orders.py
            coupons.py
            payments.py
            shipping_addresses.py
            blacklisted_tokens.py
            exceptions.py
        serializers/
            __init__.py
            serializer.py
```

# Admin Package

The admin package contains modules related to the administration of the application, such as managing user permissions and authentication mechanisms.

# Applications Package

The applications package is divided into sub-packages, each responsible for different functional areas of the application, such as:

- pages: Manages the different pages of the application.
- users: Handles user-related operations.
- products: Manages product-related functionalities.
- orders: Deals with order processing and management.
- swagger: Contains configuration for API documentation using Swagger.
- payments: Handles payment related Operations.
- shipping_addresses: Handles shipping addresses operations.

## Register Flask Blueprints to Flask

By using the function `routes` in the file `./routes.py` we can register all our flask blueprints to Flask application

Here is an example of how to set it up:

```py
from flask import Flask
from playstation.routes import routes


# Initiate flask application
app: Flask = Flask(__name__)

# Register routes
routes(app)


if __name__ == "__main__":
    # Run flask application
    app.run()
```

## Models Package

The models package defines the database models for the application. Each model represents a table in the database and includes:

- user.py: User model.
- products.py: Product model.
- orders.py: Order model.
- coupons.py: Coupon model.
- payments.py: Payment model.
- shipping_addresses.py: Shipping Address model.
- blacklisted_tokens.py: Black Listed Tokens model.

### Initiate Flask Database Configuration and Models

By using the function `database` in the file `./database.py` we can initiate flask database configurations and models

Here is an example of how to set it up:

```py
from flask import Flask
from playstation.database import database


# Initiate flask application
app: Flask = Flask(__name__)

# Register routes
database(app)


if __name__ == "__main__":
    # Run flask application
    app.run()
```

## File Handler Package

Explain the package (Amazon and localstorage are supported)

## Initializing Loggers in Flask

In Flask applications, initializing loggers ensures proper logging configurations throughout the application. Below are steps and examples for setting up logging in different parts of a Flask project.

### Setting Up Logging in the Flask Application

To configure logging for your Flask application, use the `setup_logging` function from `logger.py`.

#### Example in `app.py`

```python
from flask import Flask
from .logger import setup_logging

app = Flask(__name__)

# Setup Logger
setup_logging(app)

if __name__ == "__main__":
    app.run()
```

### Using Loggers in Flask Blueprints

When working with Flask Blueprints, initialize the logger in the `__init__.py` file of your Blueprint module.

#### File Structure Example

```
project_root/
    playstation/
        __init__.py
        app.py
        logger.py
        settings.py
        applications/
            __init__.py
            pages/
                __init__.py
                app.py
            users/
                __init__.py
                app.py
            products/
                __init__.py
                app.py
```

#### Initializing Logger in `users/__init__.py`

```python
import logging
from logging import Logger
from playstation.settings import LOGGING_CONFIGURATION

# Get the logger
logger: Logger = logging.getLogger(LOGGING_CONFIGURATION["NAME"])
```

### Using Logger in Blueprint `app.py`

To use the logger in a Flask Blueprint (`app.py`), import it as follows:

```python
from . import logger
from flask import Blueprint, make_response, Response

example_api: Blueprint = Blueprint("example_api", __name__)

logger.error("An error has occurred")

@example_api.route("", methods=['GET'])
def example(*args, **kwargs) -> Response:

    try:
        # Some code that might raise an exception
        pass
    except Exception as e:
        logger.error(f"An error has occurred: {e}")
        return make_response("error", 400)
```