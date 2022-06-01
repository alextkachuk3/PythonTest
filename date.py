from event import Event
from event_importance_enum import EventImportance


class Date:
    def __init__(self, day: int, month: int, year: int, name: str, importance: EventImportance):
        self.day = day
        self.month = month
        self.year = year
        self.event = Event(name, importance)
