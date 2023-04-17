import os
import uuid as uuid
from flask import Blueprint, render_template
from flask_login import login_required


main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('main/home.html')

@main.route('/about')
def about():
    return render_template('main/about.html')


@main.route('/dashboard', methods=['GET', 'POST'])
@login_required #This is the function that only shows this page to logged in users
def dashboard():
    return render_template('dashboard.html')













