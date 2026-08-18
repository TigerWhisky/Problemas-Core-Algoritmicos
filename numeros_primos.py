"""
Verificação de números primos e geração de primos até N
"""

def eh_primo(n: int) -> bool:
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def primos_ate(n: int) -> list:
    return [i for i in range(2, n + 1) if eh_primo(i)]

if __name__ == "__main__":
    print("Primos até 50:", primos_ate(50))
    print("97 é primo?", eh_primo(97))
