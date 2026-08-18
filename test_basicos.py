import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from problemas.basicos.fatorial import fatorial_iterativo, fatorial_recursivo
from problemas.basicos.fibonacci import fibonacci_iterativo
from problemas.basicos.numeros_primos import eh_primo

def test_fatorial():
    assert fatorial_iterativo(5) == 120
    assert fatorial_recursivo(5) == 120
    assert fatorial_iterativo(0) == 1
    assert fatorial_iterativo(1) == 1

def test_fibonacci():
    assert fibonacci_iterativo(0) == 0
    assert fibonacci_iterativo(1) == 1
    assert fibonacci_iterativo(10) == 55

def test_primos():
    assert eh_primo(2) is True
    assert eh_primo(17) is True
    assert eh_primo(15) is False
    assert eh_primo(1) is False
    assert eh_primo(97) is True
