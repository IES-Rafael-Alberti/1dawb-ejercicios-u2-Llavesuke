import pytest
from src.condicionales.ej2_09 import AskAge, Clasify

def test_AskAge(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 12)
    result = AskAge()
    assert result == 12

@pytest.mark.parametrize(
    'input, expected',
    [
        (3,'gratis'),
        (8,'5'),
        (20,'10')
    ]
)
def test_Clasify_params(input,expected):
    assert Clasify(input) == expected