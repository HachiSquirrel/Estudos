'''

Faça um algoritmo que leia o preço de um produto e mostre seu novo valor com desconto de 25%.

'''

valor = float(input('Digite o valor do produto: '))

total = valor * (5 / 100)  # calcular o desconto

print(f'O valor com o desconto é {total :.2f}')
