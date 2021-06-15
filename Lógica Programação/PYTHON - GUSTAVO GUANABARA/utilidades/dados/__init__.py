def leiaDinheiro(d=''):
    x = d.strip().replace(',', '.')
    while True:
        if x != '0' and x.replace('.', '').isnumeric() == True:
            break            
        print(f'ERRO: {x} é um preço inválido.')
        x = str(input('Digite o preço: R$')).strip().replace(',', '.')
    return float(x)
    
    
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


def leiaFloat(msg='Digite um número real: '): 
    while True:
        try:
            a = float(input(msg))
        except (ValueError, TypeError):
            print('ERRO: Por favor, digite um número real válido.')
            continue
        except KeyboardInterrupt:
            print('Usuário preferiu não digitar esse número.')
            a = 0
            break
        else:
            break
    return a  

    