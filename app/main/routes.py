from flask import render_template, redirect, url_for

from app import db
from app.main import bp
from app.main.forms import EditTicketForm
from app.models import Ticket

@bp.route('/', methods=['GET'])
@bp.route('/index', methods=['GET'])
def index():
	tickets = Ticket.query.all()
	return render_template('index.html', tickets=tickets)

@bp.route('/create', methods=['GET', 'POST'])
def create():
	form = EditTicketForm()
	
	if form.validate_on_submit():
		ticket = Ticket(title=form.title.data, body=form.body.data)
		db.session.add(ticket)
		db.session.commit()
		return redirect(url_for('main.index'))
		
	return render_template('create.html', title='New Ticket', form=form)
	
@bp.route('/view/<int:id>', methods=['GET'])
def view(id):
	ticket = Ticket.query.filter_by(id=id).first_or_404()
	return render_template('view.html', ticket=ticket)
	