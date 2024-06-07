"""
# Main Flask Application

- In this folder you will find the flask application assembled and ready to run
- The application is divided into several folders and files for better organization and maintainability
- The main application is in the `manage.py` file, the routes are defined in other folders such as  'pages', 'users', 'products' and 'orders'.
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from playstation.settings import (
    DEBUG,
    TEMPLATES_DIR,
    STATIC_DIR,
    DATABASE
)
from playstation.applications.pages.app import pages
from playstation.applications.users.app import users_api
from playstation.applications.orders.app import orders_api
from playstation.applications.products.app import products_api



# Initiate flask application
app: Flask = Flask(__name__, template_folder=TEMPLATES_DIR, static_folder=STATIC_DIR)
# Add blueprints
app.register_blueprint(pages)
app.register_blueprint(users_api)
app.register_blueprint(products_api)
app.register_blueprint(orders_api)


if __name__ == "__main__":
    # Run flask application
    app.run(debug=DEBUG)