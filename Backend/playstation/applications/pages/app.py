"""
# Application that handles the Pages Application

- This is the application that handles all user related actions such as new account creation, profile updates, registeration, login etc..

## Page routes

##### Protected Routes
- /Products/me: Get the current user's profile
- /Products/me/update: Update the current user's profile
- /Products/me/delete: Delete the current user's account

#### Public Routes
- /Products/register: Register a new user
- /Products/login: Login a user
"""

from flask import Blueprint, abort, render_template
from playstation.settings import TEMPLATES_DIR, STATIC_DIR

# Blueprint
pages: Blueprint = Blueprint(
    "pages", __name__, template_folder=TEMPLATES_DIR, static_folder=STATIC_DIR
)


# Home page
@pages.route("/")
def home_page() -> str:
    """
    Home page route
    """
    return render_template("home_page/index.html")


# login page
@pages.route("/lobby")
def login_page() -> str:
    """
    Login page route
    """
    return render_template("login_page/index.html")
