import pytest
from src.ej2_03 import division, PedirNumeros

def test_PedirNumeros(monkeypatch):
    inputs = iter(['10', '2'])
    monkeypatch.setattr('builtins.input', lambda  _: next(inputs))
    result = PedirNumeros()
    assert result == ('10','2')


@pytest.mark.parametrize(
    "input_n1, input_n2, expected",
    [
        (10,2,5),
        (11,3,'Error'),
        (4,4,1)
    ]
)
def test_division_params(input_n1,input_n2,expected):
    assert division (input_n1,input_n2) == expected