"""
Custom exceptions for the file_manager package.
"""


class FileManagerException(Exception):
    """Base exception class for the file manager."""

    pass


class FileSaveException(FileManagerException):
    """Exception raised when a file cannot be saved."""

    pass


class InvalidFileTypeException(FileManagerException):
    """Exception raised for invalid file types."""

    pass
