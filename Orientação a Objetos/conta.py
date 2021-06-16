
class Conta(object):

    # numero, titular, saldo e limite são atributos da class Conta
    def __init__(self, numero: int, titular: str, saldo: float,
                 limite: float = 1000.0):
        # Dois undercores __ tornam as variáveis privadas.
        self.__numero: int = numero
        self.__titular: str = titular
        self.__saldo: float = saldo
        self.__limite: float = limite

    def extrato(self) -> str:
        """Retorna extrato com numero da conta, titular, limite e valor."""
        extrato: str = f'\nConta: {self.__numero}\ntitular: {self.__titular}'
        extrato += f'\nLimite: {self.__limite}\nSaldo: {self.__saldo}'
        return extrato

    def depositar(self, valor: float) -> None:
        """Somar valor depositado ao saldo.

        Args:
            valor (float): Valor a ser somando/depositado
        """
        self.__saldo += valor

    def __pode_sacar(self, valor_a_sacar: float) -> bool:
        """__Função privada! Verificar se o cliente tem valor disponível para sacar.

        Args:
            valor_a_sacar (float): valor que deseja sacar

        Returns:
            bool: True se saque < (saldo + limite)
        """
        valor_disponível_a_sacar = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponível_a_sacar

    def sacar(self, valor: float) -> None:
        """Realiza saque na conta se valor de saque < saldo + limite.

        Args:
            valor (float): Valor a ser sacado
        """
        if (self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print(f'O valor {valor} passou o limite.')

    def transferir(self, valor: float, conta_destino) -> None:
        """Realiza transferência de valor de conta self para conta destino.
        Através dos metodos encapsulados sacar() e deposita().

        Args:
            valor (float): Valor a ser transferido
            conta_destino (class Conta()): Conta de destino a receber o valor
        """
        # Encapsulamento, colocamos outras funções dentro de transferir
        self.sacar(valor)
        conta_destino.depositar(valor)

    @property
    def saldo(self) -> float:
        """Getter de __saldo, retorna valor saldo."""
        return self.__saldo

    @property
    def titular(self) -> str:
        """Getter de __titular, retorna nome titular."""
        return self.__titular.title()

    @property
    def limite(self) -> float:
        """Getter de __limite, retorna valor do limite."""
        return self.__limite

    @limite.setter
    def limite(self, limite: float) -> None:  # setters com @property
        """Setter de __limite, editar limite de conta.
        Ex.: conta.limite = 10000.0"""
        self.__limite = limite

    @staticmethod
    def código_banco() -> str:
        """Retorna código do banco é uma @staticmethod."""
        return '001'

    @staticmethod
    def códigos_bancos() -> dict[str, str]:
        """Retorna códigos dos bancos em um dicionário é uma @staticmethod."""
        return {'BB': '001', 'Caixa': '104', 'Bradesco': '237'}


# .Testando o código.
if __name__ == '__main__':
    conta1 = Conta(123, 'Livio', 100)
    print(f'\n -> Criando conta1:{conta1.extrato()}')

    conta2 = Conta(124, 'Flavia', 1000.5)
    print(f'\n -> Criando conta2:{conta2.extrato()}')

    # -Depositando valor
    conta1.depositar(100)
    print(f'\n -> Depositando 100 na conta1:{conta1.extrato()}')

    # -Sacando valor
    conta1.sacar(30)
    print(f'\n -> Sacando 30 na conta1:{conta1.extrato()}')

    # -Transferindo valor entre contas
    print(f'\n -> Transferindo valor da conta1 p/ conta2:{conta1.extrato()}')
    conta1.transferir(50, conta2)
    print(f'\n -> Transferindo valor da conta1 p/ conta2:{conta2.extrato()}')

    # -Acessando getters
    print(f'\n -> Acessando saldo na conta1:\n{conta1.saldo:.2f}')
    print(f'\n -> Acessando titular na conta1:\n{conta1.titular}')
    print(f'\n -> Acessando limite na conta1:\n{conta1.limite:.2f}')

    # -Acessando setters
    conta1.limite = 1500
    print(f'\n -> Trocando limite na conta1:\n{conta1.limite:.2f}')

    # -Acessando staticmethod
    print(f'\n -> Acessando cod. do banco:\n{conta1.código_banco()}')
    print(f'\n -> Acessando cods. dos bancos:\n{conta1.códigos_bancos()}')


# ! Observações:
# .01
# Self é a referência que sabe encontrar o objeto construído em memória.

# .02
# Os atributos são as características que especificam uma classe. Estão na
#   função especial __init__

# .03
# __init__ (função construtora) é uma implícita, que é chamada
#   automaticamente.

# .04
# Não podemos acessar o atributo saldo do objeto diretamente. Teremos que
#   usar os métodos responsáveis por encapsular o acesso ao objeto. Então,
#   para melhorarmos a classe Conta, devemos restringir o acesso a saldo,
#   tornando-o privado, adicionando dois caracteres underscore (__) a esquerda.
#   A ação de tornar privado o acesso aos atributos, no mundo Orientado a
#   Objetos, chamamos de encapsulamento.

# .05
# O uso do getters são métodos usados apenas para retornar dado. Ou seja, a
#   forma mais apropriada de nomear os métodos seria usando o nome get.

# .06
# O uso do setters são métodos usados para modificar o dado. Ou seja, a
#   forma mais apropriada de nomear os métodos seria usando o nome set.

# .07
# Uma solução ao invés de usar get e set no nome das variaveis é usar uma
#   property, A declaração de uma property é feita com o uso do caractere @.
#   @property para getters e @nome da função.setter para setters.

# .08
# Todas as linguagens orientadas a objeto trabalham com métodos estáticos,
#   fica inapropriado usar property, porque ele sempre precisa do self. A
#   configuração correta será @staticmethod.
