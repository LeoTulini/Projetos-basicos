from veiculo import Veiculo
class Balsa:
    def __init__(self, peso_max_suportado, quantidade_vagas):
        self._peso_max_suportado = peso_max_suportado * 1000
        self._quantidade_vagas = quantidade_vagas
        self._quantidade_motos = 0
        self._quantidade_carros = 0
        self._quantidade_vans = 0
        self._peso_motos = 0
        self._peso_carros = 0
        self._peso_vans = 0

    @property
    def quantidade_vagas(self):
        return self._quantidade_vagas

    @property
    def quantidade_embarcada(self):
        return self.quantidade_motos() + self.quantidade_carros() + self.quantidade_vans()

    @property
    def peso_max_suportado(self):
        return self._peso_max_suportado

    @property
    def quantidade_motos(self):
        return self._quantidade_motos

    @property
    def quantidade_carros(self):
        return self._quantidade_carros

    @property
    def quantidade_vans(self):
        return self._quantidade_vans

    @property
    def peso_motos(self):
        return self._peso_motos

    @property
    def peso_carros(self):
        return self._peso_carros

    @property
    def peso_vans(self):
        return self._peso_vans

    @property
    def peso_total_embarcado(self):
        return self.peso_motos() + self.peso_carros() + self.peso_vans()

    def vagas_restantes(self):
        return self.quantidade_vagas() - self.quantidade_embarcada()

    def peso_restante(self):
        return self.peso_max_suportado() - self.peso_total_embarcado()

    def embarca_veiculo(self, veiculo):
        if (self.quantidade_embarcada() + 1) <= self.quantidade_vagas():
            if veiculo.peso() + self.peso_total_embarcado() <= self.peso_max_suportado():
                if veiculo.tipo() == 'M':
                    self.peso_motos += veiculo.peso()
                    self.quantidade_motos += 1
                elif veiculo.tipo() == 'C':
                    self.peso_carros += veiculo.peso()
                    self.quantidade_carros += 1
                elif veiculo.tipo() == 'V':
                    self.peso_vans += veiculo.peso()
                    self.quantidade_vans += 1
            else:
                print('Peso máximo atingido.')
        else:
            print('Quantidade máxima de veículos atingida.')
    
    def exibe_dados(self):
        print(f'Peso máximo suportado pela balsa: {self.peso_max_suportado()} Kg')
        print(f'Peso total de motos embarcadas: {self.peso_motos()} Kg')
        print(f'Peso total de carros embarcadas: {self.peso_carros()} Kg')
        print(f'Peso total de vans embarcadas: {self.peso_vans()} Kg')
        print(f'Peso total carregado: {self.peso_total_embarcado()} Kg')
        print(f'Peso restante: {self.peso_restante() / 1000} T')
        print(f'Quantidade de vagas na balsa: {self.quantidade_vagas()}')
        print(f'Quantidade de vagas ocupadas por motos: {self.quantidade_motos()}')
        print(f'Quantidade de vagas ocupadas por carros: {self.quantidade_carros()}')
        print(f'Quantidade de vagas ocupadas por vans: {self.quantidade_vans()}')
        print(f'Quantidade total de vagas ocupadas: {self.quantidade_embarcada()}')
        print(f'Vagas restantes: {self.vagas_restantes()}')
