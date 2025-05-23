from Controle import ControleEst
from Entidades.Veiculo import Veiculo
from Entidades.VagasComum import VagasComum

controle = ControleEst()
veiculo = Veiculo(1, "placa", "modelo", "cor", "dataEntrada", "horaEntrada")
vaga = VagasComum(2, "localizacao", "categoria", "valor")
controle.addVeiculo(veiculo, vaga)


