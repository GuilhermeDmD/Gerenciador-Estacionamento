from ConexaoBD import ConexaoBD
from Controle.ControleVeiculo import ControleVeiculo
from Entidades.Veiculo import Veiculo
from datetime import datetime, date

class ControleHist:
    def __init__(self):
        self.conexao = ConexaoBD()
        self.controleVeiculo = ControleVeiculo()
        self.horaAtual = datetime.now()
        self.dataAtual = date.today()

    #TESTADO E FUNCIONANDO
    def buscaIdHistorico(self, veiculo: Veiculo):
        idVeiculo = self.controleVeiculo.buscarIdVeiculo(veiculo)
        comandoSql = f'select id_historico from tb_historico where id_veiculo_fk = {idVeiculo}'
        self.conexao.cursor.execute(comandoSql)
        idHistorico = self.conexao.cursor.fetchone()
        return idHistorico[0]

    #TESTADO E FUNCIONANDO
    def addInfoSaida(self, veiculo:Veiculo):
        idHistorico = self.buscaIdHistorico(veiculo)
        horaFormatada = self.horaAtual.strftime("%H:%M:%S")
        dataFormatada = self.dataAtual.strftime("%Y-%m-%d")
        print(horaFormatada)
        print(self.dataAtual)
        comandoSql = f'update tb_historico set hora_saida = "{horaFormatada}", data_saida = "{dataFormatada}" where id_historico = {idHistorico}'
        self.conexao.cursor.execute(comandoSql)
        self.conexao.conexao.commit()

    