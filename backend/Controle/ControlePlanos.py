from Entidades.Plano import Planos
from ConexaoBD import ConexaoBD 
class ControlePlanos:
    def __init__(self):
        self.conexao = ConexaoBD()

    def buscarPlanoID(self, planos: Planos):
        comandoSql = f'SELECT idPlano from tb_planos where nome_plano = "{planos.nomePlano}"'
        self.conexao.cursor.execute(comandoSql)
        idPlano = self.conexao.cursor.fetchone()
        return idPlano
    
    def buscarUmPlano(self, planos: Planos):
        id = self.buscarPlanoID(planos)
        comandoSql = f'SELECT * FROM tb_planos where idPlanos = {id}'
        self.conexao.cursor.execute(comandoSql)
        plano = self.conexao.cursor.fetchone
        print(plano)
    
    def mostrarPlanos(self):
        comandoSql = f'SELECT * FROM tb_planos'
        planos = []
        self.conexao.cursor.execute(comandoSql)
        resultadoPesquisa = self.conexao.cursor.fetchall()
        for plano in resultadoPesquisa:
            dictPlanos = {"id":plano[0], "nomePlano": plano[1], "descricao":plano[2], "valor":plano[3]}
            planos.append(dictPlanos)
        print(planos)

    def addPlano(self, planos: Planos):
        comandoSql = f'INSERT INTO tb_planos(nome_plano, descricao_plano, valor_plano) values("{planos.nomePlano}", "{planos.descricao}", {planos.valorPlano})'
        self.conexao.cursor.execute(comandoSql)
        self.conexao.conexao.commit()

    #Esse tá meio entranho, não tá passando confiança
    def editarPlano(self, coluna, valorEdicao):
        if isinstance(valorEdicao, str):
            edicaoStr = f'update tb_planos set "{coluna}" = "{valorEdicao}"'
            self.conexao.cursor.execute(edicaoStr)
            self.conexao.conexao.commit()
        else:
            edicaoFloat = f'update tb_planos set "{coluna}" = {valorEdicao}'
            self.conexao.cursor.execute(edicaoFloat)
            self.conexao.conexao.commit()

    def delPlano(self, planos:Planos):
        idPlano = self.buscarPlanoID(planos)
        comandoSql = f"delete from tb_planos where idPlano = {idPlano}"
        self.conexao.cursor.execute(comandoSql)
        # self.conexao.conexao.commit()

   
