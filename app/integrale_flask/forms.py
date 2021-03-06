from flask.ext.wtf import Form
from wtforms import TextField, TextAreaField, SubmitField, validators, ValidationError, PasswordField 
from models import db, User, Entry
 
# -------------------------------------------------ContactForm-------------------------------------------------------
class ContactForm(Form):
  name = TextField("Name", [validators.Required("Enter your name.")])
  email = TextField("Email", [validators.Required("Enter your email"), validators.Email("Enter a valide email.")])
  subject = TextField("Subject", [validators.Required("Enter your subject")])
  message = TextAreaField("Message", [validators.Required("Enter your message")])
  submit = SubmitField("Send")

# --------------------------------------------------EntrieForm------------------------------------------------------
class EntrieForm(Form):
  title = TextField("Title", [validators.Required("Please enter the title")])
  text = TextAreaField("Text", [validators.Required("Please enter the text")])
  submit = SubmitField("Create news")
 
  def __init__(self, *args, **kwargs):
    Form.__init__(self, *args, **kwargs)
	
  def validate(self):
    if not Form.validate(self):
      return False
     
    else:
      return True

# ------------------------------------------------SignupForm--------------------------------------------------------
class SignupForm(Form):
  firstname = TextField("First name",  [validators.Required("Please enter your first name.")])
  lastname = TextField("Last name",  [validators.Required("Please enter your last name.")])
  email = TextField("Email",  [validators.Required("Please enter your email address."), validators.Email("Please enter your email address.")])
  password = PasswordField('Password', [validators.Required("Please enter a password.")])
  submit = SubmitField("Create account")
 
  def __init__(self, *args, **kwargs):
    Form.__init__(self, *args, **kwargs)
 
  def validate(self):
    if not Form.validate(self):
      return False
     
    user = User.query.filter_by(email = self.email.data.lower()).first()
    if user:
      self.email.errors.append("That email is already taken")
      return False
    else:
      return True

# -------------------------------------------------LoginForm-------------------------------------------------------
class LoginForm(Form):
  email = TextField("Email",  [validators.Required("Please enter your email address."), validators.Email("Please enter your email address.")])
  password = PasswordField('Password', [validators.Required("Please enter a password.")])
  submit = SubmitField("Sign In")
   
  def __init__(self, *args, **kwargs):
    Form.__init__(self, *args, **kwargs)
 
  def validate(self):
    if not Form.validate(self):
      return False
     
    user = User.query.filter_by(email = self.email.data.lower()).first()
    if user and user.check_password(self.password.data):
      return True
    else:
      self.email.errors.append("Invalid e-mail or password")
      return False