"""
# Module that has setup logging function

Usage Example:

```py
from .logger import setup_logging
from flask import Flask

# Initiate your flask application
app: Flask = Flask(__name__)


# Setup Logger
setup_logging(app)
```
"""

import logging
from logging.handlers import RotatingFileHandler
from logging import Logger
from flask import Flask
from .settings import LOGGING_COFIGURATION
import os

def setup_logging(app: Flask, name: str = LOGGING_COFIGURATION["NAME"]) -> None:
    """
    Set up logging for the Flask application.

    This function configures a logger named as specified with the following settings:
    - Log level is set to DEBUG to capture detailed log messages.
    - Logs are sent to both the console and a rotating file.
    - Console handler logs messages at the DEBUG level and above.
    - File handler logs messages at the INFO level and above.
    - Log messages are formatted to include the timestamp, logger name, log level, and message.

    Args:
        app (Flask): The Flask application instance to which the logger is attached.
        name (str): The name of the logger

    Returns:
        None
    """
    # Create a logger
    logger: Logger = logging.getLogger(name)


    logger.setLevel(logging.DEBUG)  # Set the logger to capture all levels of log messages

    # Create a console handler to output logs to the console
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)  # Console handler captures DEBUG level logs and above

    # Create a rotating file handler to output logs to a file with rotation
    log_file_path = os.path.abspath(LOGGING_COFIGURATION["FILE"])
    file_handler = RotatingFileHandler(log_file_path, maxBytes=10000, backupCount=3)
    file_handler.setLevel(logging.INFO)  # File handler captures INFO level logs and above

    # Define the format for log messages
    formatter = logging.Formatter(LOGGING_COFIGURATION["FORMAT"])
    console_handler.setFormatter(formatter)  # Apply the format to console handler
    file_handler.setFormatter(formatter)  # Apply the format to file handler

    # Add the handlers to the logger
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    # Attach the logger to the Flask application
    app.logger = logger

    @app.teardown_appcontext
    def shutdown_session(exception=None):
        print("Logger Close Handlers")
        for handler in logger.handlers:
            handler.close()
            logger.removeHandler(handler)
