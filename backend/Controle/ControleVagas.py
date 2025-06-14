from ConexaoBD import ConexaoBD
from Entidades.Vagas import Vagas
class ControleVaga:
    def __init__(self):
        self.conexao = ConexaoBD()

    #FUNCIONANDO TESTADO
    def buscarIdVaga(self, vagas: Vagas):
        comando = f'select id_vaga from tb_vagas where localizacao = "{vagas.localizacao}"'
        self.conexao.cursor.execute(comando)
        idVaga = self.conexao.cursor.fetchone()
        return idVaga[0]
    
    #TESTADO E FUNCIONANDO
    def buscarVaga(self, vagas: Vagas):
        vagaDados = []
        vagaId = self.buscarIdVaga(vagas)
        comandoSql = f'select localizacao, disponibilidade, tipo from tb_vagas where id_vaga = {vagaId}'
        self.conexao.cursor.execute(comandoSql)
        vagaPesquisada = self.conexao.cursor.fetchall()
        for vaga in vagaPesquisada:
            vagaDict = {"localizacao":vaga[0], "disponibilidade":vaga[1], "tipo":vaga[2]}
            vagaDados.append(vagaDict)
        print(vagaDados)

    #TESTADO E FUNCIONANDO
    def mostrarVagas(self):
        vagasDados = []
        comandosql = 'select localizacao, disponibilidade, tipo from tb_vagas'
        self.conexao.cursor.execute(comandosql)
        resultadoPesquisa = self.conexao.cursor.fetchall()
        for vagaItem in resultadoPesquisa:
            vagasDict = {"localizacao":vagaItem[0], "disponibilidade":vagaItem[1], "tipo":vagaItem[2]}
            vagasDados.append(vagasDict)
        print(vagasDados)

    #TESTADO E FUNCIONANDO
    def alterarTipoVaga(self, Vagas: Vagas, novoTipo):
        idVaga = self.buscarIdVaga(Vagas)
        comandoSql = f'update tb_vagas set tipo = "{novoTipo}" where id_vaga = {idVaga}'
        self.conexao.cursor.execute(comandoSql)
        self.conexao.conexao.commit()


        

