from lista_duplamente_ligada import Lista_duplamente_ligada


class Lista_de_nodos(Lista_duplamente_ligada):
    def __init__(self):
        super().__init__()

    def imprimir(self, nível):
        atual = self.inicio
        for i in range(0, self.quantidade):
            atual.conteudo.imprimir(nível)
            atual = atual.proximo

    def localizar_nodo(self, conteudo):
        atual = self.inicio
        for i in range(0, self.quantidade):
            encontrado = atual.conteudo.localizar_nodo(conteudo)
            if encontrado:
                return encontrado
            atual = atual.proximo

    def posição(self, conteudo):
        atual = self.inicio
        for i in range(0, self.quantidade):
            if atual.conteudo.conteudo == conteudo:
                return i
            atual = atual.proximo


class Nodo():
    def __init__(self, conteudo) -> None:
        self.conteudo = conteudo
        self.pai = None
        self.filhos = None

    def __repr__(self) -> str:
        return self.conteudo

    def imprimir(self, nível=0):
        print(f'{" "*nível}- {self.conteudo}')
        if self.filhos:
            self.filhos.imprimir(nível + 1)

    def inserir_filhos(self, filho):
        if self.filhos is None:
            self.filhos = Lista_de_nodos()
        nodo = Nodo(filho)
        nodo.pai = self
        self.filhos.inserir_no_fim(nodo)

    def localizar_nodo(self, conteudo):
        if conteudo == self.conteudo:
            return self
        if self.filhos:
            return self.filhos.localizar_nodo(conteudo)

    def remover(self):
        if self.pai:
            posição = self.pai.filhos.posição(self.conteudo)
            return self.pai.filhos.remover(posição)
        return self


class Arvore():
    def __init__(self, conteudo) -> None:
        self.raiz = Nodo(conteudo)

    def imprimir(self):
        self.raiz.imprimir()

    def localizar_nodo(self, conteudo):
        return self.raiz.localizar_nodo(conteudo)

    def inserir_modo(self, pai, filho):
        nodo_pai = self.localizar_nodo(pai)
        if nodo_pai:
            nodo_pai.inserir_filhos(filho)

    def remover_nodo(self, conteudo):
        encontrado = self.raiz.localizar_nodo(conteudo)
        if encontrado:
            if encontrado is self.raiz:
                self.raiz = None
            else:
                encontrado.remover()
        return encontrado
