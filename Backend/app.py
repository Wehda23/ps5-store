"""
# Main Flask Application

- In this folder you will find the flask application assembled and ready to run
- The application is divided into several folders and files for better organization and maintainability
- The main application is in the `manage.py` file, the routes are defined in other folders such as  'pages', 'users', 'products' and 'orders'.
"""

from flask import Flask
from flask_cors import CORS
from playstation.settings import (
    DEBUG,
    TEMPLATES_DIR,
    STATIC_DIR,
    SECRET_KEY,
    MEDIA_DIR,
    CORS_ALLOWED_ORIGINS
)
from playstation.routes import routes
from playstation.database import database
from playstation.logger import setup_logging


# Initiate flask application
app: Flask = Flask(__name__, template_folder=TEMPLATES_DIR, static_folder=STATIC_DIR)
app.url_map.strict_slashes = False
app.config["SECRET_KEY"] = SECRET_KEY
app.config["UPLOAD_FOLDER"] = MEDIA_DIR
app.config["MAX_CONTENT_LENGTH"] = 500 * 1000 * 1000


# Cores
CORS(app, resources={r"/api/*":{"origins":CORS_ALLOWED_ORIGINS}})

# Register routes
routes(app)

# Configure Database
database(app)

# Set up logger
setup_logging(app)


if __name__ == "__main__":
    # Run flask application
    app.run(debug=DEBUG)
