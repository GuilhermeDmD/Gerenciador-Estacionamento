from Entidades.CategoriaVaga import CategoriaVaga
from ConexaoBD import ConexaoBD
    
class ControleCategoia:
    def __init__(self):
       pass

    def buscarIdCategoria(self, descricaoPesq):
        self.conexao = ConexaoBD()
        comandoSql = f'select id_categoria from tb_categoria where descricao like "{descricaoPesq}%" limit 1'
        self.conexao.cursor.execute(comandoSql)
        idCategoria = self.conexao.cursor.fetchone
        return idCategoria
    
    def reajustarValor(self, descricaoCat, novoValor):
        self.conexao = ConexaoBD()
        idCategoria = self.buscarIdCategoria(descricaoCat)
        comandoSql = 'update tb_categoria set valor = %s where id_categoria = %s'
        self.conexao.cursor.execute(comandoSql, (novoValor, idCategoria))
        self.conexao.conexao.commit()
        self.conexao.fecharConexao()
        