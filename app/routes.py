from flask import Blueprint, render_template, redirect, url_for, flash, request, current_app
from app import db, bcrypt
from app.forms import RegistrationForm, LoginForm, EventForm, ProfileUpdateForm
from app.models import User, Event
from flask_login import login_user, logout_user, current_user, login_required
from datetime import datetime, date, timedelta
import csv
import os
from werkzeug.utils import secure_filename

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
    try:
        with open('global_events.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for idx, row in enumerate(reader):
                global_events.append({
                    'id': idx,
                    'title': row['title'],
                    'date': row['date'],
                    'category': row['category'],
                    'type': 'global',
                    'date_obj': datetime.strptime(row['date'], '%Y-%m-%d').date()
                })
    except FileNotFoundError:
        pass

    display_name = current_user.name if current_user.name else current_user.email.split('@')[0]

    timeline = []
    if current_user.birthdate:
        today = date.today()
        birthdate = current_user.birthdate
        total_weeks_lived = ((today - birthdate).days // 7) + 1
        total_weeks_to_show = 52 * 90  # Show 90 years of weeks
        
        for week_num in range(1, total_weeks_to_show + 1):
            week_start = birthdate + timedelta(weeks=week_num-1)
            week_end = week_start + timedelta(days=6)
            
            personal_events_in_week = []
            global_events_in_week = []
            
            lived = (week_start <= today)
            
            for event in personal_events:
                if event.date >= week_start and event.date <= week_end:
                    personal_events_in_week.append(f"{event.title} ({event.category})")
            
            for event in global_events:
                if event['date_obj'] >= week_start and event['date_obj'] <= week_end:
                    global_events_in_week.append(f"{event['title']} ({event['category']})")
            
            timeline.append({
                'week_num': week_num,
                'lived': lived,
                'personal_events': personal_events_in_week,
                'global_events': global_events_in_week
            })

    return render_template('dashboard.html',
                         personal_events=personal_events,
                         global_events=global_events,
                         birthdate=current_user.birthdate,
                         display_name=display_name,
                         today=date.today(),
                         timeline=timeline)

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

@main.route("/delete_event/<int:event_id>", methods=['POST'])
@login_required
def delete_event(event_id):
    event = Event.query.get_or_404(event_id)
    if event.user_id != current_user.id:
        flash('Unauthorized!', 'danger')
        return redirect(url_for('main.dashboard'))
    db.session.delete(event)
    db.session.commit()
    flash('Event deleted successfully.', 'success')
    return redirect(url_for('main.dashboard'))

@main.route("/profile", methods=['GET', 'POST'])
@login_required
def profile():
    form = ProfileUpdateForm()
    if form.validate_on_submit():
        current_user.name = form.name.data
        current_user.email = form.email.data
        current_user.birthdate = form.birthdate.data
        if form.profile_pic.data:
            pic_file = form.profile_pic.data
            filename = secure_filename(pic_file.filename)
            pic_path = os.path.join(current_app.root_path, 'static/profile_pics', filename)
            pic_file.save(pic_path)
            current_user.profile_pic = filename
        db.session.commit()
        flash('Profile updated successfully!', 'success')
        return redirect(url_for('main.profile'))

    elif request.method == 'GET':
        form.name.data = current_user.name
        form.email.data = current_user.email
        form.birthdate.data = current_user.birthdate

    profile_pic = url_for('static', filename='profile_pics/' + (current_user.profile_pic if current_user.profile_pic else 'default.jpg'))
    return render_template('profile.html', form=form, profile_pic=profile_pic)
