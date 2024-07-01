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
            views.py
        users/
            __init__.py
            views.py
        products/
            __init__.py
            views.py
        orders/
            __init__.py
            views.py
        shipping_addresses/
            __init__.py
            views.py
        payments/
            __init__.py
            views.py
        employees/
            __init__.py
            views.py
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

Use `current_app.logger` to log messages within your Blueprint modules.

#### Example in `users/__init__.py`

```python
"""
Initiate User Blueprint application
"""
from flask import Blueprint

# Declare route prefix
url_prefix = "/api/users"

# Blueprint
users_api = Blueprint("users", __name__, url_prefix=url_prefix)

# Import routes to register them with the blueprint
from . import app  # Ensure that this is done at the end
```

### Using Logger in Blueprint `app.py`

```python
from flask import current_app, Blueprint, make_response, request, Response
from playstation.models.exceptions import ExistingEmail
from .serializers import UserRegisterSerializer

# Import blueprint from __init__.py
from . import users_api

# Register User API
@users_api.route("/register", methods=["POST"])
def register(*args, **kwargs) -> Response:
    data = request.get_json()
    serializer = UserRegisterSerializer(data=data)
    try:
        if serializer.is_valid():
            serializer.save()
            return make_response("Successful Registration", 201)
        error = serializer.errors
        return make_response(error, 403)
    except ExistingEmail as e:
        current_app.logger.error(str(e))
        return make_response("Email is already registered", 409)
    except Exception as e:
        error = str(e)
        current_app.logger.error(f"Registration failed: {error}")
        return make_response("Registration Failed", 400)
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

## 🔐 Using .env File

For better security and flexibility, store sensitive information like database credentials, secret keys, and API keys in a `.env` file. Use the `python-dotenv` package to load these environment variables into your Flask application.

### Installing python-dotenv

```sh
pip install python-dotenv
```

### Creating a .env File

Create a `.env` file in your project root and add your environment-specific variables:

```env
# .env
DEBUG=True
SECRET_KEY=your_secret_key
DATABASE=mysql+pymysql://username:password@host/database_name
AWS_ACCESS_KEY_ID=your_access_key_id
AWS_SECRET_ACCESS_KEY=your_secret_access_key
AWS_STORAGE_BUCKET_NAME=your_bucket_name
```

### Loading Environment Variables in Flask

Update `settings.py` to load variables from the `.env` file:

```python
import os
from dotenv import load_dotenv
from datetime import timedelta

# Load environment variables from .env file
load_dotenv()

# Debug
DEBUG = os.getenv("DEBUG", "False") == "True"

# Secret Key
SECRET_KEY = os.getenv("SECRET_KEY", "default_secret_key")

# Base directory of the project
BASE_DIR: str = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Templates and Static paths
TEMPLATES_DIR: str = os.path.join(BASE_DIR, "templates")
STATIC_DIR: str = "static"
MEDIA_DIR: str = os.path.join(STATIC_DIR, "images")
ALLOW_IMAGE_TYPES: set[str] = {"png", "jpg", "jpeg"}

# Database
DATABASE = os.getenv("DATABASE", "sqlite:///test.db")

# JWT Authentication
JWT_AUTHENTICATIONS = {
    "SECRET_KEY": SECRET_KEY,
    "ALGORITHM": "HS256",
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=60),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    "AUTH_HEADER_TYPES": "Bearer ",
}

# Logging configuration
LOGGING_CONFIGURATION = {
    "NAME": "playstation",
    "FILE": "app.logs",
    "FORMAT": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
}

# Storage configuration
STORAGE = os.getenv("STORAGE", "")
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID", "")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY", "")
AWS_STORAGE_BUCKET_NAME = os.getenv("AWS_STORAGE_BUCKET_NAME", "")
```

Using a `.env` file helps keep your configuration secure and allows for easy changes without modifying the codebase directly.