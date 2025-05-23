from Entidades.Vagas import Vagas 

class VagasComum(Vagas):
    def __init__(self, idvaga, localizacao, categoria, valor):
        super().__init__(idvaga, localizacao)
        self.tipo = "comum"
        self.categoria = categoria
        self.valor = valor
     