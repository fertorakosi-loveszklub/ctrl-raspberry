from States.AbstractState import AbstractState


class DefaultState(AbstractState):
    def run(self):
        keypad = self.container['keypad']
        radio = self.container['radio']
        client = self.container['client']
        screen = self.container['screen']

        radio_code = radio.receive_radio()

        if radio_code:
            if radio.authorize(radio_code):
                message = radio.get(radio_code)
                if message:
                    client.send(message['message'])

        key = keypad.get_key()

        if key:
            if key in [1, 2, 3, 4, 5]:
                client.send("rotate" + str(key))

            if key == "*":
                self.stateMachine.change_state('command_select')

            if key == '#':
                radio.toggle_type2()
                if radio.disallow_type2:
                    screen.message_and_reset('Loallasok', 'letiltva')
                else:
                    screen.message_and_reset('Loallasok', 'endedelyezve')