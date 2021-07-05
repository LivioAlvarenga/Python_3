
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
    def quantidade(self):
        return self.__quantidade
