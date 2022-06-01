from date import Date
from event import Event
from event_importance_enum import EventImportance
from event_sort_enum import EventSortType


class Calendar:
    def __init__(self):
        self.dates = []

    def add_event(self, day: int, month: int, year: int, name: str, importance: EventImportance):
        self.dates.append(Date(day, month, year, name, importance))

    def get_by_sort(self, type: EventSortType):
        if type.value is EventSortType.ByDate:
            return sorted(self.dates, key=lambda x: x.day)
        else:
            return sorted(self.dates, key=lambda x: x.event.importance)
