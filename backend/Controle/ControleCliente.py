from Entidades.Cliente import Cliente
from Controle.ControlePlanos import ControlePlanos
from Controle.ControleVagas import ControleVaga
from Entidades.Plano import Planos
from Entidades.Vagas import Vagas
from conexaoBD import conexaoBD

class controleCliente:
    def __init__(self):
        self.conexao = conexaoBD()
        self.plano = ControlePlanos()
        self.vaga = ControleVaga() 
        pass
        
    def buscaIdCliente(self, Cliente: Cliente):
        busca = f'select id_cliente from tb_cliente where cpf_cliente = "{Cliente.cpf}"'
        self.conexao.cursor.execute(busca)
        idCliente = self.conexao.cursor.fetchone()
        return idCliente
    
    def mostrarClientes(self):
        listaClientes = []
        comandoSql = 'select nome_cliente, cpf_cliente, telefone_cliente, email_cliente, id_plano_fk, id_vaga_fk from tb_clientes'
        self.conexao.cursor.execute(comandoSql)
        resultadoPesquisa = self.conexao.cursor.fetchall()
        for infoCliente in resultadoPesquisa:
            clienteDict = {"nome":infoCliente[0], "cpf":infoCliente[1], "telefone":infoCliente[2], "email":infoCliente[3], "plano":infoCliente[4], "vaga":infoCliente[5]}
            listaClientes.append(clienteDict)
        print(listaClientes)

    def addCliente(self, Cliente:Cliente, Vagas:Vagas, Planos:Planos):
        idVaga = self.vaga.buscarIdVaga(Vagas)
        idPlano = self.plano.buscarPlanoID(Planos)
        comandoSql = f'insert into tb_clientes(nome_cliente, cpf_cliente, telefone_cliente, email_cliente, id_plano_fk, id_vaga_fk) values ("{Cliente.nome}", "{Cliente.cpf}", "{Cliente.telefone}", "{Cliente.email}", {idPlano}, {idVaga})'
        self.conexao.cursor.execute(comandoSql)
        self.conexao.conexao.commit()

    #metodologia para deletar cliente
    

        

