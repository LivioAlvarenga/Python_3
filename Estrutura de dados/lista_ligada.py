
class Celula():
    def __init__(self, conteudo):
        self.conteudo = conteudo
        self.proximo = None


class Lista_ligada():
    def __init__(self):
        self.__inicio = None
        self.__quantidade: int = 0

    @property
    def inicio(self):
        return self.__inicio

    @property
    def quantidade(self):
        return self.__quantidade

    def inserir_no_inicio(self, conteudo):
        celula = Celula(conteudo)
        celula.proximo = self.__inicio
        self.__inicio = celula
        self.__quantidade += 1

    def imprimir(self):
        atual = self.inicio
        for pos in range(0, self.quantidade):
            print(f'P{pos} - {atual.conteudo}')
            atual = atual.proximo
