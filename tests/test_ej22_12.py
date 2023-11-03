import pytest
from src.ej22_12 import Ask_User

def test_ej22_12(monkeypatch):
    inputs = iter(['Naruto es rubio', 'o'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    result = Ask_User()
    assert result == ('Naruto es rubio', 'o')
