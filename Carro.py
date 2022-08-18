class Carro:
    def __init__(self, placa):
        self.placa = placa
        self.estacionado = False

    def estacionar(self):
        self.estacionado = True

    def sair_da_vaga(self):
        self.estacionado = False