import psycopg2

class DataBasePostGres(object):
	def __init__(self):
		self.host = 'localhost'
		self.usuario = 'lucas'
		self.db = 'testecarga'
		self.password = 'lucas12'
		self.conexao = None
		self.cursor = None

	def connect(self):
		self.conexao = psycopg2.connect(host=self.host, database=self.db, user=self.usuario, password=self.password)
		self.cursor = self.conexao.cursor()

	def disconnect(self):
		self.conexao.close()

	def insert(self, archive):
		self.cursor.execute("""INSERT INTO workload(dado) VALUES(%s);""", (archive,))
		self.conexao.commit()

"""
teste = DataBasePostGres()
teste.connect()
bytes = b'teste2'
teste.insert(bytes)
teste.disconnect()
"""