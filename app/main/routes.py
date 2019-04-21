from flask import render_template, redirect, url_for

from app.main import bp
from app.main.forms import EditTicketForm

@bp.route('/', methods=['GET'])
@bp.route('/index', methods=['GET'])
def index():
	tickets = [
		{
			'author': 'pew',
			'title': 'some thing',
			'body': 'lorem ipsum etc etc'
		},
		{
			'author': 'anon',
			'body': 'it\'s only water, it\'s onle fire, it\'s only love'
		},
	]
	return render_template('index.html', tickets=tickets)

@bp.route('/create', methods=['GET', 'POST'])
def create():
	form = EditTicketForm()
	if form.validate_on_submit():
		return redirect(url_for('main.index'))
		
	return render_template('create.html', title='New Ticket', form=form)