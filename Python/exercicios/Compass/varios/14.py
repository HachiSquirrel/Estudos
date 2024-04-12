
'''
Escreva uma função que recebe um número variável de parâmetros
não nomeados e um número variado de parâmetros nomeados
e imprime o valor de cada parâmetro recebido.

Teste sua função com os seguintes parâmetros:



(1, 3, 4, 'hello', parametro_nomeado='alguma coisa', x=20)
'''


def variavel(n1, n2, n3, texto, texto2='alguma coisa', x=20):
    return (f'{n1}\n{n2}\n{n3}\n{texto}\n{texto2}\n{x}')


print(variavel(n1=1, n2=3, n3=4, texto='hello'))
