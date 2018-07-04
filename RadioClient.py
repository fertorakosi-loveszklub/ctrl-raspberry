import json
from rpi_rf import RFDevice
import time


class RadioClient:
    def __init__(self, config):
        self.rf_device = RFDevice(config.get("rxPin", 2))
        self.rf_device.enable_rx()
        self.rx_timestamp = None
        self.debounce_timeout = 1000
        self.last_debounce = 0
        self.keymap = {}
        self.load_keymap("radio.json")

    def load_keymap(self, filename):
        with open(filename) as f:
                self.keymap = json.load(f)
                        
    def remember(self, radio_code, remote):
        self.keymap[radio_code] = remote
        self.save_keymap("radio.json")

    def get_message(self, radio_code):
        if radio_code not in self.keymap:
            return None
        return self.keymap[radio_code]

    def save_keymap(self, filename):
        text = json.dumps(self.keymap)
        text_file = open(filename, "w")
        text_file.write(text)
        text_file.close()

    def receive_radio(self):
        if self.debounce() and self.rf_device.rx_code_timestamp != self.rx_timestamp:
            if self.rf_device.rx_code:
                return self.rf_device.rx_code

        return None

    def debounce(self):
        now = int(round(time.time() * 1000))
        if now - self.last_debounce < self.debounce_timeout:
            return False

        self.last_debounce = now
        return True
