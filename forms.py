from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, TextAreaField, BooleanField
from wtforms.validators import InputRequired, Length, NumberRange, URL, Optional




# # # # # # # # # # # # # # # # FORMS # # # # # # # # # # # # # # # # # # # # # # # # 
class AddPetForm(FlaskForm):
    '''Form to add pets'''

    name = StringField(
        'Pet Name',
        validators=[InputRequired()],
    )

    species = SelectField(
        'Species',
        choices=[('cat', 'Cat'), ('dog', 'Dog'), ('porcupine', 'Porcupine')],
    )

    img_url = StringField(
        'Photo URL',
        validators=[Optional(), URL()],
    )

    age = IntegerField(
        'Age',
        validators=[Optional(), NumberRange(min=0, max=30)],
    )

    notes = TextAreaField(
        'Notes',
        validators=[Optional()],
    )




class EditPetForm(FlaskForm):
    '''Form to edit pet info'''

    img_url = StringField(
        'Photo URL',
        validators=[Optional(), URL()],
    )

    notes = TextAreaField(
        'Notes',
        validators=[Optional()],
    )

    available = BooleanField(
        'Available?'
    )