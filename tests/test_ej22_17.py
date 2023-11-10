import pytest
from src.ej22_17 import User_Input, Digit_Sum

def test_User_Input(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: '1048')
    result = User_Input()
    assert result == '1048'

@pytest.mark.parametrize(
    ('numero,expected'),
    [
        ('14',5),
        ('45',9),
        ('129',12)
    ]
)
def test_Digit_Sum_params(numero,expected):
    assert Digit_Sum(numero) == expected