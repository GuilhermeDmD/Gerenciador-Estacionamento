from ConexaoBD import ConexaoBD
class ControleVaga:
    def __init__(self):
        pass

    def buscarIdVaga(self, localizacao):
        self.conexao = ConexaoBD()
        comando = 'select id_vaga from tb_vagas where localizacao = %s'
        self.conexao.cursor.execute(comando, (localizacao, ))
        idVaga = self.conexao.cursor.fetchone()
        return idVaga[0] if idVaga else None 

    def mostrarVagasAvulsas(self):
        self.conexao = ConexaoBD()
        comandosql = 'select localizacao, disponibilidade from tb_vagas where tipo = "Avulso" and disponibilidade = "Disponivel"'
        self.conexao.cursor.execute(comandosql)
        resultadoPesquisa = self.conexao.cursor.fetchall()
        self.conexao.fecharConexao()
        return [vagas[0] for vagas in resultadoPesquisa]

    def mostrarVagasMensais(self):
        self.conexao = ConexaoBD()
        comandosql = 'select localizacao from tb_vagas where tipo = "Mensal" and disponibilidade = "Disponível"'
        self.conexao.cursor.execute(comandosql)
        resultadoPesquisa = self.conexao.cursor.fetchall()
        self.conexao.fecharConexao()
        return[vagaItem[0] for vagaItem in resultadoPesquisa]

    def mudaEstadoVaga(self, localizacao):
        self.conexao = ConexaoBD()
        idVaga = self.buscarIdVaga(localizacao)
        comandoSql = 'select disponibilidade from tb_vagas where id_vaga = %s'
        self.conexao.cursor.execute(comandoSql, (idVaga, ))
        disponibilidade = self.conexao.cursor.fetchone()
        if disponibilidade[0] == "Disponivel":
            comandoSql = 'update tb_vagas set disponibilidade = "Ocupado" where id_vaga = %s'
            self.conexao.cursor.execute(comandoSql, (idVaga, ))
            self.conexao.conexao.commit()
            self.conexao.fecharConexao()
        elif disponibilidade[0] == "Ocupado":
            comandoSql = 'update tb_vagas set disponibilidade = "Disponivel" where id_vaga = %s'
            self.conexao.cursor.execute(comandoSql, (idVaga, ))
            self.conexao.conexao.commit()
            self.conexao.fecharConexao()


    def mostrarVagasOcupadas(self):
        self.conexao = ConexaoBD()
        comandosql = 'select v.localizacao from tb_veiculos vei inner join tb_historico h on vei.id_veiculo = h.id_veiculo_fk inner join tb_vagas v on h.id_vaga_fk = v.id_vaga where v.disponibilidade = "Ocupado" and vei.estado = "Estacionado"'
        self.conexao.cursor.execute(comandosql)
        resultado = self.conexao.cursor.fetchall()
        self.conexao.fecharConexao()
        vagas = []
        for vaga in resultado:
            vagasDict = {"localizacao":vaga[0]}
            vagas.append(vagasDict)
        return vagas

    


        

