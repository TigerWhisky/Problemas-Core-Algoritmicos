"""
Mutabilidade e referências em listas
"""

def modificar_lista(lista):
    """As Listas são passadas por referência"""
    lista.append(99)
    lista[0] = 1000

def tentar_reatribuir(lista):
    """Reatribuir a variável local não afecta o original"""
    lista = [1, 2, 3]

if __name__ == "__main__":
    dados = [10, 20, 30]
    print("Original:", dados)

    modificar_lista(dados)
    print("Depois de modificar_lista:", dados)

    tentar_reatribuir(dados)
    print("Depois de tentar_reatribuir:", dados)

    # Cópia superficial vs profunda
    original = [[1, 2], [3, 4]]
    copia = original.copy()          # shallow copy
    copia[0][0] = 999
    print("\nShallow copy afetou o original:", original)
