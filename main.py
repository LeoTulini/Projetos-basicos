from balsa import *
from veiculo import Veiculo

quantidade_vagas = int(input('Informe a quantidade máxima de veículos suportados pela balsa: '))
peso_max_suportado = float(input('Infrome o peso máximo suportado pela balsa: '))

balsa = Balsa(peso_max_suportado, quantidade_vagas)
moto_1 = Veiculo('M', 100)
moto_2 = Veiculo('M', 100)
carro_1 = Veiculo('C', 400)
van_1 = Veiculo('V', 650)
balsa.embarca_veiculo(moto_1)
balsa.embarca_veiculo(moto_2)
balsa.embarca_veiculo(carro_1)
balsa.embarca_veiculo(van_1)
balsa.exibe_dados()