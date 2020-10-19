import psycopg2

class DataBasePostGres(object):
	def __init__(self):
		self.host = '' #ip do host
		self.usuario = ''
		self.db = '' #nome do databse
		self.password = '' #senha do database
		self.conexao = None
		self.cursor = None

	def connect(self):
		self.conexao = psycopg2.connect(host=self.host, database=self.db, user=self.usuario, password=self.password)
		self.cursor = self.conexao.cursor()

	def disconnect(self):
		self.conexao.close()
teste = DataBasePostGres()

teste.connect()