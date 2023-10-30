import pytest
from src.ej2_10 import Ask_User, Clasify, Elements

def test_Ask_User(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 1)
    result = Ask_User()
    assert result == 1


@pytest.mark.parametrize(
    'input, expected',
    [
        (1,'vegetariana'),
        (2,'no vegetariana')
    ]
)
def test_Clasify_params(input,expected):
    assert Clasify(input) == expected
