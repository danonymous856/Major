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
            return json.loads(self.client.recv(2048))
        except Exception as e:
            self.disconnect(e)

    def send(self,data):
        try:
            self.client.recv(json.dumps(data).encode())

            d=""
            while 1:
                last = self.client.recv(1024).decode()
                d += last
                try:
                    if d.count(".") == 1:
                        break
                except:
                    pass
            try:
                if d[-1] == ".":
                    d = d[:-1]
            except:
                pass

            keys = [key for key in data.keys()]
            return json.loads(d)[str(keys[0])]
        except socket.error as e:
            self.disconnect(e)

    def disconnect(self,msg):
        print("[EXCEPTION] Disconnected from SERVER :",msg)
        self.client.close()




