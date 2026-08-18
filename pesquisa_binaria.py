"""
Pesquisa Binária (Binary Search)
Requisito: lista ordenada
Complexidade: O(log n)
"""

def pesquisa_binaria(lista: list, alvo) -> int:
    esquerda, direita = 0, len(lista) - 1

    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if lista[meio] == alvo:
            return meio
        elif lista[meio] < alvo:
            esquerda = meio + 1
        else:
            direita = meio - 1
    return -1

def pesquisa_binaria_recursiva(lista: list, alvo, esquerda=0, direita=None) -> int:
    if direita is None:
        direita = len(lista) - 1
    if esquerda > direita:
        return -1

    meio = (esquerda + direita) // 2
    if lista[meio] == alvo:
        return meio
    elif lista[meio] < alvo:
        return pesquisa_binaria_recursiva(lista, alvo, meio + 1, direita)
    else:
        return pesquisa_binaria_recursiva(lista, alvo, esquerda, meio - 1)

if __name__ == "__main__":
    dados = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    print("Índice de 11:", pesquisa_binaria(dados, 11))
    print("Índice de 4:", pesquisa_binaria(dados, 4))
    print("Recursiva - 13:", pesquisa_binaria_recursiva(dados, 13))
