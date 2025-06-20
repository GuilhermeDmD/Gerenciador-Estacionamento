from Entidades.Plano import Planos
from ConexaoBD import ConexaoBD 
class ControlePlanos:
    def __init__(self):
            pass

    #FUNCIONANDO TESTADO
    def buscarPlanoID(self, plano):
        self.conexao = ConexaoBD()
        comandoSql = f'SELECT id_plano from tb_planos where nome_plano = "{plano}"'
        self.conexao.cursor.execute(comandoSql)
        idPlano = self.conexao.cursor.fetchone()
        return idPlano[0]
    
    #TESTADO E FUNCIONANDO
    def buscarUmPlano(self, planos: Planos):
        self.conexao = ConexaoBD()
        id = self.buscarPlanoID(planos)
        comandoSql = f'SELECT * FROM tb_planos where id_plano = {id}'
        self.conexao.cursor.execute(comandoSql)
        plano = self.conexao.cursor.fetchone()
        self.conexao.fecharConexao()
        print(plano)
    
    # TESTADO E FUNCIONANDO
    def mostrarPlanos(self):
        self.conexao = ConexaoBD()
        comandoSql = f'SELECT tb_planos.nome_plano FROM tb_planos inner join tb_vagas on tb_planos.id_plano = tb_vagas.id_plano_fk where tb_vagas.disponibilidade = "Disponivel";'
        self.conexao.cursor.execute(comandoSql)
        resultadoPesquisa = self.conexao.cursor.fetchall()
        self.conexao.fecharConexao()
        return [planos[0] for planos in resultadoPesquisa]
       

    #TESTADO E FUNCIONANDO
    def addPlano(self, planos: Planos):
        self.conexao = ConexaoBD()
        comandoSql = f'INSERT INTO tb_planos(nome_plano, descricao_plano, valor_plano) values("{planos.nomePlano}", "{planos.descricao}", {planos.valorPlano})'
        self.conexao.cursor.execute(comandoSql)
        self.conexao.conexao.commit()
        self.conexao.fecharConexao()

    #TESTADO E FUNCIONANDO
    def editarPlano(self, coluna, valorEdicao, planos: Planos):
        self.conexao = ConexaoBD()
        idPlano = self.buscarPlanoID(planos)
        if isinstance(valorEdicao, str):
            edicaoStr = f'update tb_planos set {coluna} = "{valorEdicao}" where id_plano = {idPlano}'
            self.conexao.cursor.execute(edicaoStr)
            self.conexao.conexao.commit()
            self.conexao.fecharConexao()
        else:
            edicaoFloat = f'update tb_planos set {coluna} = {valorEdicao} where id_plano = {idPlano}'
            self.conexao.cursor.execute(edicaoFloat)
            self.conexao.conexao.commit()
            self.conexao.fecharConexao()

    #TESTADO E FUNCIONANDO
    def delPlano(self, planos:Planos):
        self.conexao = ConexaoBD()
        idPlano = self.buscarPlanoID(planos)
        comandoSql = f"delete from tb_planos where id_plano = {idPlano}"
        self.conexao.cursor.execute(comandoSql)
        self.conexao.conexao.commit()
        self.conexao.fecharConexao()

   
