"""
# File Contains Configurations for the application

- Debug setting for development/production
- Templates path
- Static files path
"""
import os

# Debug
DEBUG: bool = True

# Base directory of the project
BASE_DIR: str = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Templates and Static paths
TEMPLATES_DIR: str = os.path.join(BASE_DIR, 'templates')
STATIC_DIR: str = os.path.join(BASE_DIR, 'static')
MEDIA_DIR: str = None

# Database
DATABASE: str = 'sqlite:///test.db'

# Secret Key
SECRET_KEY: str = os.urandom(24)