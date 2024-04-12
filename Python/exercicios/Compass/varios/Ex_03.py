'''
A função calcula_saldo recebe uma lista de tuplas, correspondendo
 a um conjunto de lançamentos bancários.
 Cada lançamento é composto pelo seu valor (sempre positivo)
   e pelo seu tipo (C - crédito ou D - débito).

Abaixo apresentando uma possível entrada para a função.



lancamentos = [
    (200,'D'),
    (300,'C'),
    (100,'C')
]


A partir dos lançamentos, a função deve calcular o valor final,
somando créditos e subtraindo débitos.
Na lista anterior, por exemplo, teríamos como resultado final 200.



Além de utilizar lambdas, você deverá aplicar, obrigatoriamente,
 as seguintes funções na resolução:



reduce (módulo functools)

map

'''


def calcula_saldo(lancamentos) -> float:
    import functools

    def soma_creditos(x): return x[0] if x[1] == 'C' else 0

    def subtrai_debitos(x): return x[0] if x[1] == 'D' else 0

    creditos = list(map(soma_creditos, lancamentos))
    debitos = list(map(subtrai_debitos, lancamentos))

    saldo_final = functools.reduce(lambda x, y: x+y, creditos)
    - functools.reduce(lambda x, y: x+y, debitos)
    return saldo_final


lancamentos = [
    (200, 'D'),
    (300, 'C'),
    (100, 'C')
]

print(calcula_saldo(lancamentos))
