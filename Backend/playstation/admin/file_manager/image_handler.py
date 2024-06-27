"""
Module for handling image file operations.
"""

import os
from PIL import Image
from .file_handler import FileHandler
from .exceptions import InvalidFileTypeException
from playstation.settings import MEDIA_DIR, ALLOW_IMAGE_TYPES, STATIC_DIR


class ImageHandler(FileHandler):
    """
    A class to handle image file saving operations.

    Inherits from FileHandler.

    Methods:
        save_image(file, upload_dir, allowed_extensions=None): Saves an image file to the specified directory.
    """

    def save_image(
        self,
        file,
        upload_dir: str = MEDIA_DIR,
        allowed_extensions: set = ALLOW_IMAGE_TYPES,
        safe: bool = False,
    ):
        """
        Saves the provided image file to the specified upload directory.

        Args:
            file: The image file to be saved.
            upload_dir (str): The directory where the file should be saved.
            allowed_extensions (set, optional): A set of allowed file extensions. Defaults to {'png', 'jpg', 'jpeg'}.
            safe (bool, optional): Whether to save the file in a safe manner. Defaults to False

        Returns:
            str: The path where the image was saved.

        Raises:
            InvalidFileTypeException: If the file type is not allowed or the file is not a valid image.
        """
        if not self._is_allowed_file(file.filename, allowed_extensions):
            raise InvalidFileTypeException(f"Invalid file type: {file.filename}")
        file_path = self.save_file(file, upload_dir)
        self._validate_image(file_path)
        return file_path if not safe else file_path.replace(STATIC_DIR, "")

    def _is_allowed_file(self, filename, allowed_extensions):
        """
        Checks if the file has an allowed extension.

        Args:
            filename (str): The name of the file.
            allowed_extensions (set): A set of allowed file extensions.

        Returns:
            bool: True if the file extension is allowed, False otherwise.
        """
        return (
            "." in filename and filename.rsplit(".", 1)[1].lower() in allowed_extensions
        )

    def _validate_image(self, file_path):
        """
        Validates that the file at the specified path is a valid image.

        Args:
            file_path (str): The path to the image file.

        Raises:
            InvalidFileTypeException: If the file is not a valid image.
        """
        try:
            img = Image.open(file_path)
            img.verify()
        except (IOError, SyntaxError) as e:
            os.remove(file_path)
            raise InvalidFileTypeException(f"Invalid image file: {str(e)}")
