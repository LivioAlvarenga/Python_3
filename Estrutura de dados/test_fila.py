from fila import Fila


class Pedido():
    def __init__(self, pizza) -> None:
        self.pizza = pizza

    def __repr__(self) -> str:
        return self.pizza


# .Testando o código.
if __name__ == '__main__':

    # .Instanciando pedidos
    pizzaria = Fila()

    pedido1 = Pedido('Muçarela')
    pedido2 = Pedido('Calabresa')
    pedido3 = Pedido('Marguerita')
    pedido4 = Pedido('A moda')

    # .Recebendo os pedidos
    print(f'Recebendo pedido {pedido1}\n')
    pizzaria.entrar(pedido1)

    print(f'Recebendo pedido {pedido2}\n')
    pizzaria.entrar(pedido2)

    print(f'Recebendo pedido {pedido3}\n')
    pizzaria.entrar(pedido3)

    # .Finalizando pedidos e conferindo se a fila tem mais pedidos
    pedido = pizzaria.sair()
    print(f'Fazendo pizza {pedido}')
    print(f'Está vazia? {pizzaria.vazia}\n')

    # .Finalizando pedidos e conferindo se a fila tem mais pedidos
    pedido = pizzaria.sair()
    print(f'Fazendo pizza {pedido}')
    print(f'Está vazia? {pizzaria.vazia}')

# !Observações:
# No Python, não existe uma estrutura de dados correspondente à Fila. No
#  entanto, é possível implementar Fila de várias formas. Uma delas é usar
#  list.append() e list.pop(0), onde usamos respectivamente
#  ListaDuplamenteLigada.inserir_no_fim() e ListaLigada.remover_do_inicio().
# No entanto, como operações no início de list são mais custosas, da mesma
#  forma que nos vetores, o ideal é usar collections.deque que, como foi
#  mencionado na atividade da Aula de Lista Duplamente Ligada, é otimizado
#  para operações nas extremidades. Então, fila.sair() corresponde a
#  deque.popleft() e fila.entrar() seria deque.append(). Além de deque, há
#  outras estruturas de dados na biblioteca padrão do Python que implementam
#  Filas:
# queue - usada para comunicação segura entre threads
#  https://docs.python.org/3/library/queue.html
# multprocessing - para comunicação entre processos
#  https://docs.python.org/3.7/library/multiprocessing.html#exchanging-objects-between-processes
# asyncio - para administrar tarefas em programação assíncrona
#  https://docs.python.org/3/library/asyncio-queue.html#examples
