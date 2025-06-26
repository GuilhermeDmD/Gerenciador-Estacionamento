from Entidades.Veiculo import Veiculo
from Controle.ControleCliente import ControleCliente
from ConexaoBD import ConexaoBD

class ControleVeiculo:
    def __init__(self):
        self.controleCliente = ControleCliente()
    
    def buscarIdVeiculo(self, veiculo:Veiculo):
        self.conexao = ConexaoBD()
        comandoSql = 'select id_veiculo from tb_veiculos where placa_veiculo = %s'
        self.conexao.cursor.execute(comandoSql, (veiculo.placa, ))
        idVeiculo = self.conexao.cursor.fetchone()
        return idVeiculo[0]

    def addVeiculo(self, veiculo:Veiculo, cpf):
        self.conexao = ConexaoBD()
        idCliente = self.controleCliente.buscaIdCliente(cpf)
        comandosql = 'insert into tb_veiculos(placa_veiculo, modelo_veiculo, cor_veiculo, estado, id_cliente_fk) values(%s, %s, %s, "Não estacionado", %s)'
        self.conexao.cursor.execute(comandosql, (veiculo.placa, veiculo.modelo, veiculo.cor, idCliente))
        self.conexao.conexao.commit()
        self.conexao.fecharConexao()