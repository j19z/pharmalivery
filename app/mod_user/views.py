import os
import uuid as uuid
from flask import Blueprint, render_template, flash, redirect, url_for, current_app
from flask_login import login_required, current_user, logout_user, login_user
from werkzeug.utils import secure_filename
from app.extensions import db, bcrypt
from app.models import User
from app.mod_user.forms import LoginForm, SignupForm, ProfileUserForm
import shutil

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            if bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user)
                return redirect(url_for('main.dashboard'))
            else:
                flash('Please check your login details and try again.')
        else:
            flash('Please check your login details and try again.')

    return render_template('user/login.html', form=form)


@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        new_user = User(email=form.email.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
        return redirect(url_for('main.dashboard'))
    
    return render_template('user/signup.html', form=form)


@auth.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


def save_image(image_file):
    image_filename = secure_filename(image_file.filename)
    image_filename_UUID = str(uuid.uuid1()) + '_' + image_filename
    image_path = os.path.join(current_app._get_current_object().root_path, current_app.config.get('PROFILE_PIC_FOLDER'), image_filename_UUID)
    image_file.save(image_path)
    return image_filename_UUID

def delete_image(image_filename):
    image_path = os.path.join(current_app._get_current_object().root_path, current_app.config.get('PROFILE_PIC_FOLDER'), image_filename)
    if (os.path.exists(image_path)):
        os.remove(image_path)

@auth.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    form = ProfileUserForm()
    if current_user.image_filename != None:
        image_filename = current_user.image_filename
    else:
        image_filename = None
    
    if form.validate_on_submit():
        user = User.query.filter_by(id=current_user.id).first()
        if form.password.data and form.password.data != form.password_confirmation.data:
            flash('Password and Confirm Password does not match.', 'danger')
        else:
            if form.image_filename.data and current_user.image_filename:
                delete_image(current_user.image_filename)
                image_file = save_image(form.image_filename.data)
                user.image_filename = image_file
            if form.image_filename.data and not current_user.image_filename:
                image_file = save_image(form.image_filename.data)
                user.image_filename = image_file
            if form.name.data:
                user.name = form.name.data
            if form.email.data:
                user.email = form.email.data
            if form.password.data:
                hashed_password = bcrypt.generate_password_hash(form.password.data)
                user.password = hashed_password
            db.session.commit()
            flash('User profile was successfully updated', 'success')  
    return render_template('user/profile.html', form=form, image_filename=image_filename)
