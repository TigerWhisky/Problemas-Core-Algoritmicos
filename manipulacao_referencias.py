"""
Exemplos de referências e identidade de objetos
"""

if __name__ == "__main__":
    a = [1, 2, 3]
    b = a                    # b referencia o mesmo objeto
    c = a.copy()             # c é uma nova lista

    print("a is b:", a is b)
    print("a is c:", a is c)
    print("a == c:", a == c)

    a.append(4)
    print("\nDepois de a.append(4):")
    print("a:", a)
    print("b:", b)
    print("c:", c)
