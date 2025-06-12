from Controle.ControleEstac import ControleEstac
from Controle.ControleCliente import ControleCliente
from Controle.ControleVagas import ControleVaga
from Controle.ControlePlanos import ControlePlanos
from Controle.ControleHist import ControleHist
from Controle.ControleVeiculo import ControleVeiculo
from Controle.ControlePagamento import ControlePagamento

from Entidades.Veiculo import Veiculo
from Entidades.Vagas import Vagas
from Entidades.Cliente import Cliente
from Entidades.Plano import Planos
from Entidades.CategoriaVaga import CategoriaVaga

controleEstac = ControleEstac()
veiculo = Veiculo("", "123hj89", "gol", "vermelho")
controleCliente = ControleCliente()
# v1 = Veiculo("", "stosB2", "ferrai", "prata")
# vaga = Vagas(1, "c1", "Avulsa")
# vag = Vagas("2", "moto", "avulsa")
# #controle.encerrarVeiculo(veiculo)
# controle.addVeiculoAvulso(veiculo, vaga)
# controle.addVeiculoAvulso(v1, vag)

#testar os métodos da Vagas, Clientes, Planos
c1 = Cliente("", "111.111.111-11", "joão", "(11)99999999", "joao@joao.com" )
vg1 = Vagas("", "C1", "Mensal")
p1 = Planos("Mensal Coberto", "Acesso mensal a vaga coberta", 400.0)
#controleCliente.addCliente(c1, vg1, p1) 
# para adicionar cliente é necessário ter o cliente o plano e a vaga(vaga adicionado direto no banco)
#controleEstac.addVeiculoMensal(veiculo, c1)

#controleCliente.mostrarClientes()
controlePlanos = ControlePlanos()
p2 = Planos("Moto mania", "Garante uma vaga de moto", 80.0)
coluna1 = "descricao_plano"
coluna2 = "valor_plano"
edicao = "editei"
edicao2 = 10
controleHist = ControleHist()
controleVeiculo = ControleVeiculo()
controleVaga = ControleVaga()
controlePgt = ControlePagamento()

controlePgt.pagamentoMensal(c1)