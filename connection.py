import socket 
import time
import pickle

class Conex():
	def __init__(self, ip, port):
		self.host = ip
		self.port = port
		
	def startConnection(self):
		self.address=((self.host,self.port))
		self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
		self.client_socket.connect(self.address)

	def send(self,content):	
		self.client_socket.sendall(content) 

	def closeConnection(self):
		self.client_socket.close()