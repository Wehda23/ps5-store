"""
# Folder that contains application to handle templates

- Flask blueprint that is concerned with rendering templates
"""
from flask import Blueprint, abort, render_template


# Blueprint
pages: Blueprint = Blueprint("pages", __name__)


# Home page
@pages.route("/")
def home_page() -> str:
    """
    Home page route
    """
    return "Hello, World!! Pages"