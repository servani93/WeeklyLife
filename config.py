import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'supersecretkey')  # Use environment variable
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///site.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = Falseimport os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'supersecretkey')  # Use environment variable
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///site.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
