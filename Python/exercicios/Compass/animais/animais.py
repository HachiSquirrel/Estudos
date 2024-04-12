animais = ['Cachorro', 'Gato', 'Leão', 'Tigre', 'Elefante', 'Girafa', 'Zebra', 'Urso', 'Macaco', 'Cavalo', \
                 'Vaca', 'Porco', 'Ovelha', 'Coelho', 'Rato', 'Galinha', 'Pato', 'Peru', 'Pombo', 'Papagaio']


animais.sort()

animais_crescente = [animal for animal in animais]
animais_crescente

import csv

with open('animais_crescente.csv', mode ='w') as lista_c:
    writer = csv.writer(lista_c)
    for animal in animais_crescente:
        writer.writerow([animal])