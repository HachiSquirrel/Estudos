'''
Implemente a função my_map(list, f) que recebe uma lista
como primeiro argumento e uma função como segundo argumento.
Esta função aplica a função recebida para cada elemento da lista
recebida e retorna o resultado em uma nova lista.



Teste sua função com a lista de entrada [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
e com uma função que potência de 2 para cada elemento.

'''


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

nova_lista = []


def my_map(list, f):
    return f(list)


def lista2(li):
    for numero in li:  # variavel só para criar a formula
        nova_lista.append(numero**2)  # inserir valores na outra lista
    return nova_lista


print(my_map(lista, lista2))
