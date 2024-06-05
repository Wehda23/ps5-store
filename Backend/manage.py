"""
# Main Flask Application

- In this folder you will find the flask application assembled and ready to run
- The application is divided into several folders and files for better organization and maintainability
- The main application is in the `manage.py` file, the routes are defined in other folders such as 'users', 'products' and 'orders'.
"""
from flask import Flask




# Initiate flask application
app: Flask = Flask(__name__)



if __name__ == "__main__":
    # Run flask application
    app.run(debug=True)