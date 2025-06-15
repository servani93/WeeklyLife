import os

class Config:
    SECRET_KEY = 'supersecretkey'  # Change this in production
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
