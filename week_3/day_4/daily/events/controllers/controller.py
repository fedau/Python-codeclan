from flask import render_template, request
from models.event_list import event_list, get_event, add_event
from models.event import Event
from app import app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/events')
def all_events():
    return render_template('events.html', event_list=event_list)


@app.route('/events/<int:event_list_index>')
def order(event_list_index):
    one_event = get_event(event_list_index)
    return render_template('event.html', event=one_event)

@app.route('/events/new')
def new_event():
    return render_template('/new_event.html')


@app.route('/events', methods=['POST'])
def save_event():
    form_data = request.form
    event_date = form_data['event_date']
    event_name = form_data['event_name']
    guests = form_data["guests"]
    location = form_data["location"]
    description = form_data["description"]

    
    new_event = Event( event_date, event_name ,guests, location, description)
    add_event(new_event)
    
    return render_template('events.html', event_list=event_list)

