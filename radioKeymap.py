import json


class RadioKeymap:

    def __init__(self):
        self.keymap = {}
        self.loadKeymap("radio.json")

    def loadKeymap(self, filename):
        with open(filename) as f:
                self.keymap = json.load(f)
                        
    def remember(self, radioCode, remote):
        self.keymap[radioCode] = remote
        self.saveKeymap("radio.json")

    def getRemote(self, radioCode):
        if radioCode not in self.keymap:
            return None
        return self.keymap[radioCode]

    def saveKeymap(self, filename):
        text = json.dumps(self.keymap)
        textFile = open(filename, "w")
        textFile.write(text)
        textFile.close()

