'''

Escreva um programa que converta uma temperatura digitando em graus Celcius e converta para Fahrenheit.

'''

c = float(input('Digite o valor da temperatura atual em ºC: '))
f = (c * 1.8) + 32  # conversão

print(f'A conversão de {c} graus Celcius em Fahrenheit é igual a {f :.1f}ºF.')