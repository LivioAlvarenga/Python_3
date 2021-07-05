
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

    def inserir_em_lista_vazia(self, conteudo) -> None:
        celula = Celula(conteudo)
        self.__inicio = celula
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
