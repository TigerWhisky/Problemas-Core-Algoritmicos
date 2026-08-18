"""
Selection Sort
Complexidade: O(n²)
Não estavel
"""

def selection_sort(lista: list) -> list:
    arr = lista.copy()
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

if __name__ == "__main__":
    dados = [64, 25, 12, 22, 11]
    print("Original:", dados)
    print("Ordenado:", selection_sort(dados))
