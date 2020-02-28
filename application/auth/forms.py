from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators
  
class UserForm(FlaskForm):
    name = StringField("Name", [validators.Length(min=2, max=30)])
    username = StringField("Username", [validators.Length(min=2, max=30)])
    password = PasswordField("Password", [validators.Length(min=2, max=20)])

    class Meta:
        csrf = False

class LoginForm(FlaskForm):
    username = StringField("Username")
    password = PasswordField("Password")
  
    class Meta:
        csrf = False