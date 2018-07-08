from States.AbstractState import AbstractState
import time


class CommandSelect(AbstractState):
    def run(self):
        keypad = self.container['keypad']
        radio = self.container['radio']
        screen = self.container['screen']

        screen.write_new('Valassz', 'muveletet')

        key = None
        while key is None:
            key = keypad.get_key()

        if key in [1, 2]:
            # Teaching mode
            screen.write_new('Tavir. tanulasa', '* - megsem')
            done = False

            while not done:
                code = radio.receive_radio()

                if code:
                    # Tanuld meg
                    screen.write_new('Melyik loallas?')
                    while True:
                        newKey = keypad.get_key()
                        if newKey in [1, 2, 3, 4, 5]:
                            radio.remember(code, newKey, str(key))
                            screen.message_and_reset('Megtanulva', 'Loallas: ' + str(newKey))
                            done = True
                            self.stateMachine.change_state('default')
                            break
                        elif newKey == '*':
                            done = True
                            screen.message_and_reset('Megszakitva')
                            self.stateMachine.change_state('default')
                            break
                else:
                    newKey = keypad.get_key()
                    if newKey == '*':
                        screen.message_and_reset('Megszakitva')
                        break

                    time.sleep(0.1)

        else:
            screen.message_and_reset('Megszakitva')
            self.stateMachine.change_state('default')





