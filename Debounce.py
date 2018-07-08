import time


class Debounce:
    def __init__(self, timeout):
        self.timeout = timeout
        self.last_debounce = 0

    def debounce(self):
        now = int(round(time.time() * 1000))

        if now - self.last_debounce < self.timeout:
            return False

        self.last_debounce = now
        return True
