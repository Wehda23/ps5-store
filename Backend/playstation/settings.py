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
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Templates and Static paths
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')
STATIC_DIR = os.path.join(BASE_DIR, 'static')

# Database
DATABASE: str = 'sqlite:///test.db'