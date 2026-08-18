import pytest
from problemas.01_basicos.fatorial import fatorial_iterativo, fatorial_recursivo
from problemas.01_basicos.fibonacci import fibonacci_iterativo
from problemas.01_basicos.numeros_primos import eh_primo

def test_fatorial():
    assert fatorial_iterativo(5) == 120
    assert fatorial_recursivo(5) == 120
    assert fatorial_iterativo(0) == 1

def test_fibonacci():
    assert fibonacci_iterativo(0) == 0
    assert fibonacci_iterativo(1) == 1
    assert fibonacci_iterativo(10) == 55

def test_primos():
    assert eh_primo(2) is True
    assert eh_primo(17) is True
    assert eh_primo(15) is False
    assert eh_primo(1) is False
