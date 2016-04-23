from flask import Flask, render_template, request, flash
from forms import ContactForm
from flask.ext.mail import Message, Mail

mail = Mail()

app = Flask(__name__)

app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = ''
app.config["MAIL_PASSWORD"] = ''
 
mail.init_app(app)



app.secret_key = 'development key'

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
  form = ContactForm()
  if request.method == 'POST':
    if form.validate() == False:
      flash('All fields are required.')
      return render_template('contact.html', form=form)
    else:
      msg = Message(form.subject.data, sender='', recipients=['your_email@example.com'])
      msg.body = """
      From: %s <%s>
      %s
      """ % (form.name.data, form.email.data, form.message.data)
      mail.send(msg)
 
      return render_template('contact.html', success=True)
 
  elif request.method == 'GET':
    return render_template('contact.html', form=form)




@app.route("/membre")
def membre():
    return render_template('membre.html')

@app.route("/login")
def login():
    return render_template('login.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == "__main__":
    app.run(debug=True)