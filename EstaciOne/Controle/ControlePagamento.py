from ConexaoBD import ConexaoBD
from Entidades.Veiculo import Veiculo
from Controle.ControleVeiculo import ControleVeiculo
from Entidades.Cliente import Cliente
from Controle.ControleCliente import ControleCliente

class ControlePagamento:
    def __init__(self):
        self.conexao = ConexaoBD()
        self.clienteControle = ControleCliente()
        self.veiculoControle = ControleVeiculo()

    #Testado e funcionando
    def pagamentoAvulso(self, veiculo:Veiculo):
        idVeiculo = self.veiculoControle.buscarIdVeiculo(veiculo)
        comandoSql = f'select valor_total, id_veiculo_fk from tb_pagamento where id_veiculo_fk = {idVeiculo}'
        self.conexao.cursor.execute(comandoSql)
        infomacoesPag = self.conexao.cursor.fetchone()
          # self.conexao.fecharConexao()
        print(infomacoesPag)

    #testado e funcionando
    def pagamentoMensal(self, cliente:Cliente):
        idCliente = self.clienteControle.buscaIdCliente(cliente)
        comandoSql = f'select valor_total, id_cliente_fk from tb_pagamento where id_cliente_fk = {idCliente}'
        self.conexao.cursor.execute(comandoSql)
        informacoesPag = self.conexao.cursor.fetchone()
         # self.conexao.fecharConexao()
        print(informacoesPag)