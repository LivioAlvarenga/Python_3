import re


class Extrator_url():

    def __init__(self, url: str) -> None:
        self.url = self.__sanitiza_url(url)
        self.__valida_url()

    def __sanitiza_url(self, url: str) -> str:
        """se url != de None retira caracteres especiais e espaços em branco
        nas extremidades da url (strip())"""
        return url.strip() if type(url) == str else ''

    def __valida_url(self) -> None:
        """Verifica se a URL esta vazia ou se é válida"""
        if not self.url:
            print('A URL está vazia')
            # raise ValueError('A URL está vazia')

        padrão = re.compile('(http(s)?://)?(www.)?nubank.com(.br)?/cambio')
        match = padrão.match(self.url)
        if not match:
            print('A URL não é válida.')
            # raise ValueError('A URL não é válida.')

    def get_url_base(self):
        """Retorna a base da url."""
        indice_interrogação = self.url.find('?')
        url_base = self.url[:indice_interrogação]
        return url_base

    def get_url_parametros(self):
        """Retorna os parâmetros da url."""
        indice_interrogação = self.url.find('?')
        url_parametros = self.url[indice_interrogação + 1:]
        return url_parametros

    def get_valor_parametro(self, parametro_busca):
        """Retorna o valor do parametro `parametro_busca`."""
        indice_parametro = self.get_url_parametros().find(parametro_busca)
        indice_valor = indice_parametro + len(parametro_busca) + 1
        indice_e_comercial = self.get_url_parametros().find('&', indice_valor)
        if indice_e_comercial == -1:
            valor = self.get_url_parametros()[indice_valor:]
        else:
            valor = self.get_url_parametros()[indice_valor:indice_e_comercial]
        return valor

    def __len__(self) -> int:
        """retorna tamanho da url"""
        return len(self.url)

    def __str__(self):
        url = f'\n{self.url}\n'
        parametros = f'\nParâmetros: {self.get_url_parametros()}\n'
        url_base = f'\nURL Base: {self.get_url_base()}\n'
        return url + parametros + url_base


# .Testando o código.
if __name__ == "__main__":

    # -Testando url = vazia, None e 0
    url = '  '
    extrator_url = Extrator_url(url)
    url = None
    extrator_url = Extrator_url(url)
    url = 0
    extrator_url = Extrator_url(url)

    # -Testando extração de quantidade
    url = "bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=\
dólar"
    extrator_url = Extrator_url(url)
    valor_quantidade = extrator_url.get_valor_parametro("quantidade")
    print(f'\n{valor_quantidade}')

    # -Testando método __len__
    print(f'\nO tamanho da extrator_url é {len(extrator_url)}')

    # -Testando método __str__
    print(extrator_url)
