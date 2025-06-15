from app import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    birthdate = db.Column(db.Date, nullable=False)
    
    # ✅ Newly required columns for profile feature:
    name = db.Column(db.String(100), nullable=True)
    profile_pic = db.Column(db.String(120), nullable=True)  # stores filename of uploaded profile picture

    events = db.relationship('Event', backref='author', lazy=True)

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date = db.Column(db.Date, nullable=False)
    category = db.Column(db.String(50), nullable=False)
    type = db.Column(db.String(20), nullable=False)  # personal/global
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)  # NULL for global events
