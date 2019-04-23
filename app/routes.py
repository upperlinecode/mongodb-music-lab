import os
from app import app
from flask import render_template, request, redirect
from flask_pymongo import PyMongo

# name of database
app.config['MONGO_DBNAME'] = 'database-name' 

# URI of database
app.config['MONGO_URI'] = 'mongo-uri' 

mongo = PyMongo(app)


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


