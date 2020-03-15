from flask_wtf import FlaskForm
from wtforms import BooleanField
from wtforms import PasswordField
from wtforms import StringField
from wtforms import SubmitField
from wtforms.validators import DataRequired, Length


class LoginForm(FlaskForm):
    username = StringField(
        'Username',
        render_kw={
            'placeholder': 'username',
            'required': 'True',
            'maxlength': 10
        },
        validators=[DataRequired(), Length(max=10)]
    )
    password = PasswordField(
        'Password',
        render_kw={
            'placeholder': 'password',
            'required': 'True',
            'maxlength': 25
        },
        validators=[DataRequired(), Length(max=25)]
    )
    submit = SubmitField('Login')
    remember_me = BooleanField('Remember Me')


class RegistrationForm(FlaskForm):
    username = StringField(
        'Username',
        render_kw={
            'placeholder': 'username',
            'required': 'True',
            'maxlength': 10
        },
        validators=[DataRequired(), Length(max=10)]
    )
    password = PasswordField(
        'Password',
        render_kw={
            'placeholder': 'password',
            'required': 'True',
            'maxlength': 25
        },
        validators=[DataRequired(), Length(max=25)])
    submit = SubmitField('Register')
