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
    loja4 = Loja("Supermercado", "Rua João XX, 100")
    loja5 = Loja("Hipermercado", "Rua João XXI, 1000")
    loja6 = Loja("Epa", "Av Papa João Paulo II, 23")

    # .Criando lista Ligada
    lista = Lista_ligada()
    print(f'\n-> Criando lista Ligada\n{lista.quantidade = }')

    # .Inserindo 1ª Loja na Lista Ligada
    lista.inserir_no_inicio(loja1)
    print(f'\n-> Inserindo 1ª Loja na Lista Ligada\n{lista.quantidade = }')
    lista.imprimir()

    # .Inserindo 2ª Loja na Lista Ligada
    lista.inserir_no_inicio(loja2)
    print(f'\n-> Inserindo 2ª Loja na Lista Ligada\n{lista.quantidade = }')
    lista.imprimir()

    # .Inserindo 3ª Loja na Lista Ligada
    lista.inserir_no_inicio(loja3)
    print(f'\n-> Inserindo 3ª Loja na Lista Ligada\n{lista.quantidade = }')
    lista.imprimir()

    # .Inserindo 4ª Loja na Lista Ligada na posição 1
    lista.inserir(1, loja4)
    print(
        f'\n-> Inserindo 4ª Loja na Lista Ligada na posição 1\n\
{lista.quantidade = }')
    lista.imprimir()

    # .Inserindo 5ª Loja na Lista Ligada na posição 0
    lista.inserir(0, loja5)
    print(
        f'\n-> Inserindo 5ª Loja na Lista Ligada na posição 0\n\
{lista.quantidade = }')
    lista.imprimir()

    # .Inserindo 6ª Loja na Lista Ligada na ultima posição
    lista.inserir(lista.quantidade, loja6)
    print(
        f'\n-> Inserindo 6ª Loja na Lista Ligada na ultima posição\n\
{lista.quantidade = }')
    lista.imprimir()

    # .Removendo primeiro item da Lista Ligada
    removido = lista.remover_do_inicio()
    print(
        f'\n-> Removendo primeiro item da Lista Ligada\n{lista.quantidade = }')
    lista.imprimir()
    print(f'\nRemovido item:\n {removido}')

    # .Removendo terceiro item da Lista Ligada
    removido = lista.remover(2)
    print(
        f'\n-> Removendo terceiro item da Lista Ligada\n{lista.quantidade = }')
    lista.imprimir()
    print(f'\nRemovido item:\n {removido}')

    # .Removendo ultimo item da Lista Ligada
    removido = lista.remover(lista.quantidade - 1)
    print(
        f'\n-> Removendo ultimo item da Lista Ligada\n{lista.quantidade = }')
    lista.imprimir()
    print(f'\nRemovido item:\n {removido}')
