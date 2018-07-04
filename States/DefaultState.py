from States.AbstractState import AbstractState


class DefaultState(AbstractState):
    def run(self):
        radio = self.container['radio']
        client = self.container['client']

        radio_code = radio.receive_radio()

        if radio_code is not None:
            print(radio_code)
            return
            message = radio.get_message(radio_code)
            client.send(message)

