import mysql.connector
from mysql.connector import Error

class DataBaseMySql(object):
	def __init__(self):
		self.host = 'localhost'
		self.usuario = 'lucas'
		self.db = 'TesteCarga'
		self.password = 'Lucas12*'
		self.conexao = None
		self.cursor = None

	def connect(self):
		self.conexao = mysql.connector.connect(host=self.host, db=self.db, user=self.usuario, passwd=self.password)
		self.cursor = self.conexao.cursor()

	def disconnect(self):
		self.conexao.close()

	def select(self, fields, tables, where=None):
		query = "SELECT " + fields + " FROM " + tables

		if(where):
			query = query + " WHERE " + where

		print('query: ', query)
		self.cursor.execute(query)
		return self.cursor.fetchall() 

	def insert(self, archive):
		sql_insert_blob_query ="""INSERT INTO workLoad(dados) VALUES (%s);"""
		insert_blob_tuple = (archive,)
		self.cursor.execute(sql_insert_blob_query, insert_blob_tuple)
		self.conexao.commit()

"""
teste = DataBaseMySql()

bytes = b"0x410x420x43x02123aaa"
f = open("sample.txt", "wb")
f.write(bytes)
f.close()

teste.connect()
teste.insert(bytes)
teste.disconnect()
"""