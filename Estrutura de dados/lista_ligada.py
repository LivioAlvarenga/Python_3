
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

    def inserir(self, posição: int, conteudo):
        if posição == 0:
            self.inserir_no_inicio(conteudo)
            return
        celula = Celula(conteudo)
        esquerda = self.__celula(posição-1)
        celula.proximo = esquerda.proximo
        esquerda.proximo = celula
        self.__quantidade += 1

    def __celula(self, posição: int):
        self.__validar_posição(posição)
        atual = self.inicio
        for i in range(0, posição):
            atual = atual.proximo
        return atual

    def __validar_posição(self, posição: int):
        if 0 <= posição < self.quantidade:
            return True

        raise IndexError(f'Posição inválida {posição}')

    def imprimir(self):
        atual = self.inicio
        for pos in range(0, self.quantidade):
            print(f'P{pos} - {atual.conteudo}')
            atual = atual.proximo

    def remover_do_inicio(self):
        removido = self.inicio
        self.__inicio = removido.proximo
        removido.proximo = None
        self.__quantidade -= 1
        return removido.conteudo

    def remover(self, posição: int):
        if posição == 0:
            return self.remover_do_inicio()

        esquerda = self.__celula(posição - 1)
        removido = esquerda.proximo
        esquerda.proximo = removido.proximo
        removido.proximo = None
        self.__quantidade -= 1
        return removido.conteudo

    def item(self, posição: int):
        self.__validar_posição(posição)
        celula = self.__celula(posição)
        return celula.conteudo
