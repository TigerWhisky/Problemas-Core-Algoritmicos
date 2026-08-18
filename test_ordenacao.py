from problemas.03_ordenacao.bubble_sort import bubble_sort
from problemas.03_ordenacao.selection_sort import selection_sort
from problemas.03_ordenacao.insertion_sort import insertion_sort
from problemas.03_ordenacao.merge_sort import merge_sort

def test_ordenacoes():
    original = [64, 34, 25, 12, 22, 11, 90]
    esperado = [11, 12, 22, 25, 34, 64, 90]

    assert bubble_sort(original) == esperado
    assert selection_sort(original) == esperado
    assert insertion_sort(original) == esperado
    assert merge_sort(original) == esperado
