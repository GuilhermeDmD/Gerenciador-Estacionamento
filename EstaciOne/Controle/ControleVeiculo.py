from Entidades.Veiculo import Veiculo
from Controle.ControleCliente import ControleCliente
from ConexaoBD import ConexaoBD

class ControleVeiculo:
    def __init__(self):
        self.controleCliente = ControleCliente()
    
    #TESTADO E FUNCIONANDO
    def buscarIdVeiculo(self, veiculo:Veiculo):
        self.conexao = ConexaoBD()
        comandoSql = f'select id_veiculo from tb_veiculos where placa_veiculo = "{veiculo.placa}"'
        self.conexao.cursor.execute(comandoSql)
        idVeiculo = self.conexao.cursor.fetchone()
        return idVeiculo[0]
    
    # TESTADO E FUNCIONANDO
    def mostrarVeiculo(self):
        self.conexao = ConexaoBD()
        listaVeiculos = []
        comandoSql = f'select placa_veiculo, modelo_veiculo, cor_veiculo, estado, id_cliente_fk from tb_veiculos'
        self.conexao.cursor.execute(comandoSql)
        resultadoPesquisa = self.conexao.cursor.fetchall()
        self.conexao.fecharConexao()
        for veiculoInfo in resultadoPesquisa:
            veiculosDict = {"placa":veiculoInfo[0], "modelo":veiculoInfo[1], "cor":veiculoInfo[2], "estado":veiculoInfo[3], "cliente":veiculoInfo[4]}
            listaVeiculos.append(veiculosDict)
        print(listaVeiculos)

    def addVeiculo(self, veiculo:Veiculo, cpf):
        self.conexao = ConexaoBD()
        idCliente = self.controleCliente.buscaIdCliente(cpf)
        print(idCliente)
        comandosql = f'insert into tb_veiculos(placa_veiculo, modelo_veiculo, cor_veiculo, estado, id_cliente_fk) values("{veiculo.placa}", "{veiculo.modelo}", "{veiculo.cor}", "Excluído", {idCliente})'
        self.conexao.cursor.execute(comandosql)
        self.conexao.conexao.commit()
        self.conexao.fecharConexao()