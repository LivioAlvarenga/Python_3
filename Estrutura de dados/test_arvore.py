from arvore import Arvore

# .Testando o código.
if __name__ == '__main__':

    # .Instanciando pedidos
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
    livraria.imprimir()
