from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, PasswordField, validators

class AnimalForm(FlaskForm):
    name = StringField("Animal name", [validators.Length(min=2, max=30)])
 
    class Meta:
        csrf = False
