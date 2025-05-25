import mysql.connector

class conexaoBD:
    def __init__(self):
        self.conexao = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            #adicione aqui a sua senha para acessar o Workbeach
            password = "digite sua senha aqui",
            database = 'bd_estacionamento'
        )
        self.cursor = self.conexao.cursor()
        print("conexão com banco funcionando")

    def confirmarAlteracao(self):
        self.conexao.commit()
        

    def fecharConexao(self):
        self.cursor.close()
        self.conexao.close()
        
