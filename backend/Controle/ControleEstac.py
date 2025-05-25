from Entidades.VagasComum import VagasComum
from Entidades.Veiculo import Veiculo
from Entidades.Cliente import Cliente
from Controle.ControleCliente import controleCliente
from conexaoBD import conexaoBD


class ControleEstac:
     def __init__(self):
          self.conexao = conexaoBD()
          self.cliente = controleCliente()
          
     
     #testado e funcionando
     def addVeiculoAvulso(self, Veiculo: Veiculo, VagasComum: VagasComum):
          inserirVeiculo = f'INSERT INTO tb_veiculo(id_veiculo, placa_veiculo, modelo_veiculo, cor_veiculo, estado, horario_entrada, data_entrada, id_cliente_fk) VALUES(null, "{Veiculo.placa}", "{Veiculo.modelo}", "{Veiculo.cor}", "Ativo", "{Veiculo.horaEntrada}", "{Veiculo.dataEntrada}", null)'
          self.conexao.cursor.execute(inserirVeiculo)
          #self.conexao.conexao.commit()
          print(f"Veículo adicionado: {Veiculo.modelo} \nVaga: {VagasComum.localizacao}")
     
     #testado e funcionando 
     def encerrarVeiculo(self, Veiculo: Veiculo):
          removerVeiculo = f'update tb_veiculo set estado = "Excluído" where placa_veiculo = "{Veiculo.placa}"'
          self.conexao.cursor.execute(removerVeiculo)
          self.conexao.conexao.commit()
          print("Veículo removido")

     #não foi testado ainda
     def addVeiculoMensal(self, Veiculo: Veiculo, Cliente:Cliente ):
          idCliente = self.cliente.buscarCliente(Cliente)
          inserirVeiculoMensal = f'INSERT INTO tb_veiculo(id_veiculo, placa_veiculo, modelo_veiculo, cor_veiculo, estado, horario_entrada, data_entrada, id_cliente_fk) VALUES(null, "{Veiculo.placa}", "{Veiculo.modelo}", "{Veiculo.cor}", "Ativo", "{Veiculo.horaEntrada}", "{Veiculo.horaEntrada}", {idCliente})'
          self.conexao.cursor.execute(inserirVeiculoMensal)
          self.conexao.conexao.commit()
          print("Veículo mensal cadastrado")
          
     