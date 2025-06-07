import mysql.connector

class ConexaoBD:
    def __init__(self):
        self.conexao = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            #adicione aqui a sua senha para acessar o Workbeach
            password = "fab08052005?",
            database = 'bd_estacionamento'
        )
        self.cursor = self.conexao.cursor()
        print("conexão com banco funcionando")

    def confirmarAlteracao(self):
        self.conexao.commit()
        
    def fecharConexao(self):
        self.cursor.close()
        self.conexao.close()
        
