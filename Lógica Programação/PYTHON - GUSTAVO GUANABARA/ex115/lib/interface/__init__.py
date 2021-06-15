def leiaInt(msg='Digite um número inteiro: '): 
    while True:
        try:
            a = int(input(msg))
        except (ValueError, TypeError):
            print('ERRO: Por favor, digite um número inteiro válido.')
            continue
        except KeyboardInterrupt:
            print('Usuário preferiu não digitar esse número.')
            a = 0
            break
        else:
            break
    return a


def linha(tam=60):
    return '-' * tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(60))
    print(linha())


def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    print(linha())
    opc = leiaInt(f'Sua Opção: ')
    return opc

