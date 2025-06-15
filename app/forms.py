from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DateField, SelectField, FileField
from wtforms.validators import DataRequired, Email, EqualTo, Length, Optional
from flask_wtf.file import FileAllowed

class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    birthdate = DateField('Birthdate', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class EventForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    date = DateField('Date', validators=[DataRequired()])
    category = StringField('Category', validators=[DataRequired()])
    type = SelectField('Type', choices=[('personal', 'Personal'), ('global', 'Global')], validators=[DataRequired()])
    submit = SubmitField('Save Event')

class ProfileUpdateForm(FlaskForm):   # 👈 You missed this most likely
    name = StringField('Name', validators=[Optional(), Length(min=2, max=100)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    birthdate = DateField('Birthdate', validators=[DataRequired()])
    profile_pic = FileField('Update Profile Picture', validators=[Optional(), FileAllowed(['jpg', 'png', 'jpeg'], 'Images only!')])
    submit = SubmitField('Update Profile')
