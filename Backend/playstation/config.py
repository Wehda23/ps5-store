# playstation/config.py

import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard_to_guess_secret_key'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(os.getcwd(), 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = False

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'  # Use in-memory SQLite for testing

class ProductionConfig(Config):
    @staticmethod
    def init_app(app):
        # Production specific initialization
        pass

class MySQLProductionConfig(ProductionConfig):
    SQLALCHEMY_DATABASE_URI = os.environ.get('MYSQL_DATABASE_URL') or 'mysql+pymysql://username:password@localhost/dbname'

class PostgreSQLProductionConfig(ProductionConfig):
    SQLALCHEMY_DATABASE_URI = os.environ.get('POSTGRESQL_DATABASE_URL') or 'postgresql://username:password@localhost/dbname'


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production_mysql': MySQLProductionConfig,
    'production_postgresql': PostgreSQLProductionConfig,

    'default': DevelopmentConfig
}
