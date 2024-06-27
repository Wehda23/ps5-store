"""
Initiate logger for Flask Blueprint application

```py
from . import logger

logger.error("Error has occured")
```
"""

import logging
from logging import Logger
from playstation.settings import LOGGING_COFIGURATION


# Get the loggger
logger: Logger = logging.getLogger(LOGGING_COFIGURATION["NAME"])
