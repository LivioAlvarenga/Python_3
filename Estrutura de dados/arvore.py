from lista_duplamente_ligada import Lista_duplamente_ligada


class Lista_de_nodos(Lista_duplamente_ligada):
    def __init__(self):
        super().__init__()


class Nodo():
    def __init__(self, conteudo) -> None:
        self.conteudo = conteudo
        self.pai = None
        self.filhos = None

    def imprimir(self):
        print(self.conteudo)


class Arvore():
    def __init__(self, conteudo) -> None:
        self.raiz = Nodo(conteudo)

    def imprimir(self):
        self.raiz.imprimir()
