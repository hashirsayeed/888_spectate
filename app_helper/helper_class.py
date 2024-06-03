import json

#a class to implement serialization method of json
class Converter:
    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

class Sport(Converter):
    def __init__(self, name, slug, active):
        self.id = None
        self.name = name
        self.slug = slug
        self.active = active
    def set_id(self, id):
        self.id = id

class Event(Converter):
    def __init__(self, name, active, slug, type, sport_id, status, start_time, actual_start_time):
        self.id = None
        self.name = name
        self.active = active
        self.slug = slug
        self.type = type
        self.sport_id = sport_id
        self.status = status
        self.start_time = start_time
        self.actual_start_time = actual_start_time
    def set_id(self, id):
        self.id = id

class Selection(Converter):
    def __init__(self, name, event_id, price, active, outcome):
        self.id = None
        self.name = name
        self.event_id = event_id
        self.price = price
        self.active = active
        self.outcome = outcome
    def set_id(self, id):
        self.id = id



