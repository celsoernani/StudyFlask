from app import db

class User(db.Model):
	__tablename__= "users"

	id = db.Column(db.Integer, primary_key = True)	
	username = db.Column(db.String(50), unique = True)
	email = db.Column(db.String(100), unique= True)
	passaword = db.Column(db.String(100))
	name = db.Column(db.String(100))


	def __init__(self, username ,email ,passaword, name):
		self.username = username
		self.email = email
		self.passaword = passaword
		self.name = name
	def __repr__(self):
		return "<User %r>" % self.username





