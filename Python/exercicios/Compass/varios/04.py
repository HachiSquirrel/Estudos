'''
Escreva um código Python para imprimir todos os números primos entre 1 até 100.
Lembre-se que você deverá desenvolver o cálculo que identifica 
se um número é primo ou não.



Importante: Aplique a função range()

'''
for numero in range(0, 101):
    if numero > 1:
        for j in range(2, numero):
            if (numero % j == 0):
                break
        else:
            print(numero)
