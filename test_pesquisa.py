import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from problemas.pesquisa.pesquisa_linear import pesquisa_linear
from problemas.pesquisa.pesquisa_binaria import pesquisa_binaria

def test_pesquisa_linear():
    lista = [4, 2, 7, 1, 9]
    assert pesquisa_linear(lista, 7) == 2
    assert pesquisa_linear(lista, 10) == -1
    assert pesquisa_linear(lista, 4) == 0

def test_pesquisa_binaria():
    lista = [1, 3, 5, 7, 9, 11]
    assert pesquisa_binaria(lista, 7) == 3
    assert pesquisa_binaria(lista, 2) == -1
    assert pesquisa_binaria(lista, 1) == 0
    assert pesquisa_binaria(lista, 11) == 5
