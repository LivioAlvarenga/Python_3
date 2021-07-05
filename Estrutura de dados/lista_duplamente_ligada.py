
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
        if self.__quantidade == 0:
            return self.__inserir_em_lista_vazia(conteudo)

        celula = Celula(conteudo)
        celula.proximo = self.__inicio
        self.__inicio.anterior = celula
        self.__inicio = celula
        self.__quantidade += 1

    def inserir_no_fim(self, conteudo):
        if self.__quantidade == 0:
            return self.__inserir_em_lista_vazia(conteudo)

        celula = Celula(conteudo)
        celula.anterior = self.__fim
        self.__fim.proximo = celula
        self.__fim = celula
        self.__quantidade += 1

    def inserir(self, posição: int, conteudo):
        if posição == 0:
            return self.inserir_no_inicio(conteudo)
        if posição == self.__quantidade:
            return self.inserir_no_fim(conteudo)

        celula = Celula(conteudo)
        esquerda = self.__celula(posição-1)
        direita = esquerda.proximo
        celula.proximo = direita
        celula.anterior = esquerda
        esquerda.proximo = celula
        direita.anterior = celula
        self.__quantidade += 1

    def item(self, posição: int):
        celula = self.__celula(posição)
        return celula.conteudo

    def __validar_posição(self, posição: int):
        if 0 <= posição < self.__quantidade:
            return True

        raise IndexError(f'Posição inválida {posição}')

    def __celula(self, posição: int):
        self.__validar_posição(posição)
        metade = self.__quantidade // 2
        if posição < metade:
            atual = self.__inicio
            for i in range(0, posição):
                atual = atual.proximo
            return atual
        else:
            atual = self.__fim
            for i in range(posição + 1, self.__quantidade)[::-1]:
                atual = atual.anterior
            return atual

    def imprimir(self):
        atual = self.__inicio
        for pos in range(0, self.__quantidade):
            print(f'P{pos} - {atual.conteudo}')
            atual = atual.proximo

    def __remover_ultimo(self):
        if self.__quantidade == 1:
            removido = self.__inicio
            self.__inicio = None
            self.__fim = None
            self.__quantidade -= 1
            return removido.conteudo

    def remover_do_inicio(self):
        if self.__quantidade == 1:
            return self.__remover_ultimo()
        else:
            removido = self.__inicio
            self.__inicio = removido.proximo
            self.__inicio.anterior = None
            removido.proximo = None
            self.__quantidade -= 1
            return removido.conteudo

    def remover_do_fim(self):
        if self.__quantidade == 1:
            return self.__remover_ultimo()
        else:
            removido = self.__fim
            self.__fim = removido.anterior
            self.__fim.proximo = None
            removido.anterior = None
            self.__quantidade -= 1
            return removido.conteudo

    def remover(self, posição: int):
        if posição == 0:
            return self.remover_do_inicio()
        if posição == self.__quantidade - 1:
            return self.remover_do_fim()

        removido = self.__celula(posição)
        esquerda = removido.anterior
        direita = removido.proximo
        removido.proximo = None
        removido.anterior = None
        esquerda.proximo = direita
        direita.anterior = esquerda
        self.__quantidade -= 1
        return removido.conteudo
