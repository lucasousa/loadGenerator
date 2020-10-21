import sys
import os
from connection import Conex
import threading
import time
import pickle
import json
from monitor.usage_loger import Loger

class Client(threading.Thread):
    def __init__(self, size):
        threading.Thread.__init__(self)
        self.size_arc = size
        try:
            self.conexao = Conex('localhost', 7000)
        except:
            print("Não foi possível conectar ao servidor, tente novamente mais tarde")
            exit(-1)

    def run(self):
        self.conexao.startConnection()
        load = bytes((1024*1024)*self.size_arc)
        self.conexao.send(pickle.dumps(load))
        print("[client] archive sended")
        self.conexao.closeConnection()