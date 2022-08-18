class Vaga:
    def __init__(self, identificador, tipo):
        self.id = identificador
        self.estacionado = True
        if tipo is not 'carro' and tipo is not 'moto':
            raise ValueError(f'O tipo de vaga {tipo} não foi reconhecido')
        self.tipo = tipo
        self.placa = None

    def ocupar(self, placa):
        if self.livre is False:
            raise ValueError(f'A vaga {self.identificador} ja está ocupada')

        self.placa = placa
        self.livre = False

    def desocupar(self):
        if self.livre is True:
            raise ValueError(f'A vaga {self.identificador} ja está livre')
        self.placa = None
        self.livre = True