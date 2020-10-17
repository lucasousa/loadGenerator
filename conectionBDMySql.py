#conector do python com o mysql (pymysql)
import pymysql


class DataBase(object):
    """   
   Esta classe tem por objetivo fazer a conexão com banco de dados e realizar operaçãos (CRUD) no mesmo 
    ...

    Atributos
    ----------
    host : str
        representa o host a qual esta rodando o banco de dados, nesse caso na máquina local
    usuario : str
        define o usuário a qual terá acesso para manipular o banco de dados
    db : str
        banco de dados a qual será realizadas as operações
    password : str
        senha de acesso ao banco de dados
    conexao : objeto
        Objeto pelo qual será responsável por estabelecer a conexão, salvar arquivos e fechar banco de dados
    cursor : objeto
        objeto que será responsável por executar operações no banco, tais como: execute(inserir dados em uma tabela)
    """
    def __init__(self):
        self.host = 'localhost'
        self.usuario = 'lucas'
        self.db = 'TesteCarga'
        self.password = 'Lucas12*'
        self.conexao = None
        self.cursor = None)

    def connect(self):
        """
        Este é o método onde é iniciada uma conexão com o banco de dados
        ...

        Parâmetros
        ---------
        self.conexao: objeto
            definido como objeto de acesso ao banco de dados
        self.cursor: objeto
            definido como objeto para fazer manipulações com o banco de dados, tais como: salvar e executar uma operação
        """
        self.conexao = pymysql.connect(host=self.host, db=self.db, user=self.usuario, passwd=self.password)
        self.cursor = self.conexao.cursor(pymysql.cursors.DictCursor) # Os resultados vem em dicionario

    def disconnect(self):
        """
        método para desfazer a conexão com o banco de dados, ou seja, fechar o mesmo
        """
        self.conexao.close()
