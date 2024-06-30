"""
Initiate Pages Application
"""
from flask import Blueprint
from playstation.settings import TEMPLATES_DIR, STATIC_DIR

# Blueprint
pages: Blueprint = Blueprint(
    "pages", __name__, template_folder=TEMPLATES_DIR, static_folder=STATIC_DIR
)

from . import app
