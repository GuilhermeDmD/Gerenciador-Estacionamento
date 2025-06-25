from ConexaoBD import ConexaoBD
from Controle.ControleVeiculo import ControleVeiculo
from Controle.ControleVagas import ControleVaga
from Entidades.Veiculo import Veiculo
from datetime import datetime, date

class ControleHist:
    def __init__(self):
        self.controleVeiculo = ControleVeiculo()
        self.controleVaga = ControleVaga()
        self.dataHoraAtual = datetime.now()
       

    #TESTADO E FUNCIONANDO
    def buscaIdHistorico(self, veiculo: Veiculo):
        self.conexao = ConexaoBD()
        idVeiculo = self.controleVeiculo.buscarIdVeiculo(veiculo)
        comandoSql = f'select id_historico from tb_historico where id_veiculo_fk = {idVeiculo} order by id_historico desc limit 1'
        self.conexao.cursor.execute(comandoSql)
        idHistorico = self.conexao.cursor.fetchone()
        return idHistorico[0]

    # #TESTADO E FUNCIONANDO provavelmente essa não vai usar
    # def addInfoSaida(self, veiculo:Veiculo):
    #     self.conexao = ConexaoBD()
    #     idHistorico = self.buscaIdHistorico(veiculo)
    #     horaFormatada = self.horaAtual.strftime("%H:%M:%S")
    #     dataFormatada = self.dataAtual.strftime("%Y-%m-%d")
    #     print(horaFormatada)
    #     print(self.dataAtual)
    #     comandoSql = f'update tb_historico set hora_saida = "{horaFormatada}", data_saida = "{dataFormatada}" where id_historico = {idHistorico}'
    #     self.conexao.cursor.execute(comandoSql)
    #     self.conexao.conexao.commit()
    #     self.conexao.fecharConexao()

    def addHistorico(self, veiculo: Veiculo, vaga):
        self.conexao = ConexaoBD()
        dataHoraAtual = self.dataHoraAtual.strftime('%Y-%m-%d %H:%M:%S')
        idVeiculo = self.controleVeiculo.buscarIdVeiculo(veiculo)
        idVaga = self.controleVaga.buscarIdVaga(vaga)
        comandosql = 'insert into tb_historico (entrada, id_veiculo_fk, id_vaga_fk) values (%s, %s, %s)'
        self.conexao.cursor.execute(comandosql, (dataHoraAtual, idVeiculo, idVaga))
        self.conexao.conexao.commit()
        self.conexao.fecharConexao()

    def getHistorico(self, placa):
        self.conexao = ConexaoBD()
        comandosql = 'select get_historico(%s)'
        self.conexao.cursor.execute(comandosql, (placa, ))
        historico = self.conexao.cursor.fetchone()
        if historico:
            return{
                "historico":historico[0]
            }
        else:
            return "Dados não encontrados"


    


    