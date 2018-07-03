import json

class RadioKeymap:

    def __init__(self): 
        self.keymap = self.loadKeymap("radio.json")

    def loadKeymap(self, filename):
        with open(filename) as f:
                return json.load(f)
                        
                        
    def remember(self, radioCode, remote):
        self.keymap[radioCode] = remote

    
    def saveKeymap(self, filename):
        text = json.dumps(self.keymap)
        textFile = open(filename, "w")
        textFile.write(text)
        textFile.close()

