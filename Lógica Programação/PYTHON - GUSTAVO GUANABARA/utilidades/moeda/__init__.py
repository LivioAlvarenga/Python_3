def aumentar(x=0, y=0, formato=False):
    """
    --> Função para aumentar um determinado valor.
    :param x: Valor a ser aumentado.
    :param y: Quantidade a aumentar ex: 10 (%).
    :param format: (Opicional) Se True ativa a def formatacao
    :return: Número aumentado.
    Função criada por Livio Alvarenga GitHub ...    
    """
    r = x * ((y/100) + 1)
    return r if formato is False else formatacao(r)
    

def diminuir(x=0, y=0, formato=False):
    """
    --> Função para diminuir um determinado valor.
    :param x: Valor a ser diminuido.
    :param y: Quantidade a diminuir ex: 10 (%).
    :param format: (Opicional) Se True ativa a def formatacao
    :return: Número diminuido.
    Função criada por Livio Alvarenga GitHub ...    
    """
    r = x * (1 - (y/100))
    return r if formato is False else formatacao(r)


def dobro(x=0, formato=False):
    """
    --> Função para dobrar um determinado valor.
    :param x: Valor a ser dobrado.
    :param format: (Opicional) Se True ativa a def formatacao
    :return: Número dobrado.
    Função criada por Livio Alvarenga GitHub ...    
    """
    r = x * 2
    return r if formato is False else formatacao(r)


def metade(x=0, formato=False):
    """
    --> Função para diminuir metade de um determinado valor.
    :param x: Valor a ser diminuido.
    :param format: (Opicional) Se True ativa a def formatacao
    :return: Metade do número.
    Função criada por Livio Alvarenga GitHub ...    
    """
    r = x / 2
    return r if formato is False else formatacao(r)


def formatacao(x=0, y='R$'):
    return f'{y}{x:.2f}'.replace('.', ',')


def resumo(x=0, y=0, z=0):
    """
    --> Função para printar um resumo das funções dobro, metade, aumentar e diminuir.
    :param x: Valor a ser calculado.
    :param y: Quantidade a aumentar ex: 10 (%).
    :param z: Quantidade a diminuir ex: 10 (%).
    :return: O print do dobro, metade, aumento e redução.
    Função criada por Livio Alvarenga GitHub ...    
    """
    print(f'{"-" * 40}')
    print(f'{"RESUMO DO VALOR":^40}')
    print(f'{"-" * 40}')
    print(f'Preço analisado: \t{formatacao(x)}')
    print(f'Dobro do preço: \t{dobro(x, True)}')
    print(f'Metade do preço: \t{metade(x, True)}')
    print(f'{y}% de aumento: \t{aumentar(x, y, True)}')
    print(f'{z}% de redução: \t{diminuir(x, z, True)}')
    print(f'{"-" * 40}')
