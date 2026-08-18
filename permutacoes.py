"""
Geração das permutações de uma lista
"""

def permutacoes(lista: list) -> list:
    if len(lista) <= 1:
        return [lista.copy()]

    resultado = []
    for i in range(len(lista)):
        elemento = lista[i]
        resto = lista[:i] + lista[i+1:]
        for p in permutacoes(resto):
            resultado.append([elemento] + p)
    return resultado

if __name__ == "__main__":
    dados = [1, 2, 3]
    print("Permutações de", dados)
    for p in permutacoes(dados):
        print(p)
