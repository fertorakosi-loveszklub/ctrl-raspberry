class Container:
    def __init__(self):
        self.bindings = {}

    def bind(self, key, value):
        self.bindings[key] = value

    def resolve(self, key):
        if key not in self.bindings:
            return None

        value = self.bindings[key]
        if callable(value):
            value = value()

        return value

    def __getitem__(self, item):
        return self.resolve(item)

    def __setitem__(self, key, value):
        return self.bind(key, value)