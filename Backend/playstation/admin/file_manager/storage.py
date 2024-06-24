"""
Module for storage handling.
"""

import os
import boto3
from abc import ABC, abstractmethod
from botocore.exceptions import NoCredentialsError
from .exceptions import FileSaveException


class Storage(ABC):
    """
    Abstract base class for storage mechanisms.

    Methods:
        save(file, upload_dir, filename): Saves the file to the specified directory.
    """

    @abstractmethod
    def save(self, file, upload_dir, filename):
        """
        Saves the file to the specified directory.

        Args:
            file: The file to be saved.
            upload_dir (str): The directory where the file should be saved.
            filename (str): The name of the file.

        Returns:
            str: The path where the file was saved.
        """
        pass


class LocalStorage(Storage):
    """
    Concrete implementation of Storage for saving files locally.

    Methods:
        save(file, upload_dir, filename): Saves the file to the local filesystem.
    """

    def save(self, file, upload_dir, filename):
        """
        Saves the file to the local filesystem.

        Args:
            file: The file to be saved.
            upload_dir (str): The directory where the file should be saved.
            filename (str): The name of the file.

        Returns:
            str: The path where the file was saved.
        """
        if not os.path.exists(upload_dir):
            os.makedirs(upload_dir)
        file_path = os.path.join(upload_dir, filename)
        file.save(file_path)
        return file_path


class AmazonS3Bucket(Storage):
    """
    Concrete implementation of Storage for saving files to Amazon S3.

    Attributes:
        bucket_name (str): The name of the S3 bucket.
        s3_client: The boto3 S3 client.

    Methods:
        save(file, upload_dir, filename): Uploads the file to the S3 bucket.
    """

    def __init__(self, bucket_name, aws_access_key_id, aws_secret_access_key):
        """
        Initializes the AmazonS3Bucket with the specified bucket name and credentials.

        Args:
            bucket_name (str): The name of the S3 bucket.
            aws_access_key_id (str): The AWS Access Key ID.
            aws_secret_access_key (str): The AWS Secret Access Key.
        """
        self.bucket_name = bucket_name
        self.s3_client = boto3.client(
            "s3",
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
        )

    def save(self, file, upload_dir, filename):
        """
        Uploads the file to the S3 bucket.

        Args:
            file: The file to be uploaded.
            upload_dir (str): The directory where the file should be saved (used for organizing in S3).
            filename (str): The name of the file.

        Returns:
            str: The S3 URL where the file was saved.

        Raises:
            FileSaveException: If the file cannot be uploaded to S3.
        """
        try:
            s3_path = os.path.join(upload_dir, filename)
            self.s3_client.upload_fileobj(file, self.bucket_name, s3_path)
            s3_url = f"https://{self.bucket_name}.s3.amazonaws.com/{s3_path}"
            return s3_url
        except NoCredentialsError:
            raise FileSaveException("Credentials not available")
        except Exception as e:
            raise FileSaveException(f"Failed to upload file to S3: {str(e)}")
