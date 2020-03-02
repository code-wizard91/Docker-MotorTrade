from flask_wtf import FlaskForm
from application.models import Users
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError

class RegistrationForm(FlaskForm):
        username = StringField('Username', validators = [DataRequired(), Length(min=4, max=20)])
        first_name = StringField('First Name', validators = [DataRequired(), Length(min=3, max=30)])
        last_name = StringField('Last name', validators = [DataRequired(), Length(min=2, max=30)])
        email = StringField('Email', validators = [DataRequired(),Email()])
        password = PasswordField('Password', validators = [DataRequired(), Length(min=5)])
        confirm_password = PasswordField('Confirm Password', validators = [DataRequired(), EqualTo('password')])
        submit = SubmitField('Sign Up')

        def validate_username(self,username):
            user = Users.query.filter_by(username = username.data).first()

            if user:
                raise ValidationError('Username is taken Please use a different one')

        def validate_email(self,email):
            user = Users.query.filter_by(email = email.data).first()

            if user:
                raise ValidationError('Email is taken Please use a different one')


class LoginForm(FlaskForm):
        email = StringField('Email', validators = [DataRequired(),Email()])
        password = PasswordField('Password', validators = [DataRequired()])
        remember = BooleanField('Remember Me')
        submit = SubmitField('Login')
