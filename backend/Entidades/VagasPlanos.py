from Entidades.Vagas import Vagas

class VagasPlanos(Vagas):

    def __init__(self, idvaga, localizacao):
        super().__init__(idvaga, localizacao)
        self.tipo = "plano mensal"