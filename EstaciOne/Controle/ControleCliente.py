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
    def buscaIdCliente(self, cpf):
        busca = f'select id_cliente from tb_clientes where cpf_cliente = "{cpf}"'
        self.conexao.cursor.execute(busca)
        idCliente = self.conexao.cursor.fetchone()
        return idCliente[0]
    
    # #TESTADO E FUNCIONANDO
    # def mostrarClientes(self):
    #     listaClientes = []
    #     comandoSql = 'select nome_cliente, cpf_cliente, telefone_cliente, email_cliente, id_plano_fk, id_vaga_fk from tb_clientes'
    #     self.conexao.cursor.execute(comandoSql)
    #     resultadoPesquisa = self.conexao.cursor.fetchall()
    #     for infoCliente in resultadoPesquisa:
    #         clienteDict = {"nome":infoCliente[0], "cpf":infoCliente[1], "telefone":infoCliente[2], "email":infoCliente[3], "plano":infoCliente[4], "vaga":infoCliente[5]}
    #         listaClientes.append(clienteDict)
    #     print(listaClientes)

    def buscarCliente(self, cpf):
        comandosql = f'select c.nome_cliente, c.cpf_cliente, c.telefone_cliente, c.email_cliente, p.nome_plano, v.localizacao from tb_clientes c inner join tb_planos p on c.id_plano_fk = p.id_plano inner join tb_vagas v on p.id_plano = v.id_plano_fk where c.cpf_cliente = "{cpf}" limit 1'
        self.conexao.cursor.execute(comandosql)
        resultado = self.conexao.cursor.fetchone()
        if resultado:
            return {
                "nome":resultado[0],
                "cpf": resultado[1],
                "telefone":resultado[2],
                "email":resultado[3],
                "plano":resultado[4],
                "vaga":resultado[5]
            }
        else:
            return None


    #alterar
    def addCliente(self, cliente:Cliente, vaga, plano):
        idVaga = self.vaga.buscarIdVaga(vaga)
        idPlano = self.plano.buscarPlanoID(plano)
        print(idVaga)
        print(idPlano)
        comandoSql = f'insert into tb_clientes(nome_cliente, cpf_cliente, telefone_cliente, email_cliente, id_plano_fk, id_vaga_fk) values ("{cliente.nome}", "{cliente.cpf}", "{cliente.telefone}", "{cliente.email}", {idPlano}, {idVaga})'
        self.conexao.cursor.execute(comandoSql)
        self.conexao.conexao.commit()
         # self.conexao.fecharConexao()


    #metodologia para deletar cliente
    

        

