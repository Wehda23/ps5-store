from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase


# Base Model Class
class Base(DeclarativeBase):
    pass

# Declare Database
db: SQLAlchemy = SQLAlchemy(model_class=Base)