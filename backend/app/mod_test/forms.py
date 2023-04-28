from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import SubmitField


class TestForm(FlaskForm):
    image_filename = FileField(label='Image', validators=[FileAllowed(['jpg','png','jpeg'])])
    #image_filename = FileField('Image')
    submit = SubmitField('Update')