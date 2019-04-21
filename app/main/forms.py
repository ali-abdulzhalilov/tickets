from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length

class EditTicketForm(FlaskForm):
	title = StringField('Title', validators=[Length(min=0, max=20)])
	body = TextAreaField('Body', validators=[DataRequired(), Length(min=20, max=400)])
	submit = SubmitField('Submit')