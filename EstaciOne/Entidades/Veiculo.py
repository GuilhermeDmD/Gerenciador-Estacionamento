from datetime import date, datetime
class Veiculo:
    
    def __init__(self, idVeiculo, placa, modelo, cor):
        self.idVeiculo = idVeiculo
        self.placa = placa
        self.modelo = modelo
        self.cor = cor
        self.dataEntrada = date.today()
        self.horaEntrada = datetime.now().strftime("%H:%M:%S")
      

  
