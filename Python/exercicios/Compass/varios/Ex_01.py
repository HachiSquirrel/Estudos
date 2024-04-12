'''

Você está recebendo um arquivo contendo 10.000 números inteiros,
um em cada linha. Utilizando lambdas e high order functions,
apresente os 5 maiores valores pares e a soma destes.


Você deverá aplicar as seguintes funções no exercício:


map

filter

sorted

sum


Seu código deverá exibir na saída(simplesmente utilizando 2 comandos `print()`:


a lista dos 5 maiores números pares em ordem decrescente

a soma destes valores.

'''


lista_num = []
with open('number.txt', 'r') as numeros:
    for nums in numeros:
        lista_num.append(nums.rstrip('\n'))

lista_num_int = list(map(int, lista_num))
pares = list(filter(lambda num: num % 2 == 0, lista_num_int))
cinco_maiores = (sorted(pares, reverse=True)[:5])

print(list(cinco_maiores))
print(sum(cinco_maiores))
