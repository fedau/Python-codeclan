
import datetime
from models.event import Event

event1= Event(datetime.datetime(2022, 12, 17), 'Circus', 300, 'Grand Room', 'The circus is in town come on down')
event2= Event(datetime.datetime(2022, 12, 19), 'Who dunn it', 70, 'Theater', 'The ensemble Extraordinair from London is preforming for the last tine Who Dunn It')
event3= Event(datetime.datetime(2022, 12, 23), 'Christmas cheer', 200, 'The plaza', 'Come down to soak up Christmas joy with special disney guests')



event_list = [event1, event2,event3]


def get_event(event_list_index):
    return event_list[event_list_index]

def add_event(event):
    event_list.append(event)



 