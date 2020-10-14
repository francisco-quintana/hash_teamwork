from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length


class SignInForm(FlaskForm):
    username = StringField('User name', validators=[DataRequired(), Length(min=4, max=32, message='User name not valid')])
    password = PasswordField('Password',validators=[DataRequired(), Length(min=8, max=32, message='Password not valid')])
    submit = SubmitField('Sign in')


class SignUpForm(FlaskForm):

    username=StringField('User Name', validators=[DataRequired(), Length(min=4, max=32, message='User name not valid')])
    email=StringField('Email', validators=[DataRequired(), Length(min=4, max=32, message='Email not valid')])
    name=StringField('Name', validators=[DataRequired(), Length(min=4, max=32, message='Name not valid')])
    password=PasswordField('Password', validators=[DataRequired(), Length(min=8, max=32, message='Password not valid')])
    retry_password = PasswordField('Confirm your password', validators=[DataRequired(), Length(min=4, max=32)])
    submit = SubmitField('Sign Up')