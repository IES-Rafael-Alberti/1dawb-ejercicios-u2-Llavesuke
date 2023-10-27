import pytest
from src.ej2_04 import Pedirnumeros, par_impar

def test_PedirNumeros(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: '10')
    result = Pedirnumeros()
    assert result == 10


@pytest.mark.parametrize(
    "num, expected",
    [
            (12,True),
            (3,False)
    ]
)
def test_par_impar_params(num,expected): 
    assert par_impar (num) == expected