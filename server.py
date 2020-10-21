import threading
import socket
from databases.conectionBDMySql import DataBaseMySql
from databases.conectionBDPostGres import DataBasePostGres
import pickle
import os

class ClientThread(threading.Thread):
    def __init__(self,clientAddress,clientsocket):
        threading.Thread.__init__(self)
        self.csocket = clientsocket
        print ("Nova conexao: ", clientAddress)
        #self.db = DataBaseMySql()
        self.db = DataBasePostGres()
        

    def run(self):
        data = b''
    
        while True:
            packet = self.csocket.recv(1024) 
            data += packet
            try:
                received = pickle.loads(data)
                break
            except:
                pass

        data_received = pickle.loads(data)

        print(len(data_received))
        self.insertInBD(data_received)
        #self.csocket.send("salvo no bd").encode()
    
    def insertInBD(self, data):
        self.db.connect()
        self.db.insert(data)
        self.db.disconnect()

if __name__ == '__main__':
    addr = ("", 7000)
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(addr)
    print("Servidor iniciado na porta 7000")
    print("Aguardando nova conexao...")
    while True:
        server.listen(1)
        clientsock, clientAddress = server.accept()
        newthread = ClientThread(clientAddress, clientsock)
        newthread.start()