from Entidades.Cliente import Cliente
from Controle.ControlePlanos import ControlePlanos
from Controle.ControleVagas import ControleVaga
from Entidades.Plano import Planos
from Entidades.Vagas import Vagas
from ConexaoBD import ConexaoBD

class ControleCliente:
    def __init__(self):
        self.conexao = ConexaoBD()
        self.plano = ControlePlanos()
        self.vaga = ControleVaga() 
      
    # TESTADO E FUNCIONANDO    
    def buscaIdCliente(self, cliente: Cliente):
        busca = f'select id_cliente from tb_clientes where cpf_cliente = "{cliente.cpf}"'
        self.conexao.cursor.execute(busca)
        idCliente = self.conexao.cursor.fetchone()
        return idCliente[0]
    
    #TESTADO E FUNCIONANDO
    def mostrarClientes(self):
        listaClientes = []
        comandoSql = 'select nome_cliente, cpf_cliente, telefone_cliente, email_cliente, id_plano_fk, id_vaga_fk from tb_clientes'
        self.conexao.cursor.execute(comandoSql)
        resultadoPesquisa = self.conexao.cursor.fetchall()
        for infoCliente in resultadoPesquisa:
            clienteDict = {"nome":infoCliente[0], "cpf":infoCliente[1], "telefone":infoCliente[2], "email":infoCliente[3], "plano":infoCliente[4], "vaga":infoCliente[5]}
            listaClientes.append(clienteDict)
        print(listaClientes)

    #alterar
    def addCliente(self, cliente:Cliente, vagas:Vagas, planos:Planos):
        idVaga = self.vaga.buscarIdVaga(vagas)
        idPlano = self.plano.buscarPlanoID(planos)
        print(idVaga)
        print(idPlano)
        comandoSql = f'insert into tb_clientes(nome_cliente, cpf_cliente, telefone_cliente, email_cliente, id_plano_fk, id_vaga_fk) values ("{cliente.nome}", "{cliente.cpf}", "{cliente.telefone}", "{cliente.email}", {idPlano}, {idVaga})'
        self.conexao.cursor.execute(comandoSql)
        self.conexao.conexao.commit()

    #metodologia para deletar cliente
    

        

