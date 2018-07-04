class AbstractState:
    def __init__(self, container, stateMachine):
        self.container = container
        self.stateMachine = stateMachine

    def run(self):
        pass
