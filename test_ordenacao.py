import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from problemas.ordenacao.bubble_sort import bubble_sort
from problemas.ordenacao.selection_sort import selection_sort
from problemas.ordenacao.insertion_sort import insertion_sort
from problemas.ordenacao.merge_sort import merge_sort

def test_ordenacoes():
    original = [64, 34, 25, 12, 22, 11, 90]
    esperado = [11, 12, 22, 25, 34, 64, 90]

    assert bubble_sort(original) == esperado
    assert selection_sort(original) == esperado
    assert insertion_sort(original) == esperado
    assert merge_sort(original) == esperado

def test_lista_vazia():
    assert bubble_sort([]) == []
    assert merge_sort([]) == []

def test_lista_ja_ordenada():
    lista = [1, 2, 3, 4, 5]
    assert bubble_sort(lista) == lista
    assert insertion_sort(lista) == lista
