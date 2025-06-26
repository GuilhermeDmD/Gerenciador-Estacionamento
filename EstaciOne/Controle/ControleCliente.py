from Entidades.Cliente import Cliente
from Controle.ControlePlanos import ControlePlanos
from Controle.ControleVagas import ControleVaga
from ConexaoBD import ConexaoBD

class ControleCliente:
    def __init__(self):
        self.plano = ControlePlanos()
        self.vaga = ControleVaga() 
      
    def buscaIdCliente(self, cpf):
        self.conexao = ConexaoBD()
        busca = 'select id_cliente from tb_clientes where cpf_cliente = %s'
        self.conexao.cursor.execute(busca, (cpf, ))
        idCliente = self.conexao.cursor.fetchone()
        return idCliente[0]

    def buscarCliente(self, cpf):
        self.conexao = ConexaoBD()
        comandosql = 'select c.nome_cliente, c.cpf_cliente, c.telefone_cliente, c.email_cliente, p.nome_plano, v.localizacao, vei.modelo_veiculo, vei.placa_veiculo, vei.cor_veiculo from tb_veiculos vei inner join tb_clientes c on vei.id_cliente_fk = c.id_cliente inner join tb_planos p  on c.id_plano_fk = p.id_plano  inner join tb_vagas v  on p.id_plano = v.id_plano_fk  where c.cpf_cliente = %s limit 1'
        self.conexao.cursor.execute(comandosql, (cpf, ))
        resultado = self.conexao.cursor.fetchone()
        self.conexao.fecharConexao()
        if resultado:
            return {
                "nome":resultado[0],
                "cpf": resultado[1],
                "telefone":resultado[2],
                "email":resultado[3],
                "plano":resultado[4],
                "vaga":resultado[5],
                "modelo":resultado[6],
                "placa":resultado[7],
                "cor":resultado[8]
            }
        else:
            return None

    def addCliente(self, cliente:Cliente, vaga, plano):
        self.conexao = ConexaoBD()
        idVaga = self.vaga.buscarIdVaga(vaga)
        idPlano = self.plano.buscarPlanoID(plano)
        comandoSql = 'insert into tb_clientes(nome_cliente, cpf_cliente, telefone_cliente, email_cliente, id_plano_fk, id_vaga_fk) values (%s, %s, %s, %s, %s, %s)'
        self.conexao.cursor.execute(comandoSql, (cliente.nome, cliente.cpf, cliente.telefone, cliente.email, idPlano, idVaga))
        self.conexao.conexao.commit()
        self.conexao.fecharConexao()
    

        

