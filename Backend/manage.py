"""
# Main Flask Application

- In this folder you will find the flask application assembled and ready to run
- The application is divided into several folders and files for better organization and maintainability
- The main application is in the `manage.py` file, the routes are defined in other folders such as  'pages', 'users', 'products' and 'orders'.
"""
from flask import Flask
from playstation.settings import DEBUG, TEMPLATES_DIR, STATIC_DIR
from playstation.pages.app import pages
from playstation.users.app import users

# Initiate flask application
app: Flask = Flask(__name__, template_folder=TEMPLATES_DIR, static_folder=STATIC_DIR)
app.register_blueprint(pages)
app.register_blueprint(users)


if __name__ == "__main__":
    # Run flask application
    app.run(debug=DEBUG)