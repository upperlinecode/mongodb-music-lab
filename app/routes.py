import os
from app import app
from flask import render_template, request, redirect
from flask_pymongo import PyMongo

# name of database
# app.config['MONGO_DBNAME'] = 'database-name' 
app.config['MONGO_DBNAME'] = 'music'
# URI of database
# app.config['MONGO_URI'] = 'mongo-uri' 
app.config['MONGO_URI'] = 'mongodb+srv://music:O44MIvI1ftc8mcBo@cluster0-vovhg.mongodb.net/music?retryWrites=true'

mongo = PyMongo(app)


# INDEX

@app.route('/')
@app.route('/index')

def index():
    return "Some text here"


# CONNECT TO MONGODB, ADD DATA

@app.route('/add')

def add():
    # define a variable for the collection you want to connect to

    # use some method on that variable to add/find/delete data

    # return a message to the user (or pass data to a template)
    return ''


# ADD NEW EVENT VIA FORM

@app.route('/events/new', methods=['GET', 'POST'])

def new_event():
    if request.method == "GET":
        return render_template('new_event.html')
    else:
        user_name = request.form['user_name']
        event_name = request.form['event_name']
        event_date = request.form['event_date']

        events = mongo.db.events
        events.insert({'event': event_name, 'date': event_date, 'user': user_name})
        return redirect('/')


# SHOW ALL EVENTS IN DATABASE

@app.route('/events')

def events():
    collection = mongo.db.events
    events = collection.find({})

    return render_template('events.html', events = events)


