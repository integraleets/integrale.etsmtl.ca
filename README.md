# Integrale.etsmtl.ca

## How to
	$ sudo easy_install virtualenv 
	$ virtualenv venv
	$ . venv/bin/activate   (mac / Linux ) venv\scripts\activate (windows)
	(venv) $ pip install Flask flask-login flask-wtf flask-sqlalchemy flask-mail mysql-python
	
	see [http://flask.pocoo.org/docs/0.10/installation/#virtualenv](http://flask.pocoo.org/docs/0.10/installation/#virtualenv) for dev environment

## Utilisation
 
	$ . venv/bin/activate   ( venv\scripts\activate (windows))
	(venv) $ cd app
	(venv) $ python runserver.py
 
L'application sera disponible sur [http://localhost:5000](http://localhost:5000).


## Documentation

La documentation de Flask est accessible via [http://flask.pocoo.org/docs/0.10/](http://flask.pocoo.org/docs/0.10/).

Liste des extensions : http://flask.pocoo.org/extensions/

Intro à Flask : http://code.tutsplus.com/tutorials/intro-to-flask-signing-in-and-out--net-29982
