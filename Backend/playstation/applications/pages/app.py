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
- /images/<str:file_path>
"""

from flask import Blueprint, abort, render_template, send_from_directory, Response
from playstation.settings import TEMPLATES_DIR, STATIC_DIR, MEDIA_DIR
from .serializer import CheckImageSerializer
from . import logger
import os

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


# login page
@pages.route("/react_app")
def react_app() -> str:
    """
    Test Integrating react application
    """
    return render_template("react_test/index.html")


# Image handling route
@pages.route("/images/<path:file_path>")
def get_static_image(file_path: str) -> Response:
    """
    Get an image from the media folder
    """
    # Get the image
    image: str = file_path.split("/")[-1]
    # Sub Directory
    directory_path: str = os.path.join(MEDIA_DIR, file_path.split("/")[0])
    # Get the full relative path to the image
    relative_path: str = os.path.join(MEDIA_DIR, file_path)
    # Normalize
    relative_path: str = os.path.normpath(relative_path)
    directory_path: str = os.path.normpath(directory_path)
    # Check if the image exists
    data = {"image_url": relative_path.replace(STATIC_DIR, "")}
    try:
        # Check if the image exists
        serializer = CheckImageSerializer(data=data)
        if serializer.is_valid():
            # Return the image
            return send_from_directory(directory_path, image, as_attachment=False)
        # Error
        return send_from_directory(MEDIA_DIR, "default.png", as_attachment=False)
    except Exception as e:
        # Error Log the error
        logger.error(f"Error getting image {e}, path={relative_path}")
        return send_from_directory(MEDIA_DIR, "default.png", as_attachment=False)


# JavaScript handling route
@pages.route("/js/<path:file_name>")
def get_static_js(file_name: str) -> Response:
    """
    Get a JS file from the JavaScript files.
    """
    if file_name.endswith(".js"):
        javascript_dir = os.path.join(STATIC_DIR, "js")
        return send_from_directory(javascript_dir, file_name, as_attachment=False)
    abort(404)


# CSS handling route
@pages.route("/css/<path:file_name>")
def get_static_css(file_name: str) -> Response:
    """
    Get a CSS file from the CSS files.
    """
    if file_name.endswith(".css"):
        css_dir = os.path.join(STATIC_DIR, "css")
        return send_from_directory(css_dir, file_name, as_attachment=False)
    abort(404)