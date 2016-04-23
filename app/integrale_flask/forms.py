from flask.ext.wtf import Form
from wtforms import TextField, TextAreaField, SubmitField, validators, ValidationError
 
class ContactForm(Form):
  name = TextField("Name", [validators.Required("Enter your name.")])
  email = TextField("Email", [validators.Required("Enter your email"), validators.Email("Enter a valide email.")])
  subject = TextField("Subject", [validators.Required("Enter your subject")])
  message = TextAreaField("Message", [validators.Required("Enter your message")])
  submit = SubmitField("Send")