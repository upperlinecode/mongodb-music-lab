# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request
from flask_pymongo import PyMongo


# -- Initialization section --
app = Flask(__name__)

# name of database
app.config['MONGO_DBNAME'] = 'database-name'

# URI of database
app.config['MONGO_URI'] = 'mongo-uri'

mongo = PyMongo(app)

# -- Routes section --
# INDEX

@app.route('/')
@app.route('/index')

def index():
    return "Some text here"


# ADD SONGS

@app.route('/add')

def add():
    # define a variable for the collection you want to connect to

    # use some method on that variable to add/find/delete data

    # return a message to the user (or pass data to a template)
    return ''


# SHOW A LIST OF ALL SONG TITLES




# ADVANCED: A FORM TO COLLECT USER-SUBMITTED SONGS




# DOUBLE-ADVANCED: SHOW ARTIST PAGE




# TRIPLE-ADVANCED: SHOW SONG PAGE
