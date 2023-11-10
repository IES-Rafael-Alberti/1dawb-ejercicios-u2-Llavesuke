import pytest
from src.ej22_12 import Ask_User, Countletter

def test_ej22_12(monkeypatch):
    inputs = iter(['Naruto es rubio', 'o'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    result = Ask_User()
    assert result == ('Naruto es rubio', 'o')

@pytest.mark.parametrize(
    ('frase,letra,expected'),
    [
        ('Perrito bueno','a',0),
        ('Pedro sanchez raton','o',2)
    ]
)
def test_Counterletter_params(frase,letra,expected):
    assert Countletter(frase,letra) == expected