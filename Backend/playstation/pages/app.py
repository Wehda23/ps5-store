"""
# Folder that contains application to handle templates

- Flask blueprint that is concerned with rendering templates
"""
from flask import Blueprint, abort, render_template
from playstation.settings import TEMPLATES_DIR, STATIC_DIR

# Blueprint
pages: Blueprint = Blueprint(
    "pages",
    __name__,
    template_folder=TEMPLATES_DIR,
    static_folder=STATIC_DIR
)


# Home page
@pages.route("/")
def home_page() -> str:
    """
    Home page route
    """
    return render_template("home_page/index.html")