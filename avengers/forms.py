from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import  DataRequired, EqualTo, Email
from wtforms import ValidationError
# import phonenumbers

#FlaskForm is a Mix-in
class UserInfoForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    phone = StringField('Phone', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_pass = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField()

    # From: https://stackoverflow.com/questions/36251149/validating-us-phone-number-in-wtfforms
    # def validate_phone(form, field):
    #     if len(field.data) > 16:
    #         raise ValidationError('Invalid phone number.')
    #     try:
    #         input_number = phonenumbers.parse(field.data)
    #         if not (phonenumbers.is_valid_number(input_number)):
    #             raise ValidationError('Invalid phone number.')
    #     except:
    #         input_number = phonenumbers.parse("+1"+field.data)
    #         if not (phonenumbers.is_valid_number(input_number)):
    #             raise ValidationError('Invalid phone number.')

class BlogPostFrom(FlaskForm):
    title = TextAreaField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField()

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    pasword = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField