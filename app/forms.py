
from wtforms.fields import BooleanField, TextField, StringField, PasswordField, SubmitField
from wtforms import validators
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm

class RegistForm(FlaskForm):
    username = StringField('username', validators = [DataRequired()]) 
    slgon = StringField('Slgon', validators = [DataRequired()])
    data = StringField('data', validators = [DataRequired()])
                       
    video = StringField('video', validators = [DataRequired()])
    piclist = StringField('piclist', validators = [DataRequired()])

