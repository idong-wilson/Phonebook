from flask_wtf import FlaskForm

from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Length


class RegistrationForm(FlaskForm):
    first_name = StringField(label="First Name", validators=[DataRequired(), Length(min=3, max=25)])
    last_name = StringField(label="Lasy Name", validators=[DataRequired(), Length(min=3, max=25)])
    address = StringField(label="Address", validators=[DataRequired(), Length(min=10, max=100)])
    phone_number = StringField(label="Phone", validators=[DataRequired()])
    submit = SubmitField("Submit")