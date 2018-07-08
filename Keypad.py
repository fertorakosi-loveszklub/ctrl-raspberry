from Lib import Keypad as KeypadLib
from Debounce import Debounce


class Keypad:
    def __init__(self, config):
        self.keypad_lib = KeypadLib.keypad()
        self.debounce = Debounce(config.get('keypadDebounce', 500))

    def get_key(self):
        key = self.keypad_lib.getKey()
        if key and self.debounce.debounce():
            return key

        return None
