from lista_ligada import Lista_ligada


class Pilha():
    def __init__(self) -> None:
        self.pilha = Lista_ligada()

    def empilhar(self, conteudo):
        self.pilha.inserir_no_inicio(conteudo)

    def desempilhar(self):
        return self.pilha.remover_do_inicio()

    @property
    def topo(self):
        return self.pilha.item(0)

    @property
    def vazia(self):
        return self.pilha.quantidade == 0
