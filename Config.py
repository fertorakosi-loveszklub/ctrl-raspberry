import json


class Config:
    def __init__(self, filename):
        self.config = {}
        self.loadConfig(filename)

    def loadConfig(self, filename):
        with open(filename) as f:
            self.config = json.load(f)

    def get(self, key, default=None):
        if key not in self.config:
            return default

        return self.config[key]
