class Aviao:
    def __init__(self, modelo, velocidade_maxima, capacidade, cor):
        self.modelo = modelo
        self.velocidade_maxima = velocidade_maxima
        self.capacidade = capacidade
        self.cor = cor


avioes = []

avioes.append(Aviao('BOEING456', 1500, 400, "Azul"))
avioes.append(Aviao('Embraer Praetor 600', 863, 14, 'Azul'))
avioes.append(Aviao("Antonov An-2", 258, 12, 'Azul'))

for aviao in avioes:
    print("O aviao de modelo" + aviao.modelo + "possui uma velocidade de"
          + str(aviao.velocidade_maxima) +
          "km/h, capacidade para" + str(aviao.capacidade) +
          "passageiros e é da cor" + aviao.cor)
