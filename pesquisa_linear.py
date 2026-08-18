"""
Pesquisa Linear (Linear Search)
Complexidade: O(n)
"""

def pesquisa_linear(lista: list, alvo):
    """Retorna o índice do alvo ou -1 se não existir"""
    for i, valor in enumerate(lista):
        if valor == alvo:
            return i
    return -1

def pesquisa_linear_todos(lista: list, alvo) -> list:
    """Retorna todos os índices onde o numero aparece"""
    return [i for i, valor in enumerate(lista) if valor == alvo]

if __name__ == "__main__":
    dados = [4, 2, 7, 1, 9, 2, 5, 2]
    print("Índice de 7:", pesquisa_linear(dados, 7))
    print("Índices de 2:", pesquisa_linear_todos(dados, 2))
    print("Índice de 10:", pesquisa_linear(dados, 10))
