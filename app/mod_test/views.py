import os
import uuid as uuid
from flask import Blueprint, render_template, current_app
from werkzeug.utils import secure_filename
from app.mod_test.forms import TestForm
import pandas as pd
from app.models import Item
from app.extensions import db


test = Blueprint('test', __name__)


@test.route('/test', methods=['GET', 'POST'])
def tests():

    file_path = 'C:\\Users\\jgmus\\OneDrive\\Desktop\\data_ejemplo.xlsx'
    df = pd.read_excel(file_path)
    

    # for index, row in df.iterrows():
    #     item = Item(
    #         code=row['code'],
    #         name=row['name'],
    #         category=row['category'],
    #         quantity=row['quantity'],
    #         description=row['description'],
    #         location=row['location'],
    #     )
    #     db.session.add(item)
        
    # db.session.commit()
    # db.session.close()

    items = Item.query.all()

    return render_template('test/test.html', items=items)