"""
# Main Flask Application

- In this folder you will find the flask application assembled and ready to run
- The application is divided into several folders and files for better organization and maintainability
- The main application is in the `manage.py` file, the routes are defined in other folders such as  'pages', 'users', 'products' and 'orders'.
"""

from flask import Flask
from playstation.settings import DEBUG, TEMPLATES_DIR, STATIC_DIR, DATABASE, SECRET_KEY
from playstation.applications.pages.app import pages
from playstation.applications.users.app import users_api
from playstation.applications.orders.app import orders_api
from playstation.applications.products.app import products_api
from playstation import db
from playstation.models.users import User
from playstation.models.coupons import Coupons
from playstation.models.orders import Orders
from playstation.models.payments import Payments
from playstation.models.products import Product, Category
from playstation.models.shipping_address import ShippingAddress


# Initiate flask application
app: Flask = Flask(__name__, template_folder=TEMPLATES_DIR, static_folder=STATIC_DIR)

# Add blueprints
app.register_blueprint(pages)
app.register_blueprint(users_api)
app.register_blueprint(products_api)
app.register_blueprint(orders_api)

# Configure Database
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = SECRET_KEY

# Initialize the app with the extension
db.init_app(app)

# Create Database Tables
with app.app_context():
    db.create_all()


# Clear Session
@app.teardown_appcontext
def shutdown_session(exception=None):
    """
    Closes session after each request or application context shutdown to avoid leaks
    """
    db.session.remove()


if __name__ == "__main__":
    # Run flask application
    app.run(debug=DEBUG)
