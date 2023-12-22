'''

Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e
todas a possíveis informações sobre ele.

'''

# Lê algo do teclado
entrada = input("Digite algo: ")

# Obtém o tipo primitivo da entrada
tipo = type(entrada)

# Mostra o tipo primitivo
print(f"Tipo primitivo: {tipo}")

# Mostra informações sobre o tipo, dependendo do tipo de dado inserido
if tipo == str:
    print(f'É número? {entrada.isnumeric()}')
    print(f'São letras? {entrada.isalpha()}')
    print(f'São alfanúmericos? {entrada.isalpha()}')
    print(f'Está em letras maiúsculas? {entrada.isupper()}')
    print(f'Está em letras minúsculas? {entrada.islower()}')
    print(f'')
else:
    print("Tipo não reconhecido ou não suportado para análise.")