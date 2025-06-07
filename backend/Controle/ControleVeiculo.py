from Entidades.Veiculo import Veiculo
from ConexaoBD import ConexaoBD

class ControleVeiculo:
    def __init__(self):
        self.conexao = ConexaoBD()
    
    def buscarIdVeiculo(self, veiculo:Veiculo):
        comandoSql = f'select id_veiculo from tb_veiculos where placa_veiculo = "{veiculo.placa}"'
        self.conexao.cursor.execute(comandoSql)
        idVeiculo = self.conexao.cursor.fetchone()
        return idVeiculo
    
    def mostrarVeiculo(self):
        listaVeiculos = []
        comandoSql = f'select placa_veiculo, modelo_veiculo, cor_veiculo, estado, id_cliente__fk from tb_veiculos'
        self.conexao.cursor.execute(comandoSql)
        resultadoPesquisa = self.conexao.cursor.fetchall()
        for veiculoInfo in resultadoPesquisa:
            veiculosDict = {"placa":veiculoInfo[0], "modelo":veiculoInfo[1], "cor":veiculoInfo[2], "estado":veiculoInfo[3], "cliente":veiculoInfo[4]}
            listaVeiculos.append(veiculosDict)
        print(listaVeiculos)