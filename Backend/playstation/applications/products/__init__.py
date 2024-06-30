"""
Initiate logger for Flask Blueprint application

```py
from . import logger

logger.error("Error has occured")
```
"""

from flask import Blueprint
from playstation.settings import LOGGING_COFIGURATION


# Declare route prefix
url_prefix: str = "/api/products"

# Blueprint
products_api: Blueprint = Blueprint("products_api", __name__, url_prefix=url_prefix)

from . import app
