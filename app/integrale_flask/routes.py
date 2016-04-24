from integrale_flask import app
from functools import wraps
from flask import render_template, request, flash, session, url_for, redirect
from forms import ContactForm, SignupForm, SigninForm, EntrieForm
from flask.ext.mail import Message, Mail
from models import db, User, Entry
 
mail = Mail()

# @app.route() mappings start here
@app.route("/")
def index():
  entries = Entry.query.order_by(Entry.uid)
  return render_template('index.html', entries=entries)

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'email' not in session:
            return redirect(url_for('signin', next=request.url))
        return f(*args, **kwargs)
    return decorated_function

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

@app.route('/profile')
def profile():
 
  if 'email' not in session:
    return redirect(url_for('signin'))
 
  user = User.query.filter_by(email = session['email']).first()
 
  if user is None:
    return redirect(url_for('signin'))
  else:
    return render_template('profile.html')

# --------------------------------------------------------------------------------------------------------

@app.route('/addentry', methods=['GET', 'POST'])
@login_required
def addentry():
  form = EntrieForm()
   
  if request.method == 'POST':
    if form.validate() == False:
		return render_template('addentry.html', form=form)
      
    else:
      newentrie = Entry(form.title.data, form.text.data)
      db.session.add(newentrie)
      db.session.commit()
      return redirect(url_for('index'))
   
  elif request.method == 'GET':
    return render_template('addentry.html', form=form)

# --------------------------------------------------------------------------------------------------------
@app.route('/signup', methods=['GET', 'POST'])
def signup():
  form = SignupForm()
 
  if 'email' in session:
    return redirect(url_for('profile')) 
   
  if request.method == 'POST':
    if form.validate() == False:
      return render_template('signup.html', form=form)
    else:
      newuser = User(form.firstname.data, form.lastname.data, form.email.data, form.password.data)
      db.session.add(newuser)
      db.session.commit()
       
      session['email'] = newuser.email
      return redirect(url_for('profile'))
   
  elif request.method == 'GET':
    return render_template('signup.html', form=form)

# --------------------------------------------------------------------------------------------------------

@app.route('/signin', methods=['GET', 'POST'])
def signin():
  form = SigninForm()
 
  if 'email' in session:
    return redirect(url_for('profile')) 
   
  if request.method == 'POST':
    if form.validate() == False:
      return render_template('signin.html', form=form)
    else:
      session['email'] = form.email.data
      return redirect(url_for('profile'))
                 
  elif request.method == 'GET':
    return render_template('signin.html', form=form)


@app.route('/signout')
def signout():
 
  if 'email' not in session:
    return redirect(url_for('signin'))
     
  session.pop('email', None)
  return redirect(url_for('index'))


@app.route("/membre")
def membre():
    return render_template('membre.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == "__main__":
    app.run(debug=True)