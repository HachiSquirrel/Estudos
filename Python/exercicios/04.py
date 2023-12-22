'''

Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros.

'''

valor = int(input('Digite um valor em metros? '))
resultado_1 = valor * 100
resultado_2 = valor * 1000
if valor == 1:
    print(f'{valor} metro em centimetros é igual a {resultado_1} e em milimetros é {resultado_2}')
else:
    print(f'{valor} metros em centimetros é igual a {resultado_1} e em milimetros é {resultado_2}')
 