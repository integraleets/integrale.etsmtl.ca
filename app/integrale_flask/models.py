from flask.ext.sqlalchemy import SQLAlchemy
from werkzeug import generate_password_hash, check_password_hash
 
db = SQLAlchemy()

# ---------------------------------------------User class------------------
class User(db.Model):
  __tablename__ = 'users'
  uid = db.Column(db.Integer, primary_key = True)
  firstname = db.Column(db.String(100))
  lastname = db.Column(db.String(100))
  email = db.Column(db.String(120), unique=True)
  admin = db.Column(db.Boolean)
  pwdhash = db.Column(db.String(54))
   
  def __init__(self, firstname, lastname, email, password):
    self.firstname = firstname.title()
    self.lastname = lastname.title()
    self.email = email.lower()
    self.set_password(password)
     
  def set_password(self, password):
    self.pwdhash = generate_password_hash(password)
   
  def check_password(self, password):
    return check_password_hash(self.pwdhash, password)

  @property
  def is_authenticated(self):
    return True

  @property
  def is_active(self):
    return True

  @property
  def is_anonymous(self):
    return False

  def get_id(self):
    try:
      return unicode(self.uid)  # python 2
    except NameError:
      return str(self.uid)  # python 3

  def __repr__(self):
    return '<User %r>' % (self.nickname)

  def is_admin(self):
	return self.admin

# ----------------------------------------------Entry class----------------
class Entry(db.Model):
	
  __tablename__ = 'entries'
  uid = db.Column(db.Integer, primary_key = True)
  title = db.Column(db.String(120))
  text = db.Column(db.Text)
  
  def __init__(self, title, text):
    self.title = title
    self.text = text