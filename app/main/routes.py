from flask import render_template

from app.main import bp

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