from Controle import ControleEstac
from Controle.ControleCliente import ControleCliente
from Controle import ControleCategoria
from Controle.ControleVagas import ControleVaga


controleCliente = ControleCliente()
controleCliente.buscarCliente("222.222.222-12")
controleVaga = ControleVaga()
controleVaga.buscarIdVaga("AC1")