from Controle.ControleHist import ControleHist
from Entidades.Veiculo import Veiculo

veiculo = Veiculo("123gh45", "Sandero", "Preto")
controleHist = ControleHist()
controleHist.addHistorico(veiculo, "AC3")