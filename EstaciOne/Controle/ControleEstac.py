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
        inserirVeiculo = 'INSERT INTO tb_veiculos(placa_veiculo, modelo_veiculo, cor_veiculo, estado, id_cliente_fk) VALUES(%s, %s, %s, "Estacionado", null)'
        self.conexao.cursor.execute(inserirVeiculo, (veiculo.placa, veiculo.modelo, veiculo.cor))
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
    
    # para o menu_contexto
    def buscarVeiculoAvulsoPorVaga(self, vaga):
        self.conexao = ConexaoBD()
        comandosql = 'select v.modelo_veiculo, v.cor_veiculo, v.placa_veiculo, vg.localizacao from tb_veiculos v inner join tb_historico h on v.id_veiculo = h.id_veiculo_fk inner join tb_vagas vg on h.id_vaga_fk = vg.id_vaga where vg.tipo = "Avulso" and vg.localizacao = %s ORDER BY h.id_historico DESC LIMIT 1'
        self.conexao.cursor.execute(comandosql, (vaga, ))
        resultado = self.conexao.cursor.fetchone()
        self.conexao.fecharConexao()
        if resultado:
            return{
                "modelo":resultado[0],
                "cor":resultado[1],
                "placa":resultado[2],
                "vaga":resultado[3]
        }
        else:
            return None


    # testado e funcionando
    def encerrarVeiculo(self, veiculo: Veiculo):
        self.conexao = ConexaoBD()
        removerVeiculo = 'update tb_veiculos set estado = "Não estacionado" where placa_veiculo = %s'
        self.conexao.cursor.execute(removerVeiculo, (veiculo.placa, ))
        self.conexao.conexao.commit()
        self.conexao.fecharConexao()
        print("Veículo removido")

    # TESTADO E FUNCIONANDO
    def addVeiculoMensal(self, veiculo: Veiculo, cpf):
        self.conexao = ConexaoBD()
        idCliente = self.cliente.buscaIdCliente(cpf)
        inserirVeiculoMensal = 'INSERT INTO tb_veiculos(placa_veiculo, modelo_veiculo, cor_veiculo, estado, id_cliente_fk) VALUES(%s, %s, %s, "Estacionado", %s)'
        self.conexao.cursor.execute(inserirVeiculoMensal, (veiculo.placa, veiculo.modelo, veiculo.cor, idCliente))
        self.conexao.conexao.commit()
        self.conexao.fecharConexao()

