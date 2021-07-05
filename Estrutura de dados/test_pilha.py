from pilha import Pilha


class Fase():
    def __init__(self, cenário: str, pontuação: int, punição: int) -> None:
        self.cenário = cenário
        self.pontuação = pontuação
        self.punição = punição

    def __repr__(self) -> str:
        return self.cenário


# .Testando o código.
if __name__ == '__main__':

    # .Instanciando fases
    fases = Pilha()
    fase1 = Fase('Floresta', 300, -100)
    fase2 = Fase('Castelo', 100, -4)
    fase3 = Fase('Caverna', 400, -50)
    fase4 = Fase('Guerra', 3000, -400)

    fases.empilhar(fase1)
    fases.empilhar(fase2)
    falhou = fases.desempilhar()
    print(f'Falhou na fase: {falhou}')

    print(f'Voltou para a fase: {fases.topo}')

# ! Observações
# No Python, não existe uma estrutura de dados corresponde para Pilha, no
#  entanto, é possível implementar uma de várias formas.
# Uma delas é usar list.insert(0, dado) e list.pop(0), onde usamos
#  respectivamente ListaLigada.inserir_no_inicio() e
#  ListaLigada.remover_do_inicio().
# Mas como o desempenho de list é como o de vetor, ou seja, mais eficiente nas
#  operações no fim, o ideal é usar list.append() para inserção no fim,
#  funciona como empilhar, e list.pop() que é remoção do fim, funciona como
#  desempilhar.
