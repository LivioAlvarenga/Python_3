from lista_duplamente_ligada import Lista_duplamente_ligada


class Lista_de_nodos(Lista_duplamente_ligada):
    def __init__(self):
        super().__init__()

    def imprimir(self, nível):
        atual = self.inicio
        for i in range(0, self.quantidade):
            atual.conteudo.imprimir(nível)
            atual = atual.proximo


class Nodo():
    def __init__(self, conteudo) -> None:
        self.conteudo = conteudo
        self.pai = None
        self.filhos = None

    def imprimir(self, nível=0):
        print(f'{" "*nível}- {self.conteudo}')
        if self.filhos:
            self.filhos.imprimir(nível + 1)

    def inserir_filhos(self, filho):
        if self.filhos is None:
            self.filhos = Lista_de_nodos()
        nodo = Nodo(filho)
        self.filhos.inserir_no_fim(nodo)


class Arvore():
    def __init__(self, conteudo) -> None:
        self.raiz = Nodo(conteudo)

    def imprimir(self):
        self.raiz.imprimir()
