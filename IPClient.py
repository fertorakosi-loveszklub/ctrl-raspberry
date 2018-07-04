import socket


class IPClient:
    def __init__(self, config):
        self.remote_ip = config.get("remoteIP")
        self.remote_port = config.get("remotePort", 1993)
        self.socket = None
        self.connected = False

    def connect(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.remote_ip, self.remote_port))
        self.connected = True

    def send(self, message):
        if not self.connected:
            self.connect()

        message = str(message) + "\n"

        try:
            self.socket.send(message.encode())
        except socket.error:
            self.connected = False
            self.socket.close()
