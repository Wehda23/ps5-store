"""
Module for handling file operations.
"""

from werkzeug.utils import secure_filename
from .storage import Storage
from .exceptions import FileSaveException
from playstation.settings import STATIC_DIR


class FileHandler:
    """
    A class to handle file saving operations.

    Attributes:
        storage (Storage): The storage mechanism to use.
    """

    def __init__(self, storage: Storage):
        """
        Initializes the FileHandler with the specified storage.

        Args:
            storage (Storage): The storage mechanism to use.
        """
        self.storage = storage

    def save_file(self, file, upload_dir: str = STATIC_DIR):
        """
        Saves the provided file to the specified upload directory.

        Args:
            file: The file to be saved.
            upload_dir (str): The directory where the file should be saved.

        Returns:
            str: The path where the file was saved.

        Raises:
            FileSaveException: If the file cannot be saved.
        """
        try:
            filename = secure_filename(file.filename)
            file_path = self.storage.save(file, upload_dir, filename)
            return file_path
        except Exception as e:
            raise FileSaveException(f"Failed to save file: {str(e)}")
