'''
Dada a seguinte lista:


a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]



Faça um programa que gere uma nova lista 
contendo apenas números ímpares.

'''
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
nova_lista = []
for numero in a:
    if numero % 2 != 0:
        nova_lista.append(numero)
print(nova_lista)
