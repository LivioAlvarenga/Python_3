from lista_ligada import Lista_ligada


class Loja():
    def __init__(self, nome: str, endereco: str):
        self.nome = nome
        self.endereco = endereco

    def __repr__(self):
        return f'{self.nome}\n {self.endereco}'


# .Testando o código.
if __name__ == '__main__':

    # .Instanciando Lojas
    loja1 = Loja("Mercadinho", "Rua das Laranjeiras, 12")
    loja2 = Loja("Hortifrúti", "Rua do Pomar, 300")
    loja3 = Loja("Padaria", "Rua das Flores, 600")

    # .Criando lista Ligada
    lista = Lista_ligada()
    print(f'\n{lista.quantidade = }')

    # .Inserindo 1ª Loja na Lista Ligada
    lista.inserir_no_inicio(loja1)
    print(f'\n{lista.quantidade = }')
    lista.imprimir()

    # .Inserindo 2ª Loja na Lista Ligada
    lista.inserir_no_inicio(loja2)
    print(f'\n{lista.quantidade = }')
    lista.imprimir()

    # .Inserindo 3ª Loja na Lista Ligada
    lista.inserir_no_inicio(loja3)
    print(f'\n{lista.quantidade = }')
    lista.imprimir()
