"""
Sequência de Fibonacci
Versões: iterativa, recursiva e com memoization
"""

def fibonacci_iterativo(n: int) -> int:
    if n < 0:
        raise ValueError("n deve ser não negativo")
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def fibonacci_recursivo(n: int) -> int:
    if n < 0:
        raise ValueError("n deve ser não negativo")
    if n <= 1:
        return n
    return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)

def fibonacci_memo(n: int, memo=None) -> int:
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    return memo[n]

if __name__ == "__main__":
    for i in range(10):
        print(f"F({i}) = {fibonacci_iterativo(i)}")
