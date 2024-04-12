from statistics import mean

dados = []
with open('estudantes.csv', 'r') as dados2:
    for i in dados2:
        conteudo = i.rstrip('\n').split(',')
        dados.append(conteudo)


dado_ordenado = sorted(dados)
nomes = list(map(lambda x: x[0], dado_ordenado))
notas = list(map(lambda x: sorted(
    list(map(int, x[1:])), reverse=True), dado_ordenado))

print(notas)
for i in range(len(notas)):
    media = float(round(mean(notas[i][0:3]), 2))
    print(f'Nome: {nomes[i]} Notas: {notas[i][0:3]} Média: {media}')
