class Pessoa:
    def __init__(self, id):
        self.__nome = ""
        self.id = id

    def definir_nome(self, nome):
        self.__nome = nome

    def nome(self):
        return self.__nome


pessoa = Pessoa(0)
nome = 'Fulano De Tal'
print(nome)
