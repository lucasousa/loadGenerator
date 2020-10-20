import threading
import socket
from databases.conectionBDMySql import DataBaseMySql
import pickle
import os

class ClientThread(threading.Thread):
    def __init__(self,clientAddress,clientsocket):
        threading.Thread.__init__(self)
        self.csocket = clientsocket
        print ("Nova conexao: ", clientAddress)
        self.db = DataBaseMySql()
        

    def run(self):
        ack = None
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

        print(type(data_received))
        self.insertInBD(data_received)
    
    def insertInBD(self, data):
        self.db.connect()
        self.db.insert(data)
        self.db.disconnect()

if __name__ == '__main__':
    print("Iniciando servidor...")
    addr = ("", 7000)
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(addr)
    print("Servidor iniciado!")
    print("Aguardando nova conexao..")
    os.system('nohup ./memoryLog.sh &')
    while True:
        server.listen(10)
        clientsock, clientAddress = server.accept()
        newthread = ClientThread(clientAddress, clientsock)
        newthread.start()