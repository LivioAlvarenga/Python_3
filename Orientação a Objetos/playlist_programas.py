
class Programa():  # Super Class
    def __init__(self, nome: str, ano: int):
        self._nome = nome.title()
        self.ano = ano
        self._likes: int = 0

    @property
    def likes(self) -> int:
        return self._likes

    def dar_like(self) -> None:
        self._likes += 1

    @property
    def nome(self) -> str:
        return self._nome

    @nome.setter
    def nome(self, novo_nome: str) -> None:
        self._nome = novo_nome.title()

    def __str__(self) -> str:
        nome: str = f'\nNome: {self._nome}\n'
        ano: str = f'Ano: {self.ano}\n'
        like: str = f'Likes: {self._likes} Likes\n'
        return nome + ano + like


class Filme(Programa):
    def __init__(self, nome: str, ano: int, duração: int):
        # com esta ação estamos usando nome e ano da classe mãe Programa
        super().__init__(nome, ano)
        self.duração = duração

    def __str__(self) -> str:
        duração: str = f'Duração: {self.duração} min\n'
        return super().__str__() + duração

    def __repr__(self) -> str:
        return f'Filme: {self.nome} de {self.ano} - {self.duração} min.'


class Serie(Programa):
    def __init__(self, nome: str, ano: int, temporadas: int):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self) -> str:
        temporadas: str = f'Temporadas: {self.temporadas}\n'
        return super().__str__() + temporadas

    def __repr__(self) -> str:
        serie_repr = f'Serie: {self.nome} de {self.ano} - '
        serie_repr += f'{self.temporadas} temporadas.'
        return serie_repr


class Playlist():
    def __init__(self, nome: str, programas: list):
        self.nome = nome
        self._programas = programas

    @property
    def listagem(self):
        return self._programas

    def __len__(self):
        return len(self._programas)

    def __getitem__(self, indice):  # tornando nossa classe iterável
        return self._programas[indice]

    def __repr__(self):
        return f'{self._programas}'


# .Testando o código.
if __name__ == '__main__':

    filme1 = Filme('vingadores - guerra infinita', 2018, 160)
    serie1 = Serie('atlanta', 2018, 2)
    filme2 = Filme('Todo mundo em pânico', 1999, 100)
    serie2 = Serie('Demolidor', 2016, 2)

    # -Simulando likes
    filme1.dar_like()
    filme2.dar_like()
    filme2.dar_like()
    filme2.dar_like()
    filme2.dar_like()
    serie2.dar_like()
    serie2.dar_like()
    serie1.dar_like()
    serie1.dar_like()
    serie1.dar_like()

    listinha = [filme1, serie1, serie2, filme2]
    minha_playlist = Playlist('fim de semana', listinha)

    # testando o __len__
    print(f'O tamanho da minha lista é : {len(minha_playlist)}')

    for programa in minha_playlist:
        print(programa)  # testando __str__

    print('-' * 50)
    print(minha_playlist)  # testando __repr__
    print(minha_playlist[2])  # testando __getitem__
    print('-' * 50)


# ! Observações:
# .01
# name mangling - ao fazermos uso dos dois underscores, deixamos o atributo
#   privado. Na realidade, o que acontece é que com isso __ será transformado
#   em uma outra variável, e esta ação recebe o nome de name mangling. Onde
#   temos __nome após a transformação, o resultado seria _Programa__nome
#   (fazê-lo não seria uma boa prática). Uma melhor opção é usar simplesmente
#   um _ (underscore), assim oferecemos a ideia de protegido, sem fazermos o
#   name mangling.

# .02
# Método super() - Na classe Filme, chamamos o super(), que por sua vez chama
#   qualquer método ou atributo da classe mãe. Podemos testar isto digitando
#   super(). e observando o que o PyCharm nos sugere como autocomplete. Todos
#   os métodos ou propriedades exibidos são provenientes da classe mãe,
#   evidenciado por Programa, ao lado. Podemos acessá-los direta ou
#   indiretamente.

# .03
# __str__ Alguns métodos no Python são especiais, ou dunder methods, como
#   costumam chamar. Dunder vem de double underscore, isto é, "dois underlines"
#   __str__(), ou dunder str, ou ainda "str especial" é um método especial
#   capaz de representar um objeto textualmente.

# .04
# __repr__ é usado para mostrar uma representação que ajude no debug ou log de
#   um código. Por exemplo, se você quiser entender como funciona seu objeto,
#   ou se está válido, e imprimir o seu valor string, qual resultado facilita
#   sua vida? sem __repr__ Filme(nome='vingadores', ano=2018, duração=160) com
#   __repr__ "Filme: Vingadores de 2018 - 160 min"

# .05
# __getitem__() No Python, existe um jeito de fazer com que a classe seja
#   considerada iterável, sem a necessidade de usarmos a herança. Este método
#   define algo que é iterável. Nos ajuda a percorrermos a lista e pegarmos um
#   item específico dela.

# .06
# Duck typing - podemos substituir a herança por um pouco de composição. Sendo
#   assim, podemos fazer a nossa playlist se passar por outro tipo de objeto
#   específico, sem precisarmos da herança; e não chamamos isso de
#   polimorfismo, e sim de duck typing.

# .07
# __len__ há um dunder method que poderá ser implementado para que a lista se
#   comporte como um sized, uma ideia de algo que possui tamanho, e que então
#   precisará implementar um __len__() para que o len() externo possa
#   funcionar em nossa classe
