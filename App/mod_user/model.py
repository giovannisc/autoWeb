from autoWeb import db

class User(db.Model):
	__tablename__ = "awuser"

	user_id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(50))
	password = db.Column(db.String(50))
	name = db.Column(db.String(50))
	level = db.Column(db.Integer)
	active = db.Column(db.Boolean)
	email = db.Column(db.String(355))
	id_card = db.Column(db.Integer)

	def __init__(self, username, password, name, level, active, email, id_card):
		super(User, self).__init__()
		self.username = username
		self.password = password
		self.name = name
		self.level = level
		self.active = active
		self.email = email
		self.id_card = id_card

	def serialize(self):
		return {
			'id_user': self.id_user, 
			'username': self.username,
			'password': self.password,
			'name':self.name,
			'level':self.level,
			'active':self.active,
			'email':self.email,
			'id_card':self.id_card
		}

def findUserByName(name):
	try:
		user = User.query.filter_by(name=name).first_or_404()
		return user
	except Exception as e:
		print(e)
		return e

def findUserByCardId(id_card):
	try:
		user = User.query.filter_by(id_card=id_card)
		return user
	except Exception as e:
		print(e)
		return e

def insertUser(user):
	try:
		db.session.add(user)
		db.session.commit()
		return True
	except Exception as e:
		print(e)
		return e

def updatePasswordById(user_id, newPassword):
	try:
		user2update = User.query.filter_by(user_id=user_id)
		user2update.password = newPassword
		db.session.commit()
		return True
	except Exception as e:
		print(e)
		return e

def updateActiveById(user_id, active):
	try:
		user2update = User.query.filter_by(user_id=user_id)
		user2update.active = active
		db.session.commit()
		return True
	except Exception as e:
		print(e)
		return e
