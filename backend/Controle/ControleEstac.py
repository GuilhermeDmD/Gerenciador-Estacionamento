from Entidades.VagasComum import VagasComum
from Entidades.Veiculo import Veiculo


class ControleEstac:
     def __init__(self):
          pass
     
     def addVeiculo(self, Veiculo: Veiculo, VagasComum: VagasComum):
          print(f"Veículo adicionado: {Veiculo.modelo} \nVaga: {VagasComum.localizacao}")
          pass