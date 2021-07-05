
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

    # .Inserindo 3ª Loja no início da Lista Duplamente Ligada
    lista.inserir_no_inicio(loja3)
    print(
        f'\n-> Inserindo 3ª Loja no início da Lista Duplamente Ligada\n\
{lista.quantidade = }')
    lista.imprimir()

    # .Inserindo 4ª Loja no fim da Lista Duplamente Ligada
    lista.inserir_no_fim(loja4)
    print(
        f'\n-> Inserindo 4ª Loja no fim da Lista Duplamente Ligada\n\
{lista.quantidade = }')
    lista.imprimir()

    # .Inserindo 5ª Loja  na posição 2 da Lista Duplamente Ligada
    lista.inserir(2, loja5)
    print(
        f'\n-> Inserindo 5ª Loja  na posição 2 da Lista Duplamente Ligada\n\
{lista.quantidade = }')
    lista.imprimir()

    # .Inserindo 6ª Loja  na posição 4 da Lista Duplamente Ligada
    lista.inserir(3, loja6)
    print(
        f'\n-> Inserindo 6ª Loja  na posição 4 da Lista Duplamente Ligada\n\
{lista.quantidade = }')
    lista.imprimir()

    # .Removendo primeiro item da Lista Duplamente Ligada
    removido = lista.remover_do_inicio()
    print(
        f'\n-> Removendo primeiro item da Lista Duplamente Ligada\n\
{lista.quantidade = }')
    lista.imprimir()
    print(f'\nRemovido item:\n {removido}')

    # .Removendo ultimo item da Lista Duplamente Ligada
    removido = lista.remover_do_fim()
    print(
        f'\n-> Removendo ultimo item da Lista Duplamente Ligada\n\
{lista.quantidade = }')
    lista.imprimir()
    print(f'\nRemovido item:\n {removido}')

    # .Removendo item 2 da Lista Duplamente Ligada
    removido = lista.remover(1)
    print(
        f'\n-> Removendo item 2 da Lista Duplamente Ligada\n\
{lista.quantidade = }')
    lista.imprimir()
    print(f'\nRemovido item:\n {removido}')

# ! Observações:
# Vimos que a Lista Ligada é menos eficiente para fazer operações no fim da
#  lista, pois antes de executar qualquer operação, é necessário percorrê-la.
#  A Lista Duplamente Ligada é mais eficiente que a Lista Ligada. A Lista
#  Duplamente Ligada pode ser percorrida em dois sentidos e, antes de
#  percorrê-los, calculamos o menor percurso para que seja menos custoso.

# ! from collections import deque
# A estrutura de dados deque faz parte da biblioteca padrão do python e
#  corresponde à lista duplamente ligada, pois também é otimizado para
#  inserção e remoção dos itens nas extremidades.
# Seus atributos são:
#  append - corresponde a inserir no fim
#  appendleft - corresponde a inserir no início
#  clear
#  copy
#  count - corresponde a quantidade
#  extend
#  extendleft
#  index
#  insert - corresponde a inserir em uma dada posição
#  maxlen
#  pop - remover do fim
#  popleft - remover do início
#  remove - remover de qualquer posição
#  reverse
#  rotate
