"""
# Pages Application

This module handles the rendering of templates for various pages and serves static files such as images, JavaScript, and CSS files.

## Views

### Home Page
- **/**: Render the home page.

### Login Page
- **/lobby**: Render the login page.

### React App Page
- **/react_app**: Render a page to test integrating a React application.

### Static File Serving

#### Images
- **/images/<path:file_path>**: Serve images from the media folder.

#### JavaScript
- **/js/<path:file_name>**: Serve JavaScript files from the static directory.

#### CSS
- **/css/<path:file_name>**: Serve CSS files from the static directory.

"""

from flask import current_app, abort, render_template, send_from_directory, Response
from playstation.settings import STATIC_DIR, MEDIA_DIR
from .serializer import CheckImageSerializer
import os
from . import pages


@pages.route("/")
def home_page() -> str:
    """
    Render the home page.

    Returns:
        str: The rendered home page template.
    """
    return render_template("home_page/index.html")


@pages.route("/lobby")
def login_page() -> str:
    """
    Render the login page.

    Returns:
        str: The rendered login page template.
    """
    return render_template("login_page/index.html")


@pages.route("/react_app")
def react_app() -> str:
    """
    Render a page to test integrating a React application.

    Returns:
        str: The rendered React test page template.
    """
    return render_template("react_test/index.html")


@pages.route("/images/<path:file_path>")
def get_static_image(file_path: str) -> Response:
    """
    Serve an image from the media folder.

    Args:
        file_path (str): The relative path to the image file.

    Returns:
        Response: The image file response or a default image if the file is not found or invalid.
    """
    image: str = file_path.split("/")[-1]
    directory_path: str = os.path.join(MEDIA_DIR, file_path.split("/")[0])
    relative_path: str = os.path.join(MEDIA_DIR, file_path)
    relative_path = os.path.normpath(relative_path)
    directory_path = os.path.normpath(directory_path)
    data = {"image_url": relative_path.replace(STATIC_DIR, "")}

    try:
        serializer = CheckImageSerializer(data=data)
        if serializer.is_valid() and ".." not in file_path:
            return send_from_directory(directory_path, image, as_attachment=False)
        return send_from_directory(MEDIA_DIR, "default.png", as_attachment=False)
    except Exception as e:
        current_app.logger.error(f"Error getting image {e}, path={relative_path}")
        return send_from_directory(MEDIA_DIR, "default.png", as_attachment=False)


@pages.route("/js/<path:file_name>")
def get_static_js(file_name: str) -> Response:
    """
    Serve a JavaScript file from the static directory.

    Args:
        file_name (str): The name of the JavaScript file.

    Returns:
        Response: The JavaScript file response or a 404 error if the file is not found or invalid.
    """
    if file_name.endswith(".js") and ".." not in file_name:
        javascript_dir = os.path.join(STATIC_DIR, "js")
        return send_from_directory(javascript_dir, file_name, as_attachment=False)
    abort(404)


@pages.route("/css/<path:file_name>")
def get_static_css(file_name: str) -> Response:
    """
    Serve a CSS file from the static directory.

    Args:
        file_name (str): The name of the CSS file.

    Returns:
        Response: The CSS file response or a 404 error if the file is not found or invalid.
    """
    if file_name.endswith(".css") and ".." not in file_name:
        css_dir = os.path.join(STATIC_DIR, "css")
        return send_from_directory(css_dir, file_name, as_attachment=False)
    abort(404)
