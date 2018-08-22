from app import db

class User(db.Model):
	__tablename__= "users"

	id = db.Collumn(db.Interger, primary_key = True)	
	username = db.Collumn(db.String(50), unique = True)
	email = db.Collumn(db.String(100), unique= True)
	passaword = db.Collumn(db.String(100))
	name = db.Collumn(db.String(100))


	def __init__(self, username ,email ,passaword, name):
		self.username = username
		self.email = email
		self.passaword = passaword
		self.name = name
	def __repr__(self):
		return "<User %r>" % self.username

class Post(db.Model):
	__tablename__ = "posts"

	id = db.Collumn(db.Interger, primary_key = True)
	content = db.Collumn(db.Text)
	user_id = db.Collumn(db.Interger, db.ForeignKey('users.id'))
	user = db.relationship('User', foreing_keys = user_id)

	def __init__(self, content, user_id ):
		self.content = content
		self.user_id = user_id
	def __repr__(self):
		return "<Post %r >" % self.id
class Follow(db.Model):
	__tablename__ = "follow"

	id = db.Collumn(db.Interger, primary_key= True)
	 user_id = db.Collumn(db.Interger, db.ForeignKey('users.id'))
	id_follower = db.Collumn(db.Interger, db.ForeignKey('users.id'))

	user = db.relationship("User", foreing_keys = user_id)

