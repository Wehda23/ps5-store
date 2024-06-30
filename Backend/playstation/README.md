# PlayStation Package for Backend Project

This package contains the modules, models, and applications required for the PlayStation Store application.

1. admin
2. applications
3. models
4. serializers
5. file_manager
6. settings.py
7. logger.py
8. database.py
9. routes.py

## 📁 File/Folder Structure

```txt
playstation/
    __init__.py
    app.py
    README.md // Explains the PlayStation Package
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
        README.md // Explains how to interact with APIs and API endpoints
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

## 🔑 Admin Package

The admin package contains modules related to the administration of the application, such as managing user permissions and authentication mechanisms.

## 📦 Applications Package

The applications package is divided into sub-packages, each responsible for different functional areas of the application:

- **pages**: Manages the different pages of the application.
- **users**: Handles user-related operations.
- **products**: Manages product-related functionalities.
- **orders**: Deals with order processing and management.
- **swagger**: Contains configuration for API documentation using Swagger.
- **payments**: Handles payment-related operations.
- **shipping_addresses**: Handles shipping address operations.

## 🔗 Register Flask Blueprints to Flask

Use the `routes` function in `routes.py` to register all Flask blueprints to the main Flask application.

### Example Setup

```python
from flask import Flask
from playstation.routes import routes

# Initiate Flask application
app = Flask(__name__)

# Register routes
routes(app)

if __name__ == "__main__":
    # Run Flask application
    app.run()
```

## 🛠️ Models Package

The models package defines the database models for the application. Each model represents a table in the database:

- **user.py**: User model.
- **products.py**: Product model.
- **orders.py**: Order model.
- **coupons.py**: Coupon model.
- **payments.py**: Payment model.
- **shipping_addresses.py**: Shipping Address model.
- **blacklisted_tokens.py**: Blacklisted Tokens model.

### Initialize Flask Database Configuration and Models

Use the `database` function in `database.py` to configure the database for the Flask application.

### Example Setup

```python
from flask import Flask
from playstation.database import database

# Initiate Flask application
app = Flask(__name__)

# Setup database
database(app)

if __name__ == "__main__":
    # Run Flask application
    app.run()
```

## 📂 File Handler Package

This package manages file handling, supporting both Amazon S3 and local storage.

## 📝 Initializing Loggers in Flask

Proper logging is crucial for monitoring and debugging. Use the `setup_logging` function in `logger.py` to configure logging for your Flask application.

### Example Setup in `app.py`

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

Initialize the logger in the `__init__.py` file of your Blueprint module.

#### Example in `users/__init__.py`

```python
import logging
from logging import Logger
from playstation.settings import LOGGING_CONFIGURATION

# Get the logger
logger: Logger = logging.getLogger(LOGGING_CONFIGURATION["NAME"])
```

### Using Logger in Blueprint `app.py`

```python
from . import logger
from flask import Blueprint, make_response, Response

example_api = Blueprint("example_api", __name__)

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

## ⚙️ Configuration

### settings.py

The `settings.py` file contains configurations for the application, including:

- Debug setting for development/production
- Templates path
- Static files path
- Media files path
- Secret Key
- Database
- JWT Authentication Parameters

#### Change from SQLite to MySQL or PostgreSQL

To switch from SQLite to MySQL or PostgreSQL, update the `DATABASE` variable in `settings.py`:

```python
# SQLite
DATABASE = "sqlite:///test.db"

# MySQL
DATABASE = "mysql+pymysql://username:password@host/database_name"

# PostgreSQL
DATABASE = "postgresql+psycopg2://username:password@host/database_name"
```

#### Change from Local Storage to Amazon S3

To use Amazon S3 for storage, update the `STORAGE` variable and provide the necessary AWS credentials:

```python
# Local Storage
STORAGE = ""

# Amazon S3
STORAGE = "aws"
AWS_ACCESS_KEY_ID = "your_access_key_id"
AWS_SECRET_ACCESS_KEY = "your_secret_access_key"
AWS_STORAGE_BUCKET_NAME = "your_bucket_name"
```