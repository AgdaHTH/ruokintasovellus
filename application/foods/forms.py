from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, PasswordField, validators

class FoodForm(FlaskForm):
    name = StringField("New food:", [validators.Length(min=2, max=20)])

    class Meta:
        csrf = False

class PriceForm(FlaskForm):
    price = IntegerField("New price:", [validators.NumberRange(min=1, max=100)])

    class Meta:
        csrf = False