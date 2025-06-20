from Entidades.Vagas import Vagas
from Entidades.Veiculo import Veiculo
from Entidades.Cliente import Cliente
from Controle.ControleCliente import ControleCliente
from ConexaoBD import ConexaoBD

class ControleEstac:
    def __init__(self):
        self.cliente = ControleCliente()

    # testado e funcionando
    def addVeiculoAvulso(self, veiculo: Veiculo):
        self.conexao = ConexaoBD()
        inserirVeiculo = f'INSERT INTO tb_veiculos(placa_veiculo, modelo_veiculo, cor_veiculo, estado, id_cliente_fk) VALUES("{veiculo.placa}", "{veiculo.modelo}", "{veiculo.cor}", "Ativo", null)'
        self.conexao.cursor.execute(inserirVeiculo)
        self.conexao.conexao.commit()
        self.conexao.fecharConexao()

    def buscarVeiculoAvulso(self, placa):
        self.conexao = ConexaoBD()
        comandosql = f'select v.placa_veiculo, v.modelo_veiculo, v.cor_veiculo, vg.localizacao from tb_veiculos v inner join tb_historico h on v.id_veiculo = h.id_veiculo_fk inner join tb_vagas vg on h.id_vaga_fk = vg.id_vaga where v.placa_veiculo = "{placa}"'
        self.conexao.cursor.execute(comandosql)
        resultado = self.conexao.cursor.fetchone()
        self.conexao.fecharConexao()
        if resultado:
            return {
            "placa": resultado[0],
            "modelo": resultado[1],
            "cor": resultado[2],
            "vaga": resultado[3],
        }
        else:
            return None



    # testado e funcionando
    def encerrarVeiculo(self, veiculo: Veiculo):
        self.conexao = ConexaoBD()
        removerVeiculo = f'update tb_veiculos set estado = "Excluído" where placa_veiculo = "{veiculo.placa}"'
        self.conexao.cursor.execute(removerVeiculo)
        self.conexao.conexao.commit()
        self.conexao.fecharConexao()
        print("Veículo removido")

    # TESTADO E FUNCIONANDO
    def addVeiculoMensal(self, veiculo: Veiculo, cpf):
        self.conexao = ConexaoBD()
        idCliente = self.cliente.buscaIdCliente(cpf)
        inserirVeiculoMensal = f'INSERT INTO tb_veiculos(placa_veiculo, modelo_veiculo, cor_veiculo, estado, id_cliente_fk) VALUES("{veiculo.placa}", "{veiculo.modelo}", "{veiculo.cor}", "Ativo", {idCliente})'
        self.conexao.cursor.execute(inserirVeiculoMensal)
        self.conexao.conexao.commit()
        self.conexao.fecharConexao()
        print("Veículo mensal cadastrado")
