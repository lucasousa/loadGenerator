import sys
import os
from connection import Conex
import threading
import time
import pickle
import json

class Client(threading.Thread):
    def __init__(self, size):
        threading.Thread.__init__(self)
        self.size_arc = size
        try:
            self.conexao = Conex('192.168.31.203', 7000)
        except:
            print("Não foi possível conectar ao servidor, tente novamente mais tarde")
            exit(-1)

    def run(self):
        self.conexao.startConnection()
        load = bytes((1024*1024)*self.size_arc)
        start_time = time.time()
        self.conexao.send(pickle.dumps(load))
        print(self.conexao.receive())
        print("[client] archive sended")
        end_time = time.time()
        print("RTT -", end_time-start_time)
        self.conexao.closeConnection()