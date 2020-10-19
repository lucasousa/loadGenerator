import mysql.connector
from mysql.connector import Error
import json

class DataBaseMySql(object):
	def __init__(self):
		file = open('databases/db_auth_mysql.json')
		auth = json.load(file)
		file.close()

		self.host = auth['host']
		self.usuario = auth['user']
		self.db = auth['db']
		self.password = auth['password']
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

		query = query + ';'

		print('query: ', query)
		self.cursor.execute(query)
		return self.cursor.fetchall() 

	def insert(self, archive):
		sql_insert_blob_query ="""INSERT INTO workload(dados) VALUES (%s);"""
		insert_blob_tuple = (archive,)
		self.cursor.execute(sql_insert_blob_query, insert_blob_tuple)
		self.conexao.commit()