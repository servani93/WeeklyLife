from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from config import Config
import os

db = SQLAlchemy()
login_manager = LoginManager()
bcrypt = Bcrypt()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    database_url = os.environ.get('DATABASE_URL')

    if database_url:
        database_url = database_url.replace("postgres://", "postgresql://", 1)
        app.config['SQLALCHEMY_DATABASE_URI'] = database_url
    else:
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  # fallback for local

    db.init_app(app)
    login_manager.init_app(app)
    bcrypt.init_app(app)

    from app import routes
    app.register_blueprint(routes.main)

    with app.app_context():
        db.create_all()

    return app
