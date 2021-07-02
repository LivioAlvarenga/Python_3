
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
