from Controle.ControleEstac import ControleEstac
from Entidades.Veiculo import Veiculo
from Entidades.Vagas import Vagas

controle = ControleEstac()
veiculo = Veiculo("", "123hj89", "gol", "vermelho")
v1 = Veiculo("", "stosB2", "ferrai", "prata")
vaga = Vagas(1, "c1", "Avulsa")
vag = Vagas("2", "moto", "avulsa")
#controle.encerrarVeiculo(veiculo)
controle.addVeiculoAvulso(veiculo, vaga)
controle.addVeiculoAvulso(v1, vag)

#testar os métodos da Vagas, Clientes, Planos
