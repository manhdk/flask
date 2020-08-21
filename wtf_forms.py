# pip install flask-WTF
# pip install email_validator
from flask_wtf import Form
from wtforms import TextField, IntegerField, TextAreaField, SubmitField, RadioField, SelectField
from wtforms import validators, ValidationError
import email_validator

class ContactForm(Form):
    name = TextField('Name of Student', [validators.required('Please enter your name.')])
    email = TextField('Email', [validators.required('Please enter your email address.'), validators.Email("Please enter your email address.")])
    gender = RadioField('Gender', choices= [('M', 'Male'), ('F', 'Female')])
    address = TextAreaField('Address')
    age = IntegerField('Age')
    language = SelectField('Languages', choices= [('cpp', 'C++'), ('py', 'Python')])
    submit = SubmitField('Send')
