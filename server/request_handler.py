"""
MAIN THREADS
Handles all of the connections ,creating the new games and request from the client(/clients)
"""

import socket
import threading
from player import Player
from game import Game
import json

class Server(object):
    PLAYERS = 4

