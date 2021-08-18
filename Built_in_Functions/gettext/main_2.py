from language import set_language

_ = set_language('en_US').gettext


def print_some_strings():

    print('\n')
    print(_("Vamos traduzir este texto para inglês, testando em dois arquivos.py"))
    print('\n')
    print(_("Ola mundo!"))


if __name__ == '__main__':
    print_some_strings()
