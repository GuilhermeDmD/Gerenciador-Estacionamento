from Entidades.Vagas import Vagas
from Entidades.Veiculo import Veiculo
from Entidades.Cliente import Cliente
from Controle.ControleCliente import ControleCliente
from ConexaoBD import ConexaoBD

class ControleEstac:
    def __init__(self):
        self.conexao = ConexaoBD()
        self.cliente = ControleCliente()

    # testado e funcionando
    def addVeiculoAvulso(self, veiculo: Veiculo, vagas: Vagas):
        inserirVeiculo = f'INSERT INTO tb_veiculos(placa_veiculo, modelo_veiculo, cor_veiculo, estado, id_cliente_fk) VALUES("{veiculo.placa}", "{veiculo.modelo}", "{veiculo.cor}", "Ativo", null)'
        self.conexao.cursor.execute(inserirVeiculo)
        self.conexao.conexao.commit()
        print(f"Veículo adicionado: {veiculo.modelo} \nVaga: {vagas.localizacao}")

    # testado e funcionando
    def encerrarVeiculo(self, veiculo: Veiculo):
        removerVeiculo = f'update tb_veiculos set estado = "Excluído" where placa_veiculo = "{veiculo.placa}"'
        self.conexao.cursor.execute(removerVeiculo)
        self.conexao.conexao.commit()
        print("Veículo removido")

    # não foi testado ainda
    def addVeiculoMensal(self, veiculo: Veiculo, cliente: Cliente):
        idCliente = self.cliente.buscaIdCliente(cliente)
        inserirVeiculoMensal = f'INSERT INTO tb_veiculos(placa_veiculo, modelo_veiculo, cor_veiculo, estado, id_cliente_fk) VALUES("{veiculo.placa}", "{veiculo.modelo}", "{veiculo.cor}", "Ativo", {idCliente})'
        self.conexao.cursor.execute(inserirVeiculoMensal)
        self.conexao.conexao.commit()
        print("Veículo mensal cadastrado")
