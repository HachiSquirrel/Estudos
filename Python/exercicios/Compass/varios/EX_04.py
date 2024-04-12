'''
A função calcular_valor_maximo deve receber dois parâmetros,
 chamados de operadores e operandos.
 Em operadores, espera-se uma lista de caracteres
 que representam as operações matemáticas suportadas
 (+, -, /, *, %), as quais devem ser aplicadas à lista de operadores
 nas respectivas posições.
 Após aplicar cada operação ao respectivo par de operandos,
 a função deverá retornar o maior valor dentre eles.



Veja o exemplo:



Entrada

operadores = ['+','-','*','/','+']
operandos  = [(3,6), (-7,4.9), (8,-8), (10,2), (8,4)]


Aplicar as operações aos pares de operandos

[ 3+6 , -7-4.9, 8*-8 , 10/2 , 8+4 ]


Obter o maior dos valores

12


Na resolução da atividade você deverá aplicar as seguintes funções:

max

zip

ma
'''


import operator

simb = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '%': operator.mod
}

operadores = ['+', '-', '*', '/', '+']
operandos = [(3, 6), (-7, 4.9), (8, -8), (10, 2), (8, 4)]


def calcular_valor_maximo(operadores, operandos) -> float:

    uniao = list(map(lambda x: (x[0][0], x[1], x[0][1]),
                     (zip(operandos, operadores))))
    calc = list(map(lambda x: simb[x[1]](x[0], x[2]), uniao))

    maximo = float(max(calc))
    return maximo


print(calcular_valor_maximo(operadores, operandos))
