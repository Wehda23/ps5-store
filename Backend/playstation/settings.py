"""
# File Contains Configurations for the application

- Debug setting for development/production
- Templates path
- Static files path
- Media files path
- Secret Key
- Database
- JWT Authentication Parameters
"""

import os
from datetime import timedelta


# Debug
DEBUG: bool = True

# Base directory of the project
BASE_DIR: str = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Templates and Static paths
TEMPLATES_DIR: str = os.path.join(BASE_DIR, "templates")
STATIC_DIR: str = os.path.join(BASE_DIR, "static")
MEDIA_DIR: str = None

# Database
DATABASE: str = "sqlite:///test.db"

# Secret Key
SECRET_KEY: str = os.urandom(24)


# JWT Authentication
JWT_AUTHENTICATIONS: dict = {
    "SECRET_KEY": SECRET_KEY,
    "ALGORITHM": "HS256",
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=60),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    "AUTH_HEADER_TYPES": "Bearer ",
}
