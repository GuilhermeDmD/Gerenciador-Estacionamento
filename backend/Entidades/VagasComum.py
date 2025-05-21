class VagasComum(Vagas):
    def __init__(self, idvaga, localizacao):
        super().__init__(idvaga, localizacao)
        self.tipo = "comum"
     