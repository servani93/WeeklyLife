import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SQLALCHEMY_DATABASE_URI = (
        os.environ.get("DATABASE_URL")
        or os.environ.get("PGDATABASE_URL")
        or 'sqlite:///' + os.path.join(basedir, 'dev.db')  # fallback for dev
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False
