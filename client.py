import sys
import os
from connection import Conex
from threading import Thread
import time
import pickle
from workload.archiv_generator import config_workload

class Client():
    def __init__(self):
        try:
            Thread.__init__(self)
            self.conexao = Conex('localhost', 7000)
        except:
            print("Não foi possível conectar ao servidor, tente novamente mais tarde")
            exit(-1)

    def sendDataInBytes(self):
        self.conexao.startConnection()
        bytes = b"Testing"
        self.conexao.sendMessage(pickle.dumps(bytes))


test = Client()
test.sendDataInBytes()