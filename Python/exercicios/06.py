'''

Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pinta-la,
 sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

'''

largura = float(input('Digite a largura em metros da sua parede:'))
altura = float(input('Agora digite a altura em metros da mesma:'))
area = largura * altura  # para saber a área
metros = area / 2  # para saber os metros quadrados

print(f'A sua área quadrada é igual a {area} e será necessário {metros} litros de tinta para pintar.')
