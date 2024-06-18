"""
# Package to configer swagger
"""

from flask_swagger_ui import get_swaggerui_blueprint
from playstation.settings import STATIC_DIR
from flask import Blueprint
import os


### Swagger specific ###
SWAGGER_URL: str = "/docs"
API_URL: str = os.path.join(STATIC_DIR, "swagger_config.json")  # URI to swagger file


# Configure Swagger Application
swaggerui_blueprint: Blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,  # Swagger UI static files will be mapped to '{SWAGGER_URL}/dist/'
    API_URL,
    config={"app_name": "Play Station 5 Store"},  # Swagger UI config overrides
)
