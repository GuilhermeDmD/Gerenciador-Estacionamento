from ConexaoBD import ConexaoBD
from Entidades.Veiculo import Veiculo
from Controle.ControleVeiculo import ControleVeiculo
from Entidades.Cliente import Cliente
from Controle.ControleCliente import ControleCliente

class ControlePagamento:
    def __init__(self):
        self.clienteControle = ControleCliente()
        self.veiculoControle = ControleVeiculo()

    #Testado e funcionando
    def pagamentoAvulso(self, veiculo:Veiculo):
        self.conexao = ConexaoBD()
        idVeiculo = self.veiculoControle.buscarIdVeiculo(veiculo)
        comandoSql = 'select valor_total, id_veiculo_fk from tb_pagamento where id_veiculo_fk = %s'
        self.conexao.cursor.execute(comandoSql, (idVeiculo, ))
        infomacoesPag = self.conexao.cursor.fetchone()
        self.conexao.fecharConexao()

          # self.conexao.fecharConexao()
        print(infomacoesPag)

    #testado e funcionando
    def pagamentoMensal(self, cliente:Cliente):
        self.conexao = ConexaoBD()
        idCliente = self.clienteControle.buscaIdCliente(cliente)
        comandoSql = 'select valor_total, id_cliente_fk from tb_pagamento where id_cliente_fk = %s'
        self.conexao.cursor.execute(comandoSql, (idCliente, ))
        informacoesPag = self.conexao.cursor.fetchone()
        self.conexao.fecharConexao()

         # self.conexao.fecharConexao()
        print(informacoesPag)