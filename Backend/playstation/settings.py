"""
# File Contains Configurations for the application

- Debug setting for development/production
- Templates path
- Static files path
- Media files path
- Secret Key
- Database
- JWT Authentication Parameters
- Core Configuration
- Storage Configuration
"""

import os
from typing import Union
from dotenv import load_dotenv
from datetime import timedelta


# Load ENV
load_dotenv()


# Debug
DEBUG: bool = os.getenv("DEBUG", "False") == "True"

# Base directory of the project
BASE_DIR: str = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Templates and Static paths
TEMPLATES_DIR: str = os.path.join(BASE_DIR, "templates")
STATIC_DIR: str = "static"
MEDIA_DIR: str = os.path.join(STATIC_DIR, "images")
ALLOW_IMAGE_TYPES: set[str] = {"png", "jpg", "jpeg"}

# Database
DATABASE: str = os.getenv("DATABASE", "sqlite:///test.db")
"""
examples
DATABASE = "sqlite:///test.db"
DATABASE = "postgresql://user:password@postgresserver/dbname"
DATABASE = 'mysql+pymysql://username:password@localhost/dbname'
"""
# Secret Key
SECRET_KEY: str = os.getenv("SECRET_KEY", os.urandom(24))

# Cores Configuration Allowed origins
CORS_ALLOWED_ORIGINS: Union[list[str], str] = ["http://localhost:3000", "http://localhost:5173"]
"""
[
    "*", # Allow All Domains
    'http://localhost:3000',  # Example for React development
    'https://example.com'     # Example for a production domain
]
"""

# JWT Authentication
JWT_AUTHENTICATIONS: dict = {
    "SECRET_KEY": SECRET_KEY,
    "ALGORITHM": "HS256",
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=60),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    "AUTH_HEADER_TYPES": "Bearer ",
}
"""
Example
{
    "SECRET_KEY": SECRET_KEY,
    "ALGORITHM": "HS256",
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=60),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    "AUTH_HEADER_TYPES": "Bearer ",
}
"""

# logging configuration
LOGGING_COFIGURATION: dict[str, str] = {
    "NAME": "playstation",
    "FILE": "app.logs",
    "FORMAT": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
}
"""
Logger Configuration Example
{
    "NAME": "playstation",
    "FILE": "app.logs",
    "FORMAT": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
}
"""

# Storage
STORAGE: str = os.getenv("STORAGE", "")

# If amazon storage
AWS_ACCESS_KEY_ID: str = os.getenv("AWS_ACCESS_KEY_ID", "")
AWS_SECRET_ACCESS_KEY: str = os.getenv("AWS_SECRET_ACCESS_KEY", "")
AWS_STORAGE_BUCKET_NAME: str = os.getenv("AWS_STORAGE_BUCKET_NAME", "")
