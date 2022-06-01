from event_importance_enum import EventImportance


class Event:
    def __init__(self, name: str, importance: EventImportance):
        self.name = name
        self.importance = importance
