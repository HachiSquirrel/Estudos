'''

Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por km rodado.

'''

dias = int(input('Quantos dias o carro está alugado? '))
km = float(input('Quantos km foram rodados no total? '))
total = (dias * 60) + (km * 0.15)  # calculo para saber o total.
print(f'O valor total ficou {total :.2f} ')
