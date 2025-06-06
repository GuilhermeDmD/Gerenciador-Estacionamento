from Entidades.Cliente import Cliente
from conexaoBD import conexaoBD

class controleCliente:
    def __init__(self):
        self.conexao = conexaoBD()
        pass
        
    def buscaIdCliente(self, Cliente: Cliente):
        busca = f'select id_cliente from tb_cliente where cpf_cliente = "{Cliente.cpf}"'
        self.conexao.cursor.execute(busca)
        idCliente = self.conexao.cursor.fetchone()
        return idCliente
    

        

