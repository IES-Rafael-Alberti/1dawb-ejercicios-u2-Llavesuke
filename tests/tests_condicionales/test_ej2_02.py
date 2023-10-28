import pytest
from src.ej2_02 import ask_password, compare_password

def test_ask_passwrd(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'PERRITO')
    result = ask_password()
    assert result == 'perrito'
    monkeypatch.setattr('builtins.input', lambda _: 'Cabeza')
    result = ask_password()
    assert result == 'cabeza'
    monkeypatch.setattr('builtins.input', lambda _: 'CONTRASEÑA')
    result = ask_password()
    assert result == 'contraseña'

@pytest.mark.parametrize(
    "input_n, expected",
    [
        ('naruto', False),
        ('dragonazo', False),
        ('contraseña', True),
        ('checoslovaquia', False)
    ]
)

def test_compare_password_params(input_n,expected):
    assert compare_password(input_n) == expected