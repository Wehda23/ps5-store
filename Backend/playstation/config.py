"""
Module Contains Configuration for testing
"""

import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard_to_guess_secret_key'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(os.getcwd(), 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'  # Use in-memory SQLite for testing


config = {
    'testing': TestingConfig,
}
