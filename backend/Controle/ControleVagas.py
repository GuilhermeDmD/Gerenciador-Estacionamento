from ConexaoBD import ConexaoBD
from Entidades.Vagas import Vagas
class ControleVaga:
    def __init__(self):
        self.conexao = ConexaoBD()

    #não testado
    def buscarIdVaga(self, vagas: Vagas):
        comando = f'select id_vaga from tb_vagas where localizao = "{vagas.localizacao}"'
        self.conexao.cursor.execute(comando)
        idVaga = self.conexao.cursor.fetchone()
        return idVaga
    
    #não testado 
    def buscarVaga(self, vagas: Vagas):
        vagaDados = []
        vagaId = self.buscarIdVaga(vagas)
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


        

