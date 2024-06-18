"""
# Main Flask Application

- In this folder you will find the flask application assembled and ready to run
- The application is divided into several folders and files for better organization and maintainability
- The main application is in the `manage.py` file, the routes are defined in other folders such as  'pages', 'users', 'products' and 'orders'.
"""

from flask import Flask
from playstation.settings import DEBUG, TEMPLATES_DIR, STATIC_DIR
from playstation.routes import routes
from playstation.database import database


# Initiate flask application
app: Flask = Flask(__name__, template_folder=TEMPLATES_DIR, static_folder=STATIC_DIR)
app.url_map.strict_slashes = False

# Register routes
routes(app)

# Configure Database
database(app)


if __name__ == "__main__":
    # Run flask application
    app.run(debug=DEBUG)
