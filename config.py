import os

class Config:
    db_url = os.environ.get('DATABASE_URL')
    if db_url:
        SQLALCHEMY_DATABASE_URI = db_url.replace('postgres://', 'postgresql://')
    else:
        # fallback URI or raise a meaningful error
        raise ValueError("DATABASE_URL environment variable is not set.")
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False
