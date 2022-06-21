class Veiculo:
    def __init__(self, tipo, peso):  
        if tipo in 'MCV':
            self._tipo = tipo
        else:
            print('O tipo do Veículo deve ser Carro(C), Moto(M) ou Van(V).')
        self._peso = peso

    @property
    def peso(self):
        return self._peso

    @property
    def tipo(self):
        return self._tipo