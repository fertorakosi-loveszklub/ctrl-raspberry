from States.DefaultState import DefaultState
from States.CommandSelect import CommandSelect
import time


class StateMachine:
    def __init__(self, container):
        self.states = {
            'default': DefaultState(container, self),
            'command_select': CommandSelect(container, self)
        }

        self.current_state = self.states['default']

    def run(self):
        while True:
            self.current_state.run()
            time.sleep(0.1)

    def change_state(self, state):
        self.current_state = self.states[state]
