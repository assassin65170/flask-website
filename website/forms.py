from flask_wtf import FlaskForm
from wtforms import validators, StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, Email, ValidationError, EqualTo
from website.models import Users


class Form(FlaskForm):
    username = StringField(label='Name', validators=[DataRequired(), Length(min=2, max=30)])
    email_address = StringField(label='Email', validators=[Email(), DataRequired()])
    subject = StringField(label='Subject', validators=[DataRequired(), Length(min=2, max=50)])
    message = StringField(label='Message', validators=[DataRequired(), Length(min=2, max=300)])
    submit = SubmitField(label='Submit')

class Login(FlaskForm):
    email_address = StringField(label='Email', validators=[Email(), DataRequired()])
    password = PasswordField(label='Password', validators=[DataRequired()])
    remember = BooleanField(label='Remember Me')
    submit = SubmitField(label='Log in')


class Signup(FlaskForm):
    def validate_username(self, username_to_check):
        user = Users.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError('Username already exists! Please try a different username')

    def validate_email_address(self, email_address_to_check):
        email_address = Users.query.filter_by(email_address=email_address_to_check.data).first()
        if email_address:
            raise ValidationError('Email Address already exists! Please try a different email address')
    username = StringField(label='UserName', validators=[Length(min=2, max=30), DataRequired()])
    email_address = StringField(label='Email', validators=[Email(), DataRequired()])
    password = PasswordField(label='Password', validators=[DataRequired()])
    password1 = PasswordField(label='Confirm Password', validators=[EqualTo('password'), DataRequired()])
    submit = SubmitField(label='Create Account')

