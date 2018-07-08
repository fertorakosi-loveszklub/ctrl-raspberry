import socket
import time
import pprint

class IPClient:
    def __init__(self, config, container):
        self.remote_ip = config.get("remoteIP")
        self.remote_port = config.get("remotePort", 1993)
        self.socket = None
        self.connected = False
        self.container = container

    def connect(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.remote_ip, self.remote_port))
        self.connected = True

    def keep_connecting(self):
        screen = self.container['screen']
        screen.write_new("Csatlakozas az", "50m egyseghez...")
        while True:
            try:
                self.connect()
                break
            except:
                time.sleep(0.1)
                pass

        screen.write_new("Fertorakosi", "Loveszklub")

    def send(self, message):
        if not self.connected:
            self.keep_connecting()

        message = str(message) + "\n"

        try:
            self.socket.send(message.encode())
        except socket.error:
            self.connected = False
            self.socket.close()
