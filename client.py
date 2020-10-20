import sys
import os
from connection import Conex
from threading import Thread
import time
import pickle
import json
from workload.archiv_generator import config_workload
from monitor.usage_loger import Loger

class Client():
    def __init__(self):
        try:
            Thread.__init__(self)
            self.conexao = Conex('localhost', 7000)
        except:
            print("Não foi possível conectar ao servidor, tente novamente mais tarde")
            exit(-1)

    def sendDataInBytes(self, info_experiments_path):
        file = open(info_experiments_path)
        info = json.load(file)
        file.close()

        self.conexao.startConnection()
        print("[client] start connection")

        print("[client] start test")
        for i in range(info['n_arc']):
            print("[client] send message")
            load = bytes((1024*1024)*info['size_in_MB'])
            time.sleep(1/info['arc_per_sec'])
            self.conexao.send(pickle.dumps(load))
            print("[client] message sended")

        print("[client] end test")