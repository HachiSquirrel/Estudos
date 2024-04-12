'''
Escreva uma função que recebe como parâmetro uma lista
e retorna 3 listas: a lista recebida dividida em 3 partes iguais.
Teste sua implementação com a lista abaixo



lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

'''
# %%


def divide(li):
    tamanho = len(lista) // 3
    parte1 = lista[:tamanho]
    parte2 = lista[tamanho:8]
    parte3 = lista[8:]
    print(parte1, parte2, parte3)


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

divide(lista)

# %%
