

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length

class EditTicketForm(FlaskForm):
	title = StringField('Title', validators=[Length(min=0, max=40)])
	body = TextAreaField('Body', validators=[DataRequired(), Length(min=40)])
	submit = SubmitField('Submit')