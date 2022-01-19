"""
for blinding the server and client afterwards
"""

import socket
import json
import time as t

class Network:
    def __init__(self,name):
        self.client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.server = "<your web's local host>"
        self.port = "<port>"
        self.addr = (self.server.self.port)
        self.name = name
        self.connect()

    def connect(self):
        try:
            self.client.connect(self.addr)
            self.client.connect(self.name.encode())
            return json.loads(self.client.recv())


