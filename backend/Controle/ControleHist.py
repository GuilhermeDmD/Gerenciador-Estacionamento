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

    def buscaIdHistorico(self, veiculo: Veiculo):
        idVeiculo = self.controleVeiculo.buscarIdVeiculo(veiculo)
        comandoSql = f'select id_historico from tb_historico where id_veiculo_fk = {idVeiculo}'
        self.conexao.cursor.execute(comandoSql)
        idHistorico = self.conexao.cursor.fetchone()
        return idHistorico

    def addInfoSaida(self, veiculo:Veiculo):
        idHistorico = self.buscaIdHistorico(veiculo)
        horaFormatada = self.horaAtual.strftime("%H:%M:%S")
        comandoSql = f'update tb_historico set hora_saida = {horaFormatada}, data_saida = {self.dataAtual} where id_historico = {idHistorico}'
        self.conexao.cursor.execute(comandoSql)
        self.conexao.conexao.commit()

    