"""
Torre de Hanói
Exemplo de recursão
"""

def torre_hanoi(n: int, origem: str, auxiliar: str, destino: str):
    if n == 1:
        print(f"Mover disco 1 de {origem} para {destino}")
        return
    torre_hanoi(n - 1, origem, destino, auxiliar)
    print(f"Mover disco {n} de {origem} para {destino}")
    torre_hanoi(n - 1, auxiliar, origem, destino)

if __name__ == "__main__":
    print("Solução para 3 discos:")
    torre_hanoi(3, "A", "B", "C")
