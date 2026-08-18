from problemas.02_pesquisa.pesquisa_linear import pesquisa_linear
from problemas.02_pesquisa.pesquisa_binaria import pesquisa_binaria

def test_pesquisa_linear():
    lista = [4, 2, 7, 1, 9]
    assert pesquisa_linear(lista, 7) == 2
    assert pesquisa_linear(lista, 10) == -1

def test_pesquisa_binaria():
    lista = [1, 3, 5, 7, 9, 11]
    assert pesquisa_binaria(lista, 7) == 3
    assert pesquisa_binaria(lista, 2) == -1
