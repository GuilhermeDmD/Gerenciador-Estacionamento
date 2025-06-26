from ConexaoBD import ConexaoBD
from Entidades.Veiculo import Veiculo
from Controle.ControleVeiculo import ControleVeiculo
from Controle.ControleCliente import ControleCliente

class ControlePagamento:
    def __init__(self):
        self.clienteControle = ControleCliente()
        self.veiculoControle = ControleVeiculo()

    def getPagamentoAvulso(self, veiculo:Veiculo):
        self.conexao = ConexaoBD()
        idVeiculo = self.veiculoControle.buscarIdVeiculo(veiculo)
        comandoSql = 'select pg.valor_total, vg.localizacao, h.entrada, h.saida from tb_pagamento pg inner join tb_veiculos v on pg.id_veiculo_fk = v.id_veiculo inner join tb_historico h on v.id_veiculo = h.id_veiculo_fk inner join tb_vagas vg on h.id_vaga_fk = vg.id_vaga where id_veiculo = %s limit 1'
        self.conexao.cursor.execute(comandoSql, (idVeiculo, ))
        infomacoesPag = self.conexao.cursor.fetchone()
        if infomacoesPag:
            return{
                "valor":infomacoesPag[0],
                "vaga":infomacoesPag[1],
                "entrada":infomacoesPag[2],
                "saida":infomacoesPag[3]
                
        }
        else:
            return None


    def realizarPagamentoAvulso(self, placa):
        self.conexao = ConexaoBD()
        comandoSql = 'call registrar_saida_avulso(%s)'
        self.conexao.cursor.execute(comandoSql, (placa, ))
        self.conexao.conexao.commit()
        self.conexao.fecharConexao()

    # 
    # def getPagamentoMensal(self, cliente:Cliente):
    #     self.conexao = ConexaoBD()
    #     idCliente = self.clienteControle.buscaIdCliente(cliente)
    #     comandoSql = 'select valor_total, id_cliente_fk from tb_pagamento where id_cliente_fk = %s'
    #     self.conexao.cursor.execute(comandoSql, (idCliente, ))
    #     informacoesPag = self.conexao.cursor.fetchone()
    #     self.conexao.fecharConexao()
    #     print(informacoesPag)