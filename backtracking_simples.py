"""
Exeplo de Backtracking: Subconjuntos
"""

def subconjuntos(lista: list) -> list:
    resultado = []

    def backtrack(inicio: int, caminho: list):
        resultado.append(caminho.copy())
        for i in range(inicio, len(lista)):
            caminho.append(lista[i])
            backtrack(i + 1, caminho)
            caminho.pop()          # backtrack

    backtrack(0, [])
    return resultado

if __name__ == "__main__":
    dados = [1, 2, 3]
    print("Subconjuntos de", dados)
    for s in subconjuntos(dados):
        print(s)
