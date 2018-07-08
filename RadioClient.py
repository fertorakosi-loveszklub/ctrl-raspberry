import Debounce
import json
from rpi_rf import RFDevice


class RadioClient:
    def __init__(self, config):
        self.rf_device = RFDevice(config.get("rxPin", 2))
        self.rf_device.enable_rx()
        self.rx_timestamp = None
        self.debounce = Debounce.Debounce(config.get("rxDebounce", 1500))
        self.keymap = {}
        self.load_keymap("radio.json")
        self.disallow_type2 = False

    def authorize(self, radio_code):
        message = self.get(radio_code)
        if not message:
            return False
        if message['type'] == '1':
            return True
        return not self.disallow_type2

    def toggle_type2(self):
        self.disallow_type2 = not self.disallow_type2

    def load_keymap(self, filename):
        with open(filename) as f:
                self.keymap = json.load(f)
                        
    def remember(self, radio_code, remote, type = '2'):
        if str(radio_code) in self.keymap:
            self.keymap.pop(str(radio_code))

        self.keymap[str(radio_code)] = {
            'message': 'rotate' + str(remote),
            'type': str(type)
        }

        self.save_keymap("radio.json")

    def get(self, radio_code):
        if str(radio_code) not in self.keymap:
            return None
        return self.keymap[str(radio_code)]

    def save_keymap(self, filename):
        text = json.dumps(self.keymap)
        text_file = open(filename, "w")
        text_file.write(text)
        text_file.close()

    def receive_radio(self):
        if self.rf_device.rx_code_timestamp == self.rx_timestamp:
            return None

        if not self.rf_device.rx_code:
            return None

        if not self.rf_device.rx_proto == 1:
            return None

        if not self.debounce.debounce():
            return None

        self.rx_timestamp = self.rf_device.rx_code_timestamp
        return self.rf_device.rx_code
