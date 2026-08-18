"""
Cálculo do Fatorial
Versões: iterativa e recursiva
"""

def fatorial_iterativo(n: int) -> int:
    if n < 0:
        raise ValueError("O cálculo do fatorial não é aplicável a números negativos")
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado

def fatorial_recursivo(n: int) -> int:
    if n < 0:
        raise ValueError("O cálculo do fatorial não é aplicável a números negativos")
    if n == 0 or n == 1:
        return 1
    return n * fatorial_recursivo(n - 1)

if __name__ == "__main__":
    for i in range(0, 11):
        print(f"{i}! = {fatorial_iterativo(i)} (iterativo) | {fatorial_recursivo(i)} (recursivo)")
