import socket


class Client:
    """Docstring for Client."""

    def __init__(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect(("127.0.0.1", 8000))

        self.client_socket.close()

    def sendMessage(self, msg: str):
        self.client_socket.send(msg.encode("utf-8"))
