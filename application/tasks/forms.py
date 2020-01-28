from flask_wtf import FlaskForm
from wtforms import StringField, validators

class AnimalForm(FlaskForm):
    name = StringField("Animal name", [validators.Length(min=2)])
 
    class Meta:
        csrf = False