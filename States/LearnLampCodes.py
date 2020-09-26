from States.AbstractState import AbstractState
import time

class LearnLampCodes(AbstractState):
    def run(self):
        keypad = self.container['keypad']
        radio = self.container['radio']
        screen = self.container['screen']

        screen.write_new('Reflektor tanit.', 'Tavir. gomb...')

        while not done:
            code = radio.receive_radio()

            if code:
                # Tanuld meg
                screen.write_new('Melyik loallas?')
                while True:
                    newKey = keypad.get_key()
                    if newKey in [1, 2, 3, 4, 5]:
                        radio.rememberLamp(code, newKey, str(key))
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


