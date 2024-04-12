'''

Faça um algoritmo que leia o salário de um funcionário e mostre o seu novo salário com reajuste de 15% de aumento.

'''

salario = float(input('Qual é o seu salário? '))
novo = salario + (salario * (15 / 100))  # calculo do aumento

print(f'Seu novo salário é igual a {novo :.2f}')
