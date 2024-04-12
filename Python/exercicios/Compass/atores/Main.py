

def extrair(caminho):
    arquivo = open(caminho, "r")
    atores = []
    next(arquivo)
    for linha in arquivo:
        infoAtor = []
        if (linha[0] == "\""):
            infoAtorErrado = linha.split(",")
            infoAtor.append((infoAtorErrado[0] + infoAtorErrado[1])
                            .strip("\""))
            infoAtor.append(infoAtorErrado[2].strip())
            infoAtor.append(infoAtorErrado[3].strip())
            infoAtor.append(infoAtorErrado[4].strip())
            infoAtor.append(infoAtorErrado[5].strip())
            infoAtor.append(infoAtorErrado[6].strip())
        else:
            infoAtor = linha.split(",")
        atores.append(
            {
                "Actor": infoAtor[0].strip(),
                "Total Gross": infoAtor[1].strip(),
                "Number of Movies": infoAtor[2].strip(),
                "Average per Movie": infoAtor[3].strip(),
                "#1 Movie": infoAtor[4].strip(),
                "Gross": infoAtor[5].strip()})
    arquivo.close()
    return atores


def transformar(lista):
    for ator in lista:
        ator["Total Gross"] = float(ator["Total Gross"])
        ator["Number of Movies"] = int(ator["Number of Movies"])
        ator["Average per Movie"] = float(ator["Average per Movie"])
        ator["Gross"] = float(ator["Gross"])
    return lista


def main():
    listaAtoresString = extrair("./actors.csv")
    listaAtores = transformar(listaAtoresString)
    # A lista de atores é agora uma lista de dicionários, em que cada coluna
    # do cabeçalho é uma chave, e o valor é o correspondente
    # Exercicio 1
    # Procurar pelo valor máximo da chave "Numer of Movies" da lista de atores
    print('exercicio 1')
    exercicio1 = max(listaAtores, key=lambda x: x["Number of Movies"])
    print(exercicio1["Actor"], exercicio1["Number of Movies"])

    # Exercicio 2
    # Imprimir apenas os valores relevantes da lista
    print('exercicio 2')
    for a in listaAtores:
        print(a["Actor"], a["Average per Movie"])
    # Exercicio 3
    # Procurar pelo valor máximo da chave "Average per Movie"
    # da lista de atores
    print('exercicio 3')
    exercicio3 = max(listaAtores, key=lambda x: x["Average per Movie"])
    print(exercicio3["Actor"])
    # Exercicio 4
    # Criar um dicionário em que cada chave é o nome de um filme, e o valor
    # é a sua frequência. Depois procurar pelo valor máximo desse dicionário
    print('exercicio 4')
    listaFilmesFrequencia = {}
    for a in listaAtores:
        if a["#1 Movie"] not in listaFilmesFrequencia:
            listaFilmesFrequencia[a["#1 Movie"]] = 1
        else:
            listaFilmesFrequencia[a["#1 Movie"]] += 1

    filmeFrequente = max(listaFilmesFrequencia, key=listaFilmesFrequencia.get)
    print(filmeFrequente, listaFilmesFrequencia[filmeFrequente])
    # Exercicio 5
    # Ordenar a lista de actores pelo valor "Total Gross" na ordem decrescente,
    # e imprimir apenas os valores relevantes da lista
    print('exercicio 5')
    exercicio5 = sorted(
        listaAtores, key=lambda d: d["Total Gross"], reverse=True)
    for a in exercicio5:
        print(a["Actor"], a["Total Gross"])


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()

# %%
