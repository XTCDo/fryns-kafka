import time
import json


class RecordBuilder:
    def __init__(self):
        self.fields = {}
        self.tags = {}
        self.time = time.time()

    def add_field(self, key, value):
        self.fields[key] = value
        return self

    def add_tag(self, key, value):
        self.tags[key] = value
        return self

    def get_record(self):
        record_as_map = {
            'fields': self.fields,
            'tags': self.tags,
            'time': self.time
        }
        return json.dumps(record_as_map)
