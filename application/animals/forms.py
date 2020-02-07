from flask_wtf import FlaskForm
from wtforms import StringField, validators

class AnimalForm(FlaskForm):
    name = StringField("Animal name", [validators.Length(min=2)])
 
    class Meta:
        csrf = False

class UserForm(FlaskForm):
    name = StringField("Name", [validators.Length(min=2)])
    username = StringField("Username", [validators.Length(min=2)])
    password = StringField("Password", [validators.Length(min=2)])

    class Meta:
        csrf = False

class FoodForm(FlaskForm):
    name = StringField("New food:", [validators.Length(min=2)])

    class Meta:
        csrf = False