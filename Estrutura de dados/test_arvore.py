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
