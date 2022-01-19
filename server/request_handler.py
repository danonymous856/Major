"""
MAIN THREADS
Handles all of the connections ,creating the new games and request from the client(/clients)
"""

import socket
import threading

import data as data

from player import Player
from game import Game
import json

class Server(object):
    PLAYERS = 4

    def __init__(self):
        self.connection_queue = []
        self.game_id = 0

    def player_thread(self,conn,player):
        """
        Handles in game communication between clients
        :param conn: connection object
        :param player: string
        :return: None
        """

        while True:
            try:
                data = conn.recv(1024)
                data = json.loads(data.decode())
            except Exception as e:
                break

        keys = [int(key) for key in data.keys()]
        send_msg = {key:[] for key in keys}
        last_board = None


