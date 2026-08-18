"""
Insertion Sort
Complexidade: O(n²) | Melhor caso O(n)
"""

def insertion_sort(lista: list) -> list:
    arr = lista.copy()
    for i in range(1, len(arr)):
        chave = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > chave:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = chave
    return arr

if __name__ == "__main__":
    dados = [12, 11, 13, 5, 6]
    print("Original:", dados)
    print("Ordenado:", insertion_sort(dados))
