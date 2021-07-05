
from lista_duplamente_ligada import Lista_duplamente_ligada


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
    lista = Lista_duplamente_ligada()
    print(f'\n-> Criando lista Ligada\n{lista.quantidade = }')

    # .Inserindo 1ª Loja na Lista Duplamente Ligada vazia
    lista.inserir_no_inicio(loja1)
    print(
        f'\n-> Inserindo 1ª Loja na Lista Duplamente Ligada Vazia\n\
{lista.quantidade = }')
    lista.imprimir()

    # .Retornando item por posição da Lista Duplamente Ligada
    print(
        f'\n-> Retornando item da posição 0 da Lista Duplamente Ligada\n\
{lista.item(0)}')

    # .Inserindo 2ª Loja na Lista Duplamente Ligada
    lista.inserir_no_inicio(loja2)
    print(
        f'\n-> Inserindo 2ª Loja na Lista Duplamente Ligada\n\
{lista.quantidade = }')
    lista.imprimir()

    # .Inserindo 3ª Loja na Lista Duplamente Ligada
    lista.inserir_no_inicio(loja3)
    print(
        f'\n-> Inserindo 3ª Loja na Lista Duplamente Ligada\n\
{lista.quantidade = }')
    lista.imprimir()

    # .Inserindo 4ª Loja no fim da Lista Duplamente Ligada
    lista.inserir_no_fim(loja4)
    print(
        f'\n-> Inserindo 4ª Loja no fim da Lista Duplamente Ligada\n\
{lista.quantidade = }')
    lista.imprimir()
