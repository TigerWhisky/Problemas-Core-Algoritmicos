"""
Encontrar o máximo e mínimo numa lista
"""

def maximo(lista: list):
    if not lista:
        raise ValueError("Lista vazia")
    m = lista[0]
    for x in lista[1:]:
        if x > m:
            m = x
    return m

def minimo(lista: list):
    if not lista:
        raise ValueError("Lista vazia")
    m = lista[0]
    for x in lista[1:]:
        if x < m:
            m = x
    return m

def max_min(lista: list) -> tuple:
    if not lista:
        raise ValueError("Lista vazia")
    mx = mn = lista[0]
    for x in lista[1:]:
        if x > mx:
            mx = x
        elif x < mn:
            mn = x
    return mx, mn

if __name__ == "__main__":
    dados = [4, 1, 7, 3, 9, 2, 5]
    print("Máximo:", maximo(dados))
    print("Mínimo:", minimo(dados))
    print("Max e Min:", max_min(dados))
