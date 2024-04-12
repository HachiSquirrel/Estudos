'''
Calcule o valor mínimo, valor máximo, valor médio e a mediana da lista
 gerada na célula abaixo:



Obs.: Lembrem-se, para calcular a mediana a
lista deve estar ordenada!



import random
# amostra aleatoriamente 50 números do intervalo 0...500
random_list = random.sample(range(500),50)


Use as variáveis abaixo para representar cada operação matemática
'''
# %%

# numero aleatorio
# sorted ordena lista
import statistics
import random

random_list = random.sample(range(500), 50)

lista_ordenada = sorted(random_list)

mediana = statistics.median(lista_ordenada)
media = sum(lista_ordenada) / len(lista_ordenada)
valor_minimo = min(lista_ordenada)
valor_maximo = max(lista_ordenada)

print(f'Media:{media}, Mediana:{mediana}, Mínimo:{valor_minimo}, Máximo:{valor_maximo}')

# %%
