from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from application.models import Users
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_login import current_user

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

class UpdateAccountForm(FlaskForm):
        username = StringField('Username', validators = [DataRequired(), Length(min=4, max=20)])
        first_name = StringField('First Name', validators = [DataRequired(), Length(min=3, max=30)])
        last_name = StringField('Last name', validators = [DataRequired(), Length(min=2, max=30)])
        email = StringField('Email', validators = [DataRequired(),Email()])
        picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg','png'])])
        submit = SubmitField('Update')

        def validate_username(self,username):
            if username.data != current_user.username:
                user = Users.query.filter_by(username = username.data).first()
                if user:
                    raise ValidationError('Username is taken Please use a different one')

        def validate_email(self,email):
            if email.data != current_user.email:
                user = Users.query.filter_by(email = email.data).first()
                if user:
                    raise ValidationError('Email is taken Please use a different one')


class AdvertForm(FlaskForm):
        title = StringField('Title', validators = [DataRequired()])
        car_descr = TextAreaField('Content', validators = [DataRequired()])
        price = StringField('Price', validators = [DataRequired(), Length(min=4, max=12)])
        mileage = StringField('Mileage', validators = [DataRequired(), Length(min=0, max=20)])
        location = StringField('Location (Postcode, City Etc)', validators = [DataRequired()])
        contact_no = StringField('Contact Number', validators = [DataRequired(), Length(min=4, max=15)])
        image = FileField('Add Image', validators=[FileAllowed(['jpg','png'])])
        submit = SubmitField('Create Post')
