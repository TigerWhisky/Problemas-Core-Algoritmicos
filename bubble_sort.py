"""
Bubble Sort
Complexidade: O(n²)
"""

def bubble_sort(lista: list) -> list:
    arr = lista.copy()
    n = len(arr)
    for i in range(n):
        trocou = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                trocou = True
        if not trocou:          # optimização: já está ordenado
            break
    return arr

if __name__ == "__main__":
    dados = [64, 34, 25, 12, 22, 11, 90]
    print("Original:", dados)
    print("Ordenado:", bubble_sort(dados))
