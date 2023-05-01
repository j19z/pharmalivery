from flask import flash
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError, Optional
from app.models import User


class LoginForm(FlaskForm):
    email = StringField(validators=[InputRequired(), Length(min=4, max=20)], render_kw={'placeholder':'Email'})
    password = PasswordField(validators=[InputRequired(), Length(min=4, max=20)], render_kw={'placeholder':'Password'})
    submit = SubmitField('Login')


class SignupForm(FlaskForm):
    email = StringField(validators=[InputRequired(), Length(min=4, max=20)], render_kw={'placeholder':'Email'})
    password = PasswordField(validators=[InputRequired(), Length(min=4, max=20)], render_kw={'placeholder':'Password'})
    submit = SubmitField('Signup')

    def validate_email(self, email):
        existing_user_email = User.query.filter_by(email=email.data).first()
        if existing_user_email:
            flash('Email address already exists')
            raise ValidationError('That email already exists. Please choose a diferent one.')
        

class ProfileUserForm(FlaskForm):
    name = StringField(validators=[InputRequired(), Length(min=4, max=20)], render_kw={'placeholder':'Name'})
    email = StringField(validators=[InputRequired(), Length(min=4, max=20)], render_kw={'placeholder':'Email'})
    # Optional() helps update the name and emial without the password in case its empty but still requires Lenght()
    password = PasswordField(validators=[Optional(), Length(min=4, max=20)], render_kw={'placeholder':'Password'})
    password_confirmation = PasswordField(validators=[Optional(), Length(min=4, max=20)], render_kw={'placeholder':'Confirm Password'})
    image_filename = FileField(label='Image', validators=[FileAllowed(['jpg','png','jpeg'])])
    submit = SubmitField('Update')

class ForgotPasswordForm(FlaskForm):
    email = StringField(validators=[InputRequired(), Length(min=4, max=20)], render_kw={'placeholder':'Email'})
    submit = SubmitField('Send Reset Link')