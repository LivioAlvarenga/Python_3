from arvore import Arvore

# .Testando o código.
if __name__ == '__main__':

    """# .Instanciando pedidos
    livraria = Arvore('Livros')
    livraria.imprimir()

    # .Inserir filhos
    livraria.raiz.inserir_filhos('Gastronomia')
    livraria.imprimir()

    # .Inserir filhos
    livraria.raiz.inserir_filhos('Informática')
    livraria.imprimir()

    # .Encontrando itens na arvore
    encontrado = livraria.localizar_nodo('Livros')
    print(f'\n{encontrado = }')

    encontrado = livraria.localizar_nodo('Gastronomia')
    print(f'\n{encontrado = }')

    encontrado = livraria.localizar_nodo('Informática')
    print(f'\n{encontrado = }')

    # .Encontrando itens que não existe na arvore
    encontrado = livraria.localizar_nodo('Teste')
    print(f'\n{encontrado = }')

    # .Inserir filhos especificando o pai
    livraria.inserir_modo('Informática', 'Linguagens')
    livraria.inserir_modo('Linguagens', 'Python')
    livraria.inserir_modo('Gastronomia', 'Culinária Brasileira')
    livraria.inserir_modo('Culinária Brasileira', 'Feijoada')
    livraria.inserir_modo('Gastronomia', 'Culinária Japonesa')
    livraria.imprimir()

    # .Removendo filhos
    removido = livraria.remover_nodo('Feijoada')
    print(f'\n{removido = }\n')
    livraria.imprimir()

    # .Removendo um Nodo inteiro
    removido = livraria.remover_nodo('Informática')
    print(f'\n{removido = }\n')
    livraria.imprimir()"""

    """
    screen
        MDBoxLayout1
            TopToolbar
            box_sem_scroll_ver
            ScrollView
                box_scroll_ver
                    BoxCard
                        CardOne1
                        CardOne2
                        CardOne3
                        CardOne4
                        CardOne5
                        CardOne6
    """
    screen = Arvore('screen')
    screen.imprimir()
    screen.inserir_modo('screen', 'MDBoxLayout1')
    screen.inserir_modo('screen', 'MDBoxLayout1')
    screen.inserir_modo('MDBoxLayout1', 'TopToolbar')
    screen.inserir_modo('MDBoxLayout1', 'box_sem_scroll_ver')
    screen.inserir_modo('MDBoxLayout1', 'ScrollView')
    screen.inserir_modo('ScrollView', 'box_scroll_ver')
    screen.inserir_modo('box_scroll_ver', 'BoxCard')
    screen.inserir_modo('BoxCard', 'CardOne1')
    screen.inserir_modo('BoxCard', 'CardOne2')
    screen.inserir_modo('BoxCard', 'CardOne3')
    screen.inserir_modo('BoxCard', 'CardOne4')
    screen.inserir_modo('BoxCard', 'CardOne5')
    screen.imprimir()
    pesquisa = screen.localizar_nodo('CardOne1')
    print(f'\n{pesquisa = }')
