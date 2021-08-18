
from language import set_language

_ = set_language('en_US').gettext


def print_some_strings():

    print('\n')
    print(_("Oi, este é um tutorial do uso de gettext"))
    print('\n')
    print(_("Vamos traduzir este texto para inglês."))


if __name__ == '__main__':
    print_some_strings()

# para criar arquivo base.pot usando o pygettext
# python C:\Users\Avell\AppData\Local\Programs\Python\Python39\Tools\i18n\/
# pygettext.py -d base -o locales\base.pot *.py

# para usar pygettext em vários arquivos.py coloque *.py

'''
Encontrando diretorios de todos os idiomas, segue o exemplo no python
iterativo:

No terminal va ate o diretorio da sua aplicação mais.
digite python para abrir o python iterativo, siga os comandos abaixo, onde:

>>> é in sem >>> é out

>>> import gettext
>>> gettext.find('base')
>>> gettext.find('base', 'locales')
'locales\\pt\\LC_MESSAGES\\base.mo'
>>> import os
>>> os.environ['LANGUAGE']='en'
>>> gettext.find('base', 'locales')
'locales\\en\\LC_MESSAGES\\base.mo'
>>> os.environ['LANGUAGE']='el:en'
>>> gettext.find('base', 'locales')
'locales\\en\\LC_MESSAGES\\base.mo'
>>> gettext.find('base', 'locales', all=True)
['locales\\en\\LC_MESSAGES\\base.mo']
>>> os.environ['LANGUAGE']='pt:en'
>>> gettext.find('base', 'locales', all=True)
['locales\\pt\\LC_MESSAGES\\base.mo', 'locales\\en\\LC_MESSAGES\\base.mo']
>>>


'''
