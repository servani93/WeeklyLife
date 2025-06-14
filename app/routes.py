from flask import Blueprint, render_template, redirect, url_for, flash, request
from app import db, bcrypt
from app.forms import RegistrationForm, LoginForm, EventForm
from app.models import User, Event
from flask_login import login_user, logout_user, current_user, login_required
from datetime import datetime, date
import csv

main = Blueprint('main', __name__)

@main.route("/")
def home():
    return redirect(url_for('main.login'))

@main.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_pw = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(email=form.email.data, password=hashed_pw, birthdate=form.birthdate.data)
        db.session.add(user)
        db.session.commit()
        flash('Account created! You can now log in.', 'success')
        return redirect(url_for('main.login'))
    return render_template('register.html', form=form)

@main.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for('main.dashboard'))
        else:
            flash('Login Unsuccessful. Check email and password.', 'danger')
    return render_template('login.html', form=form)

@main.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('main.login'))

@main.route("/dashboard")
@login_required
def dashboard():
    personal_events = Event.query.filter_by(user_id=current_user.id).all()
    global_events = []
    with open('global_events.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            global_events.append({
                'title': row['title'],
                'date': row['date'],
                'category': row['category'],
                'type': 'global'
            })
    return render_template('dashboard.html', personal_events=personal_events, global_events=global_events, birthdate=current_user.birthdate)

@main.route("/add_event", methods=['GET', 'POST'])
@login_required
def add_event():
    form = EventForm()
    if form.validate_on_submit():
        event = Event(title=form.title.data, date=form.date.data, category=form.category.data,
                      type=form.type.data, user_id=current_user.id if form.type.data == 'personal' else None)
        db.session.add(event)
        db.session.commit()
        return redirect(url_for('main.dashboard'))
    return render_template('add_event.html', form=form)

@main.route("/edit_event/<int:event_id>", methods=['GET', 'POST'])
@login_required
def edit_event(event_id):
    event = Event.query.get_or_404(event_id)
    if event.user_id != current_user.id:
        flash('Unauthorized!', 'danger')
        return redirect(url_for('main.dashboard'))
    form = EventForm(obj=event)
    if form.validate_on_submit():
        event.title = form.title.data
        event.date = form.date.data
        event.category = form.category.data
        event.type = form.type.data
        db.session.commit()
        return redirect(url_for('main.dashboard'))
    return render_template('edit_event.html', form=form)

@main.route("/delete_event/<int:event_id>")
@login_required
def delete_event(event_id):
    event = Event.query.get_or_404(event_id)
    if event.user_id != current_user.id:
        flash('Unauthorized!', 'danger')
        return redirect(url_for('main.dashboard'))
    db.session.delete(event)
    db.session.commit()
    return redirect(url_for('main.dashboard'))
