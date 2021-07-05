
class Celula():
    def __init__(self, conteudo):
        self.conteudo = conteudo
        self.proximo = None
        self.anterior = None


class Lista_duplamente_ligada():
    def __init__(self):
        self.__inicio = None
        self.__fim = None
        self.__quantidade: int = 0

    @property
    def inicio(self):
        return self.__inicio

    @property
    def fim(self):
        return self.__fim

    @property
    def quantidade(self) -> int:
        return self.__quantidade

    def __inserir_em_lista_vazia(self, conteudo) -> None:
        celula = Celula(conteudo)
        self.__inicio = celula
        self.__fim = celula
        self.__quantidade += 1

    def inserir_no_inicio(self, conteudo):
        if self.quantidade == 0:
            return self.__inserir_em_lista_vazia(conteudo)

        celula = Celula(conteudo)
        celula.proximo = self.inicio
        self.__inicio.anterior = celula
        self.__inicio = celula
        self.__quantidade += 1

    def inserir_no_fim(self, conteudo):
        if self.quantidade == 0:
            return self.__inserir_em_lista_vazia(conteudo)

        celula = Celula(conteudo)
        celula.anterior = self.fim
        self.__fim.proximo = celula
        self.__fim = celula
        self.__quantidade += 1

    def item(self, posição: int):
        celula = self.__celula(posição)
        return celula.conteudo

    def __validar_posição(self, posição: int):
        if 0 <= posição < self.quantidade:
            return True

        raise IndexError(f'Posição inválida {posição}')

    def __celula(self, posição: int):
        self.__validar_posição(posição)
        atual = self.inicio
        for i in range(0, posição):
            atual = atual.proximo
        return atual

    def imprimir(self):
        atual = self.inicio
        for pos in range(0, self.quantidade):
            print(f'P{pos} - {atual.conteudo}')
            atual = atual.proximo
