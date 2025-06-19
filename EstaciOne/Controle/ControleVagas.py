from ConexaoBD import ConexaoBD
from Entidades.Vagas import Vagas
class ControleVaga:
    def __init__(self):
        self.conexao = ConexaoBD()

    #FUNCIONANDO TESTADO
    def buscarIdVaga(self, localizacao):
        comando = f'select id_vaga from tb_vagas where localizacao = "{localizacao}"'
        self.conexao.cursor.execute(comando)
        idVaga = self.conexao.cursor.fetchone()
        return idVaga[0]
    
    #TESTADO E FUNCIONANDO
    # def buscarVaga(self, vagas: Vagas):
    #     vagaDados = []
    #     vagaId = self.buscarIdVaga(vagas)
    #     comandoSql = f'select localizacao, disponibilidade, tipo from tb_vagas where id_vaga = {vagaId}'
    #     self.conexao.cursor.execute(comandoSql)
    #     vagaPesquisada = self.conexao.cursor.fetchall()
    #     for vaga in vagaPesquisada:
    #         vagaDict = {"localizacao":vaga[0], "disponibilidade":vaga[1], "tipo":vaga[2]}
    #         vagaDados.append(vagaDict)
    #     print(vagaDados)

    #TESTADO E FUNCIONANDO
    # def mostrarVagas(self):
    #     vagasDados = []
    #     comandosql = 'select localizacao, disponibilidade, tipo from tb_vagas'
    #     self.conexao.cursor.execute(comandosql)
    #     resultadoPesquisa = self.conexao.cursor.fetchall()
    #     for vagaItem in resultadoPesquisa:
    #         vagasDict = {"localizacao":vagaItem[0], "disponibilidade":vagaItem[1], "tipo":vagaItem[2]}
    #         vagasDados.append(vagasDict)
    #     print(vagasDados)

    def mostrarVagasAvulsas(self):
        comandosql = 'select localizacao, disponibilidade from tb_vagas where tipo = "Avulso" and disponibilidade = "Disponivel"'
        self.conexao.cursor.execute(comandosql)
        resultadoPesquisa = self.conexao.cursor.fetchall()
        return [vagas[0] for vagas in resultadoPesquisa]

    def mostrarVagasMensais(self):
        comandosql = 'select localizacao from tb_vagas where tipo = "Mensal" and disponibilidade = "Disponível"'
        self.conexao.cursor.execute(comandosql)
        resultadoPesquisa = self.conexao.cursor.fetchall()
        return[vagaItem[0] for vagaItem in resultadoPesquisa]

    # #TESTADO E FUNCIONANDO
    # def alterarTipoVaga(self, Vagas: Vagas, novoTipo):
    #     idVaga = self.buscarIdVaga(Vagas)
    #     comandoSql = f'update tb_vagas set tipo = "{novoTipo}" where id_vaga = {idVaga}'
    #     self.conexao.cursor.execute(comandoSql)
    #     self.conexao.conexao.commit()

    def ocuparVaga(self, localizacao):
        idVaga = self.buscarIdVaga(localizacao)
        comandoSql = f'update tb_vagas set disponibilidade = "Ocupado" where id_vaga = {idVaga}'
        self.conexao.cursor.execute(comandoSql)
        self.conexao.conexao.commit()

    


        

