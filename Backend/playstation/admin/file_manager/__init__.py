"""
file_manager package initialization.
"""

from .file_handler import FileHandler
from .image_handler import ImageHandler
from .storage import LocalStorage, AmazonS3Bucket
from playstation.settings import STORAGE


# Check if storage is local or Amazon
if STORAGE.lower() in {"amazon", "aws"}:
    from playstation.settings import (
        AWS_STORAGE_BUCKET_NAME,
        AWS_ACCESS_KEY_ID,
        AWS_SECRET_ACCESS_KEY,
    )

    storage = AmazonS3Bucket(
        AWS_STORAGE_BUCKET_NAME, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY
    )
else:
    storage = LocalStorage()

# Define image and file handlers
image_handler: ImageHandler = ImageHandler(storage)
file_handler: FileHandler = FileHandler(storage)
