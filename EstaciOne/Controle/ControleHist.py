from ConexaoBD import ConexaoBD
from Controle.ControleVeiculo import ControleVeiculo
from Controle.ControleVagas import ControleVaga
from Entidades.Veiculo import Veiculo
from datetime import datetime

class ControleHist:
    def __init__(self):
        self.controleVeiculo = ControleVeiculo()
        self.controleVaga = ControleVaga()
        self.dataHoraAtual = datetime.now()
       

    def buscaIdHistorico(self, veiculo: Veiculo):
        self.conexao = ConexaoBD()
        idVeiculo = self.controleVeiculo.buscarIdVeiculo(veiculo)
        comandoSql = 'select id_historico from tb_historico where id_veiculo_fk = %s order by id_historico desc limit 1'
        self.conexao.cursor.execute(comandoSql, (idVeiculo, ))
        idHistorico = self.conexao.cursor.fetchone()
        return idHistorico[0]

    def addInfoSaida(self, veiculo:Veiculo):
        self.conexao = ConexaoBD()
        idHistorico = self.buscaIdHistorico(veiculo)
        dataHoraAtual = self.dataHoraAtual.strftime('%Y-%m-%d %H:%M:%S')
        comandoSql = 'update tb_historico set Saida = %s where id_historico = %s'
        self.conexao.cursor.execute(comandoSql, (dataHoraAtual, idHistorico))
        self.conexao.conexao.commit()
        self.conexao.fecharConexao()

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

    


    