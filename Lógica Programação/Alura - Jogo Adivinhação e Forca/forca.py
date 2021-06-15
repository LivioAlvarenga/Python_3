from random import randrange


def jogar():

    imprime_mensagem()
    palavra_secreta = carrega_palavra_secreta('palavras.txt')
    # '_' para cada letra da palavra
    letras_acertadas = ['_' for letra in palavra_secreta]

    acertou = False
    enforcou = False
    erros = 0

    desenha_forca(0)
    print(f'\n{letras_acertadas}')
    while (not acertou and not enforcou):
        chute = str(input('\nQual letra? ')).strip().upper()[0]

        if (chute in palavra_secreta):
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            erros += 1
            print(f'{"":-^50}\n{"Ops, você errou!":^50}')

        enforcou = erros == 7  # devolve bool (False | True)
        acertou = '_' not in letras_acertadas  # devolve bool (False | True)

        desenha_forca(erros)
        print(f'\n{letras_acertadas}')

    if (acertou):
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra_secreta)


def desenha_forca(erros=0):
    """Imprime uma forca de acordo com status do jogo.

    Args:
        erros (int, optional): variavel erros. Defaults to 0.
    """
    print(f'Você tem {7 - erros} chances!')
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 0):
        print(" |            ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


def imprime_mensagem(texto='Bem vindo ao jogo da Forca!'):
    """[Imprime mensagem de texto formatada.]

    Args:
        texto (texto, optional): [mensagem impressa]. Defaults to 'Bem vindo
        ao jogo da Forca!'.
    """
    print(f'{"-=" * 25}')
    print(f'{texto:^50}')
    print(f'{"-=" * 25}')


def carrega_palavra_secreta(caminho):
    """Abre um arquivo com palavras e sorteia uma para o jogo da forca.

    Args:
        caminho (str): nome do arquivo com as palavras

    Returns:
        str: palavra sorteada
    """
    # caminho_arq = f'{dirname(realpath(__file__))}\\{caminho}'
    # obs o código abaixo so ira funcionar se o terminal estiver no mesmo
    # diretorio do arquivo
    # se quiser resolver o problema use o código dirname ou coloque o terminal
    # no mesmo diretorio.
    arquivo = "Python_3\Lógica Programação\Alura - Jogo Adivinhação e Forca\palavras.txt"
    with open(arquivo, "r", encoding="utf-8") as arquivo:
        palavras = []
        for linha in arquivo:
            linha = linha.strip()
            palavras.append(linha)

    numero = randrange(0, len(palavras))
    return palavras[numero].upper()


def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    for posicao, letra in enumerate(palavra_secreta):
        if (letra == chute):
            letras_acertadas[posicao] = letra
    print(f'{"":-^50}\n{"Eba, você acertou!":^50}')


def imprime_mensagem_perdedor(palavra_secreta):
    print("\nPuxa, você foi enforcado!\n")
    print(f'A palavra era {palavra_secreta}')
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


def imprime_mensagem_vencedor():
    print("\nParabéns, você ganhou!\n")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


if(__name__ == "__main__"):
    jogar()
