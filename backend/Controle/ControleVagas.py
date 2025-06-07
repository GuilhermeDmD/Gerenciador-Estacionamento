from conexaoBD import conexaoBD
from Entidades.Vagas import Vagas
class ControleVaga:
    def __init__(self):
        self.conexao = conexaoBD()

    #não testado
    def buscarIdVaga(self, Vagas: Vagas):
        comando = f'select id_vaga from tb_vagas where localizao = "{Vagas.localizacao}"'
        self.conexao.cursor.execute(comando)
        idVaga = self.conexao.cursor.fetchone()
        return idVaga
    
    #não testado 
    def buscarVaga(self, Vagas: Vagas):
        vagaDados = []
        vagaId = self.buscarIdVaga(Vagas)
        comandoSql = f'select localizacao, disponibilidade, tipo from tb_vagas where idVaga = {vagaId}'
        self.conexao.cursor.execute(comandoSql)
        vagaPesquisada = self.conexao.cursor.fetchall()
        for vaga in vagaPesquisada:
            vagaDict = {"localizacao":vaga[0], "disponibilidade":vaga[1], "tipo":vaga[2]}
            vagaDados.append(vagaDict)

    #não testado
    def mostrarVagas(self):
        vagasDados = []
        comandosql = 'select localizao, disponibilidade, tipo from tb_vagas'
        self.conexao.cursor.execute(comandosql)
        resultadoPesquisa = self.conexao.cursor.fetchall()
        for vagaItem in resultadoPesquisa:
            vagasDict = {"localizao":vagaItem[0], "disponibilidade":vagaItem[1], "tipo":vagaItem[2]}
            vagasDados.append(vagasDict)
        print(vagasDados)

    #não testado
    def alterarTipoVaga(self, Vagas: Vagas, novoTipo):
        idVaga = self.buscarIdVaga(Vagas)
        comandoSql = f'update tb_vagas set tipo = "{novoTipo}" where idVaga = {idVaga}'
        self.conexao.cursor.execute(comandoSql)
        self.conexao.conexao.commit()

        

