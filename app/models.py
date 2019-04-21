from datetime import datetime

from app import db

class Ticket(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(20))
	body = db.Column(db.String(400))
	created_at = db.Column(db.DateTime, index=True, default=datetime.utcnow)
	
	def __repr__(self):
		if self.title:
			return '<Ticket {}>'.format(self.title)
		else:
			return '<Ticket {}>'.format(self.body[:20])