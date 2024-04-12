# 01

import random

random.randint(0, 1000)

list_random = []

for num in range(250):
    list_random.append(random.randint(0, 1000))

list_random.reverse()
print(list_random)

# 02

animais = ['Cachorro', 'Gato', 'Leão', 'Tigre', 'Elefante', 'Girafa', 'Zebra', 'Urso', 'Macaco', 'Cavalo','Vaca', 'Porco', 'Ovelha', 'Coelho', 'Rato', 'Galinha', 'Pato', 'Peru', 'Pombo', 'Papagaio']

animais.sort()

animais_crescente = [animal for animal in animais]
animais_crescente

import csv

with open('animais_crescente.csv', mode='w') as lista_c:
    writer = csv.writer(lista_c)
    for animal in animais_crescente:
        writer.writerow([animal])

# 03

import random, time, os, names

random.seed(40)
print(random.random())

nomes_unicos = 3000

nomes_aleatorios = 10000000

aux = []

for i in range(0, nomes_unicos):
    aux.append(names.get_full_name())

print("Gerando {} nomes aleatórios".format(nomes_aleatorios))

dados = []

for i in range(0, nomes_aleatorios):
    dados.append(random.choice(aux))

print(f'Quantidade de nomes únicos: {len(aux)}')
aux

print(f'Quantidade de nomes aleatórios: {len(dados)}')
dados

with open('nomes_aleatorios.txt', 'w') as arquivo:
    for nome in dados:
        arquivo.write(f'{str(nome)}\n')
